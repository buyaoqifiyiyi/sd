# SD Film

**AI 影视虚拟制片生产系统** · Skill Version 2026.09.15-r96

不是 Prompt 生成工具，是一条真实影视制作流水线：从一句创意或一份剧本，走到可直接投喂 Seedance 的成片级视频 Prompt。全程不跳阶段，已确认的工件事后不重做。

> **本文件是面向人的能力导览，属于非运行时文件。** 它未被任何 Workflow 列为 Required Resource，不参与运行时读取，也不是规则、恢复、路由或 Schema 的来源；运行时权威是 `SKILL.md`、`rules/`、`workflows/`、`knowledge/`、`references/` 与 `templates/`，当前安装版本只看 `SKILL.md` 的 `Skill Version` 与 `Build ID`。本文件只做入口导航，不复制任何规则、字段或判据；想看怎么下指令、会在哪一步停下等确认，查 `USER_GUIDE.md`。

以下内容属于**Skill维护层**：只在你要了解或改动这套 Skill 本身时阅读，运行任何 Workflow 都不需要读它。

---

## 它能做什么

- **写剧本**：一句创意 / Brief / 品牌需求 → 可导演剧本；已有剧本则先诊断、分类，再做改编或优化，最后锁定 Production-Locked
- **管资产**：把角色、环境、道具、FX 建成带版本与 Canonical Reference 的资产，保证跨镜头不漂移
- **定视觉**：美术风格、色彩体系、光影方向、摄影基调、表演尺度、声音原则一次建立
- **设计镜头**：专业分镜脚本——TC IN / OUT、景别、焦段、分层构图、人物动作链、机位调度、台词声音
- **拆 Clip**：Shot 是导演设计单位，Clip 是 AI 生成单位，按模型时长窗口整合成 CLIP-001……
- **出 Prompt**：每个 Clip 一条连续 Prompt，按已确认资产与分镜编译，模型专属模板
- **拉片**：参考片的运镜、机位、镜头语言分析，风格反编译（"学习这个视频怎么拍"即触发）
- **配画面**：海报、Key Art、封面（带视觉母题与字体层级）
- **配声音**：角色音色资产、SeedMusic 配乐与 Cue Sheet（均需显式调用）

---

## 主流程

| 阶段 | 干什么 | 产出 |
|---|---|---|
| STATE-00 立项 | 建立项目身份与状态入口 | Project Root、最小项目事实 |
| STATE-01 剧本 | 生成 / 诊断 / 改编 / 优化 | Production-Locked 可导演剧本 |
| STATE-02 资产发现 | 分类需求 | CHAR / ENV / PROP / FX 清单 |
| STATE-03 资产制作 | Prompt → 出图 → 图片确认 | 已锁定的 Canonical 视觉资产 |
| STATE-04 视觉开发 | 建立项目视觉方向 | Visual Direction（内部） |
| STATE-05 场景拆解 | Scene / Sequence / Unit | 生产拆解结构 |
| STATE-06 详细镜头设计 | 逐镜设计 | Confirmed 专业分镜脚本 |
| STATE-07 Clip 整合 | 按模型窗口组织 | Confirmed Clip Production Plan |
| STATE-08 视频 Prompt | 编译并校验 | 最终 Prompt + 生产交付包 |
| STATE-09 审核 | 审成片（显式调用） | PASS / REVISE / REBUILD |

后续阶段必须有可验证的前置工件与 Completion Gate 证据。

---

## 支持的模型

| 类型 | 可选 | 关键边界 |
|---|---|---|
| 视频 | Seedance 2.0 | 4—15 秒，最多 9 张视觉参考 |
| 视频 | Seedance 2.5 | 4—30 秒，图片 ≤30 / 视频 ≤10 / 音频 ≤10 / 合计 ≤50 |
| 视频 | MiniMax H3 | 4—15 秒，全能参考 9 图 / 3 视频 / 3 音频 |
| 图像 | GPT Image / Midjourney | 各自独立 Prompt 模板，互不污染 |

未验证的模型不继承 Seedance 能力；Dreamina 网页端专有能力只在用户显式选择该入口时成立。

---

## 辅助能力（显式调用）

| 能力 | 触发方式 | 边界 |
|---|---|---|
| Storyboard | 明确要求分镜 | 可选辅助，不占 STATE |
| Spatial Blocking | 需要空间 / 走位关系 | `REF-SKETCH` 只控空间与机位，不成为角色资产 |
| AUDIO / SeedAudio | 要求做音色 | 文字型 Voice Profile，不创建视觉 Asset ID |
| MUSIC / SeedMusic | 要求配乐规划 | 默认纯音乐，与视频 Prompt 永久隔离 |
| Poster / Key Art | 要求海报封面 | 不进入主 Pipeline |
| Editing / Series | 要求剪辑或系列管理 | Editing 不作为独立 STATE |

---

## 硬性纪律

- **已确认工件不重做**：剧本、资产、分镜一旦确认即锁定；只有用户明确要求变更整体风格或走 Change Protocol 才新建 Revision
- **视频 Prompt 永久禁止 BGM**：配乐只能走独立 MUSIC 模块；Dreamina 网页端能力不得误报为 API 能力
- **项目数据只写独立 Project Root**：本目录只保存通用定义，不是项目仓库；根目录的同名文件是兼容入口
- **越级禁止**：不得跳过 STATE 直接出资产、分镜表、Clip 表或视频 Prompt

---

## 怎么用

触发词：`调用sd`、`用SD Film`、`继续之前的项目`、`重新调用sd`、`恢复旧项目`；也可以直接丢创意、剧本、大纲、小说章节。

- 新项目：Skill 在 STATE-00 登记事实后，同一响应内进入 STATE-01 交付剧本提案
- 已有项目：给出 Project ID 或项目目录即可恢复，按 `Last Successful Checkpoint` 续作
- 自动推进：只有你明确启用 `FAST` 时才自动确认；它只压缩确认往返，不减阶段、QA 与交付物
- 空跑演练：说"跑流程测试 / 演练 / dry run"只验证路由与 Gate，不产出交付物
- 独立调用：点名一个辅助模块或一个主阶段单独跑（如"只做 STATE-06 分镜表，别推进后面的阶段"）。它仍要满足自己的前置输入，产物照常确认、登记、进包与复用，但**不计入项目进度**——`Completed States` 与"下一步"都不会因此前进

---

## 想深入看

| 你要找的 | 入口 |
|---|---|
| Skill 入口与全局不变量 | `SKILL.md` |
| 运行默认值、索引与开关 | `config.md` |
| 阶段路由与边界 | `workflows/workflow_map.md` |
| 项目状态字段与写回 | `references/project_state_contract.md` |
| 项目目录与恢复 | `references/project_workspace.md` |
| 资产身份与版本锁 | `references/asset_lock_contract.md` |
| 交付包与文件命名 | `references/asset_package.md` |
| 用户手册 | `USER_GUIDE.md` |
| 能力总览 | `index.md` |
