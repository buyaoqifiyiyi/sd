# Midjourney Asset Prompt Template

## Scope And Ownership

仅在STATE-03资产创作且用户当前明确指定`Midjourney`时，由`adapters/midjourney.md`选择本Template。本Template是Midjourney最终可粘贴提示词正文的唯一owner；角色、环境、道具、FX资产Template继续拥有资产定义、分级、Prompt / Image确认、Candidate、Canonical与登记字段。

本Template不调用Midjourney、不上传参考图、不宣称图片已生成，也不改变任何资产事实或确认Gate。它只把已确认的资产事实投影为一条可执行英文Prompt。未明确选择Midjourney时不得使用本Template。

## Input Projection

- Asset Category：CHAR / ENV / PROP / FX
- Asset Tier And Deliverable：Core Appearance Reference / Core Main Reference / Combined Character Asset Sheet / Required Variant or View / Key Detail / Support Board
- Confirmed Asset Identity And Immutable Anchors：
- Required Current State Or Function：
- Required View, Composition And Delivery Specification：
- Confirmed Environment, Lighting, Material And Project Style Evidence：
- Real Failure Risks For This Asset：
- Confirmed Aspect Ratio / User-Specified Parameters：

没有来源或未确认的字段不得补写。一次只编译当前合法Prompt Revision；每个Core图、变体、环境视图、细节图或Support Board都必须独立完整，不能写`same as above`或依赖前一条Prompt。

## Midjourney Prompt Package

- Target Image Tool / Model：`Midjourney`
- Prompt Language：`English`
- Prompt Output Template：`templates/14_midjourney_asset_prompt.md`
- Generation Parameters：仅写已确认画幅和用户明确提供的参数；没有则`Not specified`
- Midjourney Prompt：

```text
[asset identity and type], [immutable visual anchors and visible structure], [required current state or narrative function], [specific view, camera distance and composition], [environment or controlled background], [source-grounded lighting and material evidence], [confirmed project visual style], [minimal real-risk constraint] [optional --no constraint] [optional explicit parameters]
```

提示词必须输出为一条可直接粘贴的英文行；方括号内容只代表编译位置，交付时不得保留。重要且可见的身份锚点在前，之后按可验证画面关系组织；不把资产流程状态、Registry、QA、视频模型、Clip、时长或内部路径写进Prompt。

## Asset-Specific Compilation

### Character

- Appearance Reference：先锁定单一角色的年龄感、脸部比例、肤质、发际线/发型、体态轮廓、主要服装、自然表情与头肩或半身构图；不写三视图、拼版或状态变体。
- Combined Character Asset Sheet：明确同一角色、同一版本、同一服装与发型；写出三个等比例全身区（front / strict side / back）和一个头肩特写区的区域关系。不要把四区写成四个不同人物，也不拆成独立基础资产Prompt。
- State Variant：先写必须保持的身份与外观锚点，再写唯一获确认的状态变化；不重述无关剧情。

### Environment

- Main Reference：优先空间骨架、入口/出口、活动区、尺度锚点、前中后景关系、材质、实用光源方向与时间/天气；画面必须可拍摄，而不只是氛围背景。
- Multi-View Or Detail：写明当前视点的用途和不可变空间锚点，用完整自身描述保持几何一致；不要使用前图的省略引用。

### Prop And FX

- Prop：先写可辨认轮廓、尺度参照、结构、材质、表面状态与功能，再写观看角度、背景和光线。
- Formal FX：先写可见形态、产生位置/边界、运动或消散状态、交互环境与光学证据；不得用抽象“震撼、史诗、超高级”取代物理可见事实。

### Support Board

明确Board内对象数量、各Item的可见差异、排布/留白和标签可读性；避免主体互相遮挡、混脸、串服装或把不同资产融合成一个对象。不得为了凑数虚构资产。

## Parameter And Syntax Discipline

- 已确认画幅才附`--ar W:H`；未确认时不猜测比例。
- `--v`、`--q`、`--s`、`--seed`、`--chaos`、`--raw`、`--niji`和其他版本/模型专属参数一律不是默认值；仅在用户明确提供并要求使用时原样附上。
- `--no`只排除当前有真实风险且与正向目标冲突的对象，例如`--no text, watermark`；不用长负面词堆。
- `::`权重只在用户明确要求优先级权衡、且两个可见目标确有竞争时使用；未提出时不用权重伪造精度。
- 用短而明确的英文描述和逗号分隔可见要素。艺术家姓名、器材、镜头或技术名词只在它们确实限制可见结果、且来自用户或项目事实时使用。

## Prompt QA Before The Existing Confirmation Gate

- Identity / immutable anchors are visible and appear before optional style language.
- Required asset type, state, view and composition are executable in one image.
- Lighting, material and style are evidence-based rather than generic quality adjectives.
- Parameters are confirmed or user-specified; no version-sensitive defaults were invented.
- Constraint text is minimal and does not conflict with the positive image goal.
- The output is exactly one standalone English Midjourney Prompt for the current deliverable.

随后返回对应资产Template的既有`Prompt Review Checkpoint`；本Template不得自行确认Prompt或图片。
