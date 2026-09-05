# Clip Plan

> Refactor authority: STATE-07 records a selected-model Execution Clip Plan. First preserve each model-neutral Natural Unit, then use the already selected Adapter to apply duration, timeline and execution constraints. The model may split or retain the unit but cannot change its screenplay, Director Intent, spatial facts or Canonical Assets.

## Default User-facing Delivery

默认交付标题为“Clip表”。只展示Clip ID、包含镜号、核心画面/动作、时长、起止承接和必要参考资产。Preflight、Scope Firewall、Reference Routing、参考预算、风险降级、尾帧判定、执行账本和QA均在内部运行并写入生产记录，不单独展示。用户明确请求完整制作计划时才输出其完整字段。

- Project ID：
- Status：Planning / Confirmed
- Source Detailed Shot Design Artifact / Portable Checkpoint：
- Source Detailed Shot Design Status：Confirmed
- Source Detailed Shot Design Revision：
- Selected Model：Seedance 2.0 / Seedance 2.5
- Adapter Profile：`adapters/seedance-2.0.md` / `adapters/seedance-2.5.md`；必须与Selected Model一一匹配，仅作内部执行路由，不投影为STATE-08 Prompt字段
- Model Selection Status：SELECTED（未选择不得进入Execution Clip整合）
- Execution Profile：Selected Model、Adapter Profile、Execution Mode、Long-duration Route、Effective Gateway Limits、Model Selection Scope；外部限制只作观察记录，用户选择的生成时长不在规划阶段被它压缩；仅作Confirmed Clip Production Plan内部执行信息，不投影为STATE-08 Prompt字段
- Model Duration Window：Seedance 2.0为4—15秒；Seedance 2.5为4—30秒；16—30秒须严格预检PASS，时长由用户在模型窗口内选择
- Total Formal Shots：
- Total Clips：
- Unit Rule：Shot = 导演镜头设计单位；Clip = AI视频生成执行单位；每个Shot且仅进入一个Clip；Total Clips ≤ Total Formal Shots；STATE-08每个Clip只生成一条连续Prompt
- Namespace Rule：Source Script Label ≠ SCENE ≠ UNIT ≠ SHOT ≠ CLIP；只有Confirmed Detailed Shot Design中的正式SHOT可进入Clip

## Clip Table

| Clip ID | 包含镜号 | 核心画面/动作 | 时长 | 起止承接 | 资源 |
|---|---|---|---:|---|---|
| CLIP-001 | SHOT-001 / SHOT-001 + SHOT-002 |  | 10秒 | 起始状态 → 结尾状态 → 下一Clip连接 | 已确认资产与必要参考 |

## Internal Clip Detail Cards

### CLIP-001

- 包含 Shot：按 SHOT ID 原顺序逐项列出
- Execution Mode：`Standard Clip` / `Video Extension` / `Targeted Edit`
- 目标时长：N秒（2.0为4—15秒；2.5为4—30秒；16—30秒自动触发内部严格预检）
- Long-duration Preflight：Not Applicable（4—15秒 / 非2.5）/ PASS / FAIL；16—30秒须确认镜头链、空间关系、表演连续性、动作/物理密度及适用转场逻辑均通过；FAIL返回`STATE-07 / 拆分Clip`
- Model Profile Preflight：Standard Clip沿用稳定短Clip；Video Extension必须有实际上一段成片`REF-VIDEO`作为受控输入，且叠加而不替代首/尾帧、资产锁与End-State；Targeted Edit仅在用户明确要求修改既有视频时可用，时间段控制仅可写入既有分镜正文
- 时长核算：SHOT-001=N秒 + SHOT-002=N秒；合计=N秒；平台生成时长=N秒
- 组织类型：`单Shot` / `多Shot连续生成` / `多Shot有动机剪辑`
- 组织理由：逐项说明场景连续性、时间连续性、人物动作连续性、摄影机连续性、模型执行复杂度与单次生成时长判断
- 生成合同：本Clip对应一次生成；即使包含多个Shot，STATE-08也只输出一条完整Prompt，不按Shot拆分。单Shot为单一镜头连续生成；多Shot连续生成不中断、不硬切；多Shot有动机剪辑只在Director确认的切镜合同完整时执行。内部同时锁定Dramatic Execution Unit：Clip Dramatic Function、Start → End Dramatic State、Critical Performance Beat、Critical Blocking / Spatial State、Continuity / Rhythm / Information Timing Requirement、Generation Risk / Simplification Boundary；不新增顶级字段
- 有动机切镜合同（仅`多Shot有动机剪辑`）：
  - 切镜叙事功能：
  - 切点与视觉媒介：
  - 切镜前结束状态：
  - 切镜后重建状态（世界、角色、环境、道具、摄影机、稳定构图）：
  - 连续性锚点（保留 / 改变）：
  - 容量不足安全降级（必须返回`STATE-07 / 拆分Clip`）：
- 起始状态：人物、环境、空间、道具、FX、情绪、摄影机及来源边界
- Clip Preflight Check（STATE-07前置版；必须先于Reference Budget）：
  - Temporal / Spatial Continuity Classification：视觉连续 / 剧情连续 / 主动切场或切世界（三选一）；判定证据；在同一判定中明确A【同镜头连续承接 / Direct】、B【新镜头参考型 / Reference-Only】或C【新镜头且无需尾帧 / Not Required】。A/B标记`Tail Frame Required = YES`并记录`REF-TAIL-XX｜CLIP-XX尾帧参考`、对应“同镜头连续承接用途”或“空间/站位/景别参考用途”及真实状态；未上传时仍列名并标记“待用户提供/待上传、未确认”，不计入已提交图片。C标记`NO`、不列尾帧，并记录Canonical资产、Spatial Blocking与文字重建依据
  - World-State Map（逐分镜）：当前现实 / 幻想 / 耳中玉境 / 其他已确认层；Pre/Post Transition阶段；实际角色、环境、道具、FX；不适用资产删除结果
  - Character Count Lock（逐分镜）：角色身份 × 精确数量；唯一角色的正向唯一性与前/中/背景无第二个同类锁；复制/分身/镜像/背景重复风险
  - Spatial Composition Lock：前后景、左右、朝向、视线、关系轴、摄影机轴线侧、追逃/攻击/视线路线、正脸/侧背/背身许可、同一景深许可；追逐默认后追前逃并禁止并排合影
  - Performance / Emotion Check：逐角色Inherited Baseline → Trigger → Pre-action / In-action / Post-action Residue → Arc Endpoint；Intentional Hold证据；Primary Performer / Secondary Reactor / Listener / Background Holder、反应顺序、相对幅度与视觉重点交接；静态情绪标签不得冒充表演
  - Visual Blocking Risk Pre-Assessment：`NONE / POSSIBLE / REQUIRED`；命中风险；建议`S-SKETCH / P-SKETCH / A-SKETCH / Combined`；Blocking Signature摘要；STATE-07只预判不生成。已有Confirmed `REF-SKETCH`时记录KEEP候选与Revision；最终CREATE / REPLACE / RETIRE由STATE-08 Before-Single-Clip-Prompt Gate决定
  - Prop State Check（逐关键道具）：当前形态、尺寸、持有者/左右手、位置、方向、是否允许悬浮、转换是否完成、结尾状态与下一镜继承
  - Transition Check（适用时）：起点状态；转换媒介；运动方向/过程；终点状态；转场后首个稳定构图；不适用时写明理由
  - Reference Asset Check：每个视觉候选先回答“这是不是一张实际会被投喂/引用的视觉资产？”；只列当前World-State实际存在/出场/使用且Confirmed并可回查的视觉资产，或明确需要用户实际补入、写明具体图像对象/实际投喂用途/`待用户补充或待上传、未确认`的视觉图占位。纯文字站位、换边、距离、共坐、数量、空间、行为、禁止项或镜头规则标记`NOT ELIGIBLE`并迁移到正确既有字段；角色独立图优先；C不机械计入上一尾帧；任何`REF-TAIL`必须声明用途；再进入Reference Budget
  - Preflight Result：PASS / FAIL；Affected Clip / Shot；Return Route；修正后重跑结果
- 连续动作：按 Shot 顺序描述动作、表演、情绪与必要镜头阶段如何连续执行
- 摄影机与构图路径：机位、轴线侧、景别/视点变化、主要运镜、焦段/对焦、稳定降级
- Clip Movement Plan：
  - 主导镜头语言与叙事理由：
  - 镜头间运镜变化（按Shot列出主运镜 / Static、变化触发、叙事功能、与前镜关系、终点）：
  - 视觉高潮镜头及理由；无独立高潮时写“保持克制”：
  - 最克制镜头及理由：
  - 重复规避（连续同类主运镜扫描；3次以上逐镜理由；超过4个Shot时的运镜逻辑数量与例外理由）：
  - Seedance复杂度控制（逐镜稳定等级、Clip峰值、同时负荷、删辅助 / 降速 / 缩短路径 / 固定机位 / 拆分降级；2.5多镜头能力不放宽复杂多人互动、物理或动作风险降级）：
  - Clip Camera Continuity / Visual Rhythm（建立 / 隐藏 / 泄漏 / 确认 / 压住 / 释放的功能差异；Movement Trigger / Stop；景别与距离层级；禁止无理由每镜慢推+浅景深）：
- 空间关系：人物A/B左右/前后/高低、分别朝左/朝右与侧身程度、视线目标、距离、行进方向、环境锚点和180度轴线；战斗/双主体/对峙/对话/追逐/相向运动必须写唯一关系轴或主攻击/运动轴
- 空间连线（适用时）：视线 / 武器 / 攻击 / 追逐路线 / 水流 / 能量 / 抛射物的来源 → 路径 → 目标；必须与人物朝向、喷口/武器方向、屏幕方向和受击位置一致
- 同框面部与机位限制（适用时）：双方相对时禁止同时完整正脸；优先固定侧面、侧后双人或OTS；有意越轴必须有已建立轴线、可见路径/中性机位、地标与稳定新轴线侧
- 道具连续性：身份、持有者、位置、方向、状态、变化过程与结尾状态
- 光影/色彩/FX连续性：
- 声音连续性：环境底声/空间底噪；同步动作声、Foley、呼吸、对白或剧情内声源；声音尾部与下一Clip承接
- 结尾状态：人物、动作、情绪、空间、道具、环境、光态、摄影机与稳定停留点
- 结尾帧限制：定义本Clip新的稳定结束状态；实际生成、提取并确认后登记为REF-TAIL-001｜CLIP-001尾帧参考
- 尾帧用途判定：A同镜头连续承接用途 / B空间、站位、景别参考用途 / C新镜头且无需尾帧（Canonical资产 + Spatial Blocking + 文字重建依据） / 最终收束
- 下一Clip Handoff：
- Clip End-State Record / Next-Clip Carryover（STATE-07内部连续性记录；归并已有状态，不新增STATE或STATE-08字段）：
  - Character State（人物位置/朝向/坐站姿态/距离/动作阶段/谁持有什么）：
  - Spatial State（左右前后/环境锚点/路径/关系轴与180度轴线/视线或来源—路径—目标连线；按需保存Visual Anchor State / Blocking Signature：Characters、Topology、Position、Shared Facing、Seat / Spatial Relation、Allowed Delta、Camera Logic、Axis、Movement Path、Clip Start / End Blocking、Anchor ID / Revision / Status）：
  - Prop State（身份/形态/持有者与左右手/位置/方向/接触/当前状态）：
  - Camera State（位置/高度/朝向/轴线侧/景别/构图/焦点/稳定终点）：
  - Environment State（Scene / World-State/固定结构/时间/天气/光线/综合色彩/持续声音）：
  - Performance State（情绪/公开状态与泄漏/呼吸或体力/动作结果）：
  - Continuity Risks（状态断裂/人物或道具重置/左右或轴线翻转/身份、环境、道具、光态漂移/执行风险）：
  - Next-Clip Carryover（必须保持/允许改变/不继承/待确认；A/B/C、Tail Frame Requirement、参考用途或重建依据）：
- 模型执行风险与安全降级：单Shot / 多Shot连续生成 / 多Shot有动机剪辑的容量结论；多Shot有动机剪辑不支持时必须返回`STATE-07 / 拆分Clip`
- Reference Budget Audit：
  - Reference Selection / Routing（当前Clip目标与风险 → 选择的角色/环境/道具Canonical资产、Spatial Blocking文字语义、已有Confirmed且Signature未变的`REF-SKETCH`、A/B `REF-TAIL`、2.5 Video Extension的受控`REF-VIDEO`或合格场景状态参考；逐项写用途与Authority；Clay Render / 白模只拥有位置、朝向、距离、拓扑、机位、姿态、视线和动作路径Authority，绝不覆盖Canonical身份/材质/灯光/画风；STATE-07的草图风险预判不等于已存在视觉资产；Eligible但未选项与理由；明确“参考资产按需路由，不是越多越好”）：
  - 原始候选图片资产（逐项写实际资产ID/名称、Active/Confirmed状态、真实文件/受控ID、当前Clip用途、图片位数）：
  - Visual Input Eligibility（逐项回答是否为实际会投喂/引用的视觉资产；列出移除的文字伪资产、0图片位及迁移字段；待补视觉图列具体图像、实际投喂用途与未确认状态）：
  - 删除的当前Clip无关项（未出场角色 / 未使用环境 / 未使用道具 / 未使用动作图 / 其他）及理由：
  - 去重结果（重复文件或未增加信息项；不得把不同核心角色图当作重复）：
  - 连续性图片位（A/B无论是否已上传都预留1个Projected位，并在参考资产声明直接列出`REF-TAIL-XX｜CLIP-XX尾帧参考`、用途与状态；“待用户提供/待上传、未确认”不得计为已提交图片；C不加入或预留旧尾帧）：
  - Projected Final Count（独立候选 + 必需连续性图片位）：
  - 条件判定（≤7不整合 / 8张检查预留且原则上不整合 / 9张确认无额外需求 / >9触发整合）：
  - 非角色整合（仅在触发时；列真实已确认总图、被完整覆盖的零散图与资产证据；未触发写“不整合”）：
  - 裁剪项与理由（仅整合后仍>9时，按保留优先级从低到高处理）：
  - 最终参考图片清单与总数（必须≤9）：
  - 核心角色独立图检查（逐个核心角色列各自三视图/角色锁定图；禁止角色总表；动作图不得替代外貌基准）：
  - 预算结果：PASS ≤9 / Return Route
- 知识投影摘要：写可执行语义，不输出内部模式ID

按 Clip ID 继续建立 Detail Card。

## Shot Allocation Ledger

| Shot ID | Clip ID | 原顺序 | Shot目标时长 | 分配状态 | 备注 |
|---|---|---:|---:|---|---|
| SHOT-001 | CLIP-001 | 1 |  | Assigned Once |  |

## Cross-Clip Continuity Ledger

| From | To | Boundary Class | Outgoing Anchor | Stable End Window | Incoming Anchor | Tail-Frame Use Mode | Next Start-Frame Binding | Sound Bridge | Direct-Cut Downgrade |
|---|---|---|---|---|---|---|---|---|---|
| CLIP-001 | CLIP-002 | Continuous Handoff / Motivated Discontinuity |  |  |  | A Direct / B Reference-Only / C Not Required | Tail Frame Required = YES / NO；REF-TAIL用途；已引用 / 待用户提供、待上传且未确认 / Canonical资产+Spatial Blocking+文字重建 |  |  |

## Knowledge Projection Ledger

| Clip ID | Camera/Composition | Movement | Lens/Focus | Performance | Lighting/Color | Transition | Sound | FX | Prompt Evidence Target |
|---|---|---|---|---|---|---|---|---|---|
| CLIP-001 |  |  |  |  |  |  |  |  | templates/10_video_prompt.md现有字段 |

## Reference Budget Ledger

| Clip ID | 原始候选数 | 删除无关 / 去重后 | 连续性预留 | Projected Final Count | 是否触发整合 | 整合替代与真实资产证据 | 裁剪 | 最终图片数 | 核心角色独立图 | 结果 |
|---|---:|---:|---:|---:|---|---|---|---:|---|---|
| CLIP-001 |  |  |  |  | 否 / 是（原因） | 未触发 / 实际总图→被覆盖零散图 | 无 / 列项 |  | 逐角色列出 | PASS ≤9 / Return Route |

## Clip Preflight Ledger

| Clip ID | Continuity Classification | Previous Tail Formal Reference | World-State Check | Character Count Lock | Spatial Composition Lock | Prop State Check | Transition Five Elements | Reference Asset Check | Result / Return Route |
|---|---|---|---|---|---|---|---|---|---|
| CLIP-001 | 视觉连续 / 剧情连续 / 主动切场或切世界 | A同镜头连续承接 / B新镜头参考型 / C新镜头且无需尾帧；`Tail Frame Required = YES / NO`；REF-TAIL用途与已引用 / 待用户提供、待上传且未确认 / Canonical资产+Spatial Blocking+文字重建 | PASS / Affected Shot | PASS / Affected Shot | PASS / Affected Shot | PASS / Affected Shot | PASS / N/A / Affected Shot | PASS ≤9 / Affected Asset | PASS / Return Route |

## Coverage And Validation

- 所有正式 Shot 是否按原顺序出现且只分配到一个 Clip：
- 每个 Clip 是否包含一个或多个相邻 Shot，且总时长符合已锁定Profile（2.0为4—15秒；2.5为4—30秒；16—30秒有Long-duration Preflight PASS）：
- 所有多Shot Clip是否通过组织类型、场景、时间、人物动作、摄影机、空间、道具、资产、复杂度与时长检查；有动机剪辑是否含叙事功能、切点/媒介、切前结束、切后稳定重建、保留/改变锚点和STATE-07拆分降级：
- 短于4秒的 Shot 是否只在兼容Clip中执行；超过15秒的2.5候选是否自动完成Long-duration Preflight，否则返回STATE-07拆分为4—15秒Clip（不改写STATE-06）：
- 每个 Clip 是否具有起始状态、连续动作、空间关系、道具连续性与结尾状态：
- 每个Clip是否把已有Entry / Exit / Handoff归并为八组`Clip End-State Record / Next-Clip Carryover`，且下一Clip首帧能逐项消费、没有人物/道具/相机/环境状态重置：
- 每个Clip是否先通过Clip Preflight；Continuity Classification是否三选一并明确A/B/C；A/B是否标记`Tail Frame Required = YES`、在参考资产声明直接列统一`REF-TAIL`名称、对应用途与真实状态，缺图时写“待用户提供/待上传、未确认”且不冒充已提交图片；A/B首帧句式是否正确区分；C是否标记`NO`、不列`REF-TAIL`并以Canonical资产、Spatial Blocking、文字状态或当前Scene / World-State / Start Boundary重建；Performance / Emotion Check是否证明逐角色跨镜情绪弧、动作前/中/后可见阶段、Intentional Hold与多人相对表演层级，而不是静态标签或全员同强度表演：
- 每个Clip是否完成Visual Blocking Risk Pre-Assessment并记录`NONE / POSSIBLE / REQUIRED`、风险、建议草图类型与Blocking Signature；是否只做预判而未提前生成；已有Confirmed Anchor是否仅在Signature未变时标记KEEP：
- 是否逐分镜明确World-State，并删除未出场、未使用或当前阶段不适用的角色/环境/道具/FX；完全位于耳中玉境等转换后世界的Clip是否没有现实阶段道具：
- 是否逐分镜锁定角色精确数量；剧情唯一角色是否在正向设计中明确唯一一只/名、前中后景无第二个同类，并预置复制/分身/镜像/背景重复禁令：
- 追逐/战斗/对峙/多人镜头是否锁定前后景、朝向、关系轴、运动方向、正脸许可与同景深许可；追逐是否默认后追前逃并禁止双方并排正对镜头、海报式合影和群像站桩：
- 每个关键道具是否明确当前形态、尺寸、持有者/左右手、是否允许悬浮、转换完成状态与下一镜继承；不同世界形态是否没有混用：
- 现实↔幻想/耳中玉境、地点/时间、尺度或形态转换是否在Prompt前完整定义起点状态、转换媒介、运动方向/过程、终点状态与转场后首个稳定构图：
- 每个适用Clip是否已从首帧到尾帧锁定A/B左右、朝向、关系轴、摄影机轴线侧和Connector，且没有无授权跨轴、换位、双正脸或来源—目标反转：
- 是否满足“来源 Shot 时长求和 = Clip Detail 合计 = Clip Table目标时长 = 平台生成时长”：
- 每个 Clip 的声音是否包含具体环境底声/有意静默和至少一个同步前景声层：
- 每个 Clip 是否有风险降级、稳定尾帧、尾帧用途与下一 Clip Handoff：
- 每个 Clip 是否有明确主导运镜逻辑、逐镜变化、视觉高潮、最克制镜头、重复规避与Seedance复杂度控制：
- 每个 Clip 是否是完整Dramatic Execution Unit；必须连续完成的表演/信息积累没有因技术方便拆断，Camera Continuity / Visual Rhythm具有功能差异：
- 超过4个Shot的Clip是否通常至少有2种不同运镜逻辑；同类主运镜连续3次以上是否具有逐镜叙事理由；是否避免为了多样而强制每镜不同：
- 是否完全未使用Storyboard图片、分镜板、拼图、Scene Top-down Blocking Map或多画面材料作为Clip / STATE-08视觉参考；只有经Before-Single-Clip-Prompt Gate确认、绑定当前Blocking Signature的单Clip `REF-SKETCH`可作为受限例外：
- 每个Clip是否执行Reference Budget Check；≤7未整合、8张且无额外帧需求未整合、9张无未计入连续性需求才直接使用、>9已去重/整合同类非角色信息/按优先级裁剪并最终≤9：
- 是否只列实际存在且已确认资产，没有虚构总设定图/空间关系图/动作关系图；独立资产更清晰且未超限时是否继续使用独立图：
- 是否逐项通过Visual Input Eligibility；纯文字站位/不可换边/人物距离/同坐一张板凳/道具数量/空间关系/行为/禁止项/镜头规则没有伪装成参考资产，并已迁移到`空间关系 / 起始状态 / 道具状态 / 首帧参考 / 尾帧限制 / 反向提示词 / Spatial Blocking Rules`：
- 是否先按当前Clip目标与Continuity Risks完成Reference Selection / Routing；身份/外观、空间结构、道具造型、A/B尾帧、光线/场景状态风险是否路由到正确来源；C是否未引用旧尾帧；是否没有漏选必需项、用途选错或无依据过量引用：
- 当前Clip每个核心角色是否仍保留各自独立三视图/角色锁定图，且没有角色总表或用动作图覆盖外貌基准：
- 是否已锁定 STATE-08 每个 Clip 一条 Prompt、不得按 Shot 拆分：
- Pending / Return Route：
