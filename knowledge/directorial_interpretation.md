# Directorial Interpretation

## Purpose

本Knowledge位于STATE-01 Screenplay Development / Optimization Gate中，在原创故事开发或编剧优化之后，把已经成立的故事提案转换为可拍、可表演、可被观众按预期接收的制作版叙事。它处理“信息和情绪如何在剧本层被看见与听见”，不处理“具体用哪个镜头拍”。

本层不创建新STATE，不拥有Template字段，不创建Scene / SHOT / CLIP ID，不选择焦段、机位、运镜或Seedance技术，不生成STATE-06的`Director Decision Notes`。

## Module Contract

- **Module Name**：Directorial Interpretation
- **Module Type**：STATE-01条件性导演化叙事Knowledge
- **Trigger**：`knowledge/screenplay_development.md`已形成结构成立的原创候选故事，或Screenwriting Optimization已形成结构成立且保护项清楚的候选故事
- **Not Triggered As**：导演风格选择、Visual Development、Scene Breakdown、Detailed Shot Design、Director Decision Layer、Storyboard或Seedance Prompt编译
- **Position**：Creation为`Director-first Screenplay Development → Directorial Interpretation → Directable Screenplay QA → Production Script Proposal`；Existing为`Screenwriting Optimization → Directorial Interpretation → Production Script Proposal`，全部位于STATE-01内部
- **Required Inputs / Owners**：原创开发或优化后的目标、冲突、Beat、人物动机、信息顺序、保护项、适用的局部范围、时长约束与用户明确要求；事实继续由用户及STATE-01 Workflow拥有
- **Output Owner**：本Knowledge只提供导演化处理方法与内部结论；最终Production Script Proposal结构由`templates/02_script_analysis_prompt.md`拥有
- **Read / Write Boundary**：只读STATE-01候选故事与项目事实；只写入当前STATE-01提案Artifact，不修改Confirmed Assets、Visual Direction、SHOT、CLIP或后续内部Notes
- **Downstream Consumers**：Production Script Proposal与用户确认后的Production-Locked Script
- **Protected Upstream Facts**：世界观、角色身份与关系、剧情结果、品牌要求、核心创意、用户锁定台词/事件、Optimization Scope
- **Conflict Route**：导演化表达需要改变核心结果、突破保护项/范围或补充会实质改变架构的事实时，Creation返回Screenplay Development，Existing返回Screenwriting Optimization / 用户确认；不得在本层静默补造
- **Deterministic Invariants**：Required Interpretation Dimensions均检查；每个手段服务已确认叙事目的；无正式镜头技术；无Director Decision Notes职责重叠；未确认提案不下传STATE-02

## Boundary With Director Decision Layer

两者都使用导演思维，但解决不同问题：

- **STATE-01 Directorial Interpretation**：在原创或优化后的制作版剧本提案中决定哪些信息通过动作、眼神、停顿、人物距离、声音、回忆或主观体验来表达，以及观众按什么顺序获得信息。它仍属于剧本层，并把适用结论写回轻量Scene Director Intent source data。
- **STATE-06 Director Decision Layer**：在Professional Detailed Shot Script完成后，按Scene / Shot Group决定观众如何经历已确认分镜、镜头总体动或停、构图/距离、色光、表演、声音、节奏与Seedance降级。它不得回到STATE-01改写剧情。

本层禁止出现SHOT编号、CLIP编号、焦段毫米数、机位、具体运镜路径、镜头表字段、十三维Director Decision Notes或最终Prompt字段。

## Required Interpretation Dimensions

每次至少检查以下九组导演化问题：

1. **动作表达**：哪些背景、动机、情绪或关系信息可以由选择、行为、失败动作、物件处理或行动后果表达，而不由说明性台词承担。
2. **眼神与注意**：人物看什么、回避什么、何时转移注意；视线变化传递什么已存在的信息或关系。
3. **停顿与反应**：哪些地方需要人物先接收刺激、产生可见/可听反应，再行动或说话；停顿是否承担悬念、压抑、理解或余韵。
4. **空间关系表达**：人物靠近、远离、阻挡、让路、占据、退出或保持距离如何表现权力、亲密、戒备、误解与变化。这里只定义故事调度意图，不建立STATE-06 Spatial Blocking Map。
5. **视觉揭示顺序**：观众先看到什么、后发现什么；揭示由人物行动、环境变化、道具状态或信息反应触发，避免一次性说明。
6. **人物调度意图**：谁先行动、谁等待、谁跟随、谁拒绝、谁在关键时刻改变位置或停止；调度必须服务人物关系和剧情结果。
7. **节奏与留白**：哪些Beat压缩，哪些反应或结果需要停留；高潮前是否有必要的等待，高潮后是否有收束或余韵。
8. **观众信息控制**：观众是先于人物、与人物同时、还是晚于人物知道关键信息；哪些内容必须暂缓、误导或只提供局部证据。
9. **导演化时间与声音手段**：声音先行、声音残响、碎片式回忆、主观化听觉/视觉、画外信息或有限省略是否能更清楚表达已存在的记忆、压力、误解或信息关联。

## Interpretation Method

### 1. Lock Narrative Objective

每个主要Beat先写清观众必须理解的唯一推进。若需要同时传达过多信息，返回Screenwriting Optimization删并或重排，不用导演手段掩盖结构问题。

### 2. Replace Explanation Selectively

不是所有台词都要视觉化。保留具有选择、关系、节奏或角色声音价值的台词；优先替换重复画面、解释情绪、复述背景的台词。

### 3. Build Stimulus → Reaction → Choice

关键情绪或行动变化至少具备：刺激来源、注意变化、可观察反应、行动选择、稳定结果。不得让人物无原因突然爆发或转变。

### 4. Control Reveal

为关键信息明确Audience Knowledge Position：

- `Ahead`：观众先知道，等待人物发现。
- `Aligned`：观众与人物同时知道，共享冲击。
- `Behind`：人物先知道，观众从行为和局部证据逐渐理解。

选择必须服务既有故事，不能用信息控制制造原文不存在的秘密。

### 5. Use Sound And Memory With Evidence

声音先行、回忆、主观化或残响只能来自已建立的台词、事件、环境声或角色体验。不得为了风格凭空加入旁白、幻觉、歌曲、重大闪回或新剧情事实。

### 6. Keep It At Script Level

输出描述“发生什么、谁如何行动/反应、观众何时获得信息、听见什么剧情内声音”，不描述摄影机如何拍摄。正式空间锚定、镜头节奏实现与声音执行留给STATE-05/06及Director Decision Layer。

## Production Script Proposal Handoff

交给Template的内容应包含：

- 每个段落或Beat的剧情目的
- 可见人物行动与反应链
- 必要台词、删减/合并后的信息
- 眼神、停顿、身体距离和调度意图
- 视觉揭示与观众信息顺序
- 剧情内声音、声音先行、回忆或主观化的适用位置及依据
- 节奏压缩、高潮与留白
- Protected Creative Locks、Optimization Scope与Pending Decisions

Creation Brief还必须把Scene Objective、Audience Start / End State、Character Objective、Relationship Delta、Information Strategy、Performance Opportunity、Spatial Potential与Rhythm Intent交回`knowledge/screenplay_development.md`做Directable Screenplay QA。该source data默认不作为用户可见固定栏目。

不得包含正式镜头表或为后续阶段预先锁死摄影技术。

## Completion Check

- 九组Required Interpretation Dimensions均有结论或Not Applicable理由。
- 动作、眼神、停顿、空间关系、调度、揭示、节奏、信息控制与声音/回忆手段都服务已成立的剧情。
- 没有新增世界观、角色身份、品牌事实或用户未授权情节。
- 没有创建SHOT、CLIP、机位、焦段、运镜、Director Decision Notes或Seedance字段。
- Production Script Proposal可供用户独立确认，且确认前仍是Optimized Proposal。
