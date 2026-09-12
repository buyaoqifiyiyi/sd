# Image Model Selection Module

## Contract

位置：`workflows/02_script_analysis_workflow.md`的`Production Setup Gate`在Script `Production-Locked`之后、STATE-02之前确认项目图像模型默认项与`Image Delivery Mode`；STATE-03中，当前资产批次的资产定义已可读、任何新Image Prompt编译之前，直接继承该默认项或处理明确例外。它不创建主STATE，也不属于视频模型选择。

本模块同时拥有项目级**图像交付形态**（`Image Delivery Mode`）的选择与路由：模型选择回答“用哪个工具”，交付形态回答“这一轮交付图片还是交付Prompt”，两者相互独立、不得互相推断。

### Trigger

1. `Production Setup Gate`（Script `Production-Locked`后、STATE-02之前）：必须提出一次`Production Setup Proposal`，其中含项目图像模型默认项与视频模型偏好；用户已指定图像模型时直接作为唯一候选，展示后等待确认。剧本锁定前不得提出该Proposal，也不得在STATE-00询问模型。
2. 当前资产批次需要新建或重编Image Prompt且有已确认`Project Image Model Default`时，自动继承为该批次的`Selected Image Model`、Adapter、Template与Delivery Route，不再逐批询问。
3. 仅在默认项为`UNSELECTED`（旧项目迁移）、用户明确指定当前批次例外模型、默认Adapter不可用或当前批次已被明确要求更换时，展示一次当前批次选择Proposal。
4. 同一批次已`SELECTED`且模型、Prompt Template和Scope均匹配时复用，不重复询问。

已有外部图片走Existing Asset Fast Path时不触发；用户只要求资产诊断、不生成或不重编Prompt时不触发。

### Required Inputs

- 当前Asset ID / Board ID、资产类别、Asset Tier、Prompt Revision与资产批次范围；唯一来源是当前STATE-03资产Workflow与State Contract。
- 用户当前明确的图像模型指定（如有）。
- `modules/assets.md`列出的已验证图像Adapter与其`prompt_output_template`。

### Available Choices

当前唯一可选项：

| Model | Adapter | Final prompt template | Delivery |
|---|---|---|---|
| GPT Image | `adapters/gpt-image.md` | `templates/24_gpt_image_asset_prompt.md` | 当前环境实际可用时可直接生成；不可用时只交付Prompt |
| Midjourney | `adapters/midjourney.md` | `templates/14_midjourney_asset_prompt.md` | External — only Prompt delivery |

不得默认选择GPT Image、Midjourney或其他模型。未来模型只有在已验证Adapter和独立`prompt_output_template`均存在后才能加入此表；未适配的模型名不是可选项，也不得借用现有模型模板。

### Selection Proposal And Confirmation

输出一个`Image Model Selection Proposal`，至少包含：

- Image Model Selection Scope：当前资产批次的Asset / Board / Item范围
- Proposed Image Model、Adapter Profile、Prompt Output Template、Delivery Route
- Available Choices：当前可用模型
- Awaiting User Confirmation：`Image Model Selection`

用户明确说“用Midjourney / 用GPT Image”等选择后，或当前请求已指定模型时，Proposal只有该一个`Proposed Image Model`。在这个已经展示的单一Proposal检查点，`下一步`、`下一个`、`继续`及等义推进表达按`rules/progression_rules.md`确认该选择；在`UNSELECTED`状态下，纯推进表达不凭空选模型，必须要求用户指定一个可用模型。

Production Setup确认后写入State Contract的`Project Image Model Default`与选择状态；STATE-03继承时再写当前批次的`Selected Image Model`、`Image Adapter Profile`、`Image Prompt Output Template`、`Image Model Selection Status: SELECTED`和Scope，然后才可调用对应资产Workflow的Prompt Generation。项目默认项不是图片/资产确认，也不授权外部提交。

### Change And Return Route

- Prompt尚未确认时切换图像模型：仅使当前Prompt Draft失效，按新模型Template重编；资产定义保持。
- Prompt已确认但尚未生成时切换：返回Prompt Draft并重新确认；不提交外部服务。
- 已有Candidate或Confirmed Asset时不得静默重生或改写其来源；用户明确要求新模型重生才新建Candidate Revision，现有Canonical保持不变。
- 模型能力、参数或Template与已确认资产事实冲突时，返回当前资产Workflow；不得用模型限制改写资产身份、空间、材质、Tier、Canonical或双确认Gate。

### Ownership And Invariants

本Module只拥有项目图像默认项、当前批次例外选择、Adapter / Template路由和选择写回；资产定义、Prompt / Image确认、Candidate、Canonical和Registry仍分别由资产Workflow、`rules/02_asset_rules.md`、资产类别Template与`references/asset_lock_contract.md`拥有。

允许写入：State Contract中的Image Model Selection字段和当前Asset Prompt Package的Target / Template / Delivery记录。禁止写入视频Model Lock、Clip、视频Prompt或主STATE。每个`SELECTED`模型必须有唯一、存在且匹配Adapter声明的最终提示词模板。

## Image Delivery Mode

模型选择回答“用哪个工具”，交付形态回答“这一轮交付图片还是交付Prompt”。两者独立：不得由模型反推交付形态，也不得由交付形态反推模型。

### 三档形态

| Mode | 行为 |
|---|---|
| `AUTO`（默认） | 按**当前执行环境的真实图像生成能力**路由：能直接出图则按`DIRECT_IMAGE`行为，不能则按`PROMPT_ONLY`行为 |
| `DIRECT_IMAGE` | 始终尝试直接生成；当前环境无能力时降级为`PROMPT_ONLY`行为并明确标注能力不可用，不得伪造生成结果 |
| `PROMPT_ONLY` | 始终只交付Prompt，不调用GPT Image 生成；适用于用户要在其他平台自行出图 |

`AUTO`不是猜测：判据是当前执行环境在**本轮**是否存在可实际调用的图像生成能力。不得用历史会话、其他平台或上一次运行的能力推断本轮环境，也不得因为曾经生成过就假设当前可生成。

### Trigger

1. `Production Setup Gate`：`Production Setup Proposal`必须同时包含图像模型默认项与`Image Delivery Mode`。
2. 用户当前请求明确指定时（例如“直接出图”“不要给我Prompt”“只要Prompt”），直接设为对应形态并展示一次确认，不重复询问。
3. 用户随时可以改：说“以后直接出图”写`DIRECT_IMAGE`；说“只要Prompt / 我在别处出图”写`PROMPT_ONLY`；说“你按环境来 / 你自己看着办”写`AUTO`。改动只影响之后的批次，不追溯改写已确认资产与既有生成记录。
4. 未设置时为`AUTO`，不阻塞任何资产流程。

### 与 STATE-03 的关系

交付形态只决定当前批次的两轮怎么走，不改变资产定义、Asset Tier、Prompt / Image双确认的实质或任何Hard Stop：

- `PROMPT_ONLY`：批次Prompt轮照常停止等待确认；图片来自用户外部生成后的回传。
- `DIRECT_IMAGE`且当前环境确有出图能力：批次Prompt轮仍必须输出完整Prompt并留档，但在输入完整、不触`rules/automation_mode.md`的Hard Stop且当前QA通过时，可在同一轮自行确认该Prompt Revision并按`Asset Batch Delivery`继续生成整批，不再为Prompt额外停一轮。该授权**复用`rules/automation_mode.md`的既有条款**，不新立一套。
- 无论哪种形态，图片确认都是Hard Gate，仍按`Exception-Based Batch Confirmation`整批判读；`DIRECT_IMAGE`不授权自动批准图片，也不得把未确认图片登记为Canonical / Active。

### 写回

Production Setup确认后写入State Contract的`Image Delivery Mode`；STATE-03在批次Profile中把它投影为既有的`Image Delivery Route`并按该Route执行。它不创建STATE、不改写`Selected Image Model`、不授权外部提交。
