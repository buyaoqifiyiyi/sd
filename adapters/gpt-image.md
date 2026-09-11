# GPT Image Asset Prompt Adapter

## Contract

仅在STATE-03的`modules/image-model-selection.md`已确认`Selected Image Model: GPT Image`时调用。它读取已确认资产定义、画幅/交付规格和当前Prompt Revision；只声明GPT Image路线的可用性边界与专属Prompt Template，不拥有资产状态、双确认Gate或最终Prompt Schema。

`prompt_output_template: templates/24_gpt_image_asset_prompt.md`

当前环境实际提供可调用的`GPT Image`时，Prompt确认后可以生成Candidate Image；环境无此能力时只能交付Prompt并诚实写`Image Generation Availability: Unavailable`。不得把可选中的GPT Image误说成固定默认，也不得伪称已生成。

## Boundary

- Prompt正文只由`templates/24_gpt_image_asset_prompt.md`编译；Adapter不复制其模型专属正文。
- 不假设任何**未经验证**的模型版本、图像数量、编辑、参考上传或参数名称；已核验的能力边界记在下节，并注明依据日期。
- 已确认的资产事实优先于任何图像工具偏好；模型不可用时保留当前Prompt Confirmation与STATE-03 `IN_PROGRESS`，等待工具恢复或用户提供外部Candidate。

## Verified Capability Boundary

`GPT Image`是一个**模型系列**，能力随版本分化。以下为按官方口径核验的边界，用于画幅、分辨率与张数决策：

- **`gpt-image-2`**：任意分辨率——两边均为16的倍数、长边≤3840（4K）、比例≤3:1、像素数655,360–8,294,400。**16:9与2K/4K均可行**（2K=`2048×1152`；4K=`3840×2160`）。
- **`gpt-image-1` / `gpt-image-1.5` / `gpt-image-1-mini`**：仅`1024x1024`、`1024x1536`、`1536x1024`、`auto`。**做不了16:9**（`1536x1024`是3:2）。
- 质量`low`/`medium`/`high`；张数`n`为1–10；背景`transparent`/`opaque`/`auto`。
- 资产参考图使用`opaque`：透明底会使下游合成与比对失去中性背景基准。
- **依据**：OpenAI官方图像模型口径，2026-04-21。

要求16:9或2K/4K时必须确认当前使用`gpt-image-2`；选用其他版本时据实说明可交付的画幅与分辨率，不得把版本能力差异说成参数问题。
