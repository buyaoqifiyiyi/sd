# Spatial Blocking Layer

## Purpose

Spatial Blocking Layer 用“Scene Spatial Snapshot + Text Spatial Rules + Top-down Blocking Map（按复杂度启用）”在正式 Detailed Shot Design 之前锁定长期场景几何、角色站位、摄影机位置、关系轴、移动路径、关键道具和跨 Clip 边界，减少左右漂移、反轴、无动作换边、瞬移与首尾帧衔接错误。

它是 `STATE-06 Detailed Shot Design` 的前置 / 内部子步骤，不创建新 STATE。STATE-07 必须继承其结果；STATE-09 使用同一结果做 Spatial Continuity QA。它不修改主 Pipeline、Director Decision Layer、Knowledge Application Reflection、现有运镜知识正文、任何 Template 或 STATE-08 Seedance 最终 Schema。

---

## Module Contract

- **Module Name / Type**：Spatial Blocking Layer；STATE-06 前置 / 内部辅助 Knowledge。
- **触发**：每个进入 STATE-06 的 Scene 都执行 Spatial Blocking Decision；只有达到相应复杂度时才启用俯视图。
- **不触发独立图像**：单人无走位、简单双人静态，或经判定仅有受限局部移动且不存在换边 / 越轴 / 多 Clip 风险时，不生成俯视图。
- **所属位置**：`STATE-05 Scene Breakdown → STATE-06 Spatial Blocking Decision（内部）→ Professional Detailed Shot Script → STATE-07 Clip Production`。
- **Required Inputs / 唯一来源**：Scene Breakdown 的场景边界与剧情动作、Active Environment / Character / Prop / FX 版本、Visual Direction、Sequence Plan（如适用）、已确认首尾帧和用户明确确认的空间事实。不得从风格名、运镜偏好或模型猜测新增门窗、家具、路线、人物动作或道具状态。
- **Output**：每个 Scene 一份 `Spatial Blocking Result`，至少包含 Decision、Scene Spatial Snapshot、Structured Blocking Map、Text Spatial Rules、Clip Boundary Spatial Ledger，以及适用时的 Top-down Blocking Map Prompt / 图像。该结构是生产工件，不是新的 Shot、Clip 或 Seedance 输出 Schema。
- **Output Owner / 保存位置**：本 Knowledge 定义判断方法；STATE-06 Workflow 拥有执行与确认。Work/Codex 写入 `<active-project-root>/shots/spatial_blocking/SCENE-xxx_spatial_blocking.md`，图像写入同目录并登记同一 Revision；普通 Chat 保留在当前 STATE-06 Checkpoint 与 Portable State 摘要中。
- **允许读取 / 写入**：只读已确认项目事实与 Active Canonical Assets；只写上述空间调度工件和当前 STATE-06 Checkpoint。Top-down Map 是 Planning Reference，不得登记为 Canonical Character / Environment / Prop / FX Asset，不得进入 STATE-08【参考资产】。
- **下游消费者**：STATE-06 Professional Detailed Shot Script、STATE-07 Clip Production、STATE-09 Review；STATE-08 只能通过 Confirmed Clip Production Plan 接收已投影的空间语义。
- **禁止修改**：剧情事实、资产身份 / Active Version、Scene 目的、正式 SHOT / CLIP 顺序、导演决策、既有运镜原子、Template 字段及 STATE-08 最终 Prompt 结构。
- **冲突路由**：场景结构或剧情动作不清返回 STATE-05；资产空间事实冲突返回对应 STATE-03 资产拥有者；逐镜 Blocking / 轴线 / 移动容量冲突留在 STATE-06；Clip 边界继承错误返回 STATE-07；只发生在 Prompt 转译或生成执行中的偏差返回 STATE-08。
- **Validator 可检查不变量**：每 Scene 有 Decision；复杂度理由明确；双锁场景同时存在 Top-down Map 描述 / 图像和 Text Spatial Rules；所有适用标签齐全；连续 Clip 的 Previous Clip End State 与 Next Clip First Frame Reference 可逐项对照；没有新 STATE、新 ID 命名空间或新 Seedance 字段。

---

## Spatial Blocking Decision

先判断空间复杂度，再选择最小充分锚定方式。不得为了“专业感”无差别生成俯视图，也不得在复杂场景里仅用一段文学描述代替可画出的空间合同。

### Text-Only Allowed

以下场景可只使用 Structured Blocking Map + Text Spatial Rules：

- 单人、无走位；
- 简单双人静态对话；
- 双人仅有受限局部移动，且同时满足：单一连续空间、单镜或单 Clip、无人换边、无越轴、无复杂道具交接、移动起终点可由一个固定地标唯一描述。

选择 Text-Only 时必须写明理由。Text-Only 不是自由散文，仍须完成本文件规定的结构化地图与规则。

### Top-down + Text Recommended

以下情况建议使用俯视图 + 文字双锁：

- 双人有明显走位、距离关系变化或绕过家具 / 门口；
- 同一 Scene 存在多个机位，容易造成左右 / 朝向翻转；
- 同一动作跨多个 Shot 或 Clip；
- 需要精确保持视线、攻击、追逐或道具交接方向。

### Top-down + Text Default

以下任一项成立时，默认优先双锁：

- 3 人以上；
- 打斗、追逐、多人进出场；
- 复杂道具空间，或门窗、桌椅、柱、车辆等障碍参与调度；
- 连续多 Clip；
- 严格 180 度轴线；
- 多条移动路径、来源—路径—目标 Connector，或已有生成结果发生左右翻转 / 瞬移。

用户明确不想生图、当前环境不需生图或图像工具不可用时，不阻塞为独立 STATE：输出完整 Structured Blocking Map + Text Spatial Rules，记录 `Map Mode: Structured Text Fallback` 与原因，并提高 Spatial Continuity Risk。不得声称已经存在俯视图。

---

## Spatial Blocking Result

每个 Scene 使用以下生产结构；它不得成为 Template 的新固定栏目：

```text
Scene ID:
Decision: Text-Only / Top-down + Text Recommended / Top-down + Text Default
Decision Factors:
Map Mode: Structured Text / Prompt Awaiting Confirmation / Generated Top-down Map / Structured Text Fallback
Source Facts And Revision:
Coordinate Convention:
Scene Spatial Snapshot:
Structured Blocking Map:
Text Spatial Rules:
Clip Boundary Spatial Ledger:
Spatial Risks / Downgrade:
Status: Draft / Prompt Awaiting Confirmation / Confirmed
```

### Coordinate Convention

俯视图和文字地图必须使用同一方向约定，例如：`图上方 = 场景北；图下方 = 场景南；摄影机朝向用箭头；人物面向与移动路径分别标记`。`画面左 / 右`一律以观众观看当前已命名 Camera View 的屏幕左 / 右为准；它是该机位投影结果，不能与场景东 / 西或角色自身左 / 右混写。任何左右规则都必须绑定 C1 / C2 / C3 或明确的建立镜头，不能把一个机位的屏幕左右误当成全场绝对方位。

### Scene Spatial Snapshot

Scene Spatial Snapshot 是同一连续 Scene 的长期几何骨架，至少记录：

- **Absolute Screen Direction**：所有画面左 / 右绑定已命名Camera View并以观众视角解释；
- 场景边界、可通行区与高低关系；
- 门、窗、桌、椅、柱、楼梯、车辆、主要道具等 Fixed Environment Anchors；
- Character Start Positions、身体Facing与Eyeline；
- Interaction / Eyeline / Action Axis；
- 当前 Camera Safe Side 与已建立屏幕左右关系；
- **Legal Axis-Crossing Methods**：当前空间允许的中性机位、可见摄影机路径、角色换位或插入隔离后新建立镜方案；
- **Movement Path Memory**：每名移动角色和关键道具的`Start Position → Visible Path → End Position`、转向点、停顿点与不可穿越区。

场景结构身份与人物临时站位必须分离。Active Environment Canonical Reference拥有空间身份、固定结构、材质与长期视觉基线；Scene Spatial Snapshot把这些已确认事实组织成可执行几何，但不重做环境资产。人物在同一空间内换位、移动或改变姿态时，更新的是Structured Blocking Map、Shot-State Memory或Clip End-State，不得仅因临时站位变化重做Environment Asset。只有场景固定结构、空间区域或长期环境状态发生已授权实质变化时，才返回相应事实/资产拥有者判断是否需要新版本或状态资产。

### Structured Blocking Map

无论是否生图，至少逐项标注；确实不适用时写 `N/A + 理由`：

1. 场景边界与可通行区域；
2. 门、窗、桌、椅、柱及关键道具位置；
3. 角色 A / B / C 的起点与终点；
4. 每名移动角色的连续轨迹、转向点、停顿点与不可穿越区域；
5. 摄影机 C1 / C2 / C3 的位置、机位高度 / 侧位、朝向与覆盖范围；
6. 180 度关系轴、主运动轴或主攻击轴，以及各摄影机所在轴线侧；
7. 关键视线、攻击、武器、追逐、交接或能量的来源 → 路径 → 目标；
8. 每个 Clip 首帧站位；
9. 每个 Clip 尾帧站位，以及可否作为下一 Clip 直接首帧、仅连续性参考或不继承。

### Text Spatial Rules

至少包含：

- 每个适用机位下角色的画面左 / 右、前 / 后、高 / 低关系；
- 每名角色的身体面对方向、侧身程度与视线目标；
- 移动方向、起点、路径、终点、触发和停顿；
- 谁移动、谁不动；
- 未经明确动作过程不得换边、穿越、瞬移或交换前后层级；
- 摄影机不得越过哪条 180 度轴线；有意越轴时必须记录已建立轴线、合法过渡与稳定新轴线侧。合法方式至少包括：沿轴线的中性镜头、观众可见的摄影机跨轴移动、角色在镜内明确换位后重建关系，或用特写 / 插入镜头隔离后以建立镜明确建立新轴线。插入镜头本身不能自动使随机反转合法；越轴前后仍须用固定地标、视线或动作方向让变化可感知、可解释、可连续；
- 关键道具的位置、朝向、持有者、交接过程与结束状态；
- `Previous Clip End State → Next Clip First Frame Reference`：连续边界逐项继承人物位置 / 朝向 / 视线 / 动作结果 / 道具 / 摄影机轴线侧；机位或景别有动机变化时标记 Reference-Only；已确认叙事断点标记 Not Inherited 并写明重建依据。

### Pose Hierarchy / Relationship Topology / Delta Blocking

人物姿态按以下层级记录与继承：

`Position → Torso Orientation → Shoulder Orientation → Head Orientation → Gaze Direction`

上层状态默认锁定并向下游继承；只有当前 Shot / Clip 明确授权的层级可以变化。`A看向B`不能自动解释为全身转向：若授权仅为`Gaze + LIMITED Head`，则Position、Torso、Shoulder与人物距离保持不变。手部或道具动作同样不能无依据带动躯干、座位或人物距离变化。

Relationship Topology除左右 / 前后外，按适用性记录`Side-by-side / Face-to-face / Back-to-back / Shared Facing / Same Seat or Bench / Distance / Eye Contact`。左右未交换但`Side-by-side → Face-to-face`、共同朝向变为相向、同座关系被拆开或人物距离发生无授权变化，仍属于Blocking Drift。

连续状态按Delta更新：

`Previous Blocking State + Current Shot Delta = Current Blocking State`

不得在每个连续Shot重新猜测或重建全部Blocking。Structured Blocking Map、Shot-State Memory与Clip End-State只更新当前明确发生的Position / Facing / Topology / Distance / Movement Path变化；未授权层级继续继承。

---

## Top-down Blocking Map Prompt Gate

当 Decision 为 `Top-down + Text Recommended / Default` 且当前环境支持图像生成时：

1. 先输出完整可执行的 Top-down Blocking Map Prompt；
2. 把 STATE-06 保持 `IN_PROGRESS`，记录 `Map Mode: Prompt Awaiting Confirmation`；
3. 等待用户确认当前 Prompt Revision；
4. 确认后才调用图像生成；
5. 生成图必须与 Structured Blocking Map 和 Text Spatial Rules 逐项对照，标签缺失、方向冲突或路径不可读时不得作为 Confirmed Blocking Map，先最小修正或回退 Structured Text。

用户已明确表示不需要 / 不想生成图时，跳过等待，直接使用 Structured Text Fallback。不得把 Blocking Map 误当 Storyboard、美术图、Canonical Asset 或视频视觉参考。

Prompt 至少要求：正交俯视平面图、非透视、清楚边界、统一方向标、门窗 / 家具 / 柱 / 道具标签、角色 A/B/C 起终点、颜色区分的连续路径与箭头、摄影机 C1/C2/C3 位置 / 朝向 / 视锥、180 度轴线、关键视线 / Connector、Clip 首尾帧标记、高对比可读排版、无人物写实渲染、无电影海报化、无装饰性元素。

---

## Projection Rules

- **STATE-06**：把 Confirmed Spatial Blocking Result 投影到现有 `场景 / 美术`、`画面内容 / 构图`、`人物动作`、`摄影机 / 镜头`、`镜头调度`、`画面特效 / 转场`、`AI制作备注`与`素材 / 资产`语义中；Blocking Map 本身不列入视频参考资产。
- **STATE-07**：不得重新设计 Blocking。每个 Clip 的起始状态、空间关系、摄影机与构图路径、道具连续性、结尾状态、尾帧用途和 Cross-Clip Continuity Ledger 必须读取同一结果。Continuous Handoff 强制 `Previous Clip End State = Next Clip First Frame Reference`；任何差异都必须来自可见动作过程或已确认断点。
- **STATE-09**：将 Text Spatial Rules、Top-down Map（如有）、Detailed Shot Design、Clip Plan、STATE-08 Prompt 与生成结果逐项比对；空间设计缺失返回 STATE-06，Clip 继承组织错误返回 STATE-07，仅 Prompt / 生成执行偏差返回 STATE-08。

职责分层固定为：`Scene Spatial Snapshot = 长期场景几何骨架`；`Shot-State Memory / Clip End-State Record = 当前局部站位、朝向、动作与道具状态`；`Accepted Canon State = 用户已接受 Take 的可观察瞬时事实`；`REF-TAIL = A/B需要时的瞬时视觉承接`；`Confirmed Visual Blocking Anchor = 单个Clip经门控确认的Position / Facing / Distance / Topology / Axis / Camera / Pose / Gaze / Action Path视觉执行锚点`。Scene级Top-down Blocking Map仍只是Planning Reference，不得进入STATE-08；只有按`knowledge/clip_preflight_check.md`生成、验证并确认的单Clip Visual Blocking Sketch才可进入该Clip参考资产。Reference Selection / Routing继续按当前风险选择最小充分来源，不能让REF-TAIL、Visual Blocking Anchor或人物临时站位覆盖Environment Canonical的空间身份，也不能让环境资产图替代当前局部Blocking。

---

## Minimum Validation Examples

### Example A｜双人有走位但可 Text-Only

单镜 / 单 Clip 的办公室对话：A 从门边向桌侧移动一步把文件放下，B 始终坐在桌后；A 不绕桌、不跨过 B、不换边，摄影机固定在 A—B 轴线南侧，文件从 A 右手落到桌面北侧标记点。判定为 `Text-Only Allowed`，因为移动受限、起终点唯一、无跨 Clip 与换边风险；仍需结构化写出门、桌、A/B 起终点、固定 C1、轴线、文件状态和首尾帧。

若 A 需要绕桌走到 B 身后、机位在 C1/C2 间切换或动作跨 Clip，则升级为 `Top-down + Text Recommended`。

### Example B｜三人复杂场景使用双锁

仓库内 A 追逐 B，C 从侧门进入并截断路线；空间包含货架、柱、两扇门和手提箱，道具在 B → C 间交接，动作跨两个 Clip，C1/C2/C3 必须保持同一主轴侧。命中 `3 人以上 + 追逐 + 多人进场 + 复杂障碍 / 道具 + 连续多 Clip + 严格轴线`，判定为 `Top-down + Text Default`。俯视图锁定三人路径、摄影机视锥和轴线；文字规则锁定谁移动 / 谁不动、交接过程、不可换边、尾帧到下一首帧继承。
