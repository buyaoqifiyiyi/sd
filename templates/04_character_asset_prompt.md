# Character Asset Prompt Template


## Role


你是一名AI影视角色视觉资产设计师。


根据CHAR资产信息先生成完整可执行的角色图片Prompt，等待用户确认后才生成角色参考图；图片再经用户确认后登记资产。本Template不生成Voice Profile、Seed Audio Voice Sample Prompt或Audio Reference；这些输出只属于用户显式调用的`templates/21_seed_audio_voice_asset.md`。



---

# Input


CHAR-ID：

Asset Tier：Core / Support

Tier Decision Basis：

Board Name：Core填`Not Applicable`

Board ID：Core填`Not Applicable`

Item ID：Core填`Not Applicable`

角色名称：

身份：

年龄：

外貌：

服装：

性格视觉表现：

性格与身份：

剧情情绪基调：

Active Version / Candidate Version：

Canonical References：

Immutable Traits：

Mutable State Dimensions：

Dependencies：

目标图像工具/模型（如已知）：

画幅/分辨率/交付规格：

当前Prompt Revision：

Visual Production Status：

Prompt Status：Not Started / Draft / Confirmed

Image Status：Not Generated / Candidate / Confirmed

Confirmed Status：No / Yes



---

# Generation Structure


主体：

角色身份。


外观：

脸部、发型、服装。


姿态：

自然站姿。


摄影：

角色设定参考摄影。



---

# Required Output

## Phased Output Contract

### Direct Image Default

当前agent具备直接图片生成能力且用户请求制作角色资产时，默认不输出Prompt：Core直接生成外观参考图并等待用户确认外观，外观确认后直接生成Combined Character Asset Sheet并等待用户确认正式资产图。用户明确要求查看/只要Prompt，或当前agent不能直接生成图片、或用户选择外部图像服务时，才使用下列Prompt Draft步骤。直接生成时内部保存Prompt和`Prompt Confirmation: Direct Image Default — user requested asset production`，但不向用户展示。

本Template不是一次性填写全部区块。每轮只输出当前合法阶段：

1. Core首次`Appearance Reference Prompt Draft`：输出Character Definition与单张外观参考图Prompt，然后停止，等待用户确认该外观参考图Prompt；Support直接输出其Board Prompt Draft。
2. Core外观参考图Prompt获确认后：才允许生成一张外观参考图；输出Appearance Reference Review并停止，等待用户确认外观或要求修改。该图是设计预览，不写`Visual Production Status`、Candidate / Canonical Reference、Active Version或Asset Registry。
3. Core外观获确认后：输出正式`Prompt Draft`，其中包含Combined Character Asset Sheet Prompt及必要状态变体，然后停止，等待用户确认正式资产Prompt。Support在其Prompt获确认后直接进入图片生成。
4. 正式资产Prompt Confirmed后：才允许执行正式资产图片生成；生成后输出Generated Image Review，状态写`Image Generated`，然后停止。
5. 用户确认具体正式资产图片后：输出Confirmed Asset Record，状态写`Asset Confirmed`并完成Active/Canonical登记。

不得在`Prompt Draft`同轮直接生成图片；不得在`Image Generated`同轮自动把Candidate Reference升级为Canonical Reference。

Core与Support共用上述双确认Gate。Core使用一张独立的正式角色资产设定图：同一画布内包含面部特写与正面、严格侧面、背面全身三视图；不得将其拆为独立三视图或独立面部特写Candidate Reference。Support按Board制作，不得逐个生成完整三视图或独立面部特写。Board图片确认前，Board及任何Item的`Confirmed Status`都必须为`No`。

## Character Definition

- 角色身份与剧情功能：
- 年龄感与身体比例：
- 脸型与五官：
- 肤色与肤质：
- 发型与发色：
- 服装结构、材质与配色：
- 整体气质、自然表情与动作习惯：
- Immutable Traits：
- Mutable State Dimensions：

## Image Prompt Package

- Visual Production Status：`Prompt Draft`
- Asset Tier：`Core` / `Support`
- Board ID / Item ID：Core写`Not Applicable`；Support必填
- Prompt Revision：
- Prompt Status：`Draft`
- Image Status：`Not Generated`
- Confirmed Status：`No`
- Prompt Language：
- Target Image Tool / Model：
- Asset Image Route：
- Generation Parameters：画幅、分辨率、背景控制及工具必需参数；未知平台时使用平台中性的可执行规格。

### Core Asset Package

仅当`Asset Tier: Core`时输出以下三个区块；Support写`Not Applicable — use Support Character Reference Board Prompt`。

#### Appearance Reference Prompt

仅在尚未确认外观时输出一条可独立复制执行的完整Prompt，用一张单人头肩或半身自然肖像让用户确认脸型、五官比例、肤质、年龄感、发际线、发型、体态轮廓、主要服装与项目视觉风格。必须包含构图、视角、自然表情、光影、背景、视觉风格、一致性限制、必要负面限制和生成参数；不要求三视图、拼版或状态变体。生成后写`Awaiting User Confirmation: Appearance Reference`并停止。该图只用于设计决策：不得登记为Candidate / Canonical Reference、Active Version、Confirmed Asset或下游视觉输入。

#### Combined Character Asset Sheet Prompt

仅在用户确认外观参考图后输出一条可独立复制执行的完整Prompt，且该Prompt只生成一张基础正式资产。画面固定为一个清晰的四分区角色设定图：三个等比例全身区域依次呈现正面、严格侧面、背面；第四区为正面或轻微三分之二视角的头肩面部特写。四区必须继承已确认外观，且是同一角色、同一版本、同一服装、同一发型、同一年龄感与同一视觉风格，不得让特写另成角色或改变服装/发型。Prompt必须写全主体、四区构图与区域关系、视角、姿态、表情基线、光影、背景、视觉风格、一致性限制、必要负面限制和生成参数，不使用“同上/参考前述”。禁止输出或调用独立的Three-View Prompt、Face Close-Up Prompt，禁止基础正式资产分两张生成。

#### Required State Variant Prompts

仅为已确认的剧情状态逐项输出独立完整Prompt，并明确保持不变的Immutable Traits。没有必要变体时写`Not Required`及依据。

### Support Character Reference Board Prompt

仅当`Asset Tier: Support`时输出；Core写`Not Applicable — independent Core Asset Package required`。

- Board Name / Board ID：
- Included CHAR IDs：
- Item ID Mapping：逐项固定，例如`A-01 → CHAR-004 / 官员甲`
- Object Count：建议4—9；少于4说明不虚构填充的理由，超过9拆板
- Shared Style Lock：时代、画风、光影、背景、画幅与标签体系统一
- Per-Item Distinction Anchors：逐项明确轮廓、脸部类别、服饰、颜色、比例与功能差异
- Board Prompt：一条可独立复制执行的完整Prompt；对象完整可见、标签清晰、不互相遮挡、不混脸、不串服装，不要求逐项三视图或独立面部特写
- Downstream Reference Syntax：`<Board Name> / <Board ID> / <Item ID>`

### Prompt Review Checkpoint

- Prompt Completeness Check：
- Cross-Prompt Identity Consistency Check：
- Awaiting User Confirmation：`Image Prompts`
- Prohibited Next Action：当前Prompt Revision确认前不得生成图片。

## Generated Image Review

仅在正式资产Prompt Confirmed并实际生成或回传正式资产图片后输出：

- Visual Production Status：`Image Generated`
- Prompt Status：`Confirmed`
- Image Status：`Candidate`
- Confirmed Status：`No`
- Confirmed Prompt Revision：
- Prompt Confirmation / Confirmed By / Confirmed At：
- Candidate References：逐项记录路径或受控外部ID、用途、绑定Version、生成工具/模型、参数、来源与授权。
- Image QA：基础正式资产是否为同一张含面部特写 + 正面、严格侧面、背面全身三视图的角色设定图；身份、脸型、身体比例、发型、服装、四区一致性、面部细节与状态变体边界。若特写与三视图被拆为独立Candidate Reference，判定失败并重生。
- Support Board QA：仅Support适用；核对Board ID、Item ID、对象数量、标签、轮廓/服饰/颜色/比例/功能差异及无对象混淆。
- Awaiting User Confirmation：`Generated Images`
- Prohibited Registry Upgrade：图片确认前不得写Canonical References、Active Version或`Status: Active`。

## Confirmed Asset Record

仅在用户明确批准具体Candidate References后输出：

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

Asset ID、Version、Status、Asset Tier、Board ID、Item ID、Visual Production Status、Prompt Status、Image Status、Confirmed Status、Prompt Revision、Image Prompts、Prompt Confirmation、Candidate References、Image Confirmation、Canonical References、Immutable Traits、Mutable State Dimensions、Approval Basis、Supersedes与Downstream Usage。

Core的外观参考图及其用户确认只记录在Character Definition的设计决策中，不写入本记录、Asset Registry、Candidate References、Canonical References或下游视觉输入。

## Voice Asset Isolation

不得根据角色有对白、旁白、画外音、通话、呼喊或潜在对白需求自动创建音色资产。只有用户当前请求显式要求音色提示词、音色制作、角色声音、Seed Audio、配音音色或声音资产时，才退出本Template并读取唯一`workflows/audio_router.md`；只有其返回AUDIO Route才调用`workflows/20_seed_audio_voice_asset_workflow.md`与`templates/21_seed_audio_voice_asset.md`。其输出不得混入本角色视觉资产结构。


# Prompt Rule


保持：

视觉信息明确。


避免：

长篇背景故事。

禁止只写角色“长什么样”而不提供可直接生图的完整Prompt。

未经Prompt确认不得生成图片；未经图片确认不得登记confirmed asset。


避免：

复杂负面提示词。


本Template只输出角色视觉资产。不得顺带生成任何音色自然语言描述、Voice Profile、Seed Audio样本Prompt或Audio Reference交接记录。
