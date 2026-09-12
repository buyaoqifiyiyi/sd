# Environment Multi-View Reconstruction / 环境多视角空间重建

# Read Scope

本文件被多个阶段复用，**不得整文件通读**：按当前事项只读对应小节。

| 当前事项 | 只读 |
|---|---|
| 判定是否建立空间重建 | `## Contract`、`## Reconstruction Decision And View Set` |
| 写方向锚点 | `## Direction Anchor Contract｜方向锚点契约` |
| 多参考约束 | `## Multi-Reference Constraint Rule` |
| 空间真相、Spatial Lock 与 Revision | `## Spatial Truth, Spatial Lock And Revision` |
| 空间一致性校验 | `## Spatial Consistency Check` |
| 下游继承与参考路由 | `## Downstream Inheritance And Reference Routing` |

---

## Contract

- **Type**：STATE-03 Environment Asset 的辅助 Knowledge；不是新模块、STATE、Registry 或最终 Prompt Schema。
- **Trigger**：Core ENV 先作 `Spatial Reconstruction: Full / Partial / Not Required` 判断。多个镜头、约10–15秒以上、走位/复杂动作、反打、多摄影机方向、进出场、重复使用、叙事核心地点或空间关系影响叙事时，通常为 `Full`；一闪而过、单一特写、无空间运动、单镜或虚化背景通常为 `Partial` 或 `Not Required`。
- **Inputs**：STATE-02 Asset Tiering / Dramatic Function、已确认剧本与Director Intent、当前ENV Candidate或Active Version、镜头与行动需求。不能从风格词、故事板、Blocking Map或模型猜测补写建筑事实。
- **Output owner**：STATE-03 `workflows/05_environment_asset_workflow.md` 与其既有环境资产模板、Asset Registry、Canonical Reference和Version协议。本文只定义判断与一致性方法。
- **Consumers**：STATE-06 Spatial Blocking / Detailed Shot Design、Optional Storyboard、STATE-07 Clip Production、STATE-08 Projection / Video Generation、STATE-09 Review。
- **Forbidden**：不创建真实3D/CAD承诺；不替代Spatial Blocking的角色站位、路径、轴线或单Clip Blocking Authority；不让Storyboard、STATE-06 Planning Map或纯文字成为Canonical环境图或视频参考。

## Reconstruction Decision And View Set

这是为固定场景建立的 **Pseudo-3D Spatial Reference**，以最少充分的已确认环境视角形成可继承的隐式三维空间；不是所有ENV都必须有四图。

`Full`的基础View Set如下。`Partial`只生成实际需要的连续子集，且至少保留`ENV-01`；`Not Required`在Registry说明原因，不虚构View。

| View | Semantic responsibility | Must establish |
|---|---|---|
| `ENV-01` Master Establishing View | 最高优先级母参考，位于主光轴方向的平视 | 美术风格、空间尺度、结构、墙/门/窗、大型家具/固定物、主光方向、材质、色彩、时间/天气与主要视觉特征 |
| `ENV-02` Reverse View | 相对ENV-01约180°的回望平视补全 | 同一真实空间的背向区域、门窗/家具/材质/光线逻辑；不得生成风格相似但结构不同的房间 |
| `ENV-03` Lateral View | 相对ENV-01主光轴约90°的侧向平视，视高与ENV-01/ENV-02一致 | 侧墙结构与纵深、侧面门窗/家具、通道宽窄、并排两人或多人可用的横向空间；不得生成风格相似但结构不同的房间 |
| `ENV-04` Top-Down Spatial View | 90°正俯视的环境Canonical布局视角；只作空间校验用途 | 墙、门、窗、大型家具、固定道具、通道、活动范围与可用摄影机区域；不要求CAD精度 |

仅在镜头、进出口、关键物件区或活动区确有具体用途时，才可追加`ENV-05+`（例如Oblique Overhead（约30°–60°斜俯）/ Opposite Lateral / Entrance / Exit / Activity Zone / Key Object Area）。约45°斜俯由默认必出项降为按需扩展：它同时携带空间与视点信息，作为画面参考时最易把下游机位带高。数量本身不是价值。

## Direction Anchor Contract｜方向锚点契约

单一视角只能表达一个视锥，无法完整表达360°空间；背向与侧向区域在`ENV-01`中根本不存在信息，若仅以“看图模仿”补全，模型只能虚构，而虚构结果会直接成为Canonical Reference。因此在生成`ENV-01`**之前**，必须先按方位写定完整空间锚点表：北墙/东墙/南墙/西墙各自的门、窗、通道与固定大型物件，中央物件，以及主要活动区。

- 该表就是`Major Spatial Anchors`的事前写法，不新增Registry字段、不新增确认Gate、不改变双确认闭环。
- `ENV-01`、`ENV-02`、`ENV-03`各自按表中对应方位重建，不得以另一张图的可见区域外推盲区。
- `ENV-04`按该表校验其余View：墙位、家具间距、通道与活动区是否自洽。
- 表中未写定的大型结构不得在任一View中首次出现；确需新增时按Spatial Revision处理。

## Multi-Reference Constraint Rule

禁止默认串行漂移：不得以`ENV-02 → ENV-03 → ENV-04`的单一上代图作为后续唯一约束。每一步先完成现有双确认和空间检查，再使用以下累积的已确认输入：

```text
ENV-01 → ENV-02
ENV-01 + ENV-02 → ENV-03
ENV-01 + ENV-02 + ENV-03 → ENV-04
```

`ENV-01`始终保留母参考。后续图的Prompt必须写明使用哪些已确认Canonical环境View、当前View的几何任务和不可改变的Major Spatial Anchors；不能只写“保持同风格”。出现严重冲突时，停止扩展，不继续生更多View，先修复冲突的Candidate或走Revision。

## Spatial Truth, Spatial Lock And Revision

**Spatial Truth**是环境长期固定事实：场地/房间形状、墙体、门窗、固定大型家具/物件、主要通道、重要距离与可活动范围。**Shot Composition**仅是某镜的焦段、景别、摄影机位置/方向/高度、人物临时站位、前景、景深与构图；它可变化，但不得改写Spatial Truth。

Registry中对符合本方法的Core ENV记录以下环境资产事实（由`references/asset_lock_contract.md`拥有）：

```text
Spatial Reconstruction: Full / Partial / Not Required
Environment View Set: ENV-01 ... ENV-04 / applicable extensions
Major Spatial Anchors: ...
Character Activity Zones: ...
Entrances / Exits: ...
Spatial Lock: Unlocked / Locked
```

`Spatial Lock: Locked`只在所需View经用户图片确认、通过下述检查并成为同一Active ENV Version的Canonical References后成立。它优先于Storyboard和Shot Composition，服从`ENV-01 → verified layout → ENV-02/03/04 → Storyboard → Shot Composition → model freedom`。轻微透视、非关键杂物和不可见区的合理补全可以变化；门、窗、楼梯、床、桌、钢琴、电梯、柱、走廊、入口/出口或其他叙事相关大型物体等**Major Spatial Anchors**不得变化。

导演要求改变Spatial Truth时，必须显式作为 **Spatial Revision** 走`references/asset_lock_contract.md`的Change Protocol：STATE-03创建Candidate ENV Version、更新受影响View并重新双确认；仅使依赖该空间事实的Storyboard、STATE-06 Blocking / Shot、STATE-07 Clip、STATE-08 Prompt及Review产物进入复核。临时人物站位、镜头构图或非关键装饰变化不触发Spatial Revision。

## Spatial Consistency Check

在每个候选View和锁定前，逐项检查：

1. **Geometry**：比例、墙体、空间边界没有明显冲突；
2. **Anchors**：门窗、大型家具、固定物与Major Spatial Anchors一致；
3. **Direction**：左右/前后关系可回查，ENV-02符合反向回望逻辑；
4. **Lighting / Style**：主光方向、材质、年代、美术与时间/天气状态连续；
5. **Narrative use**：空间可支持已确认的进出、走位、动作和镜头需求。

本检查不要求像素一致或CAD精度；严重冲突不得以“导演式补全”掩盖。

## Downstream Inheritance And Reference Routing

先锁空间、后植入角色：`Environment Master → applicable Multi-View Reconstruction → Spatial Lock → Character Asset / Blocking → Storyboard → Shot → Clip → Video Generation`。未锁定环境不得被大量人物镜头反向定义。

- Storyboard和STATE-06读取Active ENV Version、Spatial Lock、适用View Set、Major Spatial Anchors和活动区；每镜把ENV、Camera Zone / Direction、人物位置/朝向、关键背景结构及与上一镜的空间关系投影到既有字段。STATE-06仍拥有当下站位、路径、轴线与Planning Map。
- STATE-07/08在当前Clip实际方向、景别、活动区、背景结构与连续性风险下，从已确认View Set选择**最相关2–4张**真实环境Canonical References：通常保留ENV-01作整体母参考，并按需加入反打朝向的ENV-02、侧向朝向与横向可用宽度的ENV-03或有明确用途的Extension；再按既有规则加入角色、道具和A/B尾帧。`ENV-04`默认不进入画面参考位——它的职责是按方位校验其余View的几何自洽，只在当前Clip摄影机高度确实落在高位俯视区间时才可入选。不是把四图机械全投喂。
- 每张入选环境图按`references/asset_lock_contract.md`的Primary Responsibility声明其解决的空间/布局/朝向/材质或状态风险；文字Spatial Truth和STATE-06 Planning Map仍不进入`参考资产：`。
