# SD Film Drawn-Medium Language｜绘制媒介语言

# Read Scope

本文件是 `2d_anime` 档镜头语言的中枢入口，**不得整文件通读**：按当前事项只读对应小节。

| 当前事项 | 只读 |
|---|---|
| 判定该不该读本域 | `## Purpose And Boundary`、`## Loading Rule` |
| 定位当前需要哪个原子 | `## The Roster` |
| 写新的原子文件 | `## Shared Atom Schema`、`## Validator-Checkable Invariants` |
| 与实拍知识冲突 | `## Return Routing`、`## Shared Invariants` |
| 不必在运行时读取 | `## Validator-Checkable Invariants` |

---

## Purpose And Boundary

本域拥有 **`2d_anime` 档的镜头语言等效表达**：在一个**不存在摄影机**的媒介里，把 Director Intent 转换成具体、可执行、可验证的画面行为。

它存在的原因是一次实测缺口：`knowledge/medium_profiles.md` 明令 `2d_anime` 不得使用焦段毫米数、光比比值、器材与真实景深，并要求"改用等效表达"，而当时那套等效表达只有两行示例词；同时 `knowledge/camera_language/` 的 65 个原子全部以实拍光学为前提（默认"全画幅等效倾向"）。结果是该档项目在 STATE-06 读到的是**一整套它被禁止使用的词汇**。

**它不拥有**：剧情事实、资产身份、STATE推进、Completion Gate、任何Template字段、最终Prompt Schema，以及**镜头语言模块本身**——`knowledge/camera_language/index.md` 仍是 Camera Language Module 的唯一owner，本域是它在绘制媒介下的分化，不是第二套路由。

**它也不重建跨媒介抽象规则**：180°轴线、银幕方向、视线匹配、景别序列、信息顺序与人物在画面上的左右关系，在绘制媒介里同样成立，继续由 Spatial Blocking / Relational Screen Geometry 拥有；本域只负责"这些规则在版面上如何被画出来"。

它属于**条件性Knowledge**，与`knowledge/medium_profiles.md`同类：只在媒介已确认时加载。

## Loading Rule

**触发**：`媒介形式`确认为 `2d_anime`。此时本域**取代** `knowledge/camera_language/` 的光学原子成为镜头语言的读取对象；`knowledge/camera_language/index.md` 仍读，用于模块路由、人物拓扑、镜头必要性判断与 Relational Screen Geometry，但它目录下的光学原子（焦段、光圈、景深、稳定器、轨道/摇臂、实拍灯光相机）在该档**不读、不写**。

**不触发**：`live_action` 与 `3d_animation` 不加载本域。`3d_animation` 按`knowledge/medium_profiles.md`继承实拍知识（虚拟光学成立），不得借用本域；`Pending` 时不加载，也不得从类型、平台、题材标签或画风推定媒介。

**读取范围**：只读当前镜头命中的原子，按各原子的章节标题定点读取；不整域通读。

## The Roster

| # | Atom | File | 拥有什么 |
|---|---|---|---|
| 1 | 版面与空间 | `knowledge/anime_language/01_layout_and_space.md` | 景别的版面定义、前中后景层、遮挡与留白、人物在版面上的位置与比例 |
| 2 | 运动的版面等效 | `knowledge/anime_language/02_movement_equivalents.md` | 推、拉、摇、移、跟、环绕、升降在绘制媒介下的对等物与层级位移 |
| 3 | 帧感与冲击 | `knowledge/anime_language/03_timing_and_impact.md` | 关键帧—中割取舍、停格、速度线、smear / impact frame、集中线、残影 |
| 4 | 画风锚与一致性 | `knowledge/anime_language/04_style_and_consistency.md` | 线宽、上色法、网点/笔触、色指定的跨镜一致性纪律与漂移判据 |

本表是原子的**唯一登记处**：新增原子必须同时在此登记，文件与登记项一一对应。

## Shared Atom Schema

每个原子文件必须按下列固定小节组织，缺任一小节即视为未完成，不得入册：

| # | 小节 | 必须回答 |
|---|---|---|
| 1 | `## Purpose And Owner` | 本原子回答什么、边界在哪、与哪个实拍原子互为对等物 |
| 2 | `## Executable Vocabulary｜可执行词汇` | 实拍量 → 绘制媒介等效物的对照表，每条写明**写进哪个既有字段** |
| 3 | `## Conditions And Anti-Use｜成立条件与反用` | 每条等效物在什么条件下成立、什么条件下不得使用 |
| 4 | `## Prompt Translation｜Prompt 转译` | 等效词汇如何落进 STATE-08 的**既有字段**；不得新增字段 |
| 5 | `## Failure Signals｜失败信号` | 可观察的失效表现，用于 STATE-06 / 08 / 09 判定 |

## Shared Invariants

绘制媒介语言**不改变**以下任何一项：

- Story First、Asset First、镜头必须服务剧情
- STATE-00至STATE-09主Pipeline、Completion Gate与推进规则
- 资产双确认、Canonical Lock与连续性纪律
- 180°轴线、银幕方向、视线匹配、人物拓扑与 Relational Screen Geometry
- 资产形态：2D角色资产是**设定集与画风锚**，其结构由`templates/04_character_asset_prompt.md`拥有
- STATE-08最终Prompt字段与Template：不因媒介新增任何字段
- REF-TAIL A/B/C、REF-SKETCH边界、Voice opt-in，以及**视频Prompt永久禁止非剧情内配乐**
- **本域不得写入任何实拍专有量**：焦段毫米数、光比比值、光圈值、真实景深、轨道/摇臂/稳定器/云台、胶片型号。它们在绘制媒介里没有对应物，写入只会污染Prompt并误导生成

## Return Routing

- 媒介本身缺失、为`Pending`或冲突 → STATE-01的`Production Setup Gate`
- 镜头语言模块路由、镜头必要性、人物拓扑 → `knowledge/camera_language/index.md`
- 轴线、银幕方向、空间关系 → `knowledge/spatial_blocking_layer.md`
- 项目级美学方向、色指定与画风基线 → STATE-04与`knowledge/medium_profiles.md`的Aesthetic Layer
- 角色资产结构（设定集与画风锚） → `templates/04_character_asset_prompt.md`
- 逐镜冲突 → STATE-06；Clip内连续性与节奏 → STATE-07；最终字段 → 当前Template

## Non-Applicable Rule

- 媒介未确认为`2d_anime`时不加载；`3d_animation`与`live_action`一律走原有实拍知识。
- 本域不适用于Storyboard、Poster、Sequence、MUSIC、AUDIO等辅助模块的既有边界。
- 本域不创建STATE、不新增Template字段、不改变任何Model Adapter能力与能力数值。
- 本域不判断"画得好不好看"；审美结论由用户给出，按`knowledge/quality/aesthetic_judgement.md`。

## Validator-Checkable Invariants

- `## The Roster`登记的原子的文件必须真实存在，且`knowledge/anime_language/`下不得存在未登记的原子文件（登记项与文件一一对应）。
- 每个原子文件必须齐备`## Shared Atom Schema`列出的五个小节。
- 禁止实拍专有量的声明必须存在。
- 不新增STATE-08字段、不改变主Pipeline的声明必须存在。
- 与`knowledge/camera_language/index.md`的owner关系声明必须存在（本域是分化，不是第二套镜头语言路由）。
