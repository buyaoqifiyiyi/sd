# Asset Module

入口：`workflows/03_asset_discovery_workflow.md`、`04_character_asset_workflow.md`、`05_environment_asset_workflow.md`、`06_prop_asset_workflow.md`、`15_fx_asset_workflow.md`。

资产发现、分类、Prompt 确认、图片确认、Active Version 与 Canonical Reference 继续分别由这些 Workflow、`rules/02_asset_rules.md` 和 `references/asset_lock_contract.md` 拥有。下游只能引用已确认资产；外观变更必须走 Change Protocol。

## Asset Image Route

批次是路由与交付的默认单位：同一资产类别、同一Asset Tier、同一生产形态与同一已选图像模型构成一批，其构成、两轮交付与挑拣回退由`rules/02_asset_rules.md`的`Asset Batch Delivery`拥有。本模块只按该批次写入`Target Image Tool / Model`与交付记录，在该批次的Image轮同轮提交整批全部图片，不为批内每个资产单独重开模型路由，也不逐张生成后停顿。

本模块是STATE-03图像工具路由与提示词适配的唯一owner。读取Production Setup已确认的项目图像模型默认项、已确认的资产定义、当前Prompt Revision、画幅/交付要求和用户当前明确例外选择；只写当前Asset Prompt Package中的`Target Image Tool / Model`、提示词形态及生成记录。它不创建Video Model Lock、Clip、视频Prompt或项目主STATE，不改写资产事实、Template字段与双确认Gate。冲突返回当前资产Workflow；视频模型只由`modules/model-selection.md`的项目偏好与后续能力复核处理。

### Image Model Selection Gate

新建或重编资产Prompt前必须读取`modules/image-model-selection.md`。已确认`Project Image Model Default`且无当前批次例外时，直接将它投影为当前`Selected Image Model`，不重复提问；同一次路由还必须把`Image Delivery Mode`投影为当前批次的`Image Delivery Route`：`DIRECT_IMAGE`且当前执行环境确有出图能力时按`Built-in Candidate Generation`，否则按`External Prompt Only`；`AUTO`按当前环境的真实能力二选一，不得用历史推断；能力不可用时必须标注而不得伪造生成结果。项目默认项与当前批次均为`UNSELECTED`时，先展示该Module的`Image Model Selection Proposal`并停止；不得默认选择GPT Image、Midjourney或任何第三方服务，也不得生成或展示某个模型格式的资产Prompt。用户在当前请求明确指定图像模型时，仍先展示对应单一Proposal；在该明确检查点说“下一步 / 继续”等即确认该选择。

选择确认后，只读取唯一匹配Adapter和它声明的独立`prompt_output_template`：

- `GPT Image`：读取`adapters/gpt-image.md`和`templates/24_gpt_image_asset_prompt.md`。当前环境实际可生成时，在既有Prompt确认后生成Candidate Image；不能生成时只交付Prompt并诚实标记不可用。
- `Midjourney`：读取`adapters/midjourney.md`和`templates/14_midjourney_asset_prompt.md`。始终只交付外部Prompt，不调用`GPT Image`；用户在Midjourney生成并回传结果后，才登记Candidate Reference。
- 明确指定其他图像模型：只有其已验证Adapter和独立`prompt_output_template`都存在，才可成为选择项；否则说明尚未适配，请用户选择现有模型或明确要求模型中立的外部Prompt。不得借用GPT Image、Midjourney或任一视频模型格式。对已有图像的局部编辑，只在真实输入图可用时采用最小`CHANGE`与完整`PRESERVE`逻辑；不把编辑Prompt或外部平台能力伪称为生成结果。

图像模型选择不等于Prompt或图片确认。任何Candidate Image仍须按`rules/02_asset_rules.md`的资产检查点确认语义才可成为Canonical Reference / Active Version；在已展示的当前Candidate检查点，“下一步 / 继续”即为该确认。模型选择只作用当前资产批次，不创建Video Model Lock、Clip或视频Prompt。

### Prompt Evidence Ordering

任何Asset Prompt Draft按“身份与不可变锚点 → 可见结构/比例 → 构图与观看距离 → 有来源的光线与色彩 → 材质微观证据 → 当前任务的最小约束”组织。每一层只保留能被图像直接验证的描述：例如用可见皮肤、织物、金属或环境表面的真实纹理替代“高级细节”，用明确前/中/后景关系替代“空间感”。

正向描述负责目标画面，负向约束只保留当前资产的真实高风险失败类别（如身份漂移、重复主体、文字、水印、结构变形或不需要的塑料质感），不得把所有可能错误堆成冗长清单。数值、器材或专业名词只有在它们确实约束可见构图、透视、景深或光线结果时才使用；不得用无效精密参数替代主体与结构事实。

该排序只提升Asset Prompt Draft的可验证性，不新增Prompt字段、不改变资产事实、图像工具路由、Prompt / Image双确认或Canonical锁定。已选择图像模型时，其独立最终提示词模板拥有模型专属正文与参数策略；本节只提供跨模型的事实证据顺序。

路由在每个Prompt Draft记录；生成记录继续保存实际工具/模型、参数、来源与授权。Prompt Draft → Prompt Confirmed → Image Generated → Asset Confirmed的双确认顺序不变。

## Asset Naming And Delivery Package

图片成为Canonical Reference时，必须按`references/asset_package.md`的`Asset Image Naming`绑定稳定文件名；该文件同时唯一拥有已确认生产物的分类打包构成、包位置、来源规则与“最终视频Prompt参考条目 ↔ 包内文件”的一一对应。本模块不重复其形态，只负责在批次图片确认时把该文件名写入当前资产的Canonical References记录。
