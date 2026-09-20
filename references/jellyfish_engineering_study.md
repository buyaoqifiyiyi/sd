# Jellyfish 工程学习笔记

> Skill维护层：只在修改本Skill时读取，不参与影视生产。
>
> **本文件是面向人的外部项目学习笔记，属于非运行时文件。** 它未被任何 Workflow 列为 Required Resource，不参与运行时读取，也不是规则、恢复、路由、Schema 或知识判据的来源；不得被当作影视生产依据，也不得据此改写任何 STATE、Template、字段或 Gate。运行时权威是 `SKILL.md`、`rules/`、`workflows/`、`knowledge/`、`references/` 与 `templates/`。
>
> 笔记中所有 `backend/…`、`front/…`、`site/…` 路径都属于**外部仓库** `Forget-C/Jellyfish`，不是本 Skill 的文件，不得从本 Skill 根解析。

## 学习对象

| 项 | 事实 | 取证 |
|---|---|---|
| 仓库 | `Forget-C/Jellyfish` —— "An end-to-end production workspace for AI-generated short dramas" | GitHub API（阅读日快照：stars 6459 / forks 1118 / Apache-2.0 / `main` / `pushed_at` 2026-07-30） |
| 技术栈 | 后端 FastAPI + SQLAlchemy(async) + Celery + MySQL + Redis + RustFS；前端 React + Vite + Tailwind + i18next；文档站 Hugo | `README.md`、`deploy/compose/docker-compose.yml` |
| 规模 | 910 个受控文件（`git trees?recursive=1`，未截断）；`front/openapi.json` 270 KB / 100 个 `/api/v1` 路径 | GitHub API、本地克隆实测 |
| 本地副本 | `tmp/jellyfish-study/Jellyfish`（浅克隆；`tmp/` 不入库，不属发布内容） | `git clone --depth 1` |

它的定位与本 Skill 相邻但不同层：**Jellyfish 是带数据库、任务队列与前端工作台的 Web 生产系统；SD Film 是纯文本、无外部依赖的生产方法论。** 本笔记只提取**方法层**可迁移的部分，工程层选型一律标注不可迁移。

---

## 一、它做对的第一件事：把"状态"拆成三种，禁止互相顶替

三条规范反复锁定同一件事（`AGENTS.md` 的 `## 状态语义约定`、`site/content/docs/architecture/shot-page-boundary.md` 结尾）：

```text
准备状态（信息提取确认）
≠
视频可生成状态（video-readiness）
≠
生成中状态（runtime task）
```

1. `shot.status` 被**收窄为两个值**：`pending` / `ready`，只表示"信息提取确认是否完成"。历史上表示运行中的 `generating` 被明确删除（迁移 `backend/sql/003-normalize-shot-status-remove-generating.sql`），因为"生成中"是动态聚合结果，不是可持久化的静态状态。
2. `ready` 由后端按固定规则重算，前端**不得自行推导、也不得写回**（`site/content/docs/architecture/shot-status-flow.md`）：`skip_extraction = true` → `ready`；从未提取过 → `pending`；提取过但无候选 → `ready`；所有资产候选（`linked`/`ignored`）与对白候选（`accepted`/`ignored`）都处理完 → `ready`；其余 `pending`。
3. 中间态另开**候选明细表**（`shot_extracted_candidates` / `shot_extracted_dialogue_candidates`），逐条记 `pending / linked / ignored`，并大量"自动回退"：取消关联、替换角色、清空场景时，候选从 `linked` 退回 `pending` 并触发状态重算。

**对 SD Film 的映射**：本 Skill 的对应物是 STATE 与 `Project Status`（主状态）、`Clip Preflight`（可生成状态）、"生成尝试/返修"（runtime）。可借用的不是表结构，而是三条纪律：**(a) 主状态只回答一个问题；(b) 过程态另立"待确认明细"，不与主状态混写；(c) 派生状态必须可重算，写入者唯一。**

---

## 二、第二件事：把门槛写成可勾选证据清单，而不是一段散文

`backend/app/services/studio/shot_video_readiness.py` 是一个**实时聚合、不写库**的函数（文件头注释即写明），返回 `ready = all(item.ok for item in checks)` 与固定 7 项检查，每项为 `(key, ok, message)`：

| key | 判据 | 失败时的 message |
|---|---|---|
| `extraction_ready` | `skip_extraction` 或（已提取且无 pending 候选） | `仍有待确认项：资产 N 项，对白 M 项` |
| `duration_ready` | `ShotDetail.duration > 0` | `请先配置镜头时长` |
| `prompt_ready` | 预览链渲染出的 prompt 非空（渲染异常被捕获成失败项并带异常文本） | `视频提示词渲染失败：…` |
| `reference_frames_ready` | 按 `reference_mode` 查必需帧（`first`/`last`/`key`/`first_last`/`first_last_key`/`text_only`），缺项逐个点名 | `缺少参考帧：last, key` |
| `video_model_ready` | 默认视频模型已配置且类别正确 | `未配置默认视频模型` |
| `provider_ready` | 供应商存在且有 `api_key` | `视频模型供应商缺少 api_key：…` |
| `no_active_video_task` | 该镜头无进行中的视频任务 | `当前已有视频生成任务进行中` |

三个细节值得直接抄：**失败即给修复动作**（"请先配置镜头时长"比 `duration_ready=false` 有用一个数量级）；**检查项是封闭列表**，所以"还差什么"能逐条展示、也能批量预检；**结果不落库**——准备度是派生量，落库就会与真值不同步，而重算永远是对的。

`backend/app/services/studio/shot_preparation_state.py` 是同一思路的第二层聚合：`ready_for_generation = status == ready AND basic_info_ready AND semantic_defaults_ready AND action_beats_ready`，其中 `semantic_defaults_ready` 要求景别/机位/运镜/时长齐全，`action_beats_ready` 要求至少一条非空拍点。因此**`status = ready` 不等于可生成**——这两层被刻意分开，且每个 mutation 接口都返回**重建后的完整聚合态**，前端不需要自己猜该刷新哪些局部状态。

**与 SD Film 现状的差距（诚实标注）**：`rules/completion_gate.md` 的 Completion Decision 六条本身正确且严格，但它是**散文式判据、靠执行者自证**。Jellyfish 的增量价值只在于"把其中可机械核对的部分抽成具名检查项并逐项输出消息"——它不是更高的标准，只是更难被跳过。

---

## 三、第三件事：把导演约束做成"规则化 guidance"，并强制收敛

这是与 SD Film 最直接相关的一节。`backend/app/services/studio/shot_video_prompt_pack.py` 用**纯规则函数**（无 LLM 调用）从相邻镜头关系生成三类 guidance：

- `_build_continuity_guidance`（L230）：有上一镜头 → "承接上一镜头的动作、视线或情绪，不要像新场景重新开局"；**同场景**时追加"保持空间轴线和人物朝向稳定"；有下一镜头 → 要求形成收束落点。
- `_build_composition_anchor`（L255）：按景别分档（`ECU`/`CU` → 表情或细节为重心；`MS`/`FS` → 保持人物与环境相对位置；其余 → 先建立环境纵深）、按运镜分档（`DOLLY_IN`/`ZOOM_IN` → 重心向主体收束；`DOLLY_OUT`/`ZOOM_OUT` → 向环境退；`STATIC` → 主体位置稳定），再加"以场景 X 为主要空间锚点"与"锁定角色 A、B 的朝向与视线逻辑"。
- `_build_screen_direction_guidance`（L299）：按机位角度分档（`OVER_SHOULDER` → 前景肩部位置稳定；`EYE_LEVEL` → 平视与视线落点连续；其余 → 明确朝向与视线落点）、有对白 → 保持说话者/受话者对视逻辑、≥2 角色 → 点名左右站位稳定、同场景相邻 → 不得无故翻转左右面向。

随后是**强制收敛**（`site/content/docs/architecture/generation-workspace.md`），这是最关键的一层：

- guidance 会**自动补进最终 prompt**：若视频模板没有消费这些字段，系统在模板渲染结果后自动补一段"镜头执行约束"；**即使走手动 prompt 分支也照样补强**，避免手动文本完全绕过连续性与构图约束。
- **为防 prompt 膨胀，最多只保留 3 条**，优先级 `director_command_summary` > `continuity_guidance` > `screen_direction_guidance` > `composition_anchor`，并按 `frame_type` 动态微调：`first` 偏向保留 `composition_anchor`，`key`/`last` 偏向保留 `screen_direction_guidance`（"建立镜头先稳住空间，对峙/反打/收束镜头先稳住视线与左右轴线"）。
- 每步取舍带**可解释标签**：前端展示"最终 render prompt 保留了哪些 guidance、哪些被舍弃、每条被保留或压缩的原因"，并用短标签如 `首帧保空间`、`关键帧保轴线`，直接回答"为什么预览里有 4 条规则，最终只用 3 条"。

同一链路的字段纪律：镜头语义默认值（景别/机位/运镜/时长）与 `action_beats` 由提取阶段出候选、准备页人工确认，写回**同一份 `ShotDetail` 真值**；工作室里的微调也写回这份真值，"不是任务级临时覆盖"。`action_beats` 保持 `list[str]` 轻量形态，后端按关键词与相对位置推断 `trigger / peak / aftermath`：首帧消费 `trigger`、关键帧消费 `peak`、尾帧消费 `aftermath`；只有尚未确认拍点时才回退到 `script_excerpt + description` 的自然语言切片。同一组阶段信息**同时进入预览与调试上下文**，因此"编辑页看到的阶段标签"与"关键帧链实际使用的阶段"不会分叉。

**对 SD Film 的映射**：本 Skill 的镜头语言、转场、连续性知识远比它精细（`knowledge/camera_language/`、`knowledge/transitions/`），差距不在知识，而在落地机制的三点：guidance 是"生成"出来的（本 Skill 多数连续性纪律要求执行者在写 prompt 时想起来）；有硬性条数上限与优先级（本 Skill 缺"最多几条"的收敛纪律）；每条取舍可解释。这三点都是**减负**方向，不是加规则方向。

---

## 四、第四件事：把"生成前准备"建模成四层，消灭"预览与提交不一致"

`generation-workspace.md` 记录的统一四层模型，抽成共享类型（`backend/app/services/studio/generation/shared/types.py`）：

```text
Base Draft          → 可持久化、可编辑的业务真值
Context             → 本次生成依赖的动态上下文
Derived Preview     → 由 Base + Context 推导出的预览结果
Submission Payload  → 最终提交给模型的运行载荷
```

三链（`frame` / `video` / `asset_image`）各自实现 `build_base` / `build_context` / `derive_preview` / `build_submission`；前端用一个 hook 统一管理（`front/src/pages/aiStudio/hooks/useGenerationDraft.ts` 暴露 `base` / `context` / `derived` / `state` / `deriveNow` / `submitNow` / `hydrate` / `resetDerived`）。

它要解决的问题被明确写下来了：**"基础真值与最终提交内容混用、预览与提交使用的上下文不一致、页面内部状态散落（stale / loading / submit 语义混乱）"**。关键规矩是提交时 `submitNow()` 先确保 `derived` 最新再提交——**不允许存在"提交前手动再 render 一次"的旁路**。

**对 SD Film 的映射**：本 Skill 的 STATE-08 已区分"已确认资产/Clip Plan（真值）"与"最终 Prompt（提交物）"，但从未把"本次生成依赖的动态上下文"独立命名。最容易发生的事故正是它点名的第一种：把上游真值直接糊进最终 Prompt，之后无法判断某句话来自 Lock 还是临时发挥。四层的**命名价值大于实现价值**。

---

## 五、第五件事：LLM 输出的三层防御 + 定向重试

**三层防御**（`backend/app/chains/` 的 `agents` 基类，L133-343）：子类只固化 `prompt_template` / `output_model` / `system_prompt` 与一个 `_normalize` 钩子；调用优先走 structured output（`create_agent(response_format=…)`），失败退 `with_structured_output`，再失败退"原始文本 → 解析 → Pydantic 校验"。解析本身是六级容错链（剥 markdown 代码块 → 提取首个 JSON 片段 → 修中文引号/未加引号键名/尾逗号 → true/false/null 替换 → `ast.literal_eval` → kwargs 风格）。

配套的 schema 纪律（`backend/app/schemas/skills/`）值得单独记：所有 skill schema `extra="forbid"`，枚举一律 `Literal` 白名单，另配 EN→ZH 映射表给前端；`EvidenceSpan{chunk_id, start_char, end_char, quote}` 与 `Uncertainty{field_path, reason, evidence}` 贯穿对白、实体、变体、服装时间线。

**两个可直接借用的写法**：

1. **把提示词禁令降级为代码兜底**。画像 agent 的 `_normalize` 会**用代码删除**含"信息不详/未知"的句子——提示词里已经要求过不许写这类占位，但系统不依赖模型遵守，而是在代码层再吃一遍。
2. **质量闸 + 定向重试**（`backend/app/services/film/shot_frame_prompt_tasks.py`）：`_validate_generated_prompt`（L589）只查三件事——结果为空、混入图片映射说明（`## 图片内容说明` / `## 生成内容` / 行首 `图N：`）、缺少主角色名称；失败后 `_build_retry_guidance`（L604）把 issues 拼成 `请严格修正以下问题后重新生成：` + 列表**只重试一次**，仍不合格则取重试结果并清洗，同时把 `quality_checks` 与 `debug_context` 写进任务结果，供排查"为什么生成成这样"。

**它自己承认的短板**：最终产物 `StudioScriptExtractionDraft` **不含 evidence**——可追溯性止于中间产物，落库产物丢了溯源。这是反面教材，恰好印证本 Skill 的证据纪律：`EvidenceSpan` 若不贯穿到最终产物，等于没做。

**对 SD Film 的映射**：本 Skill 已有远比它完备的评分与硬门槛（`knowledge/quality/prompt_scorecard.md`），但那是 **Review 期的人工判定**。可在产物生成的那一刻插一个**三条以内**的确定性预检（空 / 混入非本阶段内容 / 遗漏已确认主体名），失败即带修正指令重试一次。成本极低，与既有 Gate 不冲突（它是生成前自检，不是审核结论）。

---

## 六、反模式：它自称做了、实际没做到的地方（这一节最值钱）

一个 6.4k star 的仓库照样会长期背着结构债。以下都是**代码实测**，不是文档转述。它们比正面模式更值得引以为戒。

| # | 反模式 | 实测证据 | 教训 |
|---|---|---|---|
| 1 | **门控只做了一半** | 批量生成有 readiness 硬门控（`ChapterStudio.tsx` 按 `readiness?.ready` 过滤并自动跳过）；**单镜头"生成视频"按钮无 readiness 门控**，只挡 loading / 比例 / 提示词 | 同一道门必须在**每一条入口**上成立。只挂在批量入口，等于给单发留了后门 |
| 2 | **两套门控、两个契约、互不校验** | `promptAssetReadiness` 是前端 `useMemo` 从资产总览推算（不调接口）；`videoReadiness` 走后端 `GET …/video-readiness`（7 项检查）。两者独立演进，前端推导的状态可以与后端判定矛盾 | 门控判据必须**单一 owner**。一旦允许界面层自己再算一遍，就有了两个真相 |
| 2b | **闭环只做了一半，回流方向退化** | "准备 → 生成"用客户端路由并携带焦点镜头（编辑页 `navigate(getChapterStudioPath(…), { state: { focusShotId, selectedShotIds } })`，工作室读同一份 `location.state` 完成选中闭环）；**反方向**却用整页跳转——工作室文件内 `useNavigate` 命中数为 0，回流写死在 `ChapterStudio.tsx:3689` 的 `window.location.assign("/projects/…/shots/…/edit")`，手写模板串、绕过路径构造函数、丢失 SPA 状态 | 闭环的两个方向必须共用同一套导航机制。**回流条款不能只规定"回哪去"，还要规定"带回什么状态"**——只做一半，用户就会在回来的路上丢掉上下文 |
| 2c | **同一闭合环路里混用两种导航范式** | 与 2b 同源：一侧 `navigate()`，一侧 `window.location.assign()` | 环路上的实现方式必须唯一；混用不会报错，只会在某一刻静默丢状态 |
| 3 | **迁移做了一半，旧路径烂在原地** | `chapter/ChapterPrep.tsx`（1387 行）已无路由、无 import，是死页面；`prep/usePrepFlow.ts` 是死代码（零消费方、零 Provider） | "新方案上线"不等于"旧方案下线"。没有删除动作的迁移会永久留下误读入口 |
| 4 | **口径宣布了，遗留还在用** | 规范写明"前端统一走 generated client，不再新增手写 service 封装"；实测 357 个源文件中仅 34 个引用 generated，`aiStudioApi.ts`、`http.ts`、`studioEntities.ts` 仍被 5 个页面使用 | 规范若无迁移清单与完成判据，就只是愿望 |
| 5 | **同一规则两处字面量** | 提交信息规则在 git hook 与 CI workflow 里各写一份；且 push 到 main 不受校验 | 与 #2 同源：重复的判据必然分叉 |
| 6 | **轮询裸奔** | 任务中心自递归 `setTimeout` 每 4000 ms 拉一次列表（recentSeconds=15 / pageSize=50），无退避、无 `visibilitychange` 暂停，异常分支直接 `setServerTasks([])` 造成列表抖动 | 任何"持续观察"机制都要有退避与降级，否则故障时放大器 |
| 7 | **前端零 CI** | 6 个 workflow 中只有 pylint 跑 backend，前端无类型检查门（项目自己却把 `tsc --noEmit` 写进完成定义） | 完成定义里的验证项，必须真的有人跑 |
| 8 | **设计理由只活在文档与 UI 文案里** | "准备页 / 工作室"拆分的理由在代码中**没有任何注释**，说明性文字只存在于 `site/content/docs/architecture/shot-page-boundary.md`、`AGENTS.md` 与 UI 文案三处，必须交叉阅读才能拼出全貌 | 关键职责边界必须在**离代码最近的地方**留一句理由。否则重构者只看到两个页面，看不到它们为什么被分开，边界就会回流 |

**结论**：Jellyfish 的架构文档质量明显高于它的落地完整度——文档描述了理想态，代码里留着半成品（死页面、双契约、双导航、双字面量、宣布未执行的规范）。**这正好是本 Skill 维护体系存在的理由**：`references/maintenance_self_check.md` 的"孤儿内容与不可达文件"、"Duplicate Rule Check"、"减法判定"三条，命中的就是上表 #2 / #3 / #4 / #5 这几类病；而 #2b / #2c / #8 指向的是另一类病——**边界被写下、却没被写进代码**，于是同一个闭环在两个方向上演化成了两套实现。它的价值不在"教会我们做什么"，而在"证明不做的代价"。

---

## 七、工程层：可看、不可搬的部分

以下事实都实际读到并确认，但**结论是"不要搬进 SD Film"**：

1. **异步任务系统**：业务任务真相层（`GenerationTask` / `GenerationTaskLink` / 查询接口）与执行层（Celery + Redis）分离；`celery_app` 明确 `task_ignore_result=True`、不用 result backend，Celery 只执行、不向前端暴露业务状态。执行器分两套模板：文本类走同步 LLM runtime，图片/视频/帧提示词走 async delegating executor（每次执行前重建 async runtime、结束后释放）。取消是**两级语义**：先置 `cancel_requested`，pending 直接终态；能强杀时叠加 `revoke(terminate=True)` 立即收敛业务状态，否则在**阶段边界**协作式取消——"超时语义是阶段边界超时，不是执行中强中断"。核心文本任务用**两阶段模型**：阶段 A 生成结果写进任务，阶段 B 再应用结果写业务表，于是"生成成功但落库失败"可被区分。**没有恢复语义**，只有 `_find_active_task` 去重。
   → 不迁移。唯一可带走的是"生成结果"与"应用结果"分离，以及"失败时业务状态先收敛，不必等强杀成功"。
2. **多供应商抽象**：契约（DTO 与 `ProviderConfig`）与协议适配单向依赖，能力校验集中在 capability 层（`resolve_*_capability` / `validate_*_options` / 模型前缀最长匹配），分派用 `(task_kind, provider_key)` 双键；新增供应商 ≈ 能力声明 + 适配器 + 注册两行，业务层零改动。默认模型由单例 `model_settings` 唯一拥有，未配置或模型不存在**直接 503 并指明 category**，绝不隐式回退默认值。
   → 不迁移实现。但两条可交叉印证本 Skill 既有纪律："**能力数值以各自 Adapter 为唯一真源**"（对应 `adapters/` 的 `O｜Operational Parameter`）；"**缺配置要显式报错，不要静默回退**"。它的漏点也值得记：`ProviderKey` 是硬编码 `Literal["openai","volcengine"]`——抽象做了一层，枚举却写死。
3. **契约单一事实来源**：API 变更后必须跑 `pnpm run openapi:update`，前端统一走 generated client（`front/openapi.json` 270 KB / 100 路径 → 240 models / 17 services / 138 methods）；状态语义变更后必须同步后端实现 / OpenAPI / generated types / 文档。
   → 不迁移机制。SD Film 的同构问题是"同一事实有唯一 owner，改动必须同步所有消费者"——可参照它的做法：把"改了什么之后必须同步什么"写成清单，而不是靠记忆。
4. **部署与 CI**：nginx 配置仅 17 行、**无 `/api` 反代**，前端靠运行时注入的 `window.__ENV.BACKEND_URL` 直连 8000（容器启动脚本由 nginx 官方 `/docker-entrypoint.d/` 自动执行）。
   → 与本 Skill 无关，仅作为"它并非处处完备"的旁证。

---

## 八、仓库治理：可借鉴的只有两条

Jellyfish 的文档治理值得记录，但**不要误以为它是升级**——本 Skill 的维护体系（`references/maintenance_self_check.md` + `maintenance_self_check_protocol.md` + `references/context_budget.md` + `references/recovery_guards.md`）在严格度上更高。可取者仅两条：

1. **文档四栏职责分离**（`AGENTS.md`）：`guide` = 怎么做、`architecture` = 现在是什么、`plans` = 接下来做什么、`reference` = 查什么；且规定"架构已落地但文档未更新，视为未完成"、"架构文档只记录当前真实生效的实现，不混入未来计划"。与本 Skill 的 owner 唯一性、减法判定同源——但注意第六节已证明：**这条规则它自己也没完全做到**（架构文档描述的理想态与代码里的死页面/双契约并存）。
2. **边界规则要写"回流条款"**：它不只说"编辑页负责准备、工作室负责生成"，还写明"工作室若保留提取能力，只能作为快捷入口或诊断入口，不应重新成为主入口"、"发现未 ready 时明确引导回编辑页"。**边界规则只说"谁负责什么"是不够的，还要说"越界和回流时怎么办"**——而且按第六节 #2b，回流条款还必须写明**带回哪些状态**，否则规则成立、实现仍会把上下文丢在路上。

Release note 的固定章节结构（`Highlights`/`Added`/`Changed`/`Breaking Changes`/`Migration Guide`/`Validation Commands` 等按需裁剪但顺序不变）对本 Skill 用处有限——本 Skill 的版本递增是一次定稿动作，不发版。可借用的只有一句口径：**验证命令必须可直接执行。**

---

## 九、给 SD Film 的候选迁移项（按性价比排序，均需用户确认后才可落地）

| # | 候选 | 目标 owner（待确认） | 性质 | 风险 |
|---|---|---|---|---|
| 1 | 生成前三条确定性预检（空 / 混入非本阶段内容 / 遗漏已确认主体名）+ 单次定向重试 | `knowledge/quality/`（生成时自检） | 新增轻量机制 | 低；与既有 Hard Gate 不冲突 |
| 2 | guidance 收敛纪律：同类约束在最终 Prompt 中最多保留 3 条 + 优先级 + 按帧类型微调 + 取舍可解释 | `knowledge/prompt_compilation/state08_projection.md` | 补入既有 owner | 中；须核对既有优先级口径 |
| 3 | "四层命名"（真值 / 上下文 / 派生预览 / 提交载荷）作为一处具名说明 | `knowledge/prompt_compilation/` 或 `references/` | 新增命名，不新增流程 | 低 |
| 4 | 完成门禁增补"可机械核对的检查项清单"（每条带修复指引） | `rules/completion_gate.md` | 增强既有规则 | 中；须避免与 18 项自检重复 |
| 5 | 边界规则的"回流条款"写法 | 各自模块 owner | 写法借鉴 | 低 |
| 6 | 把"证据必须贯穿到最终产物"写成一条显式纪律（反面案例见第五节短板） | `rules/` 或 `references/` 证据纪律既有 owner | 强化既有 | 低；须先确认是否已被覆盖 |

**明确不建议迁移**：异步任务/队列/数据库/前端工作台/OpenAPI 生成链、Celery 取消语义、供应商适配实现、结构化输出解析链、双引擎与运行时重建。SD Film 的价值恰恰来自"纯文本、无外部依赖、换环境也能跑"（`SKILL.md` 的 Self-Maintenance 明文要求），引入任何一层运行时依赖都会破坏这条不变量。

---

## 证据与自我限制

- 结论来自**直接阅读或逐条核对**，并由两个独立深读任务交叉取证：仓库 README 与 GitHub API 元数据、`AGENTS.md`、`site/content/docs/architecture/` 的 `task-execution` / `shot-status-flow` / `shot-frame-prompt-generation` / `generation-workspace` / `llm-default-model-resolution` / `shot-page-boundary` / `project-structure`、`site/content/product/workflow.md` 与 `roadmap.md`、`site/content/blog/v0-3-2.md`、`backend/app/chains/`（`agents` 的 `base`）、`backend/app/schemas/skills/common.py`、`backend/app/services/studio/shot_video_readiness.py`、`backend/app/services/studio/shot_preparation_state.py`、`backend/app/services/studio/shot_video_prompt_pack.py`（部分）、`backend/app/services/film/shot_frame_prompt_tasks.py`（部分），以及第六节各项反模式对应的前端与 CI 文件。
- **已发现的文档与代码不一致**（记录在此，供后续引用时警惕）：`backend/README.md` 提到 LangGraph，但 `chains/` 下只有 `agents`，无 graphs 模块；`backend/AGENTS_OVERVIEW.md`、`SCRIPT_PROCESSING_AGENTS.md`、`SCRIPT_PROCESSING_API.md` 均为 **0 字节空文件**。
- **未验证**：Jellyfish 的运行时行为（未安装、未启动、未跑测试）；未做全库代码级对账，因此"文档与代码不一致"只在已核对的点上成立，不代表已普查。
- 星标、活跃度等数字是**阅读日快照**，会变化，不作为任何判断依据。
