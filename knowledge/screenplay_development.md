# Screenwriter Module / Writer Intelligence Layer

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
- **Owner**：`knowledge/screenplay_development.md`
- **Trigger**：所有SD Film叙事项目；Creation Brief执行原创开发，Existing Script / Material执行只读Writer Diagnosis，获得合法授权后再调用现有Adaptation / Optimization子模块
- **Not Triggered As**：未经请求自动改写、Camera/Composition/Shot规则、独立Workflow、资产生成、Storyboard或最终Prompt Schema
- **Position**：`STATE-00 Writer Foundation → STATE-01 Creation / Diagnosis / Authorized Rewrite → Production-Locked Screenplay + Writer Intent → STATE-05 Writer Beat Projection → STATE-06/07/08 Preservation → Editing / STATE-09 Story Review`
- **Required Inputs / Owners**：用户Idea / Brief / Concept、已确认Project Bible事实、目标形式/大致时长或容量、受众/品牌目标、必须保留项与禁止项；这些事实只由用户和已确认项目资料拥有
- **Output Owner**：本Knowledge拥有Writer Intent Packet、原创故事开发、Writer Diagnosis、Writer→Director Handoff与跨阶段保护合同；最终用户可见Production Script Proposal及确认/交接字段只由`templates/02_script_analysis_prompt.md`拥有
- **Read / Write Boundary**：只读用户输入与已确认项目事实；只把开发结果交给STATE-01 Workflow写入当前项目的Proposal Artifact与状态；不修改资产、Visual Direction、SHOT、CLIP、Portable Schema或Skill根目录项目兼容入口
- **Downstream Consumers**：`knowledge/script_adaptation.md`、`knowledge/screenwriting_optimization.md`、`knowledge/directorial_interpretation.md`、STATE-02至09、Editing与Prompt Compiler
- **Protected Upstream Facts**：用户给定的核心创意、世界观、角色身份/关系、品牌诉求、事实/权利边界、指定结局/名场面/台词与禁止内容
- **Conflict Route**：缺失信息会实质改变题材、目标形式、品牌合规、核心人物或结局时，保持STATE-01 IN_PROGRESS并只询问最小必要问题；可用合理默认值继续且不改变核心意图时，记录Assumption并继续创作
- **Deterministic Invariants**：Creation / Existing双入口不变；Existing无授权不改写；Packet不成为Template或Portable State新Schema；Character Engine按复杂度调用；Writer Beat不等于Shot；Writer不规定Camera；Director不静默改写Writer锁；未确认Proposal不进入STATE-02

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

Existing Script默认只读检查：causality、character motivation、scene necessity、scene value change、beat progression、conflict / stakes、dialogue / subtext、setup / payoff、information architecture、pacing / escalation、character / relationship arc与ending payoff。先记录问题、影响与可优化方向；只有用户已明确授权时，才调用`knowledge/screenwriting_optimization.md`或`knowledge/script_adaptation.md`改写。

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

## Directable Screenplay QA

Production Script Proposal输出前，内部至少确认：

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

QA是内部生成与修订框架。最终剧本必须仍是可独立阅读的剧本，不得变成十项分析表、导演问答或提前写好的分镜表。

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
- Directable Screenplay QA十项通过或已完成最小修订。
- 没有SHOT、CLIP、焦段、机位、运镜、Storyboard或Prompt内容。
- Proposal仍等待用户明确确认，未提前进入STATE-02。
