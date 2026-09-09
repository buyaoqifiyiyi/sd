# Built-in Image Asset Prompt Adapter

## Contract

仅在STATE-03的`modules/image-model-selection.md`已确认`Selected Image Model: Built-in Image`时调用。它读取已确认资产定义、画幅/交付规格和当前Prompt Revision；只声明内置图像路线的可用性边界与专属Prompt Template，不拥有资产状态、双确认Gate或最终Prompt Schema。

`prompt_output_template: templates/24_builtin_image_asset_prompt.md`

当前环境实际提供可调用的内置图片生成能力时，Prompt确认后可以生成Candidate Image；环境无此能力时只能交付Prompt并诚实写`Image Generation Availability: Unavailable`。不得把可选中的Built-in Image误说成固定默认，也不得伪称已生成。

## Boundary

- Prompt正文只由`templates/24_builtin_image_asset_prompt.md`编译；Adapter不复制其模型专属正文。
- 不假设特定模型版本、图像数量、编辑、参考上传、参数名称或外部平台能力。
- 已确认的资产事实优先于任何图像工具偏好；模型不可用时保留当前Prompt Confirmation与STATE-03 `IN_PROGRESS`，等待工具恢复或用户提供外部Candidate。
