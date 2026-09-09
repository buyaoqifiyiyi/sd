# Image Model Selection Module

## Contract

位置：STATE-03中，当前资产批次的资产定义已可读、任何新Image Prompt编译之前。它不创建主STATE，也不属于STATE-06后的`modules/model-selection.md`视频模型选择。

### Trigger

1. 当前资产批次需要新建或重编Image Prompt，且`Image Model Selection Status: UNSELECTED`。
2. 用户已在当前资产请求中明确指定图像模型时，直接将该指定作为唯一候选，展示选择Proposal供确认；不得再次询问同一选择。
3. 同一批次已`SELECTED`且模型、Prompt Template和Scope均匹配时复用，不重复询问。

已有外部图片走Existing Asset Fast Path时不触发；用户只要求资产诊断、不生成或不重编Prompt时不触发。

### Required Inputs

- 当前Asset ID / Board ID、资产类别、Asset Tier、Prompt Revision与资产批次范围；唯一来源是当前STATE-03资产Workflow与State Contract。
- 用户当前明确的图像模型指定（如有）。
- `modules/assets.md`列出的已验证图像Adapter与其`prompt_output_template`。

### Available Choices

当前唯一可选项：

| Model | Adapter | Final prompt template | Delivery |
|---|---|---|---|
| Built-in Image | `adapters/built-in-image.md` | `templates/24_builtin_image_asset_prompt.md` | 当前环境实际可用时可直接生成；不可用时只交付Prompt |
| Midjourney | `adapters/midjourney.md` | `templates/14_midjourney_asset_prompt.md` | External — only Prompt delivery |

不得默认选择Built-in Image、Midjourney或其他模型。未来模型只有在已验证Adapter和独立`prompt_output_template`均存在后才能加入此表；未适配的模型名不是可选项，也不得借用现有模型模板。

### Selection Proposal And Confirmation

输出一个`Image Model Selection Proposal`，至少包含：

- Image Model Selection Scope：当前资产批次的Asset / Board / Item范围
- Proposed Image Model、Adapter Profile、Prompt Output Template、Delivery Route
- Available Choices：当前可用模型
- Awaiting User Confirmation：`Image Model Selection`

用户明确说“用Midjourney / 用内置Image”等选择后，或当前请求已指定模型时，Proposal只有该一个`Proposed Image Model`。在这个已经展示的单一Proposal检查点，`下一步`、`下一个`、`继续`及等义推进表达按`rules/progression_rules.md`确认该选择；在`UNSELECTED`状态下，纯推进表达不凭空选模型，必须要求用户指定一个可用模型。

确认后写入State Contract的`Selected Image Model`、`Image Adapter Profile`、`Image Prompt Output Template`、`Image Model Selection Status: SELECTED`和Scope，然后才可调用对应资产Workflow的Prompt Generation。

### Change And Return Route

- Prompt尚未确认时切换图像模型：仅使当前Prompt Draft失效，按新模型Template重编；资产定义保持。
- Prompt已确认但尚未生成时切换：返回Prompt Draft并重新确认；不提交外部服务。
- 已有Candidate或Confirmed Asset时不得静默重生或改写其来源；用户明确要求新模型重生才新建Candidate Revision，现有Canonical保持不变。
- 模型能力、参数或Template与已确认资产事实冲突时，返回当前资产Workflow；不得用模型限制改写资产身份、空间、材质、Tier、Canonical或双确认Gate。

### Ownership And Invariants

本Module只拥有图像模型选择、Adapter / Template路由和选择写回；资产定义、Prompt / Image确认、Candidate、Canonical和Registry仍分别由资产Workflow、`rules/02_asset_rules.md`、资产类别Template与`references/asset_lock_contract.md`拥有。

允许写入：State Contract中的Image Model Selection字段和当前Asset Prompt Package的Target / Template / Delivery记录。禁止写入视频Model Lock、Clip、视频Prompt或主STATE。每个`SELECTED`模型必须有唯一、存在且匹配Adapter声明的最终提示词模板。
