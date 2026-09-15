# SD Film Genre Profiles

# Read Scope

本文件是类型层的中枢入口，**不得整文件通读**：按当前事项只读对应小节。

| 当前事项 | 只读 |
|---|---|
| 判定该不该读类型知识 | `## Purpose And Boundary`、`## Loading Rule` |
| 定位当前项目的类型文件 | `## The Roster`、`## Loading Rule` |
| 写新的类型文件 | `## Shared Genre File Schema`、`## Orthogonality`、`## Validator-Checkable Invariants` |
| 类型之间冲突或混合 | `## Mixed Genre Rule`、`## Anti-Formula Discipline｜反公式边界` |
| 不适用 / 返回路由 | `## Non-Applicable Rule`、`## Return Routing` |
| 不必在运行时读取 | `## Validator-Checkable Invariants` |

---

## Purpose And Boundary

本Knowledge定义**类型剖面（Genre Profile）**：同一套叙事内核在不同类型承诺下，**呈现层**必须如何分化。

它回答一个问题：**为了让观众经历这个类型承诺，镜头、表演、声音与节奏各有哪些可执行倾向，各自的成立条件是什么。**

它**不拥有**：故事结构、冲突公式、节拍模型、人物关系走向、剧情事实、资产身份、STATE推进、Completion Gate、任何Template字段或STATE-08最终Prompt Schema。

**类型知识给的是带条件的倾向，不是配方。** 本模块存在的前提是：类型承诺决定观众**体验什么**，而Writer与Director决定**这一次怎么兑现**。任何把类型写成"第几分钟必须发生什么"的表述都越权，见`## Anti-Formula Discipline｜反公式边界`。

它属于**条件性Knowledge**，与`knowledge/medium_profiles.md`同类：只在类型已登记时加载，未登记时不加载、不猜测、不默认。

## The Roster

| Profile ID | 类型家族 | 承诺轴（观众为什么看下去） | 文件 | 主要消费 |
|---|---|---|---|---|
| `mystery_thriller` | 悬疑 / 惊悚 / 心理惊悚 | 未知、推断与不安全感的持续 | `knowledge/genre/01_mystery_thriller.md` | STATE-04 / 05 / 06 / 08 |
| `action` | 动作 / 冒险 / 追逐 | 身体能力与代价的可见兑现 | `knowledge/genre/02_action.md` | STATE-04 / 05 / 06 / 08 |
| `romance` | 爱情 / 关系 / 情感 | 关系变化的可信积累与克制 | `knowledge/genre/03_romance.md` | STATE-04 / 05 / 06 / 08 |
| `comedy` | 喜剧 / 黑色幽默 / 生活喜剧 | 预期与落差的节奏兑现 | `knowledge/genre/04_comedy.md` | STATE-04 / 05 / 06 / 08 |
| `horror` | 恐怖 / 怪奇 / 超自然 | 威胁的不可控与身体性恐惧 | `knowledge/genre/05_horror.md` | STATE-04 / 05 / 06 / 08 |
| `crime` | 犯罪 / 警匪 / 程序 | 规则、证据与代价的因果链 | `knowledge/genre/06_crime.md` | STATE-04 / 05 / 06 / 08 |

本表是类型的**唯一登记处**：新增类型文件必须同时在此登记，且文件与登记项一一对应。Profile ID固定，不得改名或新增同义ID。

## Loading Rule

**触发**：项目`类型`字段已登记（`templates/00_project_start_template.md`的`## Genre → 类型：`，STATE-00登记用户已提供或可从素材直接确认的类型）时加载。未登记时记`Genre Profile: PENDING`，**不加载任何类型文件、不从媒介、平台、题材标签、画风或参考片推定类型**。

**读取范围**：

- 只读**当前项目命中的**类型文件；一次最多读两个（主类型 + 一个被用户或剧本明确支撑的次类型），不为"全面"读完整目录。
- 每个类型文件按它的章节标题定点读取与当前阶段相关的节，不整文件通读。
- STATE-04按命中类型建立或修订`Visual Grammar Baseline`；STATE-05 / 06 / 08 **消费已锁定的基线**，只在当前Scene / Shot的类型兑现出现真实分歧时，才回读对应类型文件的对应小节。同一事实不重复读。

**不读**：与当前项目类型无关的其他类型文件；与当前阶段无关的类型章节；面向人阅读的非运行时文档（它们不是规则、恢复、路由或Schema的来源）。

## Shared Genre File Schema

每个类型文件必须按下列**固定小节**组织，缺任一小节即视为未完成，不得入册：

| # | 小节 | 必须回答 |
|---|---|---|
| 1 | `## Genre Promise｜类型承诺` | 观众被承诺体验什么；承诺成立的判据与最常见的落空方式 |
| 2 | `## Information Discipline｜信息与悬念纪律` | 观众此刻该知道什么、不该知道什么；信息通过可见手段建立或保留的方式 |
| 3 | `## Camera Tendencies｜镜头倾向` | 可执行的机位/景别/运动倾向，每条写明**成立条件**与**反用场景** |
| 4 | `## Performance And Reaction｜表演与反应` | 反应顺序、强度尺度、最小充分载体；不成立时改用什么 |
| 5 | `## Sound And Silence｜声音与留白` | 同期声、动效、静默与呼吸的使用条件；**永久不得写入非剧情内配乐** |
| 6 | `## Rhythm And Cutting｜节奏与剪辑` | 镜头长度倾向、切点依据、信息顺序；不预设固定节拍模型 |
| 7 | `## Model Execution Notes｜模型执行提示` | 该类型的意图在视频模型里**以什么形态能活下来**、哪些写法会崩、如何降级 |
| 8 | `## Pairs And Tensions｜组合与张力` | 与本类型常见搭配的类型、以及组合时先保谁、哪里会互相削弱 |
| 9 | `## When Not To Apply｜反公式边界与失败信号` | 本类型知识**不适用**的输入、必须让位于Writer / Director Intent的情形、可观察的失败信号 |

第9节是必答项：**没有写清"什么时候不用"的类型文件，等于把倾向变成了公式。**

## Orthogonality

三条轴互相正交，任何一条不得覆盖另一条：

- **媒介（`knowledge/medium_profiles.md`）与类型正交**：Genre承诺不因媒介改变，媒介也不改变Genre承诺。类型倾向里的光学、器材、焦段语言在`2d_anime`下必须按媒介层换用等效表达，不得直接套用。
- **导演风格（`knowledge/visual_styles/`）与类型正交**：类型决定承诺与呈现倾向，导演参考决定这一次的具体审美选择。两者冲突时，先保类型承诺的**可读性**（观众仍能收到承诺），再按已确认风格选择实现方式。
- **短剧形式（`knowledge/adaptation/short_form_drama_adapter.md`）与类型正交**：目标时长与平台改的是密度与承载方式，不改类型承诺本身。

## Mixed Genre Rule

一个项目通常携带主类型与次类型。组合时：

1. **主类型拥有承诺**：观众最终要收到的体验由主类型决定；次类型只贡献手段与质感。
2. **合并的是手段，不是承诺**：两个类型都提供"用哪种机位/表演/声音"的主张时可以择优；两个类型都要求"观众此刻必须知道/不知道什么"而互相矛盾时，服从主类型，并把次类型降级为局部使用。
3. **不得叠加成同时讨好的折中**：同一场景内同时满足两个类型的全部承诺，通常两个都不成立——写不出取舍时，按Writer / Director Intent选一个并在内部记录让位关系。
4. 组合结论必须能被说不成公式的一句话概括："这一场先保X，用Y的方式兑现"；答不出即未完成组合判定。

## Anti-Formula Discipline｜反公式边界

本模块**明令禁止**以下写法与用法。它们也是回归`R24-J Genre — No Universal Conflict Formula`的直接对象：

- **禁止固定节拍模型**：不得出现"第N分钟必须反转""每场必须有钩子""类型片必须三幕"这类与项目无关的时长或密度要求。
- **禁止冲突公式**：不得规定冲突强度、升级次数、反转数量或结局形态；冲突来自人物、关系、时间、环境、秘密、制度、信息不对称或人物内部矛盾，由Writer拥有。
- **禁止用类型替代判断**：类型倾向是**候选手段**，其成立条件不满足时不得使用；不得因为"这是悬疑片"就自动选用某个机位、某种表演或某段静默。
- **禁止升级为跨项目原则**：单次项目有效的做法不得写成通用规则；类型知识里写下的每一条都必须是"在什么条件下、观察到什么结果"。
- **禁止覆盖上游**：类型知识不得改写Production-Locked Script、Writer Intent、Director Intent、Canonical资产、已确认Blocking或任何已确认项目事实。

## Shared Invariants

类型剖面**不改变**以下任何一项：

- Story First、Asset First、镜头必须服务剧情
- STATE-00至STATE-09主Pipeline、Completion Gate与推进规则
- 资产双确认、Canonical Lock与连续性纪律
- STATE-08最终Prompt字段与Template：不因类型新增任何字段
- REF-TAIL A/B/C、REF-SKETCH边界、Voice opt-in，以及**视频Prompt永久禁止非剧情内配乐**
- Writer / Director职责分工：类型不拥有故事、不拥有观众体验的最终取舍

## Return Routing

- 类型未登记、登记冲突或无法确认 → STATE-00的项目登记（`templates/00_project_start_template.md`的`## Genre`）补正；不得由本模块代替用户确认类型
- 类型承诺与已锁定剧本冲突 → Writer Owner（`knowledge/screenplay_development.md`）
- 项目级呈现取舍与类型倾向冲突 → STATE-04（`Visual Grammar Baseline`的建立地）
- 逐镜呈现冲突 → STATE-06
- 最终Prompt字段或Schema疑问 → 当前Template与`workflows/11_video_generation_workflow.md`
- 媒介相关表达在非实拍档不成立 → `knowledge/medium_profiles.md`

## Non-Applicable Rule

- 类型为`PENDING`：不加载任何类型文件，不写`Genre Profile`结论，也不得按某个类型默认推进；需要类型才能成立的呈现选择记为待定并返回STATE-00补正。
- 本文件不适用于Storyboard、Poster、Sequence、MUSIC、AUDIO等辅助模块的既有边界；Poster的类型倾向由`knowledge/poster_design/genre_tendencies.md`拥有，与本模块不互相替代。
- 本文件不创建STATE、不新增Template字段、不改变任何Model Adapter能力与能力数值。

## Validator-Checkable Invariants

- `## The Roster`登记的类型文件必须真实存在，且`knowledge/genre/`下不得存在未登记的类型文件（登记项与文件一一对应）。
- 每个类型文件必须齐备`## Shared Genre File Schema`列出的九个小节。
- `## Anti-Formula Discipline｜反公式边界`必须存在，且必须包含禁止固定节拍模型、禁止冲突公式、禁止覆盖上游三类表述。
- 与媒介正交、与导演风格正交的声明必须存在。
- 不改变STATE-08 Schema、不新增Template字段的声明必须存在。
- 六条固定不变量（Story First / 主Pipeline / 资产纪律 / 无BGM / Writer-Director分工 / 无新增字段）必须存在。
