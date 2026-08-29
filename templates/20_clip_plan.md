# Clip Plan

- Project ID：
- Status：Planning / Confirmed
- Source Detailed Shot Design Artifact / Portable Checkpoint：
- Source Detailed Shot Design Status：Confirmed
- Source Detailed Shot Design Revision：
- Model Duration Window：4—15秒
- Total Formal Shots：
- Total Clips：
- Unit Rule：Shot = 导演镜头设计单位；Clip = AI视频生成执行单位；每个Shot且仅进入一个Clip；Total Clips ≤ Total Formal Shots；STATE-08每个Clip只生成一条连续Prompt
- Namespace Rule：Source Script Label ≠ SCENE ≠ UNIT ≠ SHOT ≠ CLIP；只有Confirmed Detailed Shot Design中的正式SHOT可进入Clip

## Clip Table

| Clip ID | 包含 Shot（原顺序） | 目标时长 | 生成方式 | 组织依据 | 起始状态 | 结尾状态/尾帧 | 下一Clip连接 |
|---|---|---:|---|---|---|---|---|
| CLIP-001 | SHOT-001 / SHOT-001 + SHOT-002 | 10秒 | 单Shot Clip / 多Shot单次连续生成 | 场景、时间、动作、摄影机、空间、道具、复杂度与时长判断 |  | 保存为[G01尾帧] | 直接起始帧继承 / 仅连续性参考 / 不继承（原因） |

## Clip Detail Cards

### CLIP-001

- 包含 Shot：按 SHOT ID 原顺序逐项列出
- 目标时长：N秒（必须4—15秒）
- 时长核算：SHOT-001=N秒 + SHOT-002=N秒；合计=N秒；平台生成时长=N秒
- 组织理由：逐项说明场景连续性、时间连续性、人物动作连续性、摄影机连续性、模型执行复杂度与单次生成时长判断
- 生成合同：本 Clip 对应一次生成；即使包含多个 Shot，STATE-08 也只输出一条连续 Prompt，不按 Shot 拆分
- 起始状态：人物、环境、空间、道具、FX、情绪、摄影机及来源边界
- Clip Preflight Check（STATE-07前置版；必须先于Reference Budget）：
  - Temporal / Spatial Continuity Classification：视觉连续 / 剧情连续 / 主动切场或切世界（三选一）；判定证据；上一尾帧是否允许正式引用；首帧重建依据
  - World-State Map（逐分镜）：当前现实 / 幻想 / 耳中玉境 / 其他已确认层；Pre/Post Transition阶段；实际角色、环境、道具、FX；不适用资产删除结果
  - Character Count Lock（逐分镜）：角色身份 × 精确数量；唯一角色的正向唯一性与前/中/背景无第二个同类锁；复制/分身/镜像/背景重复风险
  - Spatial Composition Lock：前后景、左右、朝向、视线、关系轴、摄影机轴线侧、追逃/攻击/视线路线、正脸/侧背/背身许可、同一景深许可；追逐默认后追前逃并禁止并排合影
  - Prop State Check（逐关键道具）：当前形态、尺寸、持有者/左右手、位置、方向、是否允许悬浮、转换是否完成、结尾状态与下一镜继承
  - Transition Check（适用时）：起点状态；转换媒介；运动方向/过程；终点状态；转场后首个稳定构图；不适用时写明理由
  - Reference Asset Check：只列当前World-State实际存在/出场/使用且Confirmed的候选；角色独立图优先；剧情连续/主动切场不机械计入上一尾帧；再进入Reference Budget
  - Preflight Result：PASS / FAIL；Affected Clip / Shot；Return Route；修正后重跑结果
- 连续动作：按 Shot 顺序描述动作、表演、情绪与必要镜头阶段如何连续执行
- 摄影机与构图路径：机位、轴线侧、景别/视点变化、主要运镜、焦段/对焦、稳定降级
- Clip Movement Plan：
  - 主导镜头语言与叙事理由：
  - 镜头间运镜变化（按Shot列出主运镜 / Static、变化触发、叙事功能、与前镜关系、终点）：
  - 视觉高潮镜头及理由；无独立高潮时写“保持克制”：
  - 最克制镜头及理由：
  - 重复规避（连续同类主运镜扫描；3次以上逐镜理由；超过4个Shot时的运镜逻辑数量与例外理由）：
  - Seedance复杂度控制（逐镜稳定等级、Clip峰值、同时负荷、删辅助 / 降速 / 缩短路径 / 固定机位 / 拆分降级）：
- 空间关系：人物A/B左右/前后/高低、分别朝左/朝右与侧身程度、视线目标、距离、行进方向、环境锚点和180度轴线；战斗/双主体/对峙/对话/追逐/相向运动必须写唯一关系轴或主攻击/运动轴
- 空间连线（适用时）：视线 / 武器 / 攻击 / 追逐路线 / 水流 / 能量 / 抛射物的来源 → 路径 → 目标；必须与人物朝向、喷口/武器方向、屏幕方向和受击位置一致
- 同框面部与机位限制（适用时）：双方相对时禁止同时完整正脸；优先固定侧面、侧后双人或OTS；有意越轴必须有已建立轴线、可见路径/中性机位、地标与稳定新轴线侧
- 道具连续性：身份、持有者、位置、方向、状态、变化过程与结尾状态
- 光影/色彩/FX连续性：
- 声音连续性：环境底声/空间底噪；同步动作声、Foley、呼吸、对白或剧情内声源；声音尾部与下一Clip承接
- 结尾状态：人物、动作、情绪、空间、道具、环境、光态、摄影机与稳定停留点
- 结尾帧限制：保存为[G01尾帧]
- 尾帧用途判定：直接作为下一Clip起始帧 / 仅作为下一Clip连续性参考 / 不继承（原因） / 最终收束
- 下一Clip Handoff：
- 模型执行风险与安全降级：
- Reference Budget Audit：
  - 原始候选图片资产（逐项写实际资产ID/名称、Active/Confirmed状态、真实文件/受控ID、当前Clip用途、图片位数）：
  - 删除的当前Clip无关项（未出场角色 / 未使用环境 / 未使用道具 / 未使用动作图 / 其他）及理由：
  - 去重结果（重复文件或未增加信息项；不得把不同核心角色图当作重复）：
  - 连续性图片位（Direct / Reference-Only上一Clip尾帧、当前首帧或其他合法帧；待加入与已加入分别列出）：
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
| CLIP-001 | CLIP-002 | Continuous Handoff / Motivated Discontinuity |  |  |  | Direct / Reference-Only / Not Inherited |  |  |  |

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
| CLIP-001 | 视觉连续 / 剧情连续 / 主动切场或切世界 | Direct / Reference-Only / No Formal Tail Reference | PASS / Affected Shot | PASS / Affected Shot | PASS / Affected Shot | PASS / Affected Shot | PASS / N/A / Affected Shot | PASS ≤9 / Affected Asset | PASS / Return Route |

## Coverage And Validation

- 所有正式 Shot 是否按原顺序出现且只分配到一个 Clip：
- 每个 Clip 是否包含一个或多个相邻 Shot，且总时长为4—15秒：
- 所有多 Shot Clip 是否通过场景、时间、人物动作、摄影机、空间、道具、资产、复杂度与时长检查：
- 短于4秒的 Shot 是否只在兼容的4—15秒 Clip中执行；超过15秒的 Shot 是否已返回 STATE-06 拆分：
- 每个 Clip 是否具有起始状态、连续动作、空间关系、道具连续性与结尾状态：
- 每个Clip是否先通过Clip Preflight；Continuity Classification是否三选一，且只有视觉连续正式引用上一尾帧，剧情连续或主动切场/切世界从当前Scene、World-State和Start Boundary重建：
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
- 超过4个Shot的Clip是否通常至少有2种不同运镜逻辑；同类主运镜连续3次以上是否具有逐镜叙事理由；是否避免为了多样而强制每镜不同：
- 是否完全未使用 Storyboard 图片、线稿、分镜板、拼图或多画面材料作为 Clip / STATE-08 视觉参考：
- 每个Clip是否执行Reference Budget Check；≤7未整合、8张且无额外帧需求未整合、9张无未计入连续性需求才直接使用、>9已去重/整合同类非角色信息/按优先级裁剪并最终≤9：
- 是否只列实际存在且已确认资产，没有虚构总设定图/空间关系图/动作关系图；独立资产更清晰且未超限时是否继续使用独立图：
- 当前Clip每个核心角色是否仍保留各自独立三视图/角色锁定图，且没有角色总表或用动作图覆盖外貌基准：
- 是否已锁定 STATE-08 每个 Clip 一条 Prompt、不得按 Shot 拆分：
- Pending / Return Route：
