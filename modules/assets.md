# Asset Module

入口：`workflows/03_asset_discovery_workflow.md`、`04_character_asset_workflow.md`、`05_environment_asset_workflow.md`、`06_prop_asset_workflow.md`、`15_fx_asset_workflow.md`。

资产发现、分类、Prompt 确认、图片确认、Active Version 与 Canonical Reference 继续分别由这些 Workflow、`rules/02_asset_rules.md` 和 `references/asset_lock_contract.md` 拥有。下游只能引用已确认资产；外观变更必须走 Change Protocol。

## Asset Image Route

本模块是STATE-03图像工具选择与提示词适配的唯一owner。读取已确认的资产定义、当前Prompt Revision、画幅/交付要求和用户当前明确选择；只写当前Asset Prompt Package中的`Target Image Tool / Model`、提示词形态及生成记录。它不创建Video Model Lock、Clip、视频Prompt或项目主STATE，不改写资产事实、Template字段与双确认Gate。冲突返回当前资产Workflow；视频模型词仅在STATE-06后由`modules/model-selection.md`处理。

- 未明确指定外部图像模型：`Built-in Image`。Prompt Draft交付适合内置 Image 的结构化图片提示词，按资产需要写清主请求、主体、场景/背景、风格、构图、光影、材质和约束；Prompt Confirmed后，用户要求生成且当前环境可用时调用内置`image_gen`输出图片。用户只要提示词、或当前环境不可生成时，只交付该提示词，不伪称已生成。
- 明确指定`Midjourney`：读取`adapters/midjourney.md`。交付该适配器格式的 Midjourney Prompt，且始终不调用内置`image_gen`。用户在Midjourney生成并回传结果后，才按既有流程登记Candidate Reference。
- 未明确指定模型不能静默切换至第三方服务；其它外部模型必须由用户明确指定且不继承 Midjourney 格式。

路由在每个Prompt Draft记录；生成记录继续保存实际工具/模型、参数、来源与授权。Prompt Draft → Prompt Confirmed → Image Generated → Asset Confirmed的双确认顺序不变。
