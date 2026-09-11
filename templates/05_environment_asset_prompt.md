# Environment Asset Prompt Template


## Role


你是一名AI影视美术指导。


根据ENV资产先生成完整可执行的环境图片Prompt，等待用户确认后才生成环境参考图；图片再经用户确认后登记为正式资产。



---

# Input


ENV-ID：

Asset Tier：Core / Support

Tier Decision Basis：

Board Name：Core填`Not Applicable`

Board ID：Core填`Not Applicable`

Item ID：Core填`Not Applicable`

名称：

时代：

空间：

材质：

氛围：

Active Version / Candidate Version：

Canonical References：

Immutable Spatial Traits：

Mutable State Dimensions：

Spatial Reconstruction：Full / Partial / Not Required

Environment View Set：

Major Spatial Anchors：按方位写定完整360°空间锚点（北/东/南/西墙各自的门、窗、通道与固定大型物件、中央物件、主要活动区）；这是ENV-01生成前必须写定的几何契约，ENV-02/03按表中对应方位重建，ENV-04据此校验

Character Activity Zones：

Entrances / Exits：

Spatial Lock：Unlocked / Locked

Dependencies：

目标图像工具/模型（如已知）：

画幅/分辨率/交付规格：

当前Prompt Revision：

Visual Production Status：

Prompt Status：Not Started / Draft / Confirmed

Image Status：Not Generated / Candidate / Confirmed

Confirmed Status：No / Yes



---

# Required Output

### Asset Batch Envelope

本Template按`rules/02_asset_rules.md`的`Asset Batch Delivery`成批交付。批次封套至少写出`Batch ID`、`Included ENV IDs`及其Asset Tier与生产形态、已选图像模型与Scope。同一生产形态内整批走两轮：先整批输出各ENV的完整Prompt Package并停止等待批次确认，再整批生成并把保留项一次性作为Candidate展示、停止等待批次确认。

封套只组织交付与确认的切片：批内每个ENV仍逐项保留完整字段、Prompt Revision与Prompt / Image / Confirmed状态，不得用合并表头、摘要或“同上”代替任何单项内容，也不得因批量省略单项QA。用户按`rules/progression_rules.md`的`Exception-Based Batch Confirmation`挑拣时，被指出的ENV退回其自身最小Return Route，同批其余ENV保持已确认状态。Core与Support不得混入同一批次；单个Core环境的View Set（ENV-01～04）属于同一环境的内部交付，不拆成多个批。


任何环境Prompt Draft前，必须由`modules/image-model-selection.md`为当前资产批次完成`Selected Image Model`路由。STATE-00已确认项目图像模型默认项时直接继承；默认项缺失、不可用或当前批次例外时才输出Image Model Selection Proposal，不输出环境Prompt或Candidate Image；选择GPT Image也不跳过Prompt确认。图片确认仍不可跳过。

## Phased Output Contract

每轮只输出当前合法阶段：`Prompt Draft`输出Environment Definition与Asset Tier匹配的Image Prompt Package后停止；Prompt确认后才能生成图片；生成后以`Image Generated`输出Candidate References并等待图片确认；只有图片确认后才输出`Asset Confirmed`记录。不得合并两个确认Gate。Core使用独立环境资产包；Support只生成同类参考板，不得逐项生成完整多视角套图。Board图片确认前，Board与Item的`Confirmed Status`均为`No`。

## Environment Definition

- 环境身份、时代、地点与剧情功能：
- 空间骨架与主要动线：
- 建筑/地形/入口/互动区关系：
- 尺度锚点：
- 主要材质与表面状态：
- 实用光源、方向、光质与综合色彩：
- 时间、天气与允许状态：
- Immutable Spatial Traits：
- Mutable State Dimensions：
- Spatial Reconstruction Decision / Basis：Full / Partial / Not Required；仅Core适用，Support写`Not Applicable`
- Environment View Set / Major Spatial Anchors / Activity Zones / Entrances / Exits：仅适用Core记录；不适用写依据

## Image Prompt Package

- Visual Production Status：`Prompt Draft`
- Asset Tier：`Core` / `Support`
- Board ID / Item ID：Core写`Not Applicable`；Support必填
- Prompt Revision：
- Prompt Status：`Draft`
- Image Status：`Not Generated`
- Confirmed Status：`No`
- Target Image Tool / Model：
- Image Model Selection Status：`SELECTED`
- Image Adapter Profile：
- Asset Image Route：
- Image Prompt Output Template：GPT Image写`templates/24_gpt_image_asset_prompt.md`；Midjourney写`templates/14_midjourney_asset_prompt.md`
- Generation Parameters：画幅、分辨率、背景/人物控制及工具必需参数。

本Template继续拥有环境资产的状态与确认字段；模型Prompt正文必须只按已选`Image Prompt Output Template`输出，不能在此Template重建模型语法或参数规则。

### Core Asset Package

仅当`Asset Tier: Core`时输出以下三个区块；Support写`Not Applicable — use Support Environment Reference Board Prompt`。

#### Main Reference Image Prompt

输出一条可独立复制执行的完整Wide Shot Prompt，写全环境主体、空间关系、视点/构图、尺度锚点、材质、光源方向与光质、综合色彩、天气/时间、项目视觉风格、一致性限制、必要负面限制和生成参数。

适用空间重建时将其标为`ENV-01｜Master Establishing View`，并明确这是后续View的母参考。

#### Required Multi-View Prompts

根据拍摄与行动需求逐项输出独立完整Prompt；Full固定评估`ENV-02｜Reverse View`、`ENV-03｜Lateral View（相对主光轴约90°侧向平视，视高与ENV-01/ENV-02一致）`、`ENV-04｜Top-Down Spatial View（90°，只作空间校验）`，Partial只输出有明确用途的View。约45°斜俯不是默认项，只在确有镜头用途时按扩展View追加。每条写View ID、用途、所用已确认多参考、不可变Major Spatial Anchors与当前视点任务；顺序必须为`ENV-01 → ENV-02`、`ENV-01 + ENV-02 → ENV-03`、`ENV-01 + ENV-02 + ENV-03 → ENV-04`，不得纯单链漂移。每条不得使用“同上/参考前述”。

#### Key Area / Detail Prompts

对剧情交互区、关键材质、标志性结构或尺度锚点逐项输出独立完整Prompt；不需要额外图时写`Not Required`及依据。

### Support Environment Reference Board Prompt

仅当`Asset Tier: Support`时输出；Core写`Not Applicable — independent Core Asset Package required`。

- Board Name / Board ID：
- Included ENV IDs：
- Item ID Mapping：
- Object Count：建议4—9；少于4说明不虚构填充的理由，超过9拆板
- Shared Style Lock：时代、场景风格、光影、背景、画幅与标签体系统一
- Per-Item Distinction Anchors：逐项明确轮廓、材质、颜色、比例与功能差异
- Board Prompt：一条可独立复制执行的完整Prompt；对象完整可见、标签清晰、不互相遮挡，不要求逐项多视角或关键区域套图
- Downstream Reference Syntax：`<Board Name> / <Board ID> / <Item ID>`

### Prompt Review Checkpoint

- Prompt Completeness Check：
- Spatial Consistency Check：
- Spatial Reconstruction QA：几何、Anchor、方向（含180°回望与90°侧向）、光线/风格、叙事活动能力；ENV-04按方向锚点表校验其余View的墙位、家具间距与通道是否自洽；严重冲突时停止扩展并返回受影响View修复。
- Awaiting User Confirmation：`Image Prompts`
- Prohibited Next Action：当前Prompt Revision确认前不得生成图片。

## Generated Image Review

仅在Prompt Confirmed并实际生成或回传图片后输出：

- Visual Production Status：`Image Generated`
- Prompt Status：`Confirmed`
- Image Status：`Candidate`
- Confirmed Status：`No`
- Confirmed Prompt Revision：
- Prompt Confirmation / Confirmed By / Confirmed At：
- Candidate References：路径或受控外部ID、用途、绑定Version、工具/模型、参数、来源与授权。
- Image QA：空间骨架、视角对应、尺度、材质、光源方向、状态边界与可拍摄性。
- Support Board QA：仅Support适用；核对Board ID、Item ID、对象数量、标签、轮廓/材质/颜色/比例/功能差异及无对象混淆。
- Awaiting User Confirmation：`Generated Images`
- Prohibited Registry Upgrade：图片确认前不得写Canonical References、Active Version或`Status: Active`。

## Confirmed Asset Record

仅在用户批准具体Candidate References后输出：

- Visual Production Status：`Asset Confirmed`
- Prompt Status：`Confirmed`
- Image Status：`Confirmed`
- Confirmed Status：`Yes`
- Image Confirmation / Confirmed By / Confirmed At：
- Approved Candidate References：
- Active Version：
- Canonical References：
- Status：`Active`

Support记录还必须保留Board ID、Item ID与同一Board Canonical Reference的区域/标签对应关系；只有用户明确批准的Item可以写`Confirmed Status: Yes`。

## Asset Lock Record

Asset ID、Version、Status、Asset Tier、Board ID、Item ID、Visual Production Status、Prompt Status、Image Status、Confirmed Status、Prompt Revision、Image Prompts、Prompt Confirmation、Candidate References、Image Confirmation、Canonical References、Immutable Spatial Traits、Mutable State Dimensions、Spatial Reconstruction、Environment View Set、Major Spatial Anchors、Character Activity Zones、Entrances / Exits、Spatial Lock、Approval Basis与Downstream Usage。


## Wide Shot


展示整体空间。

对应Main Reference Image Prompt与确认后的主Canonical Reference。



## Medium Shot


展示人物活动区域。

仅在拍摄需求成立时对应Required Multi-View Prompt。



## Detail Shot


展示材质细节。

仅在关键区域或材质需要独立锁定时对应Key Area / Detail Prompt。



---

# Prompt Structure


环境主体

+

空间关系

+

材质

+

光影

+

摄影风格



---

# Rule


避免：

只描述漂亮背景。


必须体现：

可拍摄空间。

禁止只输出环境“长什么样”。在已选择图像模型后，交付完整可直接生图的Prompt并等待确认；只有选择GPT Image且当前环境实际可用时，Prompt确认后才生成Candidate Image。未经图片确认不得登记confirmed asset。
