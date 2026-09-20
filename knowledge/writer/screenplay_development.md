# Screenwriter Module / Writer Intelligence Layer

# Read Scope

本文件被多个阶段复用，**不得整文件通读**：按当前事项只读对应小节。

| 当前事项 | 只读 |
|---|---|
| STATE-00 | 只读 `## Cross-stage Projection` 的 STATE-00 行 |
| STATE-01 Creation Brief | `## Module Contract`、`## Minimum Project Intent Gate`、`## Director-first Story Development`、`## WRITER INTENT PACKET`、`## Writer Decision Engines`、`## Directable Screenplay QA`、`## Directable Screenplay Gate｜可失败判定`、`## Proposal And Revision Handoff`、`## Completion Check`；项目存在已确认品牌诉求或商业目标时加读 `## Client Brief And Commercial Fact Gate｜客户与商业事实门`；项目存在 Client Brief 节时加读 `## Requirement Fidelity｜需求保真判定` |
| STATE-01 Existing Script / Material | 加读 `## AIGC Directability Check`、`## Dialogue Principle`；授权改写输出Proposal前加读 `## Directable Screenplay QA` 与 `## Directable Screenplay Gate｜可失败判定` |
| 原创开发、诊断或改写需要结构／人物／场景／对白手段时 | `## Craft Manual｜工艺手册` 的对应小节：`### 结构操作`、`### 人物构建`、`### 场景与对白技法`；按当前场景只取所需条目，不整节通读 |
| STATE-05 / STATE-06 | 只读 `## WRITER INTENT PACKET`、`## Writer → Director Handoff`、`## Cross-stage Projection`、`## Scene Director Intent Source Data` |
| 归属冲突时 | `## Route Boundary` |
| 不必在运行时读取 | `## Purpose` |

---

## Purpose

本文件是SD Film唯一的`Screenwriter Module / Writer Intelligence Layer` owner。它负责写故事及持续保护故事成立的原因：Premise、Theme、Dramatic Question、人物欲望与选择、场景目的、因果、Writer Beat、冲突与代价、潜台词、Setup / Payoff、信息进入故事的时机、人物与关系弧、结构节奏和故事层AIGC Directability。

它服务STATE-00至STATE-09与Editing，但不创建新主STATE、不建立第二套Project State、不拥有用户可见Template字段，也不直接规定Camera Language。STATE-01是它的主要创作与诊断位置；用户的Creation Brief授权生成剧本提案，Existing Script / Material仍先诊断且只在用户授权后改写。确认后的结果为`Production-Locked Directable Screenplay + WRITER INTENT PACKET`，其中Packet是按需传递的内部source data，不机械展示给用户。

核心分工固定为：

```text
Screenwriter Module = 写故事 / 人物逻辑 / 戏剧因果 / 信息架构
Director Module = 组织观众体验 / 表演策略 / Blocking / 构图 / Camera / 呈现节奏
Performance Layer = 把Character Intent + Director Intent转成可见行为
Prompt Compiler = 把已确认的Writer与Director决定翻译为模型可执行Prompt
```

`Information Architecture = Writer Authority`；`Information Presentation = Director Authority`。`Character Intent / Subtext = Writer Authority`；`Performance Direction / Blocking / Camera = Director Authority`。Writer不写35mm、85mm、推镜、特写、低机位等Camera Language；Director不得静默改变已锁定的关键因果、人物动机、信息时机与Setup / Payoff义务。

## Module Contract

- **Module Name**：Screenwriter Module / Writer Intelligence Layer；`Director-first Screenplay Development`保留为旧版Creation子模式兼容名称
- **Module Type**：贯穿式内部编剧决策Knowledge；STATE-01为主要创作/诊断位置，不是Workflow、Template、新主STATE或第二套状态系统
- **Owner**：`knowledge/writer/screenplay_development.md`
- **Trigger**：所有SD Film叙事项目；Creation Brief执行原创开发，Existing Script / Material执行只读Writer Diagnosis，获得合法授权后再调用现有Adaptation / Optimization子模块
- **Not Triggered As**：未经请求自动改写、Camera/Composition/Shot规则、独立Workflow、资产生成、Storyboard或最终Prompt Schema
- **Craft Manual Boundary**：`## Craft Manual｜工艺手册` 的条目是带条件的候选手段，每个条目只在本条目的`成立条件`满足时使用；它不规定时长、页数、幕点、节拍数或必需品清单，也不得被改写为Gate或硬门。硬门只由各自的适用Adapter拥有
- **Position**：`STATE-00 Writer Foundation → STATE-01 Creation / Diagnosis / Authorized Rewrite → Production-Locked Screenplay + Writer Intent → STATE-05 Writer Beat Projection → STATE-06/07/08 Preservation → Editing / STATE-09 Story Review`
- **Required Inputs / Owners**：用户Idea / Brief / Concept、已确认Project Bible事实、目标形式/大致时长或容量、受众/品牌目标、必须保留项与禁止项；这些事实只由用户和已确认项目资料拥有
- **Output Owner**：本Knowledge拥有Writer Intent Packet、原创故事开发、Writer Diagnosis、Writer→Director Handoff与跨阶段保护合同；最终用户可见Production Script Proposal及确认/交接字段只由`templates/02_script_analysis_prompt.md`拥有
- **Read / Write Boundary**：只读用户输入与已确认项目事实；只把开发结果交给STATE-01 Workflow写入当前项目的Proposal Artifact与状态；不修改资产、Visual Direction、SHOT、CLIP、Portable Schema或Skill根目录项目兼容入口
- **Downstream Consumers**：`knowledge/writer/script_adaptation.md`、`knowledge/writer/screenwriting_optimization.md`、`knowledge/writer/directorial_interpretation.md`、STATE-02至09、Editing与Prompt Compiler
- **Protected Upstream Facts**：用户给定的核心创意、世界观、角色身份/关系、品牌诉求、事实/权利边界、指定结局/名场面/台词与禁止内容
- **Conflict Route**：缺失信息会实质改变题材、目标形式、品牌合规、核心人物或结局时，保持STATE-01 IN_PROGRESS并只询问最小必要问题；可用合理默认值继续且不改变核心意图时，记录Assumption并继续创作
- **Deterministic Invariants**：Creation / Existing双入口不变；Existing无授权不改写；Packet不成为Template或Portable State新Schema；Character Engine按复杂度调用；Writer Beat不等于Shot；Writer不规定Camera；Director不静默改写Writer锁；未确认Proposal不进入STATE-02；`## Craft Manual｜工艺手册`的条目不得成为Gate、硬门或时长要求；`## Directable Screenplay Gate｜可失败判定`的五项必须在Proposal输出前逐项指认，指不到即不得输出

## WRITER INTENT PACKET

Packet按项目逐步充实、按当前阶段只投影必要部分。未知或不适用项保持Unknown / Not Applicable；不要求用户填写，也不把所有字段打印进剧本、Scene、Shot、Clip或Prompt。Work/Codex把它与确认剧本Revision、现有Project Bible / Scene / Clip工件或Checkpoint绑定；普通Chat保留在可恢复上下文。不得新增主STATE、Portable State字段或平行Writer文件。

### Project-level

- Premise
- Theme / Thematic Question
- Dramatic Question
- Genre Promise
- Story Engine
- Protagonist Want / Need
- Core Conflict
- Stakes
- Character Arc
- Relationship Arc
- Information Architecture
- Setup / Payoff Plan
- Emotional Arc
- Structural Rhythm
- AIGC Directability Constraints（只限故事层可视化、容量与可执行性，不决定镜头）

### Scene-level

- Scene Purpose
- Character Objective
- Obstacle / Conflict
- Tactic / Strategy
- Subtext
- Hidden Objective
- Value Change
- Relationship Change
- Information Change
- Decision Point
- Consequence
- Setup / Payoff / Callback Function
- Writer Beat Map
- Scene Exit State

### Beat-level

```text
Trigger
→ Character Interpretation
→ Desire / Intention
→ Decision
→ Action
→ Counteraction / Response
→ Consequence
→ New State
```

不是每个Beat都机械填满八格；链条只保留证明行为因果所需的最小信息。若人物“突然坐过去 / 突然告白 / 突然改变主意”而缺少Trigger、Interpretation、Desire或Decision，标记Motivation Gap，不把剧情便利当作人物行为。

### Character Performance Intent Handoff

- What the character wants
- What the character hides
- What the character wants the other person to believe
- What changes their mind
- Subtext
- Inner Conflict

这些是Writer给Director / Performance Layer的上游意图，不是表演动作清单。眼神、停顿、呼吸、身体朝向、Blocking、Composition与Camera由Director Module和Performance Layer决定。

## Writer Decision Engines

### Story Logic / Causality

关键行动至少能沿`Trigger → Interpretation → Desire → Decision → Action → Consequence → New State`追溯。外部事件可以触发故事，但人物行动必须从其认知、欲望、恐惧、关系与已有事实生长；巧合可以制造问题，不应无依据替人物解决核心问题。

### Character Engine｜Complexity-scaled

按题材和体量选择最小充分组合：`Want / Need / Fear / Flaw / Wound（题材需要时）/ Belief / Misbelief / Objective / Hidden Objective / Relationship Need`。极短片或功能角色可以只保留Want、当前Objective与关系功能；长片、剧集或角色驱动项目才展开Wound / Misbelief与长弧。禁止把完整心理表格机械塞进每个短片，也禁止把推断当成用户已确认人物事实。

### Scene Value Change

每场戏至少产生一种有意义变化：`Information / Relationship / Decision / Power / Emotional / Expectation Change`。可以是克制的微变、阶段性确认或有明确功能的Intentional Hold；若场景开始与结束在所有维度都相同，且没有必要的建立、等待、呼吸或Setup功能，标记`Weak / Replaceable Scene`，进入合并、删除或重写诊断。不得把“必须正负翻转”硬套给所有题材。

### Writer Beat Is Not A Shot

Writer Beat是剧情、人物、关系或信息状态发生变化的单位。Director Module决定一个Writer Beat用一个Shot、多个Shot、长镜头、声音、遮挡或反应来呈现；多个Writer Beat也可在生成容量允许且可读时由一个长镜承载。Writer不得规定Shot数量，Shot也不得凭空脱离Writer Beat或明确的Director Purpose。

### Conflict / Stakes / Escalation

场景Objective需要可识别的阻力；冲突可来自人物、关系、时间、环境、秘密、制度、信息不对称或人物内部矛盾，不等于争吵。逐步检查行动代价、选择难度与后果是否升级或转向；强度服从Genre Promise、时长和用户意图，不默认商业短剧式高密冲突、连续反转或“爽点”。

### Dialogue / Subtext

内部分析链为：`Dialogue → Surface Meaning → Subtext → Hidden Objective`。对白优先承担目的、权力、回避、试探、攻击、防御、欺骗、关系变化或人物声音，而不是单纯解释剧情。角色设定不支持直说时，`我一直很想你`之类台词应被识别为Subtext Opportunity，再判断改为回避、错位话题、动作、沉默或保留直说是否更符合角色；不机械删对白，也不全局强制少对白。

### Setup / Payoff And Information Architecture

维护`Setup / Plant / Foreshadow / Callback / Payoff / Reversal / Recontextualization`义务及其来源、首次出现、预期回收、实际状态与不可提前暴露项。短片只保留高价值对，长片/剧集按复杂度扩展；不设全局数量配额。

Writer决定信息何时进入故事：`Reveal / Withhold / Delay / Mislead / Confirm / Recontextualize`，并区分观众与各角色已知/未知。Director决定这些信息具体如何被看见或听见。任何下游拆分、剪辑或Prompt都不得遗漏Payoff、把Setup误提前成答案，或改变锁定的Reveal timing。

### Character / Relationship Arc And Structural Rhythm

弧线至少可追溯`Start State → Pressure → Choices → Turning Points → End State`。关系弧不仅是对白内容，还应提供距离、信任、权力、共享目标、回避或承诺变化的上游依据。Structural Rhythm同时检查外部事件密度与内在情感强度的起伏；双轨可同步或错位，不强制固定三幕百分比、固定节拍数或每段同一种冲突密度。

### Rewrite / Diagnosis

Existing Script默认只读检查：causality、character motivation、scene necessity、scene value change、beat progression、conflict / stakes、dialogue / subtext、setup / payoff、information architecture、pacing / escalation、character / relationship arc与ending payoff。先记录问题、影响与可优化方向；只有用户已明确授权时，才调用`knowledge/writer/screenwriting_optimization.md`或`knowledge/writer/script_adaptation.md`改写。

### Commercial Objective And Writer Beat｜商业目标下的Writer形态

商业目标（品牌诉求、引流与转化）**不拥有剧情事实**，但它是合法的Payoff义务来源，必须长在Writer Beat链上，不能贴在片尾。

- **传达目标=一条注意焦点链**：单一传达目标决定观众的第一注意目标依次落在哪里；多个卖点并列争夺第一注意目标时排序或明确不做，不两头兼顾。
- **转化动作是Payoff，不是落版**：结尾动作（关注、评论、私信、留资、合作、购买意向）必须由可见行为或状态收束，并回答"前面哪个Setup让它变得可信"；没有Setup支撑的转化动作标记为未兑现。
- **痛点与利益点都必须可见**：写"更省力"不构成执行内容；痛点落在可观察的处境上，利益点落在前后差异上。不得用恐吓、羞辱或不可解释的威胁制造压力。
- **专业结论不由作者生成**：知识型内容的结论、数据、剂量、适用范围与免责表述属于客户提供的事实；Writer只负责把它们变成可见过程，不负责推断、简化到失真或补写前提。
- **边界**：商业目标不得改写已锁定的关键因果、人物动机与Setup / Payoff义务；目标与已成立故事冲突时按`## Proposal And Revision Handoff`做最小修订或回报冲突，不静默改写。受众角色的说服路径与形态义务由`knowledge/branded_content/index.md`拥有；注意窗口与结尾结构由`knowledge/platform_profiles.md`拥有；年龄轴适宜性由`knowledge/audience_profiles.md`拥有且优先。

## Writer → Director Handoff

Writer交给Director的是：Story Intent、Character Intent、Scene Objective、Writer Beats、Relationship Change、Information Architecture、Subtext / Hidden Objective、Setup / Payoff obligations、Performance Intent、Scene Exit State与故事层AIGC限制。

Director据此决定Audience Experience、Performance Strategy、Blocking、Mise-en-scène、Composition、Camera Language、Rhythm Presentation与Reveal Presentation。若Director发现现有Writer Intent不可导演、相互冲突或超出执行容量，走`REDIRECT / rewrite feedback`返回STATE-01的最小受影响范围；不得在Scene、Shot、Clip或Prompt层静默改写关键因果、动机、信息时机与Payoff。

## Cross-stage Projection

| Stage | Writer projection | Boundary |
|---|---|---|
| STATE-00 | 最小Premise、Theme / Question、Dramatic Question、Genre Promise、Story Engine、Core Conflict | 只记录明确事实/Assumption，不写完整剧本或Camera |
| STATE-01 | Creation、Diagnosis、Character Engine、Scene / Beat、Dialogue / Subtext、Setup / Payoff、Arc与Information Architecture | 形成Production-Locked Script + Packet；Existing无授权不改写 |
| STATE-02 | Narrative / Character / Prop Function与Setup-Payoff relevance | Director决定视觉优先级；Writer不分配造型 |
| STATE-03 | 角色、环境、道具的剧情身份与状态变化义务 | 不负责视觉细节、材质或Camera |
| STATE-04 | Motif、Symbol、Story Arc、Setup-Payoff obligations | Director转译为Visual Dramaturgy |
| STATE-05 | Writer Beat Map、Value / Information / Relationship Change、Scene Exit State | Director形成Scene Camera Strategy；Writer Beat≠Shot |
| STATE-06 | 每个Shot可追溯到Writer Beat或合法Director Purpose | Shot数量、构图、焦段、机位与运镜归Director |
| STATE-07 | 保护Beat完整性、Setup / Payoff timing、Subtext continuity与Relationship Delta | Clip按生成容量组织，不为技术便利截断戏剧单位 |
| STATE-08 | Writer Intent Preservation + Director Intent Preservation | Writer不写Camera参数；Compiler只翻译当前Clip delta |
| Editing | 保护Beat order、Reveal timing、reaction logic、Setup / Payoff与Scene Value Change | 只在素材支持时调整呈现 |
| STATE-09 | Story Review定位Writing Failure | 与Directing / Generation / Editing Failure分层路由 |

## Route Boundary

以下输入属于`Creation Brief`：只有创意、题材、品牌需求、人物设定、情绪/场景、已有世界观，或明确说“帮我写一个剧本 / 先从剧本开始”，但没有可供逐段诊断的既有剧本或来源叙事正文。

以下输入不属于本分支：

- 完整或粗略剧本、初稿：进入Existing Script Diagnosis。
- 小说章节、故事梗概、品牌文案或其他具有既有叙事内容且用户要保留/转换的素材：进入Existing Material的Adaptation / Optimization Gate。
- 用户在既有Proposal上要求“修改这一场”：继续当前Script Development，只改受影响范围，不重新路由为从零创作。

## Minimum Project Intent Gate

先从用户输入与已确认项目事实推断：目标形式、预计时长/容量、受众、核心人物、世界/场景、主情绪或传播目标、必须保留项和禁止项。

只在缺失项会实质改变故事架构或造成品牌/事实风险时询问；问题必须最少且可直接决定分支。题材、角色名、具体地点、非关键时长等可以安全假设时，明确采用可修订默认值并继续，不用把创作变成长问卷。

## Client Brief And Commercial Fact Gate｜客户与商业事实门

项目存在已确认的品牌诉求或商业目标时，在**写任何可承诺的台词之前**必须先读`templates/00_project_start_template.md`的 Client Brief 节（客户与商业 brief）。本Gate决定商业约束以什么形态进入故事，而不是在片尾贴一句落版。

**先判定`交付语境`**：`self_initiated`（自制，用户即出品方）/ `client_commissioned`（委托，存在外部委托方）。它决定商业事实的**来源归属**，不改变本Gate的判定顺序，也不改变任何Gate、确认主体或Hard Stop。

- `self_initiated`且有自有品牌：第6项的"客户提供的受监管表述"指**用户以品牌方身份**提供或确认；第7项的审批链为`用户（品牌方）`，不产生第二个确认主体。
- `self_initiated`且无品牌诉求：本Gate不成立，按通用编剧判据走。
- `client_commissioned`：第6项指外部委托方提供或确认；第7项记录外部终审人。

**不得把"有品牌"等同于"有客户"**：品牌诉求是内容事实，委托关系是关系事实，两者各有来源、互不推定。自制片出现真实品牌时不得按"客户已确认"处理，也不得据"有品牌"提高授权假设。

按以下顺序落到剧本层，全部为Writer Authority：

1. **主传达目标先收成一条注意焦点链**：多个卖点并列时排序或明确不做，不两头兼顾；被降级的卖点只能由背景或道具承担。
2. **产品按主角型 / 使能型 / 背景型之一进入剧情**，其角色决定它在哪些场景里可以被看见、以及是否参与冲突。
3. **商业形态（宣传 / 科普 / 产品 / 案例 / 招商 / 雇主品牌）决定"必须让观众看见什么"**，不决定段落数、秒数或节拍——节奏仍按`## Minimum Project Intent Gate`确认的目标形式走`knowledge/adaptation/short_form_drama_adapter.md`。
4. **受众决策链角色决定说服路径落点**：决策者看结果与代价、使用者看过程体感、影响者要一句能转述的可见事实、代决策者看安全与后果；一条主链，其余由次级承载。
5. **转化动作是Payoff，不是落版**：结尾的关注、私信、留资、合作或购买意向必须由可见行为或状态收束，并回答"前面哪个Setup让它变得可信"；没有Setup支撑的转化动作标记未兑现。
6. **客户提供的受监管表述只能原样内置或留后期叠加**：资质、功效、价格、免责声明、真实机构与合作关系、授权人物或声音一律由客户提供；其呈现位置与可读性由`knowledge/branded_content/`各原子拥有，本Gate只决定它长在剧情的哪一拍上。
7. **客户方终审人只决定客户侧由谁确认**，不改变资产双确认、Production Script Proposal确认与任何Hard Stop；交付物规格（条数 / 版本 / 画幅 / 时长 / 字幕落版）来自 Client Brief 节，不由制作推定。

商业目标不拥有剧情事实：它与已锁定的关键因果、人物动机或Setup / Payoff冲突时，按`## Proposal And Revision Handoff`做最小修订或回报冲突，不静默改写。Client Brief 节缺失或关键项为`Pending`且会改变当前创作方向时，保持STATE-01 IN_PROGRESS并只询问最小必要项；不得为推进而虚构客户事实。

## Director-first Story Development

按以下决策链发展故事，但不把链条机械输出成分析报告：

1. **Dramatic Intent**：作品为什么存在；希望观众最终经历什么变化。
2. **Audience Experience**：开场与结尾时观众知道什么、感觉什么、等待什么。
3. **Dramatic Question / Core Conflict**：主问题、欲望、阻力与代价是否能通过选择和行动成立。
4. **Character Objective / Relationship Arc**：人物当下想得到什么、隐藏什么、彼此关系如何发生可表现的变化。
5. **Information Strategy**：决定何时`Reveal / Withhold / Delay / Confirm / Recontextualize`；不一次性解释所有事实。
6. **Visual Action Design**：把抽象心理与说明转为行动、失败动作、道具处理、视线、停顿、反应和结果。
7. **Spatial / Blocking Potential**：让距离、朝向、靠近/退让、占据/退出和空间障碍能够承载关系变化；这里只写剧情调度可能，不建立正式Blocking Map。
8. **Performance Opportunity**：给演员可观察的刺激—注意—反应—选择—余韵，而不是只给情绪形容词。
9. **Rhythm Architecture**：组织建立、累积、转折、释放与余韵；不同题材可采用不同对白密度与节奏。
10. **AIGC Directability**：在不牺牲核心意图的前提下控制人物、场景、动作阶段、转场与并发负荷，并准备可执行替代方案。

导演思维在这里决定“发生什么、观众如何获得信息、人物关系如何通过可见行为变化”，不决定“用什么镜头拍”。禁止在剧本中机械加入35mm、特写、推镜、摇镜、机位、镜头编号、时间码或正式Shot Design字段。

## Dialogue Principle

不全局要求少对白。对白可以承担角色声音、权力、回避、冲突、诱导、误解和关系变化；优先替换只负责说明剧情、复述画面或直说情绪的解释性对白。动作、表演、空间、道具和沉默能更准确表达时使用它们；类型、节奏与角色需要高对白密度时允许保留。

## Scene Director Intent Source Data

为每个候选场景内部维护以下轻量source data：

```text
Scene Objective
Audience Start State
Audience End State
Character Objective
Relationship Delta
Information Strategy
Performance Opportunity
Spatial Potential
Rhythm Intent
```

这些字段用于创作与QA，并随确认后的剧本作为上游导演意图交给STATE-05/06；默认不机械写入最终剧本文本，不成为Template新栏目、Portable State字段或STATE-06 Director Decision Notes。若剧本正文已经用行动、调度、反应与节奏充分承载，不重复附加解释。

## AIGC Directability Check

逐场检查：

- 抽象文学句是否保留原意的同时具有可见/可听载体。
- 重要动作是否有起点、路径/过程和结果；简单动作不强制过度拆解。
- 情绪是否能由可观察行为、声音或选择承载，而非只靠内心独白。
- 场景空间是否支持后续Blocking和关系变化。
- AI视频难以稳定生成的描述是否已简化、拆分或提供不损害叙事的替代方案。
- 人物、地点、动作阶段、口型、FX与状态转换的并发负荷是否适合目标时长。

文学表达可以保留，但不能成为唯一不可视化载体。

## Craft Manual｜工艺手册

本手册提供**带条件的手段**，不是配方、不是节拍表、不是页数标准。它与`knowledge/adaptation/short_form_drama_adapter.md`的硬门互不覆盖：硬门只在其适用目标下生效，本手册在所有叙事项目下可用。

**使用纪律**：条目只在`成立条件`满足时使用；条件不满足时不得因为"这是好技巧"而套用。任何把本手册条目写成"第N分钟必须发生X""每场必须有钩子""类型片必须三幕"的用法都越权，见`knowledge/genre/index.md`的`## Craft And Formula｜工艺与公式`。本手册不拥有Camera Language、Shot、Clip、资产或Prompt字段。

### 结构操作

**结构从承诺与段落生长，不从上限生长**
- 成立条件：需要一个能承载多个场景的中层单位时。
- 手段：把一组场景组织为一个段落，先定该段落的单一思想，再填场景；段落的边界由"它实现了哪个故事目标"决定，不由时长决定。
- 反用场景：单场景或两分钟以下作品不需要段落层，硬加会制造空转。
- 失效信号：段落没有可说的单一思想，只剩一串同类场景。

**支点动作两头推**
- 成立条件：素材已有明确的价值冲突，但不知从哪一段入手，或前史与结局都还立不住。
- 手段：先定一个中间动作作支点，向前推"做这件事之前他必须是什么人"，向后推"做完之后世界必须怎样处置他"。前史与结局从同一个动作生长，比分别设计更容易一致。
- 反用场景：支点动作不违反人物原有的价值观时，两头都推不出东西——此时它只是情节，不是支点。
- 失效信号：两个追问有一个答不出。

**激励事件必须上屏并打破平衡**
- 成立条件：故事的主要欲望尚未有明确起点时。
- 手段：让事件在屏幕上发生，彻底打破人物原有平衡，且人物必须对它作出反应——拒绝也是反应。事件应投射出此后必须兑现的场面。
- 反用场景：把事件放在幕后、只用对白交代，等于没有激励事件。
- 失效信号：事件之后人物的处境与事件之前没有可指认的差别。

**进展纠葛靠代价升级，不靠冲突加量**
- 成立条件：中段（第二幕、或短片的中段）出现重复感、打滑或节奏停滞时。
- 手段：追问每一次新行动是否提高了人物付出的代价或缩小了他的选择余地；难度应来自已建立的事实，而不是新增麻烦。
- 反用场景：换个更强的反派或再加一次争吵，只增加音量，不产生纠葛。
- 失效信号：后一个障碍可以用与前一个相同的方式解决。

**中点改变人物与目标的关系**
- 成立条件：作品长度足以形成两段（约四分钟以上），且中段前后需要不同的动力时。
- 手段：在中段让人物对目标、对自己或对真相的理解发生一次反转（假胜利或假失败），使后半段无法再按前半段的方式推进。
- 反用场景：长度不足，或反转只是信息量增加而人物关系与选择空间没变。
- 失效信号：把中点前后的场景互换，故事依然成立。

**危机是两难，不是意外**
- 成立条件：高潮之前需要人物作出不可回避的选择时。
- 手段：把人物放进"两个都不愿失去"或"两个都不愿承担"的位置，且这个选择必须以人物已建立的价值为准才能作出。
- 反用场景：用巧合、外援、上级来人、血缘发现或幕后处理解开困局——这会让此前积累的代价失效。
- 失效信号：观众能指出"他其实可以不做这个选择"。

**高潮集中在一次兑现**
- 成立条件：全片必须有一个最高强度的事件。
- 手段：把最强的选择、揭示、动作或情绪兑现集中在一处，并让它直接回应核心冲突、产生不可逆结果。
- 反用场景：高潮太早出现，或强度靠音量与情绪堆叠而非选择。
- 失效信号：看完之后说不出"最重的那一下"是哪一下。

**结局兑现承诺，并改变稳定状态**
- 成立条件：所有作品，独立成片时同样适用。
- 手段：结尾完成本段承诺，并把人物或关系推进到一个与开场不同的稳定状态；需要续接时留下下一事件或未完成欲望。
- 反用场景：为留钩子而推翻已建立的因果，或用一段说明代替状态变化。
- 失效信号：结尾与开场的状态在所有维度都相同。

### 人物构建

**pressure 定义人物，标签不定义人物**
- 成立条件：需要让观众相信人物的选择时。
- 手段：人物在压力下的选择才构成其真实性格；外貌、职业、说话习惯、喜好只构成识别标签，不构成性格。识别标签是快捷手段，性格必须由选择证明。
- 反用场景：把"性格标签"当成人物事实（"他很温柔"因此他做温柔的事），或用标签替代当前核心事件中的具体选择。
- 失效信号：人物在任何压力下都只按标签行事，观众能预判他的每一步。

**want 与 misbelief 成对设计**
- 成立条件：需要人物弧、或人物在结尾必须与开场不同时。
- 手段：人物意识层要什么（want）与他深信的错误见解（misbelief）分开命名；故事的转折让人物的错误见解受到压力，结局是该见解被击败、被确认或被放弃的时刻。
- 反用场景：只有want没有misbelief时，人物可以完成任务，但不会变化；此时不必强加弧线。
- 失效信号：结尾与开场，人物对同一件事的判断完全相同，且作品要求观众感受到变化。

**起源场景给misbelief一个来处**
- 成立条件：misbelief会实质影响人物在主线上的选择时。
- 手段：用一个可呈现的过去事件（回忆、物件、他人一句话）说明这个错误见解从何而来；它只需被看见一次，不需要被解释。
- 反用场景：用旁白或对白直述"他因为小时候……所以现在……"，会把人物变成案例。
- 失效信号：观众能说出人物的行为，却说不出他为什么这样看世界。

**对手必须持有可用的武器**
- 成立条件：冲突需要一个持续施压的来源时。
- 手段：对手（可以是人、关系、制度、时间、环境或人物自身）必须掌握能真正伤害主角的东西，且其动机在人性层面可理解；最强的对手常常是人物自己。
- 反用场景：对手只有恶意没有筹码，或力量明显弱于主角——冲突会退化为等待。
- 失效信号：主角只要愿意就能随时解除冲突。

**次要人物承载反照，不承载人数**
- 成立条件：需要一个角色来暴露主角不愿承认的部分，或承载主题的另一面时。
- 手段：让次要人物的立场与主角形成直接的反照或对立（旧我的镜像、主题的反题、主角不敢成为的人），并让他们之间形成一张互相牵制的网，而不是各自独立的支线。
- 反用场景：为丰富世界而增加功能重复的角色——同功能角色应合并。
- 失效信号：删掉某个次要人物，故事没有任何一处需要重写。

### 场景与对白技法

**进得晚，出得早**
- 成立条件：场景需要在有限时长内保持张力时。
- 手段：在冲突已经开始的时刻切入，在冲突被完全解决之前离开；场景开头与结尾都不交代过程。
- 反用场景：需要观众看清空间、状态或关系基线时，过早切入会让后续变化无从被察觉。
- 失效信号：场景前三分之一用于铺垫，最后一句把话说尽。

**每场至少一次状态变化，并是可指认的那种**
- 成立条件：所有叙事场景。
- 手段：写前记录开场状态，写后记录结束状态；至少一个维度必须改变——信息、关系、决定、权力、情绪或观众预期。允许有明确功能的呼吸场与等待场，但其功能必须能说出来。
- 反用场景：没有任何维度变化、也没有建立、呼吸或Setup功能的场景，应合并、删除或重写。
- 失效信号：场景删掉后，前后场景的因果与人物状态都不受影响。

**转折点只能由动作或揭示创造**
- 成立条件：场景需要让观众感到方向改变时。
- 手段：让改变状态的节点是一个可见动作或一条被揭示的信息，并让它同时产生惊奇、好奇、见识与新方向。
- 反用场景：把转折写成一次情绪升高或一句总结性台词，观众会感到"说到了"而不是"发生了"。
- 失效信号：说不出这场是在哪一句或哪个动作上转向的。

**一个场景只押一对价值，并让它翻转**
- 成立条件：冲突需要可读、可比较的强度时。
- 手段：确定本场摆在台面上的价值对（如信任/怀疑、自由/安全），标注开场负荷与结束负荷，全场的动作与台词都朝这个负荷施压。
- 反用场景：同一场里并列三对以上价值，观众无法判断自己在看什么。
- 失效信号：开场与结束的价值负荷相同，或无法命名本场的价值对。

**冲突要直接相对，不要相切**
- 成立条件：场景有两个人或两种力量时。
- 手段：确认双方想要的东西互相排斥，而不只是互不相干；对抗力量应直接相对。
- 反用场景：双方各说各话、目标不冲突的场面，无论多激烈都不构成冲突。
- 失效信号：把一方撤出场景，另一方的行动完全不受影响。

**重复节拍是场景最早的病征**
- 成立条件：场景写到中段感到打滑、或需要判断是否该删时。
- 手段：逐拍标出行动与反应的动词形态，检查是否在用不同措辞重复同一策略；每拍必须比上一拍更接近转折点。
- 反用场景：必要重复本身不是病——判断标准是该重复是否推进冲突、塑造性格或改变状态；不推进的重复才删。
- 失效信号：同一策略出现第二遍而价值负荷没有变化。

**台词的行动测试**
- 成立条件：每一次有人开口时。
- 手段：把每句台词还原为它正在执行的行动（试探、回避、攻击、安抚、交换、拖延、表明立场），答不出行动的台词应删除或重写；场景存在于人物通过说话所采取的行动里，不存在于说话本身。
- 反用场景：闲聊只有在超越自身、与主题或关系连接时才可用。
- 失效信号：把该句换成一个表情或一个动作，场景毫无损失。

**遮名测试**
- 成立条件：需要判断角色是否有可辨识的语言身份时。
- 手段：遮住角色名，只看台词——能否分辨谁在说。人物的用词、名词与动词反映其知识范围，修饰语、情态与句法反映其个性。
- 反用场景：非写实类型允许一定的语言同质化，此时测试的强度下调。
- 失效信号：所有角色都在用作者的语言说话。

**互换测试**
- 成立条件：需要判断一句台词是不是"成套大话"（换谁都能说的通用表态）时。
- 手段：把这句词换给另一个角色说——若仍然成立，说明它不来自这个人物在此情境下的性格，应重写或改为动作/沉默。
- 反用场景：功能性信息句（时间、地点、指令）不受本测试约束。
- 失效信号：整场戏的台词可以任意分配给在场任何角色。

**潜文本是默认状态**
- 成立条件：写实类型，或人物有不愿说出口的处境时。
- 手段：让人物说出口的话与其真实意图之间存在可察觉的落差；落差由处境、关系与压力产生，不由作者埋伏笔产生。
- 反用场景：非写实类型（神话、童话、科幻、动画、寓言）允许减少潜文本；人物在极端压力下直说也是真实的。
- 失效信号：角色用谁也不会使用的说话方式表达情绪，或把内心活动完整报告出来。

**对手之间不达成一致**
- 成立条件：场景中有两人以上、且需要保持张力时。
- 手段：让每句台词对下一句构成挑战；不要让任何两个人在任何一点上完全一致——一致即静止。
- 反用场景：需要表现同盟、和解、疲惫或时间流逝的场景，一致本身可以是内容。
- 失效信号：一场戏里所有人对同一件事持相同态度，且没有新的分歧被引入。

**两人对话僵住时引入第三件事**
- 成立条件：两人对话变成轮流陈述、或信息交换平铺时。
- 手段：让两人以第三方事物作为争斗的出口——一件道具、一个不在场的人、一个共同目标、一杯酒、一段距离；注意力落在第三件事上，关系通过它变化。
- 反用场景：需要正面摊牌的场景，第三件事会稀释强度。
- 失效信号：把第三件事删掉，对话仍然完全成立。

**细节必须是具体的**
- 成立条件：需要让人物、处境或关系可信时。
- 手段：用具体名词与动作动词替代概念与评价；把"他很紧张"写成可观察的行为，把"很贵的衣服"写成可指认的衣物。细节要服务"这一个"人物与场面，不卖弄。
- 反用场景：细节若只是作者展示见闻、不推进冲突也不塑造性格，无论多生动都删。
- 失效信号：同一条细节重复出现而状态没有变化。

**道具的作用由别人对它的动作累积**
- 成立条件：需要一个能承载关系与主题的实物时。
- 手段：让道具每次出现都由**另一个人的动作**改变其身份或状态（赠予、夺走、损坏、转交、改写）；每次改变压在一次价值转折上，其意义随次数累积。
- 反用场景：道具若不是可被他人夺、毁、改、传的实物，不适用本条目。
- 失效信号：某次露面没有任何人对它做事，删掉它不影响剧情。

**对白优先让位给可见行为**
- 成立条件：需要表达抽象心理、背景或评价时。
- 手段：先问这一信息能否用动作、反应、空间距离、道具处理或剧情内声音表达；可以时不再写台词。
- 反用场景：类型与节奏需要高对白密度时允许保留，本条目不构成"少对白"的全局要求。
- 失效信号：画面已经说清的事又被台词说了一遍。

**晚入场、早离场的不只是场景**
- 成立条件：需要压缩对话过程、提升节奏时。
- 手段：对白内部同样可以跳过程序性部分，直接进入有效交换。
- 反用场景：程序性内容本身承担信息或压力（等待、拖延、仪式感）时保留。
- 失效信号：对话开头与结尾承担的是礼貌，而不是内容。

## Directable Screenplay QA

Production Script Proposal输出前，内部至少确认。1—10检查每场戏与段落的成立性；11—14检查整片看点与兑现：

1. Scene Purpose清晰。
2. Audience Experience在场景或段落结束时发生变化。
3. Character Objective / Conflict可观察。
4. Relationship Change可表现，或有明确的Intentional Hold理由。
5. Visual Action足够，不依赖大段解释性对白。
6. Performance Opportunity存在。
7. Spatial Dramaturgy / Blocking Potential存在。
8. Information Strategy有层次。
9. Rhythm Curve可执行。
10. AIGC Directability合格。
11. 开场钩子成立：开场在目标媒介允许的注意窗口内建立异常、欲望、悬念、关系张力或视觉问题，核心目标与阻力不因前置信息过长而推迟进入。
12. 高潮兑现成立：最高强度的选择、揭示、动作或情绪兑现集中且可辨认，真正回应核心冲突并产生结果；巧合可以制造问题，不得无依据替人物解决核心问题。
13. 情绪体验成立：观众能经历按Genre Promise选择的目标情绪（期待、压力、释放、共鸣、惊喜、爽感、虐感、温暖等），而非只理解事件。
14. 结尾兑现成立：结尾完成本段兑现，并按项目需要留下下一事件、关系变化、信息缺口或余韵；独立成片且不需要续接时记录Not Applicable及理由。

11—14的钩子形态、强度与密度服从Genre Promise、目标媒介与用户意图；"无聊"的判据是无变化或无期待，不是密度不够，不得因本组检查机械加入反转、爽点或固定节拍模型。

QA是内部生成与修订框架。最终剧本必须仍是可独立阅读的剧本，不得变成逐项分析表、导演问答或提前写好的分镜表。

## Directable Screenplay Gate｜可失败判定

QA十四项判定"是否具备"，本Gate判定"是否成立"，因而它可以失败。以下每项必须在剧本正文里指到具体位置；指不到即判定失败，先做最小修订再输出Proposal。

1. **变化可指认**：每个场景的关系变化、信息变化或价值变化，必须能指到剧本正文中的一个动作、一个反应或一条被揭示的信息。指到的若是一句解释性台词、一个"此处插入闪回"式指令、或一次旁白说明，判定失败。
2. **人物选择可追因**：人物在关键节点上的选择，必须能沿`Trigger → Interpretation → Desire → Decision → Action`追溯到剧本已给出的事实。追不到即Motivation Gap，判定失败。
3. **场面不可随意互换**：把两个场景的位置对调、或删掉任一场，因果、人物状态或观众信息必须出现可指认的损失。无损失的场景判定失败，进入合并、删除或重写。
4. **台词具备行动**：每句台词必须能还原为一个正在执行的行动，或能在遮名测试／互换测试中被辨认归属。既无行动又无法辨认的台词判定失败。
5. **结尾状态已改变**：结尾时人物或关系的稳定状态，必须与开场存在至少一个可指认的差别；作品要求留下余韵时，该余韵必须由已建立的事实产生。

**本Gate与QA的分工固定**：QA保证作品要素齐备，本Gate保证要素成立。两者都通过才输出Proposal；本Gate失败时不得以"QA已通过"为由放行。

## Requirement Fidelity｜需求保真判定

项目存在`templates/00_project_start_template.md`的 Client Brief 节（品牌或商业项目）时，Proposal输出前必须逐项核对**客户与创作需求是否真的进入了剧本**。本判定沿用`knowledge/writer/script_adaptation.md`的`### 6. Adaptation Fidelity Check`形态，是其**片级对应物**，不新增第二套判定体系。

对 Client Brief 节中每个已确认项，以及`## Client Brief And Commercial Fact Gate｜客户与商业事实门`确认过的每一项商业约束，逐项记录一个结论：

- **`DELIVERED`**：在剧本正文中的位置可指认——写明是哪一场的哪个动作、哪条台词、哪个道具状态或哪一次信息揭示。
- **`DOWNGRADED`**：经确认由背景、道具或次级承载承担，并写明由谁确认。
- **`PENDING`**：受监管表述、商业事实或客户决定缺失，记为Pending Decision并列出缺失项与owner。
- **`NOT_APPLICABLE`**：该需求不适用于本片，并写明依据。

缺少上述任一结论的已确认需求，视为**静默丢失**，判定失败，不得输出Proposal。

**本判定与Requirement Router的分工固定**：`knowledge/writer/index.md`的`## Requirement Router｜需求路由`决定本次**读什么**；本判定决定产出**兑现了什么**。路由命中而未兑现时，本判定失败；本判定通过也不代表创作质量成立，质量仍由`## Directable Screenplay QA`与`## Directable Screenplay Gate｜可失败判定`判定。

## Proposal And Revision Handoff

1. 完成原创故事开发、Directorial Interpretation与QA后，输出完整`Production Script Proposal`。
2. 写`Script Status: Optimized Proposal`、`STATE-01: IN_PROGRESS`与`Pending Decision: 等待用户确认Production Script Proposal`并停止。
3. 用户要求修改某场、对白、人物线、节奏或结局时，保持Script Development，只修订明确范围及必要相邻因果，再次执行受影响场景QA并等待确认。
4. 只有用户明确确认当前Proposal后，才升级为`Production-Locked Directable Screenplay`（状态字段仍使用`Production-Locked`），完成STATE-01并进入STATE-02。

## Completion Check

- Input Route确为Creation Brief，未误吞已有剧本或来源叙事文本。
- Minimum Project Intent Gate只询问真正影响架构的缺失项，其他可安全项已用可修订假设继续。
- Director-first Story Development十步均有内部结论。
- 每个场景已建立轻量Scene Director Intent，且未污染最终剧本文本。
- Directable Screenplay QA十四项通过或已完成最小修订（11—14为整片看点项）。
- `## Directable Screenplay Gate｜可失败判定`五项在Proposal输出前逐项指认，指不到的已完成最小修订。
- 项目存在 Client Brief 节时，`## Requirement Fidelity｜需求保真判定`已对每个已确认需求给出`DELIVERED / DOWNGRADED / PENDING / NOT_APPLICABLE`结论，无静默丢失项。
- 没有SHOT、CLIP、焦段、机位、运镜、Storyboard或Prompt内容。
- Proposal仍等待用户明确确认，未提前进入STATE-02。
