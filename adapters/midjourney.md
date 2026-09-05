# Midjourney Asset Prompt Adapter

## Contract

仅在STATE-03资产创作中，用户当前明确指定`Midjourney`时调用。本Adapter读取已确认资产定义、资产类别、画幅/交付规格、当前Prompt Revision和既有Canonical约束；只输出可直接粘贴的 Midjourney Prompt。它不调用内置`image_gen`、不生成或上传图片、不创建Candidate Reference，也不改变Prompt确认与图片确认Gate。

输出只由对应资产Template承载；本文件不拥有Template字段、资产锁或项目状态。用户在外部生成并回传图片后，原资产Workflow登记实际来源、模型/版本（如已知）、参数和Candidate Reference。未明确指定Midjourney时不得读取本Adapter。

## Prompt Form

使用一条独立、可复制的英文提示词，按重要性从左到右组织：

`[asset / scene identity], [immutable visual anchors], [required state or function], [view and composition], [environment/background], [lighting and material treatment], [project visual style], [concise constraints] [optional explicit parameters]`

- 每条Core图或Support Board均完整自足；不得使用“same as above”、省略继承关系或把内部字段粘入Prompt。
- 优先正向描述。只有确有必要时以简短`--no <unwanted element>`排除明显冲突；不用冗长负面词堆。
- 画幅已明确时附`--ar W:H`；未明确时不臆造比例。
- 只保留用户已指定或为交付格式必需的参数。不得默认附加`--v`、`--seed`、`--stylize`、`--chaos`、`--quality`、`--raw`或任何版本专属值；用户明确要求时才加入其提供的参数，并原样记录。
- 提示词服务于角色身份、环境空间或道具结构锁定；不加入资产流程状态、模型能力声明、视频时长、Clip、Seedance、Registry路径或内部QA标签。

## Output Record

在现有Image Prompt Package内记录：

- `Target Image Tool / Model: Midjourney`
- `Prompt Language: English`（用户明确要求其他语言时从用户要求）
- `Generation Parameters: --ar ...`及用户明确提供的可选参数；没有则`Not specified`
- `Midjourney Prompt:` 后跟一条可复制提示词

Prompt Confirmed后交付该Prompt供用户外部生成，并保持`Image Generation Availability: External — Midjourney`；不得将提示词交付误记为`Image Generated`。
