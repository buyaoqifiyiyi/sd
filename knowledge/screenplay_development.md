# Director-first Screenplay Development

## Purpose

本Knowledge只服务STATE-01的`Creation Brief / Idea-to-Screenplay`分支：当用户明确要求“写剧本 / 从剧本开始 / 根据创意或品牌需求创作”且当前没有可供诊断的既有剧本或叙事文本时，把Idea / Brief / Concept发展为可独立确认的`Production Script Proposal`。

它不创建新STATE、不替代`workflows/02_script_analysis_workflow.md`、不拥有用户可见字段，也不把剧本创作伪装成既有文本优化。用户的创作请求本身授权生成剧本草案；它不授权越过Proposal Confirmation Gate、修改已确认项目事实或直接进入资产、Scene、Shot、Clip与Prompt阶段。

## Module Contract

- **Module Name**：Director-first Screenplay Development
- **Module Type**：STATE-01条件性原创剧本开发Knowledge
- **Trigger**：Input Route为`Creation Brief`，用户明确要求创作剧本或从剧本开始，且没有应优先走Existing Script Diagnosis的完整/粗略剧本或来源叙事文本
- **Not Triggered As**：既有剧本诊断、小说/故事文本改编、未经请求自动创作、独立Workflow、新主STATE、Scene Breakdown、Shot Design、Storyboard或Prompt编译器
- **Position**：`Creation Brief → Minimum Project Intent Gate → Director-first Story Development → Directorial Interpretation → Directable Screenplay QA → Production Script Proposal → User Review / Revision → Production-Locked`
- **Required Inputs / Owners**：用户Idea / Brief / Concept、已确认Project Bible事实、目标形式/大致时长或容量、受众/品牌目标、必须保留项与禁止项；这些事实只由用户和已确认项目资料拥有
- **Output Owner**：本Knowledge拥有原创故事开发方法、内部Scene Director Intent与Directable Screenplay QA；最终用户可见Production Script Proposal及确认/交接字段只由`templates/02_script_analysis_prompt.md`拥有
- **Read / Write Boundary**：只读用户输入与已确认项目事实；只把开发结果交给STATE-01 Workflow写入当前项目的Proposal Artifact与状态；不修改资产、Visual Direction、SHOT、CLIP、Portable Schema或Skill根目录项目兼容入口
- **Downstream Consumers**：`knowledge/directorial_interpretation.md`、用户确认后的Production-Locked Directable Screenplay、STATE-05 Scene Breakdown和STATE-06 Director Decision Layer
- **Protected Upstream Facts**：用户给定的核心创意、世界观、角色身份/关系、品牌诉求、事实/权利边界、指定结局/名场面/台词与禁止内容
- **Conflict Route**：缺失信息会实质改变题材、目标形式、品牌合规、核心人物或结局时，保持STATE-01 IN_PROGRESS并只询问最小必要问题；可用合理默认值继续且不改变核心意图时，记录Assumption并继续创作
- **Deterministic Invariants**：创作请求直接进入Creation Route而非Optimization Opportunity Report；不要求用户先在普通Chat写完整剧本；十项Directable Screenplay QA均通过或形成最小修订；每个场景有轻量Scene Director Intent；无机位、焦段、运镜、SHOT/CLIP或分镜表；未确认Proposal不进入STATE-02

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
