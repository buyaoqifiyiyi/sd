# Director Module / Director Intelligence Layer

## Purpose

本文件是SD Film贯穿式Director Thinking、唯一的`Director Module / Director Intelligence Layer`连续性owner。它从STATE-00建立项目导演基线，在STATE-01形成剧本级意图，在STATE-05投影为场景执行意图，在STATE-06具体化为Shot级Director Decision Notes，在STATE-07形成Clip级执行合同，在STATE-08由Prompt Compiler翻译，在Editing中保护剪辑观点，并在STATE-09执行Director's Cut Review。

核心分层固定为：

`Director Module = 决策层 → Workflow = 执行层 → Knowledge = 专业知识支持层 → Prompt Compiler = 模型执行翻译层`

本层是persistent cross-stage decision layer，不创建新主STATE，不改变STATE-00至STATE-09，不拥有任何最终Template Schema，也不直接生成Seedance Prompt。内部使用轻量`DIRECTOR INTENT PACKET`传递方向；正式用户交付只保留当前阶段有用的摘要或可执行结果，不机械展示Packet字段、候选方案、拒绝理由或逐步推理。

## Module Contract

- **Module Name**：Director Module / Director Intelligence Layer；`Director Decision Layer`保留为兼容名称
- **Module Type**：贯穿STATE-00至STATE-09与Editing的内部导演决策Knowledge；不是Workflow、Template、新STATE或第二套Project State
- **Owner**：`knowledge/director_decision_layer.md`
- **Core Externalization**：Camera Language Module，owner为`knowledge/camera_language/index.md`
- **Trigger**：所有SD Film主流程项目；按当前阶段、当前Scene / Shot / Clip和任务dominance只运行最小充分部分
- **Not Triggered As**：独立用户步骤、固定分析报告、导演风格库、Camera Movement选择器、Knowledge Reflection替代品、最终Prompt新字段
- **Position**：`STATE-00 Project Director Baseline → STATE-01 Scene Director Intent → STATE-05 Scene Projection → STATE-06 Director Decision Notes → STATE-07 Clip Production → STATE-08 Director-to-Prompt Translation → Editing / STATE-09 Review`
- **Required Inputs / Owners**：剧情、项目目标、Confirmed Assets、Visual Direction、Scene / Shot / Clip事实、时长、边界和用户约束均由对应上游owner提供；本层只作导演判断，不静默新增或改写事实
- **Internal Output Owner**：本文件定义Packet与传递合同；当前Workflow拥有本阶段投影。Work/Codex按项目现有工件保存到`project_bible.md`相关既有区、确认剧本的Scene Intent source data、Scene Breakdown、`shots/director_decision_notes.md`或既有Execution Ledger、Clip Plan内部合同；普通Chat保留在当前Checkpoint / 可恢复上下文。不得在Skill根目录创建项目状态副本
- **Read / Write Boundary**：只读已确认项目事实；只写当前阶段内部导演数据和既有工件中的投影，不修改Canonical资产、Template字段、正式SHOT / CLIP顺序或Production-Locked剧情
- **Downstream Consumers**：STATE-00至STATE-09对应Workflow、`workflows/12_editing_workflow.md`、Prompt Compiler与Review
- **Conflict Route**：Project / Story事实返回STATE-00/01；资产叙事功能与外观权威返回STATE-02/03；Visual Dramaturgy返回STATE-04；Scene边界/Beat返回STATE-05；Shot Purpose / Blocking / Camera Decision返回STATE-06；Clip编排返回STATE-07；仅模型翻译、Prompt压缩或生成执行偏差留在STATE-08；后期可修项进入Editing
- **Deterministic Invariants**：主Pipeline不变；Packet不成为新Schema；每个Scene / Shot Group有且只有一份当前有效Director Decision Notes；Director Intent先于Knowledge选择；Camera choice由intent推导；最终Prompt保持`templates/10_video_prompt.md`兼容；Voice仍opt-in；Source Carries State, Prompt Carries Delta

## Camera Language Is The Execution Language Of Director Intent

镜头语言是Director Intent最主要、最直观的执行语言。它必须改变或控制观众知道什么、感受到什么、期待什么或理解什么，不能只为了“更电影”。

Director Module决定：为什么观察或介入、观众站在哪里、何时隐藏或揭示、人物关系需要被压缩还是拉开、镜头何时必须停住或开始运动。Camera Language Module负责把这些决定落实为构图、景别、机位、POV / Audience Position、焦段与画面距离感、前中后景、遮挡/Reveal、人物关系构图、运镜触发、Hold / Pause / Cut节奏及稳定降级。

空间与轴线不重复造规则：Camera Language必须调用现有Spatial Blocking、Pose Hierarchy、Relationship Topology、Delta Blocking、Relational Screen Geometry、REF-SKETCH与REF-TAIL合同。Director Module决定为什么保持或改变关系，Blocking系统决定如何锁定和验证。

## DIRECTOR INTENT PACKET

Packet是按项目逐步充实、按当前任务投影的内部source data，不是一次性长表，也不是要求用户填写的问卷。未知项保持Unknown / Not Applicable；只有会改变当前阶段决策的内容才进入工作上下文。上游事实改变时，只重算受影响层与下游投影。

### Project-level

- Directorial Thesis
- Audience Contract / Intended Audience Experience
- Genre Strategy
- Emotional / Dramatic Core
- Character & Relationship Arc
- Information Strategy
- Performance Strategy
- Spatial Dramaturgy
- Visual Dramaturgy
- Rhythm Strategy
- Sound Strategy
- AIGC Directability Constraints

STATE-00只建立可由用户输入直接确认的最小Project Director Baseline：`Directorial Thesis / Audience Contract / Genre Strategy / Intended Viewing Experience / Non-negotiable Dramatic Core`。STATE-01至04可以依据确认剧本与资产逐步补齐其余项目项，但不得把早期假设冒充锁定事实。

### Scene-level

- Scene Objective
- Audience Start State
- Audience End State
- Character Objective
- Relationship Delta
- Information Change / Reveal Strategy
- Performance Opportunity / Peak
- Spatial Evolution
- Rhythm Intent
- Transition Intent

Scene-level Packet由STATE-01生成source data，STATE-05结合Production-Locked剧本正式投影。它描述“这场戏怎样改变观众、人物与关系”，不写35mm、特写、低机位或推镜等Shot Design参数。

### Shot-level

- Shot Purpose
- Audience Effect
- POV / Audience Position
- Information Function
- Performance Function
- Blocking Function
- Camera Motivation
- Composition Strategy
- Shot Size / Lens / Camera choice as consequence of intent
- Cut / Hold Motivation

Shot-level Packet在STATE-06形成，并兼容既有`Director Decision Notes`。具体Camera choice必须服从固定决策顺序和现有Camera / Blocking owner，不能先选技术再补理由。

### Clip-level

- Clip Dramatic Function
- Start Dramatic State
- End Dramatic State
- Critical Performance Beat
- Critical Blocking / Spatial State
- Continuity Requirement
- Rhythm Requirement
- Information Timing Requirement
- Generation Risk / Simplification Boundary

Clip-level Packet由STATE-07在现有Clip Contract内投影，把Clip定义为`Dramatic Execution Unit`。它决定哪些相邻Shots必须保持在同一Clip才能完成情绪、关系或信息积累；不能为了技术方便把“怀疑→证据→确认”错误拆断，也不能为了保留情绪而把不兼容的时空、动作或模型负荷强行合并。

## Packet Persistence And Projection

Packet遵守“source data向下传递、阶段owner只写自己的具体化结果”：

1. STATE-00在Project Bible既有项目/故事/制作方向区域保存最小Project Director Baseline；不增加Portable State字段。
2. STATE-01把项目基线具体化为Project-level剩余策略与Scene Director Intent source data，随Production-Locked Directable Screenplay版本绑定。
3. STATE-02/03只读取资产相关的Dramatic Function、Narrative Priority与Casting / Screen Presence要求，不复制完整Packet。
4. STATE-04把项目意图翻译为Visual Dramaturgy / Mise-en-scène Direction，写入现有Visual Direction / Project Bible区域。
5. STATE-05生成Scene-level投影与Scene Camera Strategy，不创建SHOT或具体摄影参数。
6. STATE-06生成Shot-level Director Decision Notes，并让Camera Language / Performance / Blocking / Action PREVIS等能力执行。
7. STATE-07在现有Clip Detail / Clip Director Direction中形成Clip-level执行合同，不创建新ID或顶级Schema。
8. STATE-08只读取当前Clip必要的1—3个导演优先级并执行Director-to-Prompt Translation；Packet标题和内部标签不得输出。
9. Editing与STATE-09读取实际结果和当前有效Packet，不重新导演；如果结果证明上游决定错误，按owner返回。

## Task Dominance Router

每个Scene / Shot Group / Clip选择一种主要dominance；Mixed只在两个以上维度共同决定结果时使用。不得机械全量运行全部导演知识。

- **Performance-dominant**：主要变化来自注意、压制/泄漏、反应、对白倾听或关系微变；调用现有Performance Progression与Performance Arc Map
- **Spatial-Blocking-dominant**：主要变化来自距离、朝向、站位、遮挡、权力或共享空间；调用Spatial Blocking / Pose Hierarchy / Relationship Topology / Delta Blocking
- **Action-dominant**：主要变化来自路径、接触、受力、追逐、打斗或动作结果；调用Action PREVIS A1/A2/A3，并优先动作可读性、空间和力线
- **Information-dominant**：主要变化来自Reveal / Withhold / Delay / Confirm / Recontextualize；优先观众信息顺序、视点、遮挡、焦点与反应时机
- **Atmosphere-Rhythm-dominant**：主要价值来自等待、压迫、呼吸、余韵、环境接管或声画节奏；仍须能说明观众损失，不能把氛围当空洞装饰
- **Mixed**：只联合运行直接影响当前目的的能力，并先保护剧情、空间、动作因果和生成容量

## Stage Responsibilities

### STATE-00 Project Setup

建立最小Project Director Baseline，而不只记录平台、时长、画幅和最终目标。基线只来自用户已明确内容与可安全标记的假设，不进行剧本、视觉或镜头设计。

### STATE-01 Screenplay Development And Analysis

导演层控制Dramatic Intent、Audience Experience、Character Objective、Relationship Arc、Information Strategy、Visual Action、Performance Opportunity、Spatial Potential、Rhythm与AIGC Directability。Creation Brief与Existing Script / Diagnosis双入口保持不变。剧本阶段识别可镜头化机会，例如“先看见她没有回头，随后才意识到另一个人一直看她”，但不提前写Shot List、焦段、景别、机位或运镜。

### STATE-02 Asset Discovery

每个候选资产内部判断Asset Dramatic Function、Narrative Priority、Casting Logic、identity-critical / supporting，以及道具/环境是否承载故事意义、关系或状态变化。结果投影到现有Tier、Priority与制作依据，不膨胀用户输出。

### STATE-03 Asset Development

资产设计服从Character Presence / Screen Presence、必要的Costume / Silhouette Dramaturgy、Performance Feasibility、Prop State Evolution、Environment Narrative Force与story-function-based visual authority；不覆盖Canonical身份和双确认合同。

### STATE-04 Visual Development

把Style Development升级为`Visual Dramaturgy / Mise-en-scène Direction`：建立Visual Arc，而不是全片统一色调说明；让色彩、光线、对比、深度、负空间、环境压力、视觉层级、前中后景关系和视觉母题随戏剧推进保持或变化。项目级摄影倾向仍不预定逐Shot参数。

### STATE-05 Scene Breakdown

拆分Dramatic Beat、Relationship Beat、Information Beat、Performance Beat、Scene / Dramatic Geography、Spatial Evolution、Reveal / Withhold Timing与Beat-to-beat Rhythm。每场形成轻量`Scene Camera Strategy`：观察 / 跟随 / 隐藏 / 揭示 / 压住 / 释放，以及Audience Position和何处Hold；不得写具体焦段、机位或运镜路径。

### STATE-06 Detailed Shot Design

每个Shot固定按以下顺序决策：

`Shot Purpose → Audience Attention → POV / Audience Position → Relationship & Blocking → Composition Strategy → Shot Size → Lens → Camera Position → Camera Movement → Duration / Hold → Cut Motivation`

Shot Purpose类别为：`Narrative Change / Emotional Change / Relationship Change / Spatial-Action Progression / Information Reveal-Withhold / Atmosphere-Rhythm Control`。创建或保留前必须回答：`如果删掉这个Shot，观众会损失什么？` 若没有具体信息、情绪、关系、空间/动作、氛围/节奏或边界损失，合并或删除。

Camera Movement必须有`Camera Movement Trigger`：人物进入/退出、动作启动/停止、关系改变、信息Beat完成、注意转移或节奏释放。人物压抑且没有触发时可以整镜固定；摄影机可以在关键表演或信息Beat完成后才启动，并必须写停止点。禁止只写“镜头缓慢推进”。

### STATE-07 Clip Production

Clip是Dramatic Execution Unit，不只是时长合并单元。检查Start→End dramatic delta、performance buildup、blocking continuity、Camera Continuity / Visual Rhythm、information timing和generation boundary。必须同Clip完成的情绪/信息链不得因技术便利拆开；超过容量或跨越互斥导演方向时仍须拆分或返回STATE-06。

### STATE-08 Clip-based Video Prompt / Video Generation

本阶段不重新导演，执行`Director Intent Preservation + Model Translation`。先提取当前Clip最重要的1—3个导演目标，再由`knowledge/prompt_compilation/state08_projection.md`完成Dramatic Priority、Audience Attention、Performance Beat、Composition Function、Camera Motivation、Information Timing、Spatial / Relationship、Rhythm与Sound Function翻译，最后压缩并做Director Intent Preservation QA。最终Schema保持不变。

### Editing

Editing保护Editorial POV、Cut / Hold动机、Information Timing、Reaction Priority、Emotional Rhythm、Ellipsis、Match / Contrast、J-cut / L-cut、Sound Bridge、Transition Logic与shot-duration pressure / release。优先用剪辑恢复导演意图；素材不能支持时返回生成或上游owner。

### STATE-09 Review

并行区分Technical Review与Director's Cut Review。前者检查identity、continuity、blocking、props、camera/visual defects等；后者检查Intent vs Result、Audience Attention、Performance Truth、Relationship Readability、Information Timing、Shot Necessity、Rhythm与Emotional Residue。技术正确但情绪信息提前暴露仍是Director-level failure，不得判KEEP。

## Required Decision Dimensions

STATE-06的当前有效Director Decision Notes继续按Scene / Shot Group覆盖十三项，作为Shot-level Packet的兼容具体化：Narrative Objective、Audience Experience、Character Relationship、Blocking、Camera Strategy、Composition Strategy、Lens / Distance、Color & Lighting Strategy、Performance Direction、Sound Strategy、Editing / Rhythm、Continuity Risk、Seedance Feasibility。

每项只记录结论或Not Applicable理由。`Downstream Non-negotiables`只保留3—7条；不预选知识技巧。

## Mandatory Director Questions

1. 观众在这一段应知道什么、感受什么、等待什么？
2. 人物关系如何通过距离、视线、站位、动作、遮挡或共享空间被看见？
3. 镜头应该动还是停；什么Beat触发运动，在哪里停止？
4. 构图、景别、机位和距离分别承担什么信息/关系功能？
5. 表演由脸、身体、呼吸、手部还是延迟反应承担；谁先泄漏、谁压住？
6. 哪项信息应Reveal / Withhold / Delay / Confirm / Recontextualize？
7. 声音在哪里成为前景、在哪里退后或留白；剪辑为何Hold或Cut？
8. 删除这一Scene / Shot / Clip后，观众具体损失什么？

只能用风格标签、技巧名称、器材参数或“为了电影感”回答时，决策不合格。

## Internal Notes Shape

```text
Scene / Shot Group:
Source SHOTs:
Dominance:
Narrative Objective:
Audience Experience — Know / Feel / Wait:
Character Relationship / Blocking:
Information Strategy:
Camera Strategy — Audience Position + Move / Hold + Trigger + Stop:
Composition / Lens-Distance:
Performance Direction:
Color / Lighting / Sound Function:
Editing / Rhythm — Hold / Cut / Reaction / Residue:
Continuity Risk:
Seedance Feasibility / Safe Downgrade:
Deletion Loss:
Downstream Non-negotiables:
```

这是紧凑决策记录，不是逐步隐式推理，也不是用户可见Template。

## Director-to-Prompt Boundary

STATE-08固定链为：

`Clip Production Result → Current Director Intent → Dramatic Priority Extraction → Director-to-Prompt Translation → Prompt Compression → Director Intent Preservation QA → Final Clip Prompt`

Knowledge Application Reflection只能选择最适合实现已确认意图的1—3项策略，不能反向决定剧情、关系、信息顺序或镜头目的。Prompt Compiler负责把理论判断改写成动作顺序、视觉优先级、可见表演、空间关系、摄影机行为、声画节拍和稳定Endpoint；不得输出Director Module、Packet、dominance、BUILD/HOLD/PEAK/RELEASE等内部标签。

## Workflow Handoff

### From STATE-01 / Through STATE-05

STATE-05读取确认剧本中的Scene Director Intent source data，并投影Scene Objective、Audience Start / End State、Character Objective、Relationship Delta、Information Change、Performance Opportunity、Spatial Evolution、Rhythm Intent与Transition Intent。与剧本冲突时返回STATE-01；没有独立Artifact时只从锁定剧本提取可验证事实。

### To STATE-06

STATE-06先读取Scene-level Packet，再按固定导演决策顺序建立正式SHOT、Camera Language Decision与Director Decision Notes。Director Notes不能绕过Professional Detailed Shot Script静默补造字段。

### To STATE-07

STATE-07读取当前有效Notes并形成Clip-level Dramatic Execution Contract。不能为了减少Clip数量合并互相冲突的方向，也不能拆断必须连续积累的performance / information beat。

### To STATE-08

STATE-08先锁定Current Director Intent，后运行`STATE-08 Knowledge Application Reflection / Prompt`翻译。顺序不可反转。跨阶段只传递source data与当前投影，不要求把相同规则复制进每个Workflow。

### To Editing / STATE-09

Editing只改变有素材依据的排列、时长、反应优先级、声音连接和后期可修项。STATE-09区分generation failure与directing failure，并输出兼容Result及`KEEP / RE-EDIT / REGENERATE / REDIRECT`处置。

## Internal Visibility Rule

默认不向用户输出完整Packet或Director Decision Notes。用户明确要求“显示导演意图 / 为什么这样拍 / 显示镜头语言策略”时，只给当前对象的简洁决策摘要，不展示逐步推理；摘要不得成为后续Seedance Prompt固定章节。

正式Prompt禁止出现：

- `DIRECTOR INTENT PACKET`、`Director Decision Notes`、dominance或十三维度标题
- “观众应知道 / 感受 / 等待”的内部问答、候选方案、拒绝理由、风险权衡过程或Knowledge文件名
- “因为导演决策所以……”等理论解释句
- Shot Purpose类别、BUILD / HOLD / PEAK / RELEASE、S1-S4或内部模式ID

只保留模型能执行和观察的构图、调度、摄影机、光色、表演、声音、节奏、信息时序、边界与稳定降级语义。

## Completion Check

- Director Thinking从STATE-00/01持续到Scene、Shot、Clip、Prompt、Editing与Review，没有创建新主STATE。
- Project / Scene / Shot / Clip四层Packet具有当前有效source、owner、Revision或Checkpoint关联；未知项没有被虚构。
- 每个Shot通过固定决策顺序和Deletion Loss检查；Camera choice是intent的后果。
- 镜头运动具有Trigger与Stop；Static同样具有保护对象和理由。
- Director Module调用现有Performance、Spatial Blocking、Action PREVIS、Camera Language、Prompt Compiler与Continuity能力，没有复制其规则。
- Clip保留必要的performance / information积累，且通过Camera Continuity / Visual Rhythm与生成容量检查。
- STATE-08只翻译、不重新导演；最终Prompt可读出核心dramatic delta、注意力、表演、关系、Camera trigger和信息时序，但没有理论说明或Packet泄漏。
- Editing与Review能区分技术失败、生成失败、剪辑可修和导演决策失败。
- `templates/10_video_prompt.md`、Voice opt-in、REF-SKETCH、REF-TAIL、Accepted Take Canon、Shot-State Memory、Runtime Reload / Re-entry与Source Carries State, Prompt Carries Delta均保持兼容。
