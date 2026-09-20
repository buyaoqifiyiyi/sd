# SD Film Branded Content｜品牌与商业片

# Read Scope

本文件是品牌与商业片知识域的中枢入口，**不得整文件通读**：按当前事项只读对应小节。

| 当前事项 | 只读 |
|---|---|
| 判定该不该读本域 | `## Purpose And Boundary`、`## Loading Rule` |
| 定位当前需要哪个原子 | `## The Roster` |
| 判断某个事实能不能自己生成 | `## Commercial Fact Discipline｜商业事实纪律` |
| 写新的原子文件 | `## Shared Atom Schema`、`## Validator-Checkable Invariants` |
| 不适用 / 返回路由 | `## Non-Applicable Rule`、`## Return Routing` |
| 不必在运行时读取 | `## Validator-Checkable Invariants` |

---

## Purpose And Boundary

本域拥有**已确认的品牌诉求如何变成呈现层语言**：单一传达目标如何决定注意焦点链、产品在画面中承担什么角色、可信度如何被建立、利益点如何用可见结果而不是形容词表达，以及商业事实的边界。它也拥有商业传播的**受众角色说服路径**（决策链上的不同角色凭什么被说服）与**商业影片形态义务**（宣传 / 科普 / 产品 / 案例 / 招商 / 雇主品牌各自必须让观众看见什么）。

**它不拥有**：

- **商业事实本身**——真实SKU、价格、Logo、功效、资质、授权、法务文案由用户与已确认项目材料拥有；**资产侧的三类归类（客户必须提供 / 可由制作生成 / 优先后期叠加）由`workflows/03_asset_discovery_workflow.md`的`## Commercial Fact Triage`拥有**，本域只引用不重复。
- 剧情事实与故事结构（Writer Owner与`knowledge/writer/screenplay_development.md`）。
- 项目级美学方向（STATE-04）、媒介分化（`knowledge/medium_profiles.md`）、类型呈现（`knowledge/genre/index.md`）、时代与地域（`knowledge/period_and_place/index.md`）、交付画幅（`knowledge/camera_language/composition_language/vertical_framing.md`）。
- 目标形式的节奏适配：短剧 / 竖屏剧情 / 1—3分钟剧情视频仍由`knowledge/adaptation/short_form_drama_adapter.md`拥有；本域不新建节拍模型。形态原子只决定"必须让观众看见什么"，不决定段落数、秒数或五段模型。
- **年龄轴的适宜性与理解难度**：`knowledge/audience_profiles.md`拥有`preschool` / `children_family` / `general`三档、三张分层表与"不得推定受众"纪律。`04_commercial_audience.md`是**角色轴**——它回答"凭什么被说服"，不改年龄轴的值域、不新增同义档，两轴冲突时年龄轴优先。
- **平台事实、注意窗口与结尾结构**：由`knowledge/platform_profiles.md`拥有。本域不登记任何平台的机制、时长上限、审核条文或尺寸数值，也不从平台反推形态或受众角色。

**它不是"广告模板"**：本域不规定段落数与秒数，不提供可以套用的构型；它只回答"这个品牌诉求要求观众看到什么、以及哪些事实不能由制作生成"。

它属于**条件性Knowledge**，与`knowledge/medium_profiles.md`同类：只在品牌诉求或商业目标已确认时加载。

## Loading Rule

**触发**：项目存在**已确认**的品牌诉求或商业目标——`templates/00_project_start_template.md`的`# Input Material`已勾选`品牌需求`且内容已给出，或STATE-01的Creation Brief含明确品牌目标，或用户当前请求明确要求品牌 / 产品 / 服务传播。

**不触发**：普通叙事项目即使出现道具品牌、商标背景或商业场景也不加载；**不得推定**——项目时长短、平台是短视频、题材像广告、画面里出现商标，都不构成"这是商业片"的判定依据。品牌诉求未确认时不加载本域，也不得自行补写品牌目标。

**读取范围**：只读当前命中的原子，按各原子的章节标题定点读取；不整域通读。

## The Roster

| # | Atom | File | 拥有什么 |
|---|---|---|---|
| 1 | 品牌诉求的呈现转译 | `knowledge/branded_content/01_brand_requirement_translation.md` | 单一传达目标、产品角色、可信度锚点、利益点的可见化 |
| 2 | 产品可读性与宣称边界 | `knowledge/branded_content/02_product_legibility_and_claims.md` | 产品识别点、模型能生成什么与必须后期叠加什么、宣称与授权边界 |
| 3 | 形态与交付 | `knowledge/branded_content/03_form_and_delivery.md` | 时长形态的候选用法、结尾落地方式、与画幅、海报、Clip划分的关系 |
| 4 | 商业受众与说服路径 | `knowledge/branded_content/04_commercial_audience.md` | 决策链角色的说服路径，及其落在画面的哪个位置 |
| 5 | 商业影片形态 | `knowledge/branded_content/05_commercial_format.md` | 宣传 / 科普 / 产品 / 案例 / 招商 / 雇主品牌六类形态的内容义务与科普准确性纪律 |

本表是原子的**唯一登记处**：新增原子必须同时在此登记，文件与登记项一一对应。

## Shared Atom Schema

每个原子文件必须按下列固定小节组织，缺任一小节即视为未完成，不得入册：

| # | 小节 | 必须回答 |
|---|---|---|
| 1 | `## Purpose And Owner` | 本原子回答什么、边界在哪、与哪个相邻owner不重合 |
| 2 | `## Executable Vocabulary｜可执行词汇` | 诉求/风险 → 呈现落点 → **写进哪个既有字段** |
| 3 | `## Conditions And Anti-Use｜成立条件与反用` | 每条落点的成立条件、不成立时怎么办 |
| 4 | `## Commercial Fact Boundary｜商业事实边界` | 本原子涉及的事实哪些必须由客户提供、哪些不得由模型生成 |
| 5 | `## Failure Signals｜失败信号` | 可观察的失效表现 |

## Commercial Fact Discipline｜商业事实纪律

**任何商业事实都不得由制作推断或生成。** 一等禁项（与`rules/automation_mode.md`的Hard Stop同一口径）：真实价格、SKU与组合、可读品牌/Logo文字、功效与资质表述、受监管承诺、免责声明、授权人物或声音、真实机构与合作关系。

**专业结论同样是一等禁项**：医学、健康、法律、金融、安全、工程等领域的结论、数据、剂量、适用范围与前提条件必须由客户提供，制作不得推断、不得为可读性简化到失真，也不得省略必要前提——`05_commercial_format.md`的`### Explainer Discipline｜科普纪律`是这一条在科普形态下的执行入口。

- 缺这些事实时按`workflows/03_asset_discovery_workflow.md`的`## Commercial Fact Triage`归类并记录Pending Decision；只有会改变产品身份、商业承诺、法律风险或当前关键剧情时才向用户询问。
- **不得用"看起来专业"的画面替代缺失的事实**：编造的价格、功效或Logo不是创意，是风险。
- 需要文字级正确的元素（长文案、价签、免责声明、精确Logo）默认按"优先后期叠加"处理，不写进模型生成承诺。

## Orthogonality

- **与媒介、类型、时代地域三条轴正交**：品牌诉求不改变媒介档、不改变类型承诺、不改变时代与地域的事实约束；反过来这三条也不得静默抹掉商业目标。它同时与`knowledge/audience_profiles.md`的年龄轴、`knowledge/platform_profiles.md`的平台轴正交——五条轴互不覆盖，任一轴都不得被另一轴静默抹掉。
- **与叙事的关系**：商业目标不拥有剧情事实，也不得为了露出而改写Production-Locked Script、Canonical资产或已确认Blocking；它能影响的是**呈现的选择与优先级**，且这些影响必须能被说明。
- **与美学基线的关系**：品牌调性通过已有的`Visual Grammar Baseline`与`Aesthetic Decision Lock`表达，不新建设计体系或平行Schema。

## Shared Invariants

- Story First、Asset First、镜头必须服务剧情
- STATE-00至STATE-09主Pipeline、Completion Gate与推进规则
- 资产双确认、Canonical Lock与连续性纪律
- STATE-08最终Prompt字段与Template：不因品牌新增任何字段
- REF-TAIL A/B/C、REF-SKETCH边界、Voice opt-in，以及**视频Prompt永久禁止非剧情内配乐**
- 一等禁项与Hard Stop不因"商业需要"放宽

## Return Routing

- 商业事实缺失或冲突 → `workflows/03_asset_discovery_workflow.md`的`## Commercial Fact Triage`与Pending Decision
- 品牌诉求本身未确认 → STATE-00的`# Input Material`与STATE-01的Creation Brief；不得由本域代替用户确认
- 目标形式的节奏适配 → `knowledge/adaptation/short_form_drama_adapter.md`（短剧 / 竖屏剧情 / 1—3分钟）
- 年龄轴的适宜性与理解难度 → `knowledge/audience_profiles.md`；两轴冲突时年龄轴优先，不得为说服力突破其分层表
- 平台事实、注意窗口与结尾结构 → `knowledge/platform_profiles.md`；本域不猜平台机制
- 受众角色或形态未声明 → 用户与已确认项目材料；记Pending Decision，不自行推定
- 交付画幅 → `knowledge/camera_language/composition_language/vertical_framing.md`
- 项目级美学方向 → STATE-04；剧情事实 → Writer Owner
- 海报与封面 → `knowledge/poster_design/index.md`（本域不重复其判据）

## Non-Applicable Rule

- 品牌诉求未确认：不加载任何原子，不写`Branded Content`结论，也不得把项目当商业片推进；需要品牌事实才能成立的选择记为待定。
- 普通叙事项目中的道具品牌、店铺招牌、背景商标不触发本域——它们按资产与时代地域规则处理。
- 本域不适用于Poster、MUSIC、AUDIO等辅助模块的既有边界。
- 本域不创建STATE、不新增Template字段、不改变任何Model Adapter能力与能力数值。

## Validator-Checkable Invariants

- `## The Roster`登记的原子文件必须真实存在，且`knowledge/branded_content/`下不得存在未登记的原子文件（登记项与文件一一对应）。
- 每个原子必须齐备`## Shared Atom Schema`列出的五个小节。
- `## Commercial Fact Discipline｜商业事实纪律`必须存在，且必须包含一等禁项清单与指向`workflows/03_asset_discovery_workflow.md`的归类路由。
- 不得新建节拍模型、不新增STATE-08字段、不改变主Pipeline的声明必须存在。
- "不得推定项目为商业片"的声明必须存在。
- 与媒介、类型、时代地域三条轴正交的声明必须存在。
