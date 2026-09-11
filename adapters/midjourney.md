# Midjourney Asset Prompt Adapter

## Contract

仅在STATE-03资产创作中，用户当前明确指定`Midjourney`时调用。本Adapter读取已确认资产定义、资产类别、画幅/交付规格、当前Prompt Revision和既有Canonical约束；只输出可直接粘贴的 Midjourney Prompt。它不调用`GPT Image`、不生成或上传图片、不创建Candidate Reference，也不改变Prompt确认与图片确认Gate。

`prompt_output_template: templates/14_midjourney_asset_prompt.md`

对应资产Template继续承载资产定义、阶段状态与确认字段；`templates/14_midjourney_asset_prompt.md`是Midjourney最终Prompt正文的唯一owner。本Adapter只拥有Midjourney路由和能力边界，不复制最终Prompt Schema、资产锁或项目状态。用户在外部生成并回传图片后，原资产Workflow登记实际来源、模型/版本（如已知）、参数和Candidate Reference。未明确指定Midjourney时不得读取本Adapter。

## Capability Boundary

- Prompt正文必须由`templates/14_midjourney_asset_prompt.md`编译；它的英文单行、资产类别策略、参数纪律与Prompt QA不得在本Adapter复写。
- Midjourney Prompt只能外部交付：Prompt Confirmed后保持`Image Generation Availability: External — Midjourney`；不得将提示词交付误记为`Image Generated`。
- 不假设或默认任何版本、质量、风格化、种子、动漫模型、图像权重或编辑能力。用户明确提供的可核验参数由独立Template原样投影。
