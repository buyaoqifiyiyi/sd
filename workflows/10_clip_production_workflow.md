# SD Film Clip Production Workflow

## Workflow Contract

- Module Type：主流程 Workflow
- Current State：STATE-07 Clip Production
- Entry：STATE-06 Detailed Shot Design Complete
- Required Input Owner：STATE-06 Detailed Shot Design、Confirmed Assets、Visual Direction、Scene / Sequence资料
- Output Owner：`templates/20_clip_plan.md`
- Output：Confirmed Clip Production Plan
- Next：STATE-08 Clip-based Video Prompt / Video Generation

本 Workflow 把导演层的正式 Shot 组织为 AI 视频模型的一次生成执行单元。它不改写剧情、资产身份、Shot ID、Shot顺序或镜头目的，也不拥有 STATE-08 最终 Seedance 字段。

任何来自原剧本的“镜头1 / 镜头2 / Scene 1 / 段落A / Clip A”都只属于Source Script Label，不是正式Shot或Clip来源。不得按Source Script Label数量、标题或段落边界创建Clip。

## Unit Definitions

- **Shot**：导演镜头设计单位。用于定义景别、机位、镜头目的、表演、动作、声音、边界与摄影语言。
- **Clip**：AI 视频生成执行单位。一个 Clip 包含一个或多个按原顺序排列的 Shot，并对应一次完整生成。
- **Prompt**：STATE-08 以一个 Confirmed Clip 为单位编译的一条连续 Seedance Prompt；不得按 Shot 拆成多条 Prompt。

## Required Inputs

- 实际可读且Status为Confirmed的Detailed Shot Design Artifact，以及其Artifact标识/路径与Revision
- STATE-06 Confirmed `Professional Detailed Shot Script` 与原正式 SHOT 顺序；每个Shot已完整包含镜号、TC IN、TC OUT、时长(s)、景别、焦段、场景/美术、画面内容/构图、人物动作、摄影机/镜头、摄影参数、镜头调度、光线/色彩、画面特效/转场、台词/旁白/口播、同期声音设计、AI制作备注、素材/资产
- 每个Scene的Confirmed `Spatial Blocking Result`：Spatial Blocking Decision、Map Mode、Structured Blocking Map、Text Spatial Rules、Clip Boundary Spatial Ledger，以及适用时已核对的Top-down Blocking Map；STATE-07只读继承，不得重新设计
- STATE-06为每个Scene / Shot Group生成的当前有效`Director Decision Notes`
- 每个 Shot 的精确时间码与目标时长，以及`AI制作备注`中保存的Start Boundary、End-Frame Constraint、Next-Shot Handoff、执行风险与稳定降级
- 每个 Shot 已确认的 Camera Language Decision，包括镜头目的、情绪/空间功能、人物运动、节奏阶段、主/辅助/禁止运镜、Seedance稳定等级、选择理由与原子知识证据
- 已确认 Character / Environment / Prop / FX Asset
- Scene Breakdown、Visual Direction、Sequence Plan / Coverage / UNIT（如适用）
- Camera、Composition、Movement、Lens、Performance、Lighting、Color、Transition、Sound 与 FX 的适用结果

缺少正式 Shot、Confirmed Spatial Blocking Result、关键边界、必要资产版本或可判断的目标时长时，保持 STATE-07 IN_PROGRESS，并返回 STATE-06 或相应事实拥有者补齐；不得用 Clip 文案静默补造。

不存在上述Confirmed Artifact、匹配Revision、STATE-06 Complete证据和完整正式SHOT清单时，不得创建任何Draft、Provisional、Tentative、占位或正式CLIP ID。

## Resource Gate

执行前必须读取：

1. `knowledge/spatial_blocking_layer.md`
2. `knowledge/director_decision_layer.md`
3. `knowledge/clip_planning/index.md`
4. `knowledge/clip_planning/foundations.md`
5. `knowledge/clip_planning/decision_engine.md`
6. `knowledge/clip_planning/continuity_and_projection.md`
7. `knowledge/clip_preflight_check.md`
8. `knowledge/reference_budget.md`
9. `knowledge/transitions/index.md`及其要求文件
10. `knowledge/camera_language/movement_combinations/index.md`及其要求文件
11. `knowledge/camera_language/camera_movement/selection_matrix.md`
12. `knowledge/camera_language/camera_movement/index.md`及本Clip各Shot已选主运镜的原子知识文件
13. `templates/20_clip_plan.md`

并按适用性读取 Camera / Composition、Lens、Performance、Lighting、Color、Sound 与 FX 模块。

候选Clip包含战斗、双主体、对峙、对话、追逐、相向运动或来源—目标交互时，还必须执行`knowledge/camera_language/index.md`中的Relational Screen Geometry Contract。

## Step 1｜Normalize Detailed Shots

先核验Detailed Shot Design Artifact的Status、Revision与STATE-06完成证据，再读取正式SHOT。只声明Revision但无法关联到实际Artifact或Portable Checkpoint，不构成有效入口。

建立按正式 SHOT ID 和原顺序排列的清单。每个 Shot 至少记录：

- `镜号 / TC IN / TC OUT / 时长(s)`，并复核`TC OUT - TC IN = 时长(s)`；Clip时长只能逐项求和，不得重新估算
- `景别 / 焦段 / 摄影机/镜头 / 摄影参数`，保持机位、焦段距离、轴线、焦点、景深与稳定方式的原始约束
- `画面内容/构图`中的前景/中景/背景、主体位置、遮挡/反射/景深、视觉焦点与结束构图
- `人物动作`中的起始 → 刺激/注意 → 反应 → 决定/动作 → 稳定结束动作链
- `镜头调度`中的摄影机运动、人物调度、两者配合/触发和镜头结束状态；不得把该字段缩减成单一运镜名
- `光线/色彩`的真实来源、叙事功能、变化触发/稳定理由和结束光色态
- `画面特效/转场、台词/旁白/口播、同期声音设计、AI制作备注、素材/资产`中的执行与连续性事实；任何后期配乐规划都不属于STATE-07输入，也不得进入STATE-08音效

- Scene / Sequence / Coverage / UNIT 映射
- 导演镜头目的与目标时长
- 起始人物、环境、道具、FX 与情绪状态
- 动作过程、表演、台词与声音
- 空间关系、轴线、视线、行进方向与摄影机路径
- Confirmed Spatial Blocking Result中的场景坐标约定、固定结构、角色起终点 / 路径、C1/C2/C3位置 / 朝向、Text Spatial Rules与Clip首尾帧站位；Top-down Map只作规划核对，不得进入STATE-08【参考资产】
- A/B画面左右与前后、各自朝向、关系轴、摄影机轴线侧，以及视线/攻击/武器/追逐路线/水流/能量的来源—路径—目标连线（适用时）
- Start Boundary、End-Frame Constraint、Next-Shot Handoff
- 所属Scene / Shot Group的Director Decision Notes，以及该组Narrative Objective、Audience Know / Feel / Wait、关系变化、Blocking、Camera动/停理由、功能性色光、表演尺度、声音重点/留白、节奏高潮/留白与Seedance降级

不得重排、遗漏、复制、跨过中间 Shot 或把多个 Shot 改写成一个新 Shot。

如果Detailed Shot Design与Confirmed Spatial Blocking Result在人物位置 / 朝向、移动路径、摄影机轴线侧、关键道具或Clip首尾站位上冲突，返回STATE-06最小修正Affected SHOT及相邻边界；STATE-07不得择一猜测。

STATE-07只组织这些Detailed Shots，不得回到原剧本重新简化画面、动作、调度、色光、声音或资产，也不得用Clip Movement Plan覆盖正式分镜中的摄影机/人物配合与结束状态。

任一Scene / Shot Group缺少Director Decision Notes、Notes与Confirmed Detailed Shot Design冲突，或十三个维度无法确定时，保持STATE-07 IN_PROGRESS并返回STATE-06补齐；STATE-07不得根据已有Camera/Color技巧反向猜测导演意图。

## Step 2｜Build Clip Candidates

从首个未分配 Shot 开始建立 `CLIP-001`，依次编号。候选合并必须同时评估：

- 场景与时间连续性
- 人物动作、表演与情绪连续性
- 摄影机、构图、轴线、视线与运动连续性
- 每个 Shot 的 Camera Language Decision与主运镜叙事功能；不得以“统一风格”为由把不同决策抹平成慢推/横移模板
- Director Decision Notes中的主叙事目标、观众等待、关系/Blocking变化、摄影机介入程度、视觉高潮与留白是否能在同一Clip内保持一个清楚方向；互相冲突时不得强行合并
- 空间关系和道具持有/位置/状态连续性
- 候选Clip必须保持Confirmed Spatial Blocking Result中的角色路径、摄影机位置 / 轴线侧与关键道具空间锚点；合并不得制造地图中不存在的穿越、换边或捷径
- 镜头几何连续性：单一主轴、屏幕左右、身体朝向、眼线、摄影机轴线侧和来源—目标连线不得在合并后翻转
- 角色、环境、道具与 FX 资产版本一致性
- 模型执行复杂度、动作/口型/FX容量和稳定性
- 目标模型单次生成适宜时长；每个 Confirmed Clip 必须为 4—15 秒

单 Shot 可以独立成为 Clip。多个相邻 Shot 只有在同一次生成内可清楚、连续地执行且总时长不超过15秒时才可合并；不得为了减少 Clip 数量强行合并。

Shot 是导演设计单位，因此单个 Shot 可短于4秒；它必须与相邻、兼容的 Shot 组成4—15秒 Clip。单个 Shot 超过15秒或无法在15秒内稳定执行时，返回 STATE-06 按自然动作/覆盖/机位/时空边界拆分。

## Step 2A｜Run Clip Preflight Draft

每个候选Clip在编写正式执行合同、Reference Budget Audit与尾帧用途之前，必须按`knowledge/clip_preflight_check.md`执行STATE-07前置版。顺序不可变：

`Continuity Classification → World-State Check → Character Count Lock → Spatial Composition Lock → Performance / Emotion Check → Visual Blocking Risk Pre-Assessment → Prop State Check → Transition Check（适用时）→ Reference Asset Eligibility / Check / Budget`

逐Clip至少记录：

- **Continuity Classification / Tail Frame Requirement**：从`视觉连续 / Visual Continuity`、`剧情连续 / Narrative Continuity Only`、`主动切场 / 切世界 / Motivated Scene-or-World Change`中三选一并写证据；随后在同一既有判定中把尾帧使用方式明确为A【同镜头连续承接 / Direct】、B【新镜头参考型 / Reference-Only】或C【新镜头且无需尾帧 / Not Required】。A/B均标记`Tail Frame Required = YES`，C标记`NO`；不得因系统当前没有尾帧图改变分类。A/B还必须记录用途类型、需锁定的具体维度及缺图时的待补充声明。
- **World-State Map**：逐分镜写现实世界、幻想世界、耳中玉境或项目已确认层，列出该层实际角色、环境、道具、FX与转换前/后阶段。完全在耳中玉境的Clip必须删除现实标准耳勺等现实阶段资产；转换Clip才可按阶段同时保留两种道具形态。
- **Character Count Lock**：逐分镜列出`角色 × 精确数量`。剧情唯一角色必须正向锁定唯一数量与前中后景无第二个同类，并预置反向复制/分身/镜像/背景重复限制。
- **Spatial Composition Lock**：对追逐、战斗、对峙、对话和多人镜头锁定前后景、左右、朝向、关系轴、摄影机轴线侧、追逃/攻击/视线路线、可见面部与同景深许可。追逐默认后追前逃，禁止并排正对镜头和海报式合影。
- **Performance / Emotion Check**：逐角色读取STATE-06 Performance Goal / Performance Arc Map与上一有效Performance State，核对Inherited Baseline、已确认Trigger、Pre-action / In-action / Post-action Residue、Arc Endpoint、Next-shot Carryover与动作后余韵；Intentional Hold仍须有注意、呼吸/姿态、延迟或行动证据。多人镜头锁定Primary Performer、Secondary Reactor / Listener / Background Holder、反应顺序、相对幅度与视觉重点交接；静态情绪标签、无刺激重置、全员同强度或全员同脸固定FAIL。
- **Visual Blocking Risk Pre-Assessment**：每个Clip都按`knowledge/clip_preflight_check.md`检查人物数量、固定左右/前后、共享座椅/桌面/车辆/床/门口、Facing / Eyeline / Axis、局部Pose权限、换位/进出画、前中后景、复杂道具、Relationship Topology、A2/A3动作与复杂机位，记录`NONE / POSSIBLE / REQUIRED`、建议`S / P / A / Combined`与轻量Blocking Signature。此处只标风险，不生成草图；STATE-08最终Gate可因实际Reference、Accepted Canon或修订变化调整结果。
- **Prop State Check**：逐关键道具写当前形态、尺寸、持有者/左右手、位置、方向、是否允许悬浮、转换是否完成与结束状态；不同世界形态不得无过程混用。
- **Transition Five Elements**：现实↔幻想/耳中玉境、地点/时间跳跃、尺度或角色/道具形态转换时，必须先锁定起点状态、转换媒介、运动方向/过程、终点状态、转场后首个稳定构图。缺一不得用“金光一闪 / 突然切换”代替。
- **Reference Asset Check**：只在上述项目通过后筛选资产。每个视觉候选先回答“这是不是一张实际会被投喂/引用的视觉资产？”；只有真实可回查的已确认视觉资产，或明确需要用户实际补入、写明具体图像对象/投喂用途/`待用户补充或待上传、未确认`状态的视觉图占位可继续。纯文字站位、换边、距离、共坐、数量、空间、行为、禁止项或镜头规则必须移到`空间关系 / 起始状态 / 道具状态 / 首帧参考 / 尾帧限制 / 反向提示词 / Spatial Blocking Rules`，不得作为资产。之后再删除未出场、未使用及当前World-State不适用项并执行预算；角色独立锁定图优先，最终≤9，只有超限风险时整合非角色信息。

任一项失败时记录Affected Clip / Shot与Return Route，先修设计再从Continuity Classification重跑。Preflight为FAIL时不得进入Step 3、不得生成或确认Clip Plan。

## Step 3｜Author Clip Execution Contract

STATE-07把Clip定义为`Dramatic Execution Unit`，不是仅按时长或技术便利合并的容器。每个Clip先在现有生成合同 / Clip Director Direction中记录：Clip Dramatic Function、Start Dramatic State、End Dramatic State、Critical Performance Beat、Critical Blocking / Spatial State、Continuity Requirement、Rhythm Requirement、Information Timing Requirement、Generation Risk / Simplification Boundary。

合并/拆分必须同时通过两类判断：

- **Dramatic Integrity**：怀疑→证据→确认、压制→泄漏→余韵或进入→关系改变等必须连续积累才能成立的相邻Shots，不能因技术方便错误拆开。
- **Generation Capacity**：若同一Clip跨越互斥时空/方向、需要状态重置、动作/口型/FX/Camera负荷过高，或超过4—15秒，必须拆分或返回STATE-06；不能以“情绪连续”为由强行过载。

Packet语义只投影到现有Clip字段，不新增顶级Template字段或新ID。

每个 Clip 必须记录：

- Clip ID 与包含的 Shot ID（原顺序）
- 起始状态与来源
- **Clip Scope Firewall**：在现有`生成合同 / 起始状态 / 连续动作 / 结尾状态 / 下一Clip Handoff`语义中内部区分`already_happened`（此前已完成，不得重播）、`this_clip_only`（本Clip允许出现的可见剧情/动作）、`reserved_for_later`（只作后续导演上下文，不得提前表演）与`do_not_show_yet`（明确禁止提前出现的元素、状态或结果）。每个生成单元原则上只承担一个主要可见Beat，并以一个清楚改变的Endpoint结束；这不等于只允许一个动作，多个动作只有在共同构成同一Beat、同一方向的状态变化且不超出模型容量时才可连续执行。四类边界只投影到上述Template既有字段，不新增Clip Plan或STATE-08字段
- 连续动作、表演与情绪弧
- 摄影机/构图/焦段/对焦的执行路径
- 人物与环境的空间关系、轴线、视线和行进方向
- Spatial Blocking继承：引用当前Scene的Decision / Map Mode，逐项锁定固定结构、角色路径、C1/C2/C3摄影机侧和Text Spatial Rules；不得把Top-down Map本身登记为视频参考资产
- Visual Anchor State / Blocking Signature：复用`Spatial State / Continuity Risks / Reference Budget`既有位置记录Characters、Topology、Position、Shared Facing、Seat / Spatial Relation、Allowed Delta、Camera Logic、Axis、Movement Path、Clip Start / End Blocking与Pre-Assessment；不新增Template顶级字段。已有Confirmed `REF-SKETCH`且Signature未变时标记KEEP，原为NONE或旧草图失效时仅记录需由STATE-08 Final Assessment决定CREATE / REPLACE / RETIRE
- 战斗/双主体/对峙关系的几何锁定：A/B左右与前后、朝向、距离、主轴、摄影机轴线侧、Connector及首尾帧继承；双方同框相对时禁止双正脸
- 道具持有者、位置、方向、状态及变化
- 光影、色彩、FX 与声音连续性
- 结尾状态、稳定尾帧限制及下一 Clip Handoff
- 模型执行风险与安全降级
- `Clip End-State Record / Next-Clip Carryover`：把上述已有Entry、内部Shot状态链、Exit、Spatial Blocking、道具连续性、摄影机路径、环境/表演状态和Handoff合并为STATE-07内部连续性记录，作为Shot-State Memory所需语义的既有合同内实现。固定使用`Character State / Spatial State / Prop State / Camera State / Environment State / Performance State / Continuity Risks / Next-Clip Carryover`八组简洁语义；不新增STATE、ID、资产类型或STATE-08字段，不复制Professional Detailed Shot Script全部字段。下一Clip必须以此记录而不是凭记忆重建起始状态；若上一Clip已有用户接受Take及`Accepted Canon State`，以该Take的Observed State覆盖同维度Planned State，再组织本Clip首帧。未接受Take不得改变记录
- Clip Preflight Check：连续性主分类、逐分镜World-State、角色精确数量、空间构图锁、Performance / Emotion Check、关键道具状态、适用Transition五要素、Reference Asset Check与`PASS / Return Route`
- Reference Selection / Routing + Reference Budget Audit：先从当前Clip目标、八组End-State Record、Visual Anchor State、`Continuity Risks`与下一Clip起始要求选择最小充分视觉参考，再执行预算；不是把全部Eligible或Registry资产机械塞入。每个入选Reference必须声明唯一`Primary Role / Purpose`并遵守`rules/04_consistency_rules.md`的Reference Authority Hierarchy：身份/外观风险路由到Active Character Canonical References；空间结构风险路由到Active Environment Canonical References并消费Confirmed Spatial Blocking文字语义；道具造型风险路由到Active Prop Canonical References；已有Confirmed `REF-SKETCH`且Blocking Signature未变时仅路由其Position / Facing / Distance / Topology / Axis / Camera / Pose / Gaze / Action Path Authority；STATE-07新判`POSSIBLE / REQUIRED`只记录预判，不虚构或预先生成草图；A/B状态锚定路由到对应Accepted Canon State / `REF-TAIL`并声明用途，C不路由旧尾帧；Motion / Camera / Audio Reference只控制其授权维度。草图与临时状态参考不得覆盖正式角色身份、环境结构或道具造型；尾帧或草图脸部漂移时只消费合法Authority。光线/天气/场景状态漂移只有在实际存在已确认的场景视觉基准或合法参考帧时才选图，否则写入现有文字字段。每个入选条目记录所解决的具体风险/目标，合格但无关项记录不选理由。随后只列通过Visual Input Eligibility、当前Clip实际需要且通过World-State的候选图片资产；真实资产须存在/已确认并可回查文件或受控ID。明确需要用户实际补入的视觉参考图占位须写具体图像对象、投喂用途与“待用户补充/待上传、未确认”，只计Projected位、不计已提交图片；它不得绕过应返回STATE-03的正式Canonical资产流程。A/B `REF-TAIL`继续以统一名称、用途类型和专用状态声明预留1个Projected连续性图片位；C不加入或预留旧尾帧。再计算Projected Final Count，并按`knowledge/reference_budget.md`记录文字伪资产迁移、是否触发整合、替代关系、裁剪与最终≤9张提交清单

参考资产默认保持原始独立结构。Projected Final Count≤7时不得整合；8张且无额外帧需求时原则上不整合；9张只有在确认没有未计入连续性需求时才允许；已有9张且仍需上一Clip尾帧/当前首帧时按10张处理并至少释放1位；>9张时才执行同类非角色信息的去重/整合/裁剪。当前Clip每个核心角色始终保留各自独立三视图/角色锁定图，多个核心角色不得合并成角色总表，动作图不得替代外貌基准。

只有真实存在、已确认且完整覆盖对应零散图的环境/道具/空间/动作/使用示意总图才可用于替代。若需要新建总图，返回对应STATE-03资产Workflow完成双确认闭环后再继续；STATE-07不得虚构资产名称。独立资产更清晰且未超限时继续使用独立图，不因已有总图而强制替换。

组织上述执行合同时，必须先把当前Clip所覆盖Shot Group的Director Decision Notes综合为一条内部`Clip Director Direction`：

- **主导镜头语言**：摄影机总体观察、跟随、逼近、揭示、释放或保持不介入的理由；具体运镜仍服从STATE-06 Camera Language Decision
- **节奏**：观众等待如何建立、在哪个动作/视线/声音节拍释放，以及Clip结尾保留多大程度的留白
- **调度**：人物距离、视线、站位、先后动作与关系变化如何在Clip内部连续发展
- **表演层级与情绪弧**：逐角色从Inherited Baseline到Arc Endpoint如何变化；谁承担Primary Performer，谁延迟/低幅承接，视觉重点何时交接；动作或台词后的余韵在哪里可读
- **视觉高潮 / 留白**：哪一个SHOT承担最大摄影或光色强调，哪一个SHOT必须克制、固定或降低视听密度
- **功能性色光与声音**：只保留有真实来源和剧情触发的变化；没有功能性变化时明确保持稳定

`Clip Director Direction`只作为组织与校验语义，必须投影到`templates/20_clip_plan.md`已有的Clip目标、连续动作、Clip Movement Plan、光色/声音连续性、高潮/克制与风险位置；不得新增Template字段，也不得在STATE-07重新选择知识策略。

Clip确认前还必须执行`Clip Camera Continuity / Visual Rhythm`检查：逐Shot确认建立、隐藏、泄漏、确认、压住、释放等功能变化；运动Trigger / Stop、景别/距离变化、视觉高潮与最克制镜头共同形成层级。三个镜头不得无理由都变成“慢推+浅景深”；同一逻辑若刻意重复，必须说明重复如何累积信息、动作或关系。

如STATE-07在整理上述已确认信息时发现明确的Knowledge应用机会，可在现有“知识投影摘要”或`Knowledge Projection Ledger`对应栏目中增加简短的`Knowledge Opportunity Notes`。Notes只记录“可增强的Clip目标 + 候选知识方向 + 已知连续性/复杂度限制”，不得新增Template字段、替STATE-08做最终选择，也不得改写STATE-06 Camera Language Decision或Clip Movement Plan。STATE-08必须重新执行完整Knowledge Opportunity Check；Notes只是可追溯线索，不是强制采用项。

同时必须建立`Clip Movement Plan`：

- **主导镜头语言**：用一句话锁定本Clip的主导观察逻辑及叙事理由，并可追溯到Director Decision Notes，例如“稳定关系轴观察→关键信息处一次靠近→结尾释放距离”；不得只列运镜词
- **镜头间运镜变化**：按Shot原顺序写明主运镜、变化触发、叙事功能、与前一镜的关系和终点；不允许STATE-07静默修改STATE-06 Camera Language Decision
- **视觉高潮镜头**：指定一个SHOT，说明为什么它承担本Clip最大的摄影强调；没有高潮时明确“无独立高潮，保持克制”
- **最克制镜头**：指定一个固定/低幅度/最少摄影干预的SHOT，说明它如何给表演、信息或节奏留出空间
- **重复规避**：列出重复主运镜扫描结果；同类主运镜连续3次以上必须逐镜说明叙事理由，否则返回STATE-06调整
- **Seedance复杂度控制**：记录每镜稳定等级、全Clip复杂度峰值、同时发生的人物/运镜/FX/口型负荷，以及删辅助、降速、缩短路径、固定机位或拆Clip/返回拆Shot的降级顺序

多样但不杂乱：

- 每个Clip必须有明确主导运镜逻辑，变化只发生在镜头目的、刺激、人物关系、空间任务或节奏阶段改变处。
- 一个Clip超过4个Shot时通常至少包含2种不同运镜逻辑；若只有1种，必须说明连续动作、长镜观察或刻意重复的叙事理由。
- 同类主运镜连续出现3次及以上必须有逐镜理由；不强制每个Shot都不同，也不得为达成数量随机加入运镜。
- 优先使用Push In、Pull Out、Tracking、Side Tracking、Pan、Tilt、Crane、Handheld、Shoulder Follow、Dolly Tracking与Static / Locked-Off。复杂Orbit / 360、穿墙、无人机或多段一镜到底只有在叙事明确需要、模型容量允许且有基础降级时可保留。

一个 Clip 内即使包含多个 Shot，也仍是一次生成执行合同。Clip 可在同一 Prompt 内表达已确认的镜头阶段或切换，但不得输出成多条 Shot Prompt，不得重置人物/空间/道具状态，也不得插入未确认剧情。

## Step 4｜Duration And Continuity Ledger

为每个 Clip 写出可复算时长账本：

`Shot A 时长 + Shot B 时长 + … = Clip 目标时长 = STATE-08 平台生成时长`

四项必须一致：来源 Shot 时长、Clip Detail 合计、Clip Table 目标时长、STATE-08【时长】平台生成时长。

同时记录 Entry、内部 Shot 状态链、Exit、尾帧用途和跨 Clip 声音/动作/视线/构图锚点，并把它们归并为本Clip的八组`Clip End-State Record / Next-Clip Carryover`。先沿用Preflight的`视觉连续 / 剧情连续 / 主动切场或切世界`主分类，再判定A【同镜头连续承接】、B【新镜头参考型】或C【新镜头且无需尾帧】，据此标记`Tail Frame Required = YES / NO`并映射既有Handoff；此判定必须先于尾帧可用性检查。A/B统一使用`REF-TAIL-XX｜CLIP-XX尾帧参考`且必须声明用途；缺图时保留待补充状态而不声称已确认。C不列`REF-TAIL`。叙事断点必须明确重建，不得伪装为连续继承。

对每一对相邻Clip强制建立：

`Previous Clip End State → Next Clip First Frame Reference`

- **A｜Continuous Handoff / Direct｜同镜头连续承接**：上一Clip最后一个镜头在当前Clip继续，目标接近一镜到底。下一Clip第一帧逐项等于上一尾帧的人物姿态、位置、左右/前后、朝向、视线、距离、动作结果与阶段、道具持有/位置、构图、景别、机位/轴线侧、环境、光线、天气、情绪与持续声音；不得重置、重播已完成动作或无过程换边。用途写为“同镜头连续承接用途”。
- **B｜Continuous Handoff / Reference-Only｜新镜头参考型**：当前Clip另起新镜头重新构图，但上一尾帧仍作为站位、朝向、人物距离、景别衔接、空间关系、道具状态或起始构图基准。必须写明保持项、允许改变的新机位/景别/视角/构图及“空间/站位/景别参考用途”，不得记录为Direct或同镜头续拍。
- **C｜Not Required / Not Inherited｜新镜头且无需尾帧**：当前镜头明确换机位、换景别、反打、特写、俯拍/仰拍或重构图，且不依赖上一尾帧画面状态。不得把上一尾帧列入参考资产；以Canonical基础资产、Confirmed Spatial Blocking与文字空间规则核对连续性并记录新首帧重建依据。

A/B必须标记`Tail Frame Required = YES`，再检查视觉资产可用性。无论尾帧是否已产生、可访问或已确认，当前Clip参考资产声明都必须列出统一`REF-TAIL-XX｜CLIP-XX尾帧参考`及用途：A写“同镜头连续承接用途”；B写“空间/站位/景别参考用途”。缺图时同时写“待用户提供/待上传、未确认”，主动提示用户从上一Clip最终成片中手动截取最终有效尾帧后添加，不得伪造路径或声称已确认；该声明只占Projected位，不计入已提交图片数。Prompt可以完整编译和交付，实际提交生成前必须补图。

A的`首帧参考：`必须写`以 REF-TAIL-XX｜CLIP-XX尾帧参考 为直接承接依据起镜。`并逐项锁定全部承接维度。B的`首帧参考：`必须写明参考该尾帧延续站位/朝向/距离/景别/空间/道具或构图逻辑，但当前Clip另起新镜头重新构图；禁止使用A类固定直接承接句。C标记`Tail Frame Required = NO`，不要求截图、不列`REF-TAIL`，可由文字End State、Canonical基础资产与Spatial Blocking建立新首帧。尾帧只作为时刻状态与连续性锚点，不替代角色、环境、道具Active Canonical资产。

当前Clip的`结尾状态`与`结尾帧限制`必须定义一个新的稳定结束状态，为下一Clip提供新的连续性锚点；实际生成、提取并确认后才可按当前Clip编号登记为新的`REF-TAIL-XX｜CLIP-XX尾帧参考`。

任何未被可见动作过程或已确认断点授权的差异都视为空间继承失败：SHOT / Blocking设计错误返回STATE-06；仅Clip边界组织或尾帧用途错误留在STATE-07修正。

尾帧用途判定后必须更新下一Clip的Reference Budget Audit。A/B的`Tail Frame Required = YES`即形成1个Projected连续性预留位，与尾帧当前是否已上传无关；若下一Clip原已有9张候选，Projected Final Count按10计算，必须主动从同类非角色整合或低优先项裁剪中至少释放1位，不得通过省略必需尾帧伪造预算通过。尚无实际尾帧图时仍在参考资产声明中列出统一`REF-TAIL`名称、用途与“待用户提供/待上传、未确认”，但不得计为已存在/已提交图片；Projected Final Count仍预留1位。

## Step 5｜Write And Validate

输出严格使用 `templates/20_clip_plan.md`，写入 Active Project Root 的 `clips/`、`sequences/` 或 `shots/` 目录，并登记 Revision。

运行：

Work/Codex：

`validate_sd_film.py clip <clip-plan.md> --project-status <project_status.md> --shot-design <confirmed-detailed-shot-script.md>`

Portable模式没有本地Artifact路径时，必须从Portable Checkpoint交叉核验同等的STATE-06完成证据、Artifact Status、Revision与正式SHOT清单；不得只运行声明式Clip结构校验后直接标记Confirmed。

只有以下条件全部满足才能标记 Confirmed：

- 每个正式 Shot 按原顺序且仅进入一个 Clip
- 每个 Clip 包含一个或多个相邻 Shot，时长为4—15秒
- 所有合并均通过场景、时间、动作、摄影机、空间、道具、资产与复杂度检查
- 每个 Clip 具有起始状态、连续动作、空间关系、道具连续性与稳定结尾状态
- 每个 Clip 已完成Scope Firewall：此前事件未重播，本Clip只执行一个主要可见Beat所需的动作链，后续剧情未提前表演，明确禁提前元素未出现，并以清楚改变的Endpoint结束；多动作例外仍服务同一Beat
- 每个 Clip 的已有Entry / Exit / Handoff事实已归并为八组`Clip End-State Record / Next-Clip Carryover`；下一Clip首帧能逐项消费Character、Spatial、Prop、Camera、Environment、Performance、Continuity Risks与Carryover，不存在无依据的人物/道具重置
- 上一Clip存在用户接受Take时，本Clip已从Execution Ledger读取Observed Start / End与Accepted Canon State，并以其合法瞬时状态覆盖同维度Planned State；被拒绝或未确认Take未进入Canon，Accepted Take中的身份/结构漂移未覆盖正式Canonical资产
- 每个Clip已完成STATE-07 Clip Preflight前置版并为PASS：连续性已三选一；逐分镜World-State与实际资产一致；角色精确数量、空间构图、Performance / Emotion、道具状态已锁定；逐角色动作前/中/后可见阶段与跨镜Arc可复算，Intentional Hold有证据，多人相对表演层级清楚；适用转场五要素完整；预算只在前述检查后执行
- 每个Clip已完成Visual Blocking Risk Pre-Assessment并记录`NONE / POSSIBLE / REQUIRED`、风险理由、建议草图类型与Blocking Signature；STATE-07没有为统一流程提前生成草图，也没有把Scene Top-down Blocking Map误登记为Clip视觉参考
- 每个相邻Clip已在既有判定中明确A【同镜头连续承接】、B【新镜头参考型】或C【新镜头且无需尾帧】，未用资产可用性反向决定需求；A/B均在参考资产声明列出统一`REF-TAIL`名称、对应用途和真实状态，缺图时明确“待用户提供/待上传、未确认”且未伪造路径或确认；C未列`REF-TAIL`，并从Canonical基础资产、Confirmed Spatial Blocking、文字End State或当前Scene / World-State / Start Boundary建立首帧
- 每个完全位于转换后世界的Clip已删除转换前世界资产；只有正在执行转换的Clip才按阶段引用转换前后资产，且没有把同一道具不同形态混成两件道具
- 剧情规定唯一角色时，Clip Plan已有正向唯一数量锁与背景无第二个同类限制；追逐镜头默认后追前逃且无双方并排正对镜头、同景深合影或群像站桩
- 每个关键道具已明确当前形态、尺寸、持有者、是否允许悬浮与转换完成状态；现实/幻想形态没有跨世界误用
- 每个 Clip 已读取对应Confirmed Spatial Blocking Result；角色路径、C1/C2/C3轴线侧、Text Spatial Rules和关键道具锚点没有被重新设计，Top-down Map没有进入视频参考资产
- 每个适用Clip具有唯一可读的关系几何；首帧、内部Shot状态链和尾帧没有无授权跨轴、左右交换、朝向翻转、双正脸或来源—目标反转
- 每一对相邻Clip都完成`Previous Clip End State → Next Clip First Frame Reference`逐项核对；A Direct完全继承并使用固定直接承接句，B Reference-Only明确另起新镜头、保留项与允许变化且不误写Direct，C不列尾帧并明确文字/资产/Spatial Blocking重建依据；任何`REF-TAIL`均已声明用途类型
- 时长账本可复算且与平台生成时长一致
- 每个 Clip 有明确风险、降级、尾帧用途和下一 Clip Handoff
- 每个 Clip 已完成Clip Movement Plan，主导逻辑、逐镜变化、视觉高潮、最克制镜头、重复规避与Seedance复杂度控制均可验证
- 每个 Clip 已完成Reference Budget Audit：≤7不整合；8张无额外帧需求不整合；9张无未计入连续性需求才允许；>9完成去重/非角色整合/优先级裁剪；最终真实图片清单≤9且无重复、无无关项、无虚构资产
- 每个 Clip 已先完成Reference Selection / Routing：每个入选资产能对应当前具体风险/目标并声明Primary Role / Purpose，身份、空间结构、道具造型、A/B尾帧、Motion、Camera、Audio与光线/场景状态使用正确Authority；C未路由旧尾帧；Transient Reference未覆盖正式身份/结构/造型；Eligible但无关资产没有因Registry存在、上一Clip使用或预算空位被机械加入
- 每个视觉候选均通过“这是不是一张实际会被投喂/引用的视觉资产？”检查；纯文字站位、换边、距离、共坐、数量、空间、行为、禁止项与镜头规则已从参考清单移出并进入正确既有字段；真实道具图使用正式资产ID，待补视觉图明确具体图像、实际投喂用途与未确认状态
- 当前Clip每个核心角色仍有各自独立三视图/角色锁定图，未合并为角色总表，动作/互动图未替代外貌基准；独立资产未超限时没有被强制换成总图
- 每个 Clip 已读取并保持对应Director Decision Notes；主导镜头语言、节奏、调度、视觉高潮/留白、功能性色光与声音设计均能追溯到导演意图
- Director Decision Notes没有成为新Template字段，Knowledge Opportunity Notes也没有反向改写导演方向或被当作最终策略
- 如存在Knowledge Opportunity Notes，其内容来自已确认Clip事实，已写入现有知识投影位置，且没有被当成最终策略或新Schema字段
- 超过4个Shot的Clip通常至少包含2种运镜逻辑；同类主运镜连续3次以上均有逐镜叙事理由，且没有为多样性随机堆叠运镜
- 没有 Storyboard 视觉材料进入 Clip 或 STATE-08 参考资产

## State Handoff

完成后更新Selected State Source：Work/Codex写Active Project Root的`project_status.md`，普通Chat本机Root不可读时写`portable_project_status.md`：

- Current State：STATE-07
- State Status：COMPLETE
- Active Workflow：10_clip_production_workflow.md
- Last Completed Step：STATE-07 Clip Production
- Last Successful Checkpoint：Confirmed Clip Production Plan Revision
- Active Artifacts：登记 Clip Plan 路径与 Revision ID
- Next Workflow：11_video_generation_workflow.md

随后按`references/project_state_contract.md`同步或输出更新后的完整Portable State，并执行其`Portable Required Field Writeback`；同步失败不得阻塞STATE-08，也不得改变`STATE-06 Detailed Shot Design → STATE-07 Clip Production → STATE-08 Clip-based Video Prompt / Video Generation`。

STATE-08 必须读取该 Confirmed Clip Production Plan，并按 CLIP-001、CLIP-002……一对一编译 Prompt。不得绕过 Clip 重新按 Shot 或剧本自由组合。
