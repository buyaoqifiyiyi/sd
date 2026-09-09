# Built-in Image Asset Prompt Template

## Scope And Ownership

仅在STATE-03已确认`Selected Image Model: Built-in Image`时，由`adapters/built-in-image.md`选择本Template。本Template独占内置Image的最终Prompt正文；角色、环境、道具、FX资产Template继续拥有资产定义、分级、Prompt / Image确认、Candidate、Canonical与登记字段。

本Template不假设特定内置模型、版本、参数或编辑能力。它只将已确认资产事实编译为清晰、可见、可验证的图像描述；是否实际生成由Adapter和当前环境能力决定。

## Input Projection

- Asset Category、Asset Tier、current deliverable and Prompt Revision
- Confirmed asset identity, immutable anchors and required state/function
- Required view, composition, background/environment and delivery specification
- Source-grounded lighting, color, material and project style evidence
- Minimal real failure risks and only applicable constraints

每个Core图、状态变体、环境视图、细节图或Support Board都必须独立完整；不得写`同上`、内部状态、Registry、视频模型、Clip、时长或QA标签。

## Built-in Image Prompt Package

- Target Image Tool / Model：`Built-in Image`
- Prompt Output Template：`templates/24_builtin_image_asset_prompt.md`
- Generation Parameters：仅记录当前环境实际支持且用户确认的规格；未知则`Not specified`
- Built-in Image Prompt：

```text
[画面主请求与资产身份]。 [不可变外观/结构锚点与可见比例]。 [当前必须呈现的状态或功能]。 [视角、观看距离、构图及前中后景关系]。 [场景或受控背景]。 [有来源的光线、色彩与材质微观证据]。 [已确认的项目视觉风格]。 [当前任务最小且真实的限制]。
```

交付时将方括号替换为实际事实，输出一段可直接生成的自然语言Prompt；中文为默认语言，用户明确指定英语时完整改用英语。正向画面目标优先；只保留真实高风险限制，不堆叠无关否定词。

## Asset-Specific Precision

- Character：外观参考先锁脸型、五官比例、肤质、发型、体态和服装；正式Sheet明确四区的同一角色关系；状态图只改变获确认状态。
- Environment：先锁空间骨架、活动区、尺度、入口/出口、材质与实际光源，再说明当前视点；不把环境写成纯氛围背景。
- Prop：先锁轮廓、尺度参照、结构、材料、表面状态与功能，再写展示视角与背景。
- Formal FX：写清可见形态、出现位置/边界、状态、交互环境与光学证据，不使用无法验证的质量形容词。
- Support Board：写明对象数、逐项差异、分区/留白与可读标签；禁止对象遮挡、混合或虚构填充。

## Prompt QA Before The Existing Confirmation Gate

- 资产身份和不可变锚点在正文前部，且均可从画面验证。
- 当前交付物在一张图内可执行，构图、光线、材质和背景没有互相矛盾。
- 未把假定的平台参数、模型能力或抽象“高级感”写成事实。
- 最终输出仅含当前交付物的一段Prompt，随后返回资产类别Template原有的Prompt Review Checkpoint；本Template不得自行确认Prompt或图片。
