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
- STATE-06 Confirmed `Professional Detailed Shot Script` 与原正式 SHOT 顺序；每个Shot已完整包含镜号、TC IN、TC OUT、时长(s)、景别、焦段、场景/美术、画面内容/构图、人物动作、摄影机/镜头、摄影参数、镜头调度、光线/色彩、画面特效/转场、台词/旁白/口播、音效/BGM、AI制作备注、素材/资产
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
- `画面特效/转场、台词/旁白/口播、音效/BGM、AI制作备注、素材/资产`中的执行与连续性事实；后期BGM规划不自动进入STATE-08音效

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

`Continuity Classification → World-State Check → Character Count Lock → Spatial Composition Lock → Prop State Check → Transition Check（适用时）→ Reference Asset Check / Budget`

逐Clip至少记录：

- **Continuity Classification / Tail Frame Requirement**：从`视觉连续 / Visual Continuity`、`剧情连续 / Narrative Continuity Only`、`主动切场 / 切世界 / Motivated Scene-or-World Change`中三选一，并写证据；随后根据当前Clip Start Requirement是否需要严格视觉承接，在同一既有判定中标记`Tail Frame Required = YES / NO`。Direct / Reference-Only需要精确继承上一可见状态时必须为`YES`，不得因系统当前没有尾帧图改成`NO`。剧情连续、主动切场或画面独立重建通常为`NO`。
- **World-State Map**：逐分镜写现实世界、幻想世界、耳中玉境或项目已确认层，列出该层实际角色、环境、道具、FX与转换前/后阶段。完全在耳中玉境的Clip必须删除现实标准耳勺等现实阶段资产；转换Clip才可按阶段同时保留两种道具形态。
- **Character Count Lock**：逐分镜列出`角色 × 精确数量`。剧情唯一角色必须正向锁定唯一数量与前中后景无第二个同类，并预置反向复制/分身/镜像/背景重复限制。
- **Spatial Composition Lock**：对追逐、战斗、对峙、对话和多人镜头锁定前后景、左右、朝向、关系轴、摄影机轴线侧、追逃/攻击/视线路线、可见面部与同景深许可。追逐默认后追前逃，禁止并排正对镜头和海报式合影。
- **Prop State Check**：逐关键道具写当前形态、尺寸、持有者/左右手、位置、方向、是否允许悬浮、转换是否完成与结束状态；不同世界形态不得无过程混用。
- **Transition Five Elements**：现实↔幻想/耳中玉境、地点/时间跳跃、尺度或角色/道具形态转换时，必须先锁定起点状态、转换媒介、运动方向/过程、终点状态、转场后首个稳定构图。缺一不得用“金光一闪 / 突然切换”代替。
- **Reference Asset Check**：只在上述项目通过后筛选资产与执行预算；角色独立锁定图优先，删除未出场、未使用及当前World-State不适用项，最终≤9，只有超限风险时整合非角色信息。

任一项失败时记录Affected Clip / Shot与Return Route，先修设计再从Continuity Classification重跑。Preflight为FAIL时不得进入Step 3、不得生成或确认Clip Plan。

## Step 3｜Author Clip Execution Contract

每个 Clip 必须记录：

- Clip ID 与包含的 Shot ID（原顺序）
- 起始状态与来源
- 连续动作、表演与情绪弧
- 摄影机/构图/焦段/对焦的执行路径
- 人物与环境的空间关系、轴线、视线和行进方向
- Spatial Blocking继承：引用当前Scene的Decision / Map Mode，逐项锁定固定结构、角色路径、C1/C2/C3摄影机侧和Text Spatial Rules；不得把Top-down Map本身登记为视频参考资产
- 战斗/双主体/对峙关系的几何锁定：A/B左右与前后、朝向、距离、主轴、摄影机轴线侧、Connector及首尾帧继承；双方同框相对时禁止双正脸
- 道具持有者、位置、方向、状态及变化
- 光影、色彩、FX 与声音连续性
- 结尾状态、稳定尾帧限制及下一 Clip Handoff
- 模型执行风险与安全降级
- Clip Preflight Check：连续性主分类、逐分镜World-State、角色精确数量、空间构图锁、关键道具状态、适用Transition五要素、Reference Asset Check与`PASS / Return Route`
- Reference Budget Audit：只列当前Clip实际需要、真实存在/已确认且通过World-State的候选图片资产，删除不出场角色、未使用环境/道具/动作图和当前阶段不适用资产；`Tail Frame Required = YES`时无论资产是否已经上传都预留1个Projected连续性图片位，但只有上传、可访问且确认可用后才进入最终真实图片清单；`NO`不预留旧尾帧。再计算Projected Final Count，并按`knowledge/reference_budget.md`记录是否触发整合、替代关系、裁剪与最终≤9张清单

参考资产默认保持原始独立结构。Projected Final Count≤7时不得整合；8张且无额外帧需求时原则上不整合；9张只有在确认没有未计入连续性需求时才允许；已有9张且仍需上一Clip尾帧/当前首帧时按10张处理并至少释放1位；>9张时才执行同类非角色信息的去重/整合/裁剪。当前Clip每个核心角色始终保留各自独立三视图/角色锁定图，多个核心角色不得合并成角色总表，动作图不得替代外貌基准。

只有真实存在、已确认且完整覆盖对应零散图的环境/道具/空间/动作/使用示意总图才可用于替代。若需要新建总图，返回对应STATE-03资产Workflow完成双确认闭环后再继续；STATE-07不得虚构资产名称。独立资产更清晰且未超限时继续使用独立图，不因已有总图而强制替换。

组织上述执行合同时，必须先把当前Clip所覆盖Shot Group的Director Decision Notes综合为一条内部`Clip Director Direction`：

- **主导镜头语言**：摄影机总体观察、跟随、逼近、揭示、释放或保持不介入的理由；具体运镜仍服从STATE-06 Camera Language Decision
- **节奏**：观众等待如何建立、在哪个动作/视线/声音节拍释放，以及Clip结尾保留多大程度的留白
- **调度**：人物距离、视线、站位、先后动作与关系变化如何在Clip内部连续发展
- **视觉高潮 / 留白**：哪一个SHOT承担最大摄影或光色强调，哪一个SHOT必须克制、固定或降低视听密度
- **功能性色光与声音**：只保留有真实来源和剧情触发的变化；没有功能性变化时明确保持稳定

`Clip Director Direction`只作为组织与校验语义，必须投影到`templates/20_clip_plan.md`已有的Clip目标、连续动作、Clip Movement Plan、光色/声音连续性、高潮/克制与风险位置；不得新增Template字段，也不得在STATE-07重新选择知识策略。

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

同时记录 Entry、内部 Shot 状态链、Exit、尾帧用途和跨 Clip 声音/动作/视线/构图锚点。先沿用Preflight的`视觉连续 / 剧情连续 / 主动切场或切世界`主分类，再根据下一Clip是否需要严格视觉承接标记`Tail Frame Required = YES / NO`并映射具体Handoff；此判定必须先于尾帧可用性检查。实际生成并确认的尾帧资产统一命名为`REF-TAIL-XX｜CLIP-XX尾帧参考`，其中`XX`沿用来源Clip编号；叙事断点必须明确重建，不得伪装为连续继承。

对每一对相邻Clip强制建立：

`Previous Clip End State → Next Clip First Frame Reference`

- **Continuous Handoff / Direct**：下一Clip第一帧逐项等于上一Clip尾帧的人物位置、左右 / 前后、面对方向、视线、动作结果、道具持有 / 位置、环境锚点和摄影机轴线侧；不得重置、重播已完成动作或无过程换边。
- **Continuous Handoff / Reference-Only**：上一尾帧仍是第一顺位空间基准；只允许已确认的景别 / 机位 / 构图变化，并明确保持哪些空间事实。
- **Motivated Discontinuity / Not Inherited**：适用于剧情连续但画面独立重建，或主动切场 / 切世界。不得把上一尾帧作为正式生成参考，但必须记录它用于人物 / 视觉连续性核对的范围、经确认的断点与下一首帧重建依据。

Direct / Reference-Only需要严格视觉承接时必须标记`Tail Frame Required = YES`，再检查视觉资产承接条件：若上一Clip已有实际可用最终尾帧图、定格图或经确认截图，登记真实引用并统一命名为`REF-TAIL-XX｜CLIP-XX尾帧参考`；若尚未产生、无法访问或未确认，STATE-07必须主动提示用户从上一Clip最终成片中手动截取最终有效尾帧并作为当前Clip参考资产上传，只在现有起始状态、下一Clip Handoff和Reference Budget Audit的“待加入”位置标记“待用户提供/待上传”，不得把计划名称列为真实参考资产。允许继续形成设计与Prompt草案，但STATE-08最终可执行版必须等待上传。

`Tail Frame Required = YES`时逐项锁定人物姿态、位置、朝向、人物间距离、构图、机位关系、环境、光线、天气、道具与情绪。尾帧上传后必须加入当前Clip参考资产，并由当前Clip`首帧参考：`明确写`以 REF-TAIL-XX｜CLIP-XX尾帧参考 为直接承接依据起镜。`。尾帧只作为时刻状态与连续性锚点，不替代角色、环境、道具Active Canonical资产。换场、明显时间跳跃、构图无需连续或其他不需严格视觉承接时标记`Tail Frame Required = NO`，不要求截图，可文字承接或建立新首帧。

当前Clip的`结尾状态`与`结尾帧限制`必须定义一个新的稳定结束状态，为下一Clip提供新的连续性锚点；实际生成、提取并确认后才可按当前Clip编号登记为新的`REF-TAIL-XX｜CLIP-XX尾帧参考`。

任何未被可见动作过程或已确认断点授权的差异都视为空间继承失败：SHOT / Blocking设计错误返回STATE-06；仅Clip边界组织或尾帧用途错误留在STATE-07修正。

尾帧用途判定后必须更新下一Clip的Reference Budget Audit。`Tail Frame Required = YES`即形成1个Projected连续性预留位，与尾帧当前是否已上传无关；若下一Clip原已有9张候选，Projected Final Count按10计算，必须主动从同类非角色整合或低优先项裁剪中至少释放1位，不得通过省略必需尾帧伪造预算通过。尚无实际尾帧图时只记录“待用户提供/待上传”，不得计为已存在资产或进入最终真实图片清单。

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
- 每个Clip已完成STATE-07 Clip Preflight前置版并为PASS：连续性已三选一；逐分镜World-State与实际资产一致；角色精确数量、空间构图、道具状态已锁定；适用转场五要素完整；预算只在前述检查后执行
- 每个相邻Clip已先按当前Clip Start Requirement标记`Tail Frame Required = YES / NO`，未用资产可用性反向决定需求；`YES`时已主动请求用户截取并上传上一Clip最终有效尾帧，未上传状态明确为“待用户提供/待上传”且没有虚构资产；`NO`时没有要求截图，并从文字End State或当前Scene / World-State / Start Boundary建立首帧
- 每个完全位于转换后世界的Clip已删除转换前世界资产；只有正在执行转换的Clip才按阶段引用转换前后资产，且没有把同一道具不同形态混成两件道具
- 剧情规定唯一角色时，Clip Plan已有正向唯一数量锁与背景无第二个同类限制；追逐镜头默认后追前逃且无双方并排正对镜头、同景深合影或群像站桩
- 每个关键道具已明确当前形态、尺寸、持有者、是否允许悬浮与转换完成状态；现实/幻想形态没有跨世界误用
- 每个 Clip 已读取对应Confirmed Spatial Blocking Result；角色路径、C1/C2/C3轴线侧、Text Spatial Rules和关键道具锚点没有被重新设计，Top-down Map没有进入视频参考资产
- 每个适用Clip具有唯一可读的关系几何；首帧、内部Shot状态链和尾帧没有无授权跨轴、左右交换、朝向翻转、双正脸或来源—目标反转
- 每一对相邻Clip都完成`Previous Clip End State → Next Clip First Frame Reference`逐项核对；Direct完全继承，Reference-Only明确保留项，Not Inherited明确断点和重建依据
- 时长账本可复算且与平台生成时长一致
- 每个 Clip 有明确风险、降级、尾帧用途和下一 Clip Handoff
- 每个 Clip 已完成Clip Movement Plan，主导逻辑、逐镜变化、视觉高潮、最克制镜头、重复规避与Seedance复杂度控制均可验证
- 每个 Clip 已完成Reference Budget Audit：≤7不整合；8张无额外帧需求不整合；9张无未计入连续性需求才允许；>9完成去重/非角色整合/优先级裁剪；最终真实图片清单≤9且无重复、无无关项、无虚构资产
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
