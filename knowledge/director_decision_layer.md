# Director Module / Director Intelligence Layer

## Purpose

本文件是SD Film贯穿式Director Thinking、唯一的`Director Module / Director Intelligence Layer`连续性owner。它从STATE-00建立项目导演基线，在STATE-01接收Screenwriter Module的Story / Character / Scene Intent并形成呈现策略，在STATE-05投影为场景执行意图，在STATE-06具体化为Shot级Director Decision Notes，在STATE-07形成Clip级执行合同，在STATE-08由Prompt Compiler翻译，在Editing中保护剪辑观点，并在STATE-09执行Director's Cut Review。

核心分层固定为：

`Director Module = 决策层 → Workflow = 执行层 → Knowledge = 专业知识支持层 → Prompt Compiler = 模型执行翻译层`

本层是persistent cross-stage decision layer，不创建新主STATE，不改变STATE-00至STATE-09，不拥有任何最终Template Schema，也不直接生成Seedance Prompt。内部使用轻量`DIRECTOR INTENT PACKET`传递方向；正式用户交付只保留当前阶段有用的摘要或可执行结果，不机械展示Packet字段、候选方案、拒绝理由或逐步推理。

## Boundary With Screenwriter Module

`knowledge/screenplay_development.md`是唯一Screenwriter owner。Writer负责故事发生什么以及为什么成立：Premise / Theme、人物Want / Need / Objective / Hidden Objective、关键因果、Writer Beat、Scene Value Change、Dialogue / Subtext、Information Architecture、Setup / Payoff及Character / Relationship Arc。Director负责观众如何经历这些事实：Audience Experience、Performance Strategy、Blocking、Mise-en-scène、Composition、Camera Language、Rhythm Presentation与Reveal Presentation。

`Information Architecture = Writer Authority`，`Information Presentation = Director Authority`。Director可以决定用动作、沉默、声音、遮挡或镜头关系呈现一个Writer Beat，但不得改变其锁定的因果、动机、信息时机与Setup / Payoff义务。发现不可导演或执行容量冲突时，走REDIRECT / rewrite feedback返回STATE-01最小受影响范围。

## Module Contract

- **Module Name**：Director Module / Director Intelligence Layer；`Director Decision Layer`保留为兼容名称
- **Module Type**：贯穿STATE-00至STATE-09与Editing的内部导演决策Knowledge；不是Workflow、Template、新STATE或第二套Project State
- **Owner**：`knowledge/director_decision_layer.md`
- **Core Externalization**：Camera Language Module，owner为`knowledge/camera_language/index.md`
- **Trigger**：所有SD Film主流程项目；按当前阶段、当前Scene / Shot / Clip和任务dominance只运行最小充分部分
- **Not Triggered As**：独立用户步骤、固定分析报告、导演风格库、Camera Movement选择器、Knowledge Reflection替代品、最终Prompt新字段
- **Position**：`STATE-00 Project Director Baseline → STATE-01 Writer → Director Handoff / Scene Presentation Intent → STATE-05 Scene Projection → STATE-06 Director Decision Notes → STATE-07 Clip Production → STATE-08 Director-to-Prompt Translation → Editing / STATE-09 Review`
- **Required Inputs / Owners**：Story / Character Intent、Writer Beats、Information Architecture、Setup / Payoff obligations与Scene Exit State由Screenwriter owner提供；Confirmed Assets、Visual Direction、Scene / Shot / Clip事实、时长、边界和用户约束由对应上游owner提供。本层只作呈现判断，不静默新增或改写事实
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
- Genre Presentation Strategy（消费Writer的Genre Promise）
- Emotional / Dramatic Presentation（消费Writer的Emotional Arc与Dramatic Core）
- Performance Strategy
- Spatial Dramaturgy
- Visual Dramaturgy
- Rhythm Strategy
- Sound Strategy
- AIGC Directability Constraints

STATE-00只建立可由用户输入直接确认的最小Project Director Baseline：`Directorial Thesis / Audience Contract / Genre Strategy / Intended Viewing Experience / Non-negotiable Dramatic Core`。STATE-01至04可以依据确认剧本与资产逐步补齐其余项目项，但不得把早期假设冒充锁定事实。

### Scene-level

- Writer-supplied Scene Objective / Writer Beat Map
- Audience Start State
- Audience End State
- Writer-supplied Character Intent / Relationship Change
- Writer-supplied Information Change / Setup-Payoff obligations
- Information Presentation / Reveal Strategy
- Performance Opportunity / Peak
- Spatial Evolution
- Rhythm Intent
- Transition Intent

Scene-level Packet由STATE-01在Writer → Director Handoff后生成呈现source data，STATE-05结合Production-Locked剧本与Writer Intent正式投影。Writer字段仍由Writer owner控制；本Packet描述观众如何经历既定变化，不写35mm、特写、低机位或推镜等Shot Design参数。

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

### Visual Grammar Baseline And Scene Delta

STATE-04在既有Visual Direction / Project Bible中建立`Visual Grammar Baseline`：这是全片可持续识别的世界规则，而不是一个导演名或“高级、低饱和、电影感”等风格标签。它只归纳会影响后续判断的稳定倾向：摄影/材质质感、可用色谱与强调色出现条件、真实光源逻辑、空间气质、构图与景深倾向、以及摄影机克制或介入的总体边界。它不预写逐Shot技术参数，不把任一参考片的具体审美强加给所有项目，也不新建用户可见Schema。

每个Scene / Shot只携带相对该Baseline的必要`Scene Delta`：此处空间承担的戏剧功能、人物与空间的压力/亲密/秩序关系、当前信息的可见或遮挡方式、以及由锁定故事事实触发的光色、构图或观察变化。全片统一不等于每场采用相同色调、景别、构图或运镜；没有戏剧、空间或信息触发时优先保持Baseline，发生变化时必须说明它服务的观众体验并在结束时落回可读的稳定状态。

色彩的导演功能是“权限”而非默认滤镜：先界定哪些色相/明度/饱和度层级可作为世界常态，再界定强调色只在何种人物状态、剧情事件、空间光源或资产事实下出现。颜色不得凭“好看”新增光源、改写资产固有色或取代Writer锁定的意义。

## Packet Persistence And Projection

Packet遵守“source data向下传递、阶段owner只写自己的具体化结果”：

1. STATE-00在Project Bible既有项目/故事/制作方向区域保存最小Project Director Baseline；不增加Portable State字段。
2. STATE-01先把Writer Intent与Production-Locked Directable Screenplay绑定，再由Director把Handoff具体化为Project-level呈现策略与Scene Director Intent source data；两个Packet不互相覆盖。
3. STATE-02/03只读取资产相关的Dramatic Function、Narrative Priority、Casting / Screen Presence、Environment Narrative Force、Prop State Evolution与FX的视觉/遮挡/后果功能，不复制完整Packet。
4. STATE-04把项目意图翻译为Visual Dramaturgy / Mise-en-scène Direction与Visual Grammar Baseline，写入现有Visual Direction / Project Bible区域；各阶段只记录相对此基线有剧情依据的Scene Delta。
5. STATE-05生成Scene-level投影、Dramatic Geography、Scene Delta与Scene Camera Strategy，不创建SHOT或具体摄影参数。
6. STATE-06生成Shot-level Director Decision Notes，并让Camera Language / Performance / Blocking / Action PREVIS等能力执行。
7. STATE-07在现有Clip Detail / Clip Director Direction中形成Clip-level执行合同，不创建新ID或顶级Schema。
8. STATE-08只读取当前Clip必要的1—3个导演优先级并执行Director-to-Prompt Translation；Packet标题和内部标签不得输出。
9. Editing与STATE-09读取实际结果和当前有效Packet，不重新导演；如果结果证明上游决定错误，按owner返回。
10. 条件性Sequence Planning只消费STATE-05已确认的Scene Director Intent、Information Presentation与Rhythm Intent来组织BEAT / Coverage / UNIT，不创建SHOT、Camera参数或平行Director Packet。

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

Screenwriter Module先控制Dramatic Intent、Character Objective、Relationship Arc、Writer Beats、Information Architecture、Subtext与Setup / Payoff；导演层在Handoff后控制Audience Experience、Performance / Spatial opportunity、Reveal Presentation、呈现节奏与导演层AIGC Directability。Creation Brief与Existing Script / Diagnosis双入口保持不变。剧本阶段可以识别“先让观众看见她没有回头，随后才意识到另一个人一直看她”这样的呈现机会，但不提前写Shot List、焦段、景别、机位或运镜。

### STATE-02 Asset Discovery

每个候选资产内部判断Asset Dramatic Function、Narrative Priority、Casting Logic、identity-critical / supporting，以及道具/环境是否承载故事意义、关系或状态变化。结果投影到现有Tier、Priority与制作依据，不膨胀用户输出。

### STATE-03 Asset Development

资产设计服从Character Presence / Screen Presence、必要的Costume / Silhouette Dramaturgy、Performance Feasibility、Prop State Evolution、Environment Narrative Force与story-function-based visual authority；不覆盖Canonical身份和双确认合同。

### STATE-04 Visual Development

把Style Development升级为`Visual Dramaturgy / Mise-en-scène Direction`：先建立Visual Grammar Baseline，再建立Visual Arc与有依据的Scene Delta，而不是全片统一色调说明；让色彩、光线、对比、深度、负空间、环境压力、视觉层级、前中后景关系和视觉母题随戏剧推进保持或变化。项目级摄影倾向仍不预定逐Shot参数。

Visual Grammar Baseline之后必须完成`Aesthetic Decision Lock`：在反差与光比结构、色彩对抗关系、构图主张、视觉母题与变化轨迹四个维度各做出一次排他性决定。Baseline只描述世界的稳定倾向，Lock必须给出选择、被放弃的选项、事实依据与可见后果。没有放弃项的表述是描述而不是决定，不得写入Project Bible。四项决定共用`Mandatory Director Questions`的判定纪律：只能用风格标签、技巧名称、器材参数或“为了电影感”回答时，项目级决策与Shot级决策同样不合格。四项决定是项目级承诺，不是逐镜参数；具体焦段、机位、运镜与逐镜光态仍由STATE-06决定。

### STATE-05 Scene Breakdown

先消费Writer Beat Map、Scene Value / Relationship / Information Change、Setup / Payoff Function与Scene Exit State；Director不重写这些Beat，而是以Visual Grammar Baseline为底补充Performance Beat、Scene / Dramatic Geography、当前空间的戏剧功能、必要Scene Delta、Spatial Evolution、Reveal / Withhold呈现与Beat-to-beat Rhythm。每场形成轻量`Scene Camera Strategy`：观察 / 跟随 / 隐藏 / 揭示 / 压住 / 释放，以及Audience Position和何处Hold；不得写具体焦段、机位或运镜路径。

### STATE-06 Detailed Shot Design

每个Shot固定按以下顺序决策：

`Shot Purpose → Audience Attention → POV / Audience Position → Relationship & Blocking → Composition Strategy → Shot Size → Lens → Camera Position → Camera Movement → Duration / Hold → Cut Motivation`

Shot Purpose类别为：`Narrative Change / Emotional Change / Relationship Change / Spatial-Action Progression / Information Reveal-Withhold / Atmosphere-Rhythm Control`。创建或保留前必须回答：`如果删掉这个Shot，观众会损失什么？` 若没有具体信息、情绪、关系、空间/动作、氛围/节奏或边界损失，合并或删除。

Camera Movement必须有`Camera Movement Trigger`：人物进入/退出、动作启动/停止、关系改变、信息Beat完成、注意转移或节奏释放。人物压抑且没有触发时可以整镜固定；摄影机可以在关键表演或信息Beat完成后才启动，并必须写停止点。禁止只写“镜头缓慢推进”。

### STATE-07 Clip Production

Clip是Dramatic Execution Unit，不只是时长合并单元。先判断观众需要看到什么、何时揭示信息、是否需要切镜，再检查Start→End dramatic delta、performance buildup、blocking continuity、Camera Continuity / Visual Rhythm、information timing和generation boundary。执行模式只可为单Shot、多Shot连续生成或多Shot有动机剪辑；后者必须由Director确认叙事功能、切点、视觉媒介、切前结束、切后世界/角色/环境/道具/摄影机稳定重建和连续性锚点。必须同Clip完成的情绪/信息链不得因技术便利拆开；超过容量或跨越互斥导演方向时仍须返回STATE-07拆分Clip或STATE-06，不得用无原因跳变伪装导演剪辑。

### STATE-08 Clip-based Video Prompt / Video Generation

本阶段不重写故事、不重新导演，执行`Writer Intent Preservation + Director Intent Preservation + Model Translation`。先锁定当前Clip的关键Writer Beat、Character Intent / Subtext、因果、信息与Setup / Payoff义务，再提取1—3个导演目标，由`knowledge/prompt_compilation/state08_projection.md`翻译。Writer只提供必须保住的戏剧含义，Camera仍只来自Director / Shot / Clip决定。最终Schema保持不变。

### Editing

Editing保护Editorial POV、Cut / Hold动机、Information Timing、Reaction Priority、Emotional Rhythm、Ellipsis、Match / Contrast、J-cut / L-cut、Sound Bridge、Transition Logic与shot-duration pressure / release。优先用剪辑恢复导演意图；素材不能支持时返回生成或上游owner。

### STATE-09 Review

并行区分Story Review、Director's Cut Review与Technical Review。Story Review检查causality、motivation、scene value、Writer Beat、Subtext、Setup / Payoff、arc与ending payoff；Director's Cut检查Intent vs Result、Audience Attention、Performance Truth、Relationship Readability、Information Presentation、Shot Necessity、Rhythm与Emotional Residue；Technical Review检查identity、continuity、blocking、props、camera/visual defects等。技术与导演呈现都正确但人物行为本身无动机时是Writing Failure，应返回Writer layer。

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
9. 若要在同一生成Clip内切镜：观众因此会看见或理解什么，切点由何种视觉媒介触发，切后如何在稳定构图中重建世界与关系？

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

### From Screenwriter Module

接收Story Intent、Character Intent、Scene Objective、Writer Beats、Relationship Change、Information Architecture、Subtext / Hidden Objective、Setup / Payoff obligations、Performance Intent与Scene Exit State。Director只增加Audience Experience与呈现选择；任何Camera参数都必须来自STATE-06固定决策链，而不是从Writer Packet推断为既定镜头。

### From STATE-01 / Through STATE-05

STATE-05读取确认剧本中的Writer Intent和Scene Director Intent source data，并投影Scene Objective、Audience Start / End State、Character Objective、Writer Beat Map、Relationship Delta、Information Change、Setup / Payoff、Performance Opportunity、Spatial Evolution、Rhythm Intent与Transition Intent。与剧本冲突时返回STATE-01；没有独立Artifact时只从锁定剧本提取可验证事实。

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
- STATE-04建立了Aesthetic Decision Lock，四个维度各有选择、被放弃的选项、依据与可见后果；项目级视觉说明如果只有风格标签、技巧名称、器材参数或“为了电影感”，不合格。
- 每个Shot通过固定决策顺序和Deletion Loss检查；Camera choice是intent的后果。
- 镜头运动具有Trigger与Stop；Static同样具有保护对象和理由。
- Director Module调用现有Performance、Spatial Blocking、Action PREVIS、Camera Language、Prompt Compiler与Continuity能力，没有复制其规则。
- Clip保留必要的performance / information积累，且通过Camera Continuity / Visual Rhythm与生成容量检查。
- STATE-08只翻译、不重新导演；最终Prompt可读出核心dramatic delta、注意力、表演、关系、Camera trigger和信息时序，但没有理论说明或Packet泄漏。
- Editing与Review能区分技术失败、生成失败、剪辑可修和导演决策失败。
- `templates/10_video_prompt.md`、Voice opt-in、REF-SKETCH、REF-TAIL、Accepted Take Canon、Shot-State Memory、Runtime Reload / Re-entry与Source Carries State, Prompt Carries Delta均保持兼容。
