# SD Film 使用说明书

这是一份面向用户的“怎么用”手册。想知道某件事该怎么下指令、SD Film 会做什么、会在哪一步停下来等确认，直接查本文件即可。

内部 Pipeline、字段权威和开发规则仍以 `SKILL.md`、`rules/`、`workflows/`、`references/` 与 `templates/` 为准；当前安装版本只看 `SKILL.md` 中的 `Skill Version` 和 `Build ID`。

## 默认导演系统

SD Film现在默认由`Director Module / Director Intelligence Layer`贯穿剧本→视觉→场景→镜头→Clip→Prompt→Editing→Review。它从“这段戏为什么存在、观众先知道/感受什么、人物关系怎样变化”开始，再让镜头语言承担构图、景别、机位、焦段/距离、前中后景、遮挡/揭示、运镜触发与Hold / Cut节奏。最终Seedance Prompt仍使用原有模板，不会多出一整套导演分析字段。

正常调用方式不变：继续使用`调用sd`开始或路由，使用`下一步 / 继续`从当前Checkpoint推进。普通“下一步”不会无意义全量reload。

在Codex中需要确定性启动时使用`$sd-film`。在当前用户客户端的普通Chat中，`@`选择器只显示Plugin，本机独立SD Film没有以`@`选择显示名的入口；`agents/openai.yaml`也不会把它注册成Plugin。普通Chat只有在宿主实际暴露本机Skills时，才可能通过`调用sd`等自然语言隐式选择。Skill更新后若Codex旧会话没有刷新，先重启桌面应用或新建Codex任务再试。移动到`.agents/skills`能改善Codex本地发现，但不能突破普通Chat、网页端或移动端的宿主边界。

如需查看内部方向，可以说：`显示当前Scene的导演意图`、`为什么这样拍`或`显示这个Clip的镜头语言策略`。Skill只会给简洁摘要，不会把完整内部Packet塞进最终Prompt。

## 先记住这条万能公式

```text
调用sd + 我要做什么 + 当前输入 + 必须保持什么 + 重点优化什么 + 做到哪一步停
```

### 已有资产快速通道

如果项目目录已有角色、环境、道具或FX图片，可以直接说“使用现有资产”或“跳过制作阶段”。SD Film会只核验当前对象，将文件登记为Candidate Reference，并请求你确认；确认后才升级为Canonical Reference与Active Version。该路径不会重复生成图片，但不会省略资产确认和一致性锁定。

例如：

```text
调用sd，根据这个已定稿剧本进入完整视频制作流程。不要修改剧情和人物关系，重点保证角色、空间与道具连续性。项目启动和状态记录在内部完成；默认只给我剧本、设定资源、分镜表、Clip表和最终提示词。
```

## 快速索引

| 任务 | 你可以直接这样说 | 默认进入 / 调用模块 |
|---|---|---|
| 完整视频 | `调用sd，根据这个剧本进入完整视频制作流程。` | STATE-00 → STATE-09 主流程 |
| 从创意写剧本 | `调用sd，我只有一个故事概念，直接从剧本开始。` | STATE-01 Screenplay Generation branch |
| 品牌需求写短片 | `调用sd，根据这个品牌需求写一支宣传短片，先完成剧本提案。` | STATE-01 Screenplay Generation branch |
| 剧本优化 | `调用sd，分析这个剧本并给出优化机会报告，先不要改写。` | STATE-01 Script Analysis |
| 定稿剧本直接制作 | `调用sd，这个剧本已经定稿，不要修改剧情，直接进入制作。` | STATE-01 No Revision / Final Script 路由 |
| 资产缺失检查 | `调用sd，只检查当前项目缺少哪些角色、环境、道具和正式FX资产，不生成图片。` | STATE-02 Asset Discovery / 状态核验 |
| 角色资产 | `调用sd，只制作CHAR-001角色视觉资产，先输出生图提示词，等我确认。` | STATE-03 Character Asset |
| 环境资产 | `调用sd，只制作ENV-001环境资产，先输出生图提示词，等我确认。` | STATE-03 Environment Asset |
| 道具资产 | `调用sd，只制作PROP-001道具资产，先输出生图提示词，等我确认。` | STATE-03 Prop Asset |
| 角色音色 | `调用sd，为CHAR-001设计角色音色，并输出独立Seed Audio兼容提示词。` | AUDIO / SEED-AUDIO 可选模块 |
| 配乐 | `调用sd，为整条片子规划配乐与留白，并输出需要的SeedMusic纯音乐提示词。` | MUSIC / SEED-MUSIC 可选模块 |
| 专业分镜 | `调用sd，根据已确认场景和资产制作Professional Detailed Shot Script。` | STATE-06 Detailed Shot Design |
| Storyboard | `调用sd，根据已确认Detailed Shot Design制作Storyboard。` | Optional Storyboard |
| Shot组合为Clip | `调用sd，把已确认的Detailed Shot Design组织为4—15秒Clip。` | STATE-07 Clip Production |
| 单个Clip Prompt | `调用sd，只输出CLIP-003的Seedance视频提示词。` | STATE-08 单Clip交付 |
| 全部Clip Prompt | `调用sd，按顺序输出全部Confirmed Clip的完整Seedance视频提示词；过长就按完整Clip自动分批。` | STATE-08 批量交付 |
| 下一个Clip | `调用sd，下一个Clip。` | STATE-08 下一个未交付Clip |
| Clip返修 | `调用sd，只修CLIP-003的站位错误，其他内容和字段保持不变。` | STATE-08最小修订或对应上游Return Route |
| 连续性检查 | `调用sd，只检查CLIP-002到CLIP-003的角色、站位、道具、轴线和首尾帧连续性，不重新生成。` | STATE-07 / STATE-09连续性核验 |
| Review | `调用sd，审核这个实际生成结果，给出PASS / REVISE / REBUILD、KEEP / RE-EDIT / REGENERATE / REDIRECT和最小返修方案。` | STATE-09 Technical + Director's Cut Review |
| 技能经验 | `调用sd，Review后提出可跨项目复用的经验候选，等我确认后再写入Skill。` | Skill Experience候选确认机制 |
| 电影海报 / Key Art | `调用sd，根据当前项目设计一张9:16数字竖版电影Key Art，沿用现有角色和环境资产。` | Poster Design辅助Workflow |
| 继续旧项目 | `重新调用sd，恢复当前项目，从最后一个安全Checkpoint继续。` | Runtime Reload + Legacy Project Recovery + Project Resume |
| 检查Skill | `调用sd，只检查当前实际安装版的Pipeline、STATE和音色规则，不执行制作。` | Runtime Reload + 只读规则检查 |
| 修改Skill | `进入Work，读取当前实际安装的sd Skill，只修改我指定的规则，并同步版本、回归检查和USER_GUIDE.md。` | Work / Codex本地修改任务 |

## SD Film 什么时候会停下来

常见停止点如下：

1. 新项目首次进入时，项目初始化和`Creation Brief / Existing Script / Material`入口登记在内部完成，不会展示项目登记页、搜索类似项目或越级输出分镜、Clip或视频 Prompt。
2. 只有创意并明确要写剧本时，STATE-01直接生成`Production Script Proposal`，不要求你先去普通Chat写完整剧本，也不先对不存在的剧本做优化机会报告。
3. 上传已有剧本/来源材料时，默认先给 `Optimization Opportunity Report`，等你决定锁定、轻度优化或结构优化；如果当前指令已明确“直接优化 / 直接改写”，不会重复询问是否优化。
4. 任一创作或优化分支生成 `Production Script Proposal` 后都会停下来，等你确认制作版剧本。
5. 每类视觉资产先给生图 Prompt，等你确认；生成候选图后再停一次，等你确认图片。
6. STATE-06 若复杂空间需要俯视 Blocking Map，可能先给地图 Prompt，等你确认后再生成图；不需要图或工具不可用时可使用完整文字 Blocking。
7. Clip Plan、分镜或其他需要明确确认的生产成果未确认时，不会擅自标为 Confirmed。
8. 长视频 A / B 接续模式缺少上一 Clip 尾帧时，Prompt 可以先交付，但真正提交生成前会要求你补入尾帧。
9. 单个Clip在最终Prompt前若被判定需要Visual Blocking Sketch，本轮会先给你经验证的调度草图、注册名与用途说明，暂停Prompt；你下次说“继续 / 下一个”时再输出该Clip Prompt。简单Clip不会为了统一流程强制出草图。
10. Review同时区分Technical Review与Director's Cut Review，并在兼容的`PASS / REVISE / REBUILD`外给出`KEEP / RE-EDIT / REGENERATE / REDIRECT`处置。技术正确但信息或情绪提前暴露仍会返修；修复后必须重新Review。
11. Review或失败复盘后，系统可以自动提出跨项目技能经验候选；候选不会自动写入Skill。只有你明确确认后才入库，并在适用条件满足时影响后续产出或形成项目迭代建议。经验不能直接覆盖已确认剧情、资产、镜头、Clip或Prompt，项目修改仍经过对应流程与确认。

---

## 1）完整制作一个视频

**最简指令**

```text
调用sd，根据这个剧本进入完整视频制作流程。
```

**进阶指令**

```text
调用sd，根据这个剧本制作一条9:16真人剧情短片。保持核心剧情、人物关系和结局不变，重点保证角色外貌、空间轴线、道具和跨Clip连续性。按STATE-00到STATE-09推进，每遇到剧本决策、资产Prompt、候选图片、Clip Plan或返修决定时停下来等我确认；STATE-08默认逐个Clip输出。
```

**Skill 行为 / 停止点**

- 固定主流程是 `STATE-00 Project Setup → STATE-01 Script Analysis → STATE-02 Asset Discovery → STATE-03 Asset Development → STATE-04 Visual Development → STATE-05 Scene Breakdown → STATE-06 Detailed Shot Design → STATE-07 Clip Production → STATE-08 Video Prompt / Generation → STATE-09 Review`。
- “我要最终视频”只表示目标，不表示可以跳过前置阶段。
- 新项目首次响应静默完成项目确认、初始化和输入分析准备，并直接交付当前合法的剧本阶段成果。
- Storyboard、角色音色和配乐都不是主流程必经步骤，只有显式请求才进入对应辅助模块。
- STATE-08 默认一次输出一个尚未交付的 Clip；想一次拿全部，必须明确说“全部 / 批量 / 连续输出多个”。

## 2）只有故事概念，先开发剧本

**最简指令**

```text
调用sd，我只有一个故事概念，先开发剧本。
```

也可以直接说：

```text
调用sd，帮我写一个雨夜双女主重逢短片。
```

```text
调用sd，根据这个品牌需求写一支宣传短片，先从剧本开始。
```

**进阶指令**

```text
调用sd，把这个故事概念开发成一条3分钟竖屏剧情片的可制作剧本。必须保留核心人物、世界观和结局；先建立人物目的、因果、冲突、关系弧、潜台词、Writer Beat、信息策略和Setup / Payoff，再由导演模块建立观众体验与可见表演方向。完成完整剧本提案后停下来等我确认。不要提前写分镜、焦段或运镜。
```

**Skill 行为 / 停止点**

- 只有Idea / Brief且明确要求写剧本时，会被识别为 `Creation Brief`，STATE-01直接进入Screenplay Generation，不要求你先提供完整剧本。
- SD Film现在默认同时包含Screenwriter Module与Director Module。Screenwriter负责故事、人物、因果、潜台词、Writer Beat、Setup / Payoff和信息架构；Director负责观众体验、表演调度、空间、镜头语言、构图、运镜与呈现节奏。
- 两者通过内部Writer → Director Handoff衔接；用户不需要填写完整WRITER INTENT PACKET，最终交付仍是可独立阅读的剧本。
- `Writer Beat ≠ Shot`。Writer只确定人物/剧情状态发生了什么变化；一个Beat用一个或多个Shot、或多个Beat用一个长镜头，由Director决定。
- 这不等于提前写分镜；35mm、推镜、特写、摇镜、机位、SHOT / CLIP仍留给后续Director / STATE-06/07。
- 剧本内部会经过Directable Screenplay QA，但最终交给你的仍是可独立阅读的剧本，不是十项分析报告。
- Proposal 输出后会停下；只有你明确确认，才成为 `Production-Locked Directable Screenplay`并进入后续资产阶段。
- 你说“修改这一场”时会保持在Script Development，只改该场与必要相邻因果，不会跳到Shot Design。
- 只有当缺失信息会实质改变故事架构或造成品牌/事实风险时，Skill才会询问最小必要问题；其他可安全信息会用清楚、可修订的假设继续。

如果你提供的是小说章节、已有故事梗概、品牌文案或其他要保留/转换的叙事正文，它属于`Existing Script / Material`，仍会先诊断并保护来源事实，不会冒充从零创作。

## 3）分析 / 优化 / 改写剧本

**最简指令**

```text
调用sd，分析并优化这个剧本。
```

如果你不想在诊断后重复确认是否优化，可以明确说：

```text
调用sd，直接优化这个剧本；保持世界观、人物身份和结局，完成Production Script Proposal后停下来等我确认。
```

**更稳妥的两步指令**

```text
第一步：调用sd，分析这个剧本并给出优化机会报告，先不要改写。
第二步：调用sd，按刚才的B档建议执行轻度优化，只改台词效率、动作可视化和节奏，不改世界观、人物身份和结局。
```

**进阶指令**

```text
调用sd，只优化第二场和第三场：压缩重复信息，让冲突更早进入，把不可拍的心理描写转成可见动作。其他场次保持原文，不要顺手润色。完成Production Script Proposal后停下来等我确认。
```

**Skill 行为 / 停止点**

- 只要求分析、没有明确允许改写时，会先评为 A（无明显优化必要）、B（轻度优化空间）或 C（明显结构问题），然后停在 User Decision Gate。
- 已有剧本会先检查因果、人物动机、场景价值变化、Writer Beat推进、冲突/风险、潜台词、Setup / Payoff、人物/关系弧、结局回收与信息架构；不会默认改写。
- 可直接说“显示编剧意图”“为什么人物这么做”或“检查潜台词”。这些只展开必要的Writer分析，不改变当前剧本确认边界。
- 如果当前指令已经明确“分析并优化 / 直接优化 / 直接改写 / 只优化某一场”，这已构成改写授权；Skill仍先保留诊断依据，但不会重复问你是否要优化。最终Proposal仍必须由你确认。
- 单独说“继续”“好的”“下一步”不等于授权改写，也不等于确认 Proposal。
- 局部优化只改指定范围；若必须影响相邻内容，会先列为待决定项。
- 改写后仍需你明确确认当前 Proposal，才能锁定并进入资产阶段。

## 4）剧本已定稿，禁止修改，直接制作

**最简指令**

```text
调用sd，这个剧本已经定稿，不要修改剧情，直接进入制作。
```

**进阶指令**

```text
调用sd，这个版本是最终定稿。禁止修改剧情、台词、人物关系、世界观和结局；只做制作分析并把原稿锁定为Production-Locked Script，然后进入资产发现。发现事实矛盾时只列出问题，不要静默修复。
```

**Skill 行为 / 停止点**

- 进入 `No Revision / Final Script` 路由，跳过优化机会报告和内容改写。
- 仍会进行故事、人物、环境、视觉元素和制作风险分析。
- 原稿按你的明确授权直接锁定；真正无法支持制作的矛盾会列为 Pending Decision，不会擅自改稿。

## 5）角色资产制作

**最简指令**

```text
调用sd，只制作CHAR-001角色视觉资产。
```

**进阶指令**

```text
调用sd，只制作CHAR-001角色视觉资产。沿用当前剧本和Visual Direction，锁定脸型、年龄感、身体比例、发型、服装形制和配色。先输出当前Revision的完整生图Prompt，停下来等我确认；不要自动生成图片，也不要设计音色。
```

**Skill 行为 / 停止点**

- 必须先有 STATE-02 的角色资产需求和 `Core / Support` 分层。
- Core 角色通常制作独立三视图、面部特写和确有剧情需要的状态变体；Support 角色进入同类型 Reference Board，不逐个做完整套图。
- 固定双确认：`Prompt Draft → 你确认Prompt → 生成候选图 → 你确认图片 → 登记Active / Canonical资产`。
- 角色有对白不会自动触发音色模块。

## 6）环境资产制作

**最简指令**

```text
调用sd，只制作ENV-001环境资产。
```

**进阶指令**

```text
调用sd，为ENV-001制作可重复拍摄的环境资产，锁定空间结构、入口、主要活动区、关键家具、材质和主光方向。先给主参考图与必要多视角Prompt，等我确认后再生成图片。
```

**Skill 行为 / 停止点**

- Core 环境建立主参考图、必要多视角和关键区域 / 细节；Support 环境按同类 Board 组织。
- 环境不是“漂亮背景”，必须能支持人物行动与空间连续性。
- 同样执行 Prompt 确认和图片确认两道 Gate；候选图未经确认不能成为 Canonical 环境资产。

## 7）道具资产制作

**最简指令**

```text
调用sd，只制作PROP-001道具资产。
```

**进阶指令**

```text
调用sd，为PROP-001制作道具资产。锁定整体形态、尺寸比例、结构、材质和关键识别细节；只为剧本已确认的开合、破损和使用状态制作变体。先输出生图Prompt，等我确认。
```

**Skill 行为 / 停止点**

- Core 道具可包含主参考图、必要状态 / 细节图，以及确有需要的使用关系图；Support 道具进入同类 Board。
- 不能用下游 Prompt 临时重设计正式道具。
- 仍需两次明确确认：先 Prompt，后图片。

## 8）资产缺失检查

**最简指令**

```text
调用sd，只检查当前项目缺少哪些资产，不生成图片。
```

**进阶指令**

```text
调用sd，核对Production-Locked Script、Asset Registry和当前State，只检查CHAR、ENV、PROP和正式FX：列出缺失、未确认、版本冲突、Support Board缺项和会阻塞后续阶段的资产；不要制作资产，不要生成Prompt或图片。
```

**Skill 行为 / 停止点**

- 会区分“未发现”“已登记但未确认”“Prompt已确认但图片未确认”“Active / Canonical版本冲突”等状态。
- 角色音色不属于视觉资产缺失 Gate：默认不检查、不补建、不写 Not Applicable，也不阻塞 STATE-03 或 STATE-08。
- 配乐同样不是资产缺失项，除非你显式请求独立 Music 模块。

## 9）角色音色模块（显式调用才启动）

**最简指令**

```text
调用sd，为CHAR-001设计角色音色，并输出独立Seed Audio兼容提示词。
```

**进阶指令**

```text
调用sd，为CHAR-001建立长期稳定的Voice Profile，并为这句台词输出独立Seed Audio兼容提示词。把稳定声音身份与本句Dialogue Performance分开；只输出Prompt，不生成音频。未知口音不要猜。
```

**如果你确实要把声音控制写进当前视频模型 Prompt**

```text
调用sd，只在CLIP-003这次Seedance视频Prompt中使用已确认的VOICE-REF-01做声音控制，按最小Delta写入；不要复制完整Voice Profile，也不要把授权延续到后续Clip。
```

**Skill 行为 / 停止点**

- 默认不启动：普通视频、角色分析、角色视觉资产、Detailed Shot、Storyboard、Clip、Seedance、对白、口型、音效、“继续”或“下一个”都不会自动制作音色。
- 未显式调用时，默认外部已有可用角色音色资源；不检查缺失、不提示补建、不形成 Asset Gate。
- 常规 STATE-08 视频 Prompt 默认完全不出现 `音色特征：`、Voice Profile、Voice / Audio Reference 或“已有 / 缺少音色”等文字。
- 显式调用后输出独立 AUDIO / SEED-AUDIO Package。当前结构是“基于 Seed Audio 官方支持维度整理的 SD Film 兼容模板”，不是官方唯一字段格式。
- Voice Identity 与当前一句的情绪、停顿、力度、韵律分开；Ambience、Key Sound Effects、Scene Progression 只在场景级声音任务需要时出现。
- 只要求 Prompt 时，交付 Prompt 后即停止；只有你同时明确要求实际音频且工具与授权条件满足时，才生成候选音频。

## 10）配乐 / BGM / 声音设计

### A. 对白、环境声、动作声、Foley 等同期声音

**最简指令**

```text
调用sd，只优化CLIP-003的同期声音设计：对白、环境声、动作声、Foley和声音尾部，不要设计配乐。
```

“声音设计”如果语义更像对白、同期声或音效，不会自动触发角色音色，也不会自动触发 Music 模块。

### B. 后期配乐 / BGM / SeedMusic

**最简指令**

```text
调用sd，为整条片子规划配乐与留白。
```

**进阶指令**

```text
调用sd，审阅全部Confirmed Clip，为整条片子做Music Spotting、Music Bible和Cue Sheet，并为实际需要音乐的Cue输出SeedMusic纯音乐提示词。由你专业判断哪里进音乐、哪里只保留同期声；不要全片持续铺乐。
```

**Skill 行为 / 停止点**

- Music 模块只在你明确要求配乐规划、Cue Sheet、主题动机、SeedMusic Prompt等交付物时启动。
- 默认是纯音乐；歌词、演唱、合唱、哼唱、吟唱或 Vocalise 必须另行明确要求。
- 即使你同时要求视频 Prompt 和配乐，也会拆成两个独立 Package。
- STATE-08 视频 Prompt 永久禁止非剧情内配乐；配乐只能进入独立 MUSIC / SEED-MUSIC Package，不能混写进视频 Prompt。
- Music 模块会同时设计音乐与留白，不会把“全片配乐”理解成每个 Clip 都持续有音乐。

## 11）Detailed Shot Design / 专业分镜设计

**最简指令**

```text
调用sd，根据已确认场景和资产制作Professional Detailed Shot Script。
```

**进阶指令**

```text
调用sd，为SCENE-003制作Professional Detailed Shot Script。先完成Spatial Blocking Decision，锁定角色起终点、移动路径、180度轴线、机位侧和关键道具位置；再逐镜完整设计时间码、构图、表演、镜头调度、光色、同期声音、首尾边界和下一镜Handoff。不要输出Seedance Prompt。
```

**Skill 行为 / 停止点**

- 必须已有 Scene Breakdown、必要资产和 Visual Direction；不足时会返回事实拥有者，不靠分镜文字补造。
- 复杂多人、打斗、追逐、进出场或严格轴线场景会优先使用“俯视 Blocking Map + 文字规则”双锁；如需生成地图图像，会先给地图 Prompt 等确认。
- 正式输出是完整 Professional Detailed Shot Script，不是“景别 + 运镜 + 画面”简表。
- 单镜和批量字段完全相同；过长时默认按每批约 4—5 个完整 Shot 分批，不会压缩字段或写“同上”。
- STATE-06 不输出 Seedance Prompt，也不提前创建 Clip ID。

## 12）Storyboard 分镜板

**最简指令**

```text
调用sd，根据已确认Detailed Shot Design制作Storyboard。
```

**进阶指令**

```text
调用sd，把SHOT-001到SHOT-006制作成16:9 Storyboard，每镜一个画格，保留Shot ID、构图、人物空间关系、关键动作状态和边界注记。不要改变镜头设计，也不要把Storyboard作为视频参考资产。
```

**Skill 行为 / 停止点**

- Storyboard 只有你显式请求时才启动，是可选辅助产物，不是 STATE。
- 前置条件是已确认 Detailed Shot Design 和必要资产。
- 它不替代 STATE-07 Clip Production，不参与 Clip 划分，也不是进入 STATE-08 的必要条件。
- Storyboard 图片、多格拼图、线稿或截图不能成为 STATE-08 Canonical Reference。

## 13）把 Shot 组合为 Clip

**最简指令**

```text
调用sd，把已确认的Detailed Shot Design组织为Clip。
```

**进阶指令**

```text
调用sd，把当前Confirmed Detailed Shot Design按正式Shot顺序组织为4—15秒Clip。不要改Shot ID、顺序、剧情或镜头目的；逐Clip完成Preflight、Scope Firewall、End-State Record、Reference Routing、尾帧A/B/C判定和不超过9张的参考预算。输出Clip Plan后停下来给我确认。
```

**Skill 行为 / 停止点**

- 只能基于实际可读且 Confirmed 的 Professional Detailed Shot Script；原剧本中的“镜头1 / Clip A”等标题不能直接变成正式 Clip。
- 一个 Clip 可以包含一个或多个相邻、兼容的 Shot，目标时长必须为 4—15 秒。
- 每个正式 Shot 按原顺序且只进入一个 Clip；不能为减少数量强行合并。
- 每个 Clip 原则上只承担一个主要可见 Beat。此前事件不重播，后续事件不提前表演。
- Clip Plan 不输出最终 Seedance Prompt；确认后才进入 STATE-08。

## 14）生成单个或全部 Seedance Clip Prompt

### 单个 Clip

```text
调用sd，只输出CLIP-003的Seedance视频提示词。
```

### 全部 Clip

```text
调用sd，按顺序输出全部Confirmed Clip的完整Seedance视频提示词；过长时只在完整Clip之间自动分批，不要压缩字段。
```

### 指定范围

```text
调用sd，只输出CLIP-003到CLIP-005的完整Seedance视频提示词，其他Clip不要输出。
```

**Skill 行为 / 停止点**

- 必须已有 Confirmed Clip Production Plan；不能直接根据原始剧本生成最终 Prompt。
- 一个 Confirmed Clip 对应一条完整 Prompt；即使包含多个 Shot，也不拆成多条 Shot Prompt。
- 默认一次只交付一个待处理 Clip。批量授权只改变数量，不改变每个 Clip 的完整结构。
- 每个Clip都会在最终Prompt前自动检查是否需要人物 / 空间调度草图。判定不需要时直接输出Prompt；判定需要时先生成并验证草图，把它作为只控制站位、朝向、距离、关系轴、姿态或动作路径的参考资产，下一次继续才输出Prompt。草图不替代角色、环境或道具正式资产。
- 当前Skill已注册真实`REF-SKETCH-MASTER`图片。生成需要的草图时会把该PNG作为实际视觉参考输入，并走独立Technical Visual Blocking Sketch模板，不会调用Storyboard模板；只有文件或工具输入失败时才会明确报告文字合同回退。草图人物默认统一使用无性别技术调度人偶，仅靠角色标签、技术颜色和位置区分；明显脸、发型、服装、性别化体态或角色外貌重绘会被拒绝注册。候选图缺少主Blocking、角色标签、箭头、适用俯视 / 路径图、镜头信息、动作权限或用途说明，或仍是单幅电影感铅笔插画时，也会以`Artistic Storyboard Drift`失败并拒绝注册。
- `REF-SKETCH-MASTER`只用于生成当前Clip的`REF-SKETCH-XX`，默认不会出现在最终视频Prompt的`参考资产：`里，也不占视频模型的9张图片预算；真正投喂视频模型的是经验证的当前Clip草图。
- 编译前会做 Prompt Control：只填补当前 Clip 尚未被资产、首尾帧或 Blocking 锁定且确实需要控制的内容；内部控制矩阵不会变成最终 Prompt 的额外栏目。
- 会先做字段归属：每条约束只在一个权威字段完整定义。`首帧参考`负责起始状态，`尾帧限制`负责结束状态与carryover，`人物一致性`只负责长期人物身份，`环境一致性`只负责场景结构与环境基线，逐镜只写新增动作/状态变化/局部连续性；其他位置只在真实变化或边界接口需要时写最短Delta，不会为强调而在6—9个字段全文重复。
- 会做 Prompt Pollution 清理：合并重复、消解冲突。导演名、流派名、题材风格名、情绪标签和“电影级 / 高级感 / 治愈感 / 青春感 / 潮湿夏日”等高层词可以保留；重要标签首次出现在最终 Prompt 时，会在同一风格段解释它在本项目中的具体含义，并选择当前 Clip 必要的 3—5 个（或更少）可见 / 可听执行项。具象化后不会默认删除标签，只有完全冗余、无关、冲突或会误触发默认视觉包时才省略。项目风格已由正式资产、视觉开发或 Style Bible 锁定后，后续连续 Clip 只补当前差异，不重复整段解释；动作复杂 Clip 会把风格压到 1—3 项或更少，确保主体、动作、空间、时间顺序、镜头与状态承接优先。“短”或“长”本身都不是质量标准。
- 会分配 Generation Budget：只设一个主要生成负荷，最多一至两个辅助负荷，并主动降低非核心复杂度；不会把身份一致性、复杂动作、高密场景、复杂运镜、群体、口型、FX和光色变化同时拉满。
- 会执行 Reference Routing：只选择能解决当前风险的最小充分参考集合，不会因为资产在 Registry 中、上一 Clip 用过或预算还有空位就全部塞入。
- 会遵守 Clip Scope Firewall：已发生的事件不重播，只执行本 Clip 的主要可见 Beat，未来事件和暂不应出现的结果不提前进入画面；这些内部标签不会出现在最终 Prompt 中。
- 常规视频 Prompt 默认不出现音色字段；雨声、风声、纸张、脚步、道具或乐器声只进入各分镜`音效`。正文以正向、可执行的目标状态为主：能写成“表演克制、镜头简洁自然、左手持续持伞”等正向要求时，不在`主风格`、一致性或各分镜里反复堆“禁止 / 不要 / 避免”。通用高风险禁止项会合并压缩到每个Clip末尾唯一的`反向提示词：`，该段固定以禁背景音乐规则开头，并且后面不再追加任何正文。历史事故物、其他Clip状态、未来剧情和与当前Clip无关的词会删除，同义错误合并为少量当前风险类别。只有必须贴近某个具体动作、空间关系或物理连续性才能说清楚的最小约束，会留在对应分镜字段。

## 15）逐个 Clip 输出（支持“下一个”）

**开始**

```text
调用sd，从下一个尚未交付的Clip开始，每次只输出一个完整Seedance视频提示词。
```

**继续**

```text
调用sd，下一个Clip。
```

或：

```text
调用sd，继续输出下一个尚未交付的Clip，不重复前面的内容。
```

**Skill 行为 / 停止点**

- 会读取当前 Checkpoint，只输出下一个未交付 Clip，不重复已完成内容。
- “下一个 / 继续”只授权一个合法Checkpoint，不自动授权批量输出、普通资产生图、确认候选资产、启用音色或启用配乐；但它会自动执行单Clip草图Gate。若当前Clip确实需要Visual Blocking Anchor，系统可先生成并验证这张受限调度草图，因为这是该Prompt的内部必经检查，不是角色 / 环境 / 道具资产制作授权。
- 下一步若需要确认、外部输入或尾帧，会在对应 Checkpoint 停下说明。

## 16）优化 / 返修某个 Clip Prompt

**最简指令**

```text
调用sd，只优化CLIP-003的Seedance视频提示词，其他Clip不变。
```

**单变量返修示例**

```text
调用sd，CLIP-003只有站位错：A应该在画面左侧，B在右侧，摄影机保持原轴线侧。只修Spatial / Blocking和必要的首尾边界，剧情、动作、资产、运镜、光色、声音和其他Clip全部不变。
```

```text
调用sd，CLIP-003只修雨伞从右手瞬移到左手的问题。保持人物、镜头、表演、环境和风格不变。
```

```text
调用sd，CLIP-003只修模板格式，补齐缺失字段，不重新设计镜头。
```

**Skill 行为 / 停止点**

- 先诊断问题属于 Identity、Spatial / Blocking、Prop、Motion / Performance、Camera、Lighting / Color、FX / Sound、Coverage 或 Prompt Scope / Template。
- 第一轮只改影响最大的一个变量及必需相邻边界，保留 Accepted Unaffected Artifacts。
- 如果根因在角色 / 环境 / 道具资产、Shot Design或Clip Plan，会返回对应上游最小修正；不会用 Prompt 掩盖上游错误。
- 同一Clip只是改措辞、压缩、主风格、反向提示词、台词或音效时，会继续复用已确认草图，不重复生成。只有并排变面对面、换位、离座、明显转身 / 靠近、正反打切换、轴线侧 / 环绕、角色数量、复杂道具、动作路径或Clip起止Blocking发生实质重构时，才重新判断并KEEP / REPLACE / RETIRE / CREATE草图。
- 同类失败第二次必须使用稳定降级；第三次停止盲重试并返回事实 / 设计拥有者。

## 17）长视频连续性：REF-TAIL 三种模式

用户不必记英文术语，只要说明你想怎么接：

| 模式 | 什么时候用 | 是否需要上一Clip尾帧 | 可复制指令 |
|---|---|---|---|
| A 同镜头连续承接 | 上一个镜头在下一Clip继续，接近一镜到底 | 需要 | `调用sd，CLIP-004必须从CLIP-003同一镜头无缝续接，使用上一Clip最终尾帧作为直接承接依据，不得重新摆位或重播动作。` |
| B 新镜头但参考尾帧 | 换了新机位 / 景别，但仍要锁定站位、朝向、距离、空间或道具状态 | 需要 | `调用sd，CLIP-004另起新镜头重新构图，但参考CLIP-003尾帧保持人物站位、朝向、距离和道具状态。` |
| C 新镜头无需尾帧 | 明确反打、特写、俯仰拍、重构图、换场或其他不依赖旧画面的新镜头 | 不需要 | `调用sd，CLIP-004是新镜头且无需上一尾帧；用Canonical资产、Spatial Blocking和文字End State重建首帧。` |

**Skill 行为 / 停止点**

- A / B 都会标记 `Tail Frame Required = YES`。即使你尚未上传尾帧，Prompt 仍可先完整交付，但会把 `REF-TAIL` 标为“待用户提供 / 待上传、未确认”；实际提交生成前必须补图。
- A 是同镜头直接接上；B 是新镜头重新构图，只用尾帧保持连续性。两者不能混写。
- C 标记 `Tail Frame Required = NO`，不会要求截图，也不会把上一尾帧列入参考资产。
- 尾帧只锁定瞬时姿态、站位、动作阶段和构图；角色身份、环境结构、道具造型仍以正式 Canonical 资产为准。
- 每个 Clip 都必须定义自己的新稳定尾帧，最后 1 秒不启动新复杂动作，供下一 Clip 再判断 A / B / C。

## 18）连续性 / 穿帮检查

**最简指令**

```text
调用sd，只做连续性和穿帮检查，不重新生成。
```

**进阶指令**

```text
调用sd，只检查CLIP-002到CLIP-004：角色身份、人数、左右站位、180度轴线、视线、动作阶段、道具持有者、环境结构、光色、声音尾部和REF-TAIL用途。逐项指出问题、受影响ID、事实拥有者和最小修复；不要改Prompt或重新生成。
```

**Skill 行为 / 停止点**

- 会把计划的 End-State、实际生成的 Observed State、已接受的 Canon State 分开核对。
- 会检查 A / B / C 是否选对、尾帧用途是否正确、参考资产是否越权，以及是否发生换脸、换边、道具瞬移、动作重播、无授权跨轴等问题。
- 只分析时不会自动生成、重试、修改资产或把结果写成 Accepted Canon；需要修复时会先给 Return Route。

## 19）根据实际生成结果更新 Accepted Canon

**最简指令**

```text
调用sd，我接受CLIP-003的这个Take。根据实际画面更新Accepted Canon，并让后续Clip从这个实际状态继续。
```

**进阶指令**

```text
调用sd，审核RUN-CLIP003-02的实际起止状态。我明确接受这个Take：把可观察到的人物站位、朝向、动作阶段、道具持有、摄影机终点和临时光态写入Accepted Canon；不要把其中的脸部或服装漂移升级为角色资产。绑定Run ID、Prompt Revision和Review ID。
```

**Skill 行为 / 停止点**

- 只有你明确接受具体 Take，才会建立 / 更新 Accepted Canon；技术 Review PASS 本身不等于用户接受。
- Accepted Canon 来自实际 `Observed State`，不是把原计划值抄一遍。
- 后续 Clip 在同一维度优先从 Accepted Canon 继续，不能无过程强行纠回原计划。
- 已接受 Take 中的脸、服装、环境结构或道具造型漂移不会覆盖正式 Canonical 资产；只继承合法瞬时状态，并把漂移列为 Continuity Risk。

## 20）STATE-09 Review / 是否重做 / 单变量返修

**最简指令**

```text
调用sd，审核这个实际生成结果，判断PASS、REVISE还是REBUILD。
```

**进阶指令**

```text
调用sd，对CLIP-003的实际视频做STATE-09 Review。对照Project Bible、Canonical Assets、Detailed Shot Design、Clip Plan、Prompt和上一Clip Accepted Canon，输出受影响ID、问题等级、最小必要修复、Return Route、Recheck Scope和Must Not Change。第一轮只修最高影响变量，不要整段推翻。
```

**Skill 行为 / 停止点**

- `PASS`：硬门槛通过，允许完成 Review；如要把 Take 写成 Accepted Canon，仍需你明确接受该 Take。
- `REVISE`：局部可修复，返回最小必要 Workflow；修完必须重新 Review。
- `REBUILD`：上游事实或设计严重错误，返回事实 / 设计拥有者；不会把 STATE-09 标为完成。
- 站位错优先只修 Spatial / Blocking；身份漂移优先修 Identity Reference 路由；动作错优先修 Motion / Performance；镜头错优先修 Camera。
- 只有多变量确实耦合、单变量无法形成合法输入，或你明确要求整体重做时，才允许多变量修订。

## 21）视频封面设计

**当前能力边界**

当前 Skill **没有独立的普通“视频封面”Workflow**。现有正式能力是电影海报 / Key Art，包括数字竖版海报与横版平台 Key Art；普通社媒封面和普通缩略图被 Poster Workflow 明确排除。

如果你要的是影片主视觉式封面，推荐这样说：

```text
调用sd，根据当前项目设计一张9:16数字竖版电影Key Art，作为视频封面主视觉。沿用已确认角色、环境和道具资产，不重新设计；保留标题安全区，不生成最终文字。
```

你也可以说：

```text
调用sd，根据当前项目设计9:16视频封面。
```

但 Skill 应先判断它是否能合法归入“电影 Key Art / 数字竖版海报”；若你要的是普通平台缩略图，则会明确提示当前未支持，而不是伪装成现有模块。

**停止点**

- 核心影片事实、资产或 Visual Direction 不足时，会返回对应阶段补齐。
- 片名、日期、credits、logo 或授权不确定时会标为待确认，不会虚构。
- 默认继承现有角色 / 环境 / 道具资产；除非你明确要求并走资产变更流程，否则不重新设计。

## 22）宣传海报设计

**最简指令**

```text
调用sd，根据当前项目设计电影海报。
```

**进阶指令**

```text
调用sd，根据当前项目设计一张9:16先导电影海报。沿用当前Active Character、Environment和Prop资产，只改变宣传构图、光色和视觉母题；片名为“……”，其他日期、credits和logo未确认的内容不要生成。输出Poster Design Package、Base-image Prompt和排版规格。
```

**Skill 行为 / 停止点**

- 正式支持电影海报、Key Art、One-sheet、先导 / 正式 / 角色 / 概念海报和标题字方向。
- 默认选择一个一级视觉母题和一个主要构图模型，不做无意义头像墙。
- 准确文字采用可控排版层；生成式文字只作草案，最终需逐字核验。
- 参考图只提取抽象设计原则，不能复制可识别构图；未授权素材不进入最终海报。
- 海报是辅助 Workflow，不改变主 Pipeline 当前 STATE。

## 23）社媒封面 / 缩略图

**当前状态：未发现专用支持。**

当前 Poster Workflow 明确不处理普通社交媒体封面、普通缩略图或非电影宣传图。因此不要把下面这类任务当作已有 SD Film 正式模块：

```text
为普通账号做YouTube缩略图、直播封面、信息流社媒卡片。
```

如果目标本质上是影片的横版 / 竖版平台 Key Art，可以明确按电影 Key Art 路由：

```text
调用sd，把当前电影海报主视觉重排为16:9横版平台Key Art。沿用现有资产与视觉母题，不做普通网红缩略图风格。
```

若目标确实是普通社媒封面或缩略图，应使用其他合适的设计工具 / Skill；SD Film 会如实说明当前未支持，不硬写不存在的流程。

## 24）只分析图片 / 视频结果，不重新生成

**最简指令**

```text
调用sd，只分析这个图片/视频结果，不重新生成，也不要修改Prompt。
```

**进阶指令**

```text
调用sd，只读检查这个CLIP-003实际结果。对照当前Canonical Assets、Detailed Shot Design、Clip Plan和上一Clip尾帧，分析身份、空间、动作、道具、摄影、光色、声音与连续性；列出证据、问题和最小Return Route。不要生成、编辑、重试、改状态或写入Accepted Canon。
```

**Skill 行为 / 停止点**

- 需要实际图片 / 视频或可访问的生成结果；未看到结果时不会假装完成 Review。
- 只分析不会自动重做、后期编辑、生成新 Prompt、确认候选图片或更新 Canon。
- 如需把结果接受为 Canon，另发第19节的明确接受指令。

## 25）继续旧项目 / 重新调用最新 Skill

### 继续但不强制重载

```text
继续。
```

会从当前已验证 Checkpoint 继续最近未完成步骤；普通“继续”不是 Skill 重载指令。

### 重新读取当前实际安装版再继续

```text
重新调用sd，恢复当前项目，从最后一个安全Checkpoint继续。
```

或：

```text
重新加载SD，保留当前项目、Production-Locked Script、Confirmed Assets、Accepted Artifacts和用户约束，然后继续下一个合法步骤。
```

**Skill 行为 / 停止点**

- 首次或普通`调用SD / 调用sd / 调用SD流程`会激活SD Film，读取当前可访问规则并按项目事实进入正确STATE / Workflow；不存在可恢复项目时可建立新项目入口。
- 明确`重新调用SD / 重新调用sd / 重新加载SD / 重新加载sd / 按当前Skill继续 / 按当前 skill 继续`会重新读取当前可访问Skill，同时保留已确认的项目事实，从当前STATE / Workflow入口重新处理当前对象；不会只拿上一版Prompt继续润色，也不会无故清空已确认资产、草图或进度。
- `重新调用sd，恢复当前项目`会优先使用当前Chat实际可访问的Skill资源，并依次尝试可用项目状态、Portable Project State和当前可验证的项目上下文；Skill规则来源和项目事实来源可以不同，不会因此恢复失败。
- 普通`继续 / 下一步 / 下一个`只从当前合法Checkpoint继续，不等于强制重新加载；当前Workflow本来要求的检查仍会照常执行。
- 普通Chat会先使用当前运行时可访问的Skill资源；本机Windows路径不可读不代表必须切Work。Work不是恢复旧项目的默认要求，只有必须读取/修改普通Chat无法访问的本地文件且现有Portable State与项目上下文不足时才需要。
- 旧项目已有的定稿剧本、角色/环境/道具资产、Blocking、Spatial Snapshot、Confirmed草图、Accepted Take / accepted prompt和已确认镜头会保留；新版Screenwriter / Director规则只补当前Workflow确实缺少且可可靠推导的Intent，不会把项目退回STATE-01重做。
- 只有本轮真的读到当前Skill入口、版本和必需路由文件，Skill才能说“已重新加载”或“严格按当前Skill执行”；失败时会说明实际使用的是当前可访问资源、Portable State或Project Context等fallback，不会拿旧对话摘要冒充当前安装版。
- 显式恢复会简短显示Skill来源、项目状态来源、映射后的STATE、当前Workflow / Object、保留的Canon、需要补的Writer / Director Intent和Next Workflow，方便核对实际恢复依据。
- 会核验 Project ID、State Source、Revision、Checkpoint和 Artifact；不能唯一识别项目时会停下确认，不会猜“最近项目”。
- 生成失败第一次最小修正，第二次稳定降级，第三次返回事实 / 设计拥有者。

## 26）只检查 Skill 当前 Pipeline / STATE / 某条规则，不执行制作

**最简指令**

```text
调用sd，只检查当前Pipeline和STATE，不执行制作。
```

**进阶指令**

```text
调用sd，读取当前实际安装版SKILL.md、config、workflow map和相关权威文件，只检查“Voice opt-in、STATE-08音色省略、REF-TAIL A/B/C、单Clip交付”四条规则是否一致。报告文件证据、冲突和当前版本；不要修改文件、推进项目、生成Prompt或调用媒体工具。
```

**其他可复制示例**

```text
调用sd，只告诉我当前项目处于哪个STATE、依据是什么、下一个合法Workflow是什么，不继续执行。
```

```text
调用sd，只检查CLIP-003的Reference Budget和Reference Routing规则是否满足，不修改Prompt。
```

**Skill 行为 / 停止点**

- “调用sd”会先重新解析当前Chat可访问的Skill资源并重读入口；只有实际取得 `Skill Version`、`Build ID`和必要读取证据才能报告 `RELOADED`或声称严格遵守当前Skill。
- 只检查不会自动推进主 Pipeline，也不会因发现问题直接修改 Skill 或项目成果。

## 27）进入 Work 修改 Skill 的推荐指令

**最简指令**

```text
进入Work，读取当前实际安装的C:\Users\Lenovo\.agents\skills\sd，只修改我指定的规则。
```

**推荐完整指令**

```text
进入Work，修改用户当前实际使用的C:\Users\Lenovo\.agents\skills\sd。

先完整读取SKILL.md，并读取config、workflow map、相关rules/workflows/templates/references；先搜索是否已有同类规则，优先修改权威原文件，不平行新增重复Schema。

本次目标：<写清要改什么>。
必须保持：<写清不能动什么>。
影响范围：<指定Workflow、STATE、Template或规则>。
完成标准：<列出需要通过的正例、反例和回归场景>。

正式修改后按SKILL.md的版本纪律同步更新Skill Version和Build ID，并自动执行`references/module_contracts.md`中的`Skill Update Self-Check / Change Safety Checklist`。如果用户调用方式、模块入口、Prompt输出结构、音色、连续性或Review等用户可见行为变化，同步更新USER_GUIDE.md。最后报告变更分类、修改文件、规则真源、重复/冲突/污染/路由/模板/引用检查、定向回归、USER_GUIDE同步状态和未解决Warning。
```

**Skill 修改任务建议写清**

- 改什么：例如“音色必须 opt-in”“只修 REF-TAIL B 模式”“增加一个真正的社媒封面模块”。
- 不改什么：例如“不改变主 STATE 编号”“不修改视频 Prompt Template”“不重做已有项目资产”。
- 权威位置：规则、Workflow、Template、Reference分别由谁拥有；不知道时要求先扫描路由再决定。
- 验证场景：至少写正向触发、负向不触发、旧项目恢复、单 Clip / 批量、Review返修等。
- 完成后不要只说“已改”，要报告实际文件、版本、回归检查和残留冲突。

**以后固定执行的 Skill 维护链**

```text
读取当前规则
→ 定位相关规则与权威来源
→ 分类现有覆盖
→ 最小修改
→ Skill Update Self-Check
→ 对整个 Skill 的发现项做风险分级
→ 当轮修复所有安全和可控问题
→ 对原始修改与附带修复分别做定向回归
→ 用户可见行为变化时同步 USER_GUIDE
→ 输出变更报告
```

变更分类固定使用`no_change / optimize_existing / merge_existing / add_new / deprecate/remove`。自检是维护层，不是新的影视制作STATE；它不会推进项目或改变已确认成果。纯拼写修正也会至少检查重复、冲突和文件引用。

自检的发现范围覆盖整个Skill，不只检查本次改动。已经发现的安全局部问题和所有者、回归路径明确的跨文件问题，应在当轮修复；只有可能改变用户已确认行为、主Pipeline、STATE、资产锁、最终Schema、外部兼容，或无法可靠验证的大规模迁移，才可标记`WARN`并说明证据、影响、修复方案和需要的决定。“与本次修改无关”本身不再是延期理由。

## 28）万能指令公式

```text
调用sd + 我要做什么 + 当前输入 + 必须保持什么 + 重点优化什么 + 做到哪一步停
```

### 模板

```text
调用sd，我要【目标】。
当前输入是【剧本 / 项目 / 资产 / Shot / Clip / 实际生成结果】。
必须保持【剧情、角色身份、资产版本、空间关系、道具、风格、已接受结果】。
重点优化【节奏 / 表演 / Blocking / Camera / Lighting / Sound / Prompt Control】。
只做到【具体STATE / 具体Artifact / 具体Clip / 诊断报告】后停下来，等待我确认；不要【明确禁止的动作】。
```

### 示例：完整视频

```text
调用sd，我要把这个定稿剧本做成9:16视频。当前输入是最终剧本和现有角色参考图。必须保持剧情、人物关系和现有角色外貌。重点优化空间连续性、动作可执行性和长视频接续。先完成项目初始化、剧本锁定和资产缺失检查，在资产清单后停下来；不要修改剧本或设计音色。
```

### 示例：单个 Clip

```text
调用sd，我要CLIP-003的Seedance视频提示词。当前输入是Confirmed Clip Plan和上一Clip已接受Take。必须保持Accepted Canon中的站位、动作阶段、道具持有和摄影机轴线。重点优化动作稳定性和尾帧可继承性。只输出CLIP-003，其他Clip不动；默认不要写任何音色文字。
```

### 示例：单变量返修

```text
调用sd，我要返修CLIP-003。当前问题只有A/B站位左右颠倒。必须保持剧情、角色资产、动作、运镜、光色、声音和其他Clip。重点只修Spatial / Blocking及必要首尾边界。输出修订后的CLIP-003 Prompt后停，不要整段重写。
```

## 常见误区

- `调用sd，生成Seedance Prompt` 不代表前置阶段可以跳过；Skill 会先检查 State 和 Confirmed Artifacts。
- `继续 / 下一步 / 好的` 不等于同意剧本改写、确认 Proposal、确认资产 Prompt、确认候选图片或授权批量输出。
- 角色有对白不等于要做音色；没有音色资产也不阻塞主流程。
- “声音设计”不自动等于角色音色或配乐；请明确说“角色音色”或“配乐规划”。
- Storyboard 不是 STATE，也不能作为视频参考资产。
- 一个 Shot 不是一个 Prompt；一个 Confirmed Clip 才对应一条完整 Seedance Prompt。
- 尾帧不是角色资产替代物；尾帧轻微换脸时仍以角色 Canonical Reference 锁身份。
- 局部错误先修单变量；不要用“整体感觉不对”直接推翻全部已接受成果。
- 电影海报 / Key Art 当前受支持；普通社媒封面和普通缩略图当前没有专用模块。

## 维护约定

每次Skill正式修改完成后都必须执行`references/module_contracts.md`中的`Skill Update Self-Check / Change Safety Checklist`、`Standalone Skill Discovery Guard`和`Unconditional Chat Runtime Startup And Recovery Guard`。即使只修改文案、Knowledge、Template或拼写，也必须运行普通Chat启动与旧项目恢复基线，以及独立Skill发现基线，避免后续优化使Chat无法正常调用、出现两份同名Skill或误要求Work。该Reference是维护QA的唯一权威来源；本说明书只说明用户可见的调用和报告方式，不复制完整检查细则。

以后发生以下用户可见变化时，应同步更新本说明书：

- 用户调用方式或主要模块入口改变；
- 主 Pipeline、STATE路由或关键停止点改变；
- Prompt最终输出结构、默认单 Clip / 批量行为改变；
- 角色音色、配乐、连续性、REF-TAIL、Accepted Canon或Review行为改变；
- 海报、封面或其他对用户宣称的能力边界改变；
- 推荐指令不再能正确触发当前 Workflow。

不要求每次内部 Knowledge、实现细节或不影响用户下指令的文件变化都同步更新。只更新会改变“用户该怎么说、Skill 会做什么、何时会停”的内容。
