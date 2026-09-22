# SD Film Writer Layer｜编剧层

# Read Scope

本文件是编剧层的**发现入口与需求路由表**，不拥有任何创作判据：**不得整文件通读**，按当前事项只读对应小节。

| 当前事项 | 只读 |
|---|---|
| 判定该不该进本层、本层给什么 | `## Purpose And Boundary`、`## Module Contract` |
| 定位当前品牌需求该读哪个文件与哪一节 | `## Requirement Router｜需求路由` |
| 定位编剧层的文件清单与各自 owner | `## The Roster`、`### Growth Boundary｜体量边界`（新增内容前必读） |
| 写新的编剧层文件 | `## Shared File Schema`、`## Validator-Checkable Invariants` |
| 不适用 / 返回路由 | `## Non-Applicable Rule`、`## Return Routing` |
| 不必在运行时读取 | `## Validator-Checkable Invariants` |

---

## Purpose And Boundary

本层拥有**同一套编剧工艺在不同品牌、不同需求下的定制**：把一份已确认的客户或创作需求，逐项路由到命中的工艺条目、品牌原子、受众轴与类型剖面，并保证产出的剧本逐项兑现该需求。

它回答一个问题：**这一份需求，该读哪些节、产出必须兑现什么。**

它**不拥有**：

- **创作判据本身**：故事逻辑、人物构建、场景与对白技法、可失败判定归`knowledge/writer/screenplay_development.md`；授权后优化归`screenwriting_optimization.md`；来源素材改编归`script_adaptation.md`；导演化处理归`directorial_interpretation.md`。本文件只做发现与路由，**不复述任何判据、阈值或条目正文**。
- **品牌诉求的呈现转译**：归`knowledge/branded_content/index.md`及其登记的五个原子。
- **需求来源事实**：品牌诉求、商业事实、平台事实、目标形式、媒介、类型、受众由用户与已确认项目材料拥有，登记于`templates/00_project_start_template.md`与`project_bible.md`；本层不得推断或补写。
- **输出格式**：STATE-01用户可见字段、顺序与排版归`templates/02_script_analysis_prompt.md`。
- **相机、镜头、Clip、资产与Prompt**：由各自owner拥有，本层不越界。

**它不是一个新STATE**：本层是STATE-01的读取入口与路由层，不创建主STATE、不新增Template字段、不改变任何Gate、Completion Gate或交付物。

**它不套用配方**：本层的路由只决定"读什么"，不决定"必须发生什么"。任何把路由结论写成"第N分钟必须…""每场必须有…"的用法都越权，边界见`knowledge/genre/index.md`的`## Craft And Formula｜工艺与公式`。

## Module Contract

- **Module Name**：Writer Layer｜编剧层
- **Module Type**：STATE-01的域入口与需求路由Knowledge；不是Workflow、不是Template、不是新STATE
- **Owner**：`knowledge/writer/index.md`（本文件）拥有**发现、需求路由、Roster登记与文件Schema**；创作判据全部由`## The Roster`列出的各文件拥有
- **Trigger**：所有SD Film叙事项目。STATE-01进入时先读本文件，再按`## Requirement Router｜需求路由`只读命中项
- **Not Triggered As**：资产生产、镜头与Clip设计、Prompt编译、独立Workflow、用户可见Schema、第二套编剧判据
- **Required Inputs / Owners**：`templates/00_project_start_template.md`的`# Input Material`、`# Client Brief｜客户与商业 brief`（仅品牌项目）与`## Genre`；`project_bible.md`的`媒介形式` / `目标形式` / `Project Information`；用户当前请求。事实由用户与已确认项目材料拥有
- **Output Owner**：本层不产出文件；产出为`Production-Locked Directable Screenplay + WRITER INTENT PACKET`，其用户可见形态归`templates/02_script_analysis_prompt.md`
- **Read / Write Boundary**：只读用户输入与已确认项目事实；只把路由结论交给STATE-01 Workflow。不修改资产、Visual Direction、SHOT、CLIP、Portable Schema或项目状态字段
- **Downstream Consumers**：`knowledge/director_decision_layer.md`、STATE-05 / 06 / 07 / 08、Editing与State-09 Story Review
- **Conflict Route**：需求未确认、为`Pending`或互相冲突时，保持STATE-01 IN_PROGRESS并记录Pending Decision；不得为推进而推定品牌诉求、受众、平台或目标形式
- **Deterministic Invariants**：Roster登记项与文件一一对应；路由按需求逐项命中；本层不复述任何创作判据；需求保真判定在Proposal输出前完成；本层不创建STATE、不新增Template字段、不新建节拍模型

## The Roster

| # | File | 拥有什么 | 何时进入 |
|---|---|---|---|
| 1 | `knowledge/writer/screenplay_development.md` | 故事逻辑、人物与关系、冲突与代价、信息架构、Setup/Payoff、工艺手册、Directable Screenplay QA与可失败判定、`## Client Brief And Commercial Fact Gate｜客户与商业事实门`、`## Requirement Fidelity` | 所有叙事项目；STATE-01主要创作与诊断位置 |
| 2 | `knowledge/writer/screenwriting_optimization.md` | 授权后的优化方法：十二项诊断维度、最小干预阶梯、Scope Fence | 明确优化授权之后 |
| 3 | `knowledge/writer/script_adaptation.md` | 通用六层改编方法与Fidelity Check | C类Source Material获准改编之后 |
| 4 | `knowledge/writer/directorial_interpretation.md` | 剧本层的导演化处理：观众如何经历已成立的信息与情绪 | Writer → Director Handoff之后 |
| 5 | `knowledge/adaptation/short_form_drama_adapter.md` | 短剧 / 竖屏 / 1—3分钟的Hook窗口、五段功能、单集容量与角色识别卡 | 目标形式确认为上述三类时（加载入口见`## Requirement Router｜需求路由`） |

本表是编剧层的**唯一登记处**：新增文件必须同时在此登记，且文件与登记项一一对应。

### Growth Boundary｜体量边界

编剧层新增内容前先看这一节，它记录本层当前的**物理容量约束**，避免下一次改动直接撞上`references/context_budget.md`的复核线。

| 文件 | 本次实测 | 状态 |
|---|---|---|
| `knowledge/writer/screenplay_development.md` | 46,067 B = 复核线 50 KB 的 **90.0%** | **余量不足 4 KB，不得再作为新内容的落点** |
| `knowledge/writer/index.md`（本文件） | 13,169 B ≈ 26% | 可承接路由与边界层内容 |
| 回归语料`references/regression_scenarios_craft.md`（99.6%）与`references/regression_scenarios.md`（98.3%） | 均已逼近复核线 | 新增回归场景前必须先做瘦身 |

**分配纪律**：

- 创作判据的补充仍归`screenplay_development.md`所属owner，但**新内容不得落入该文件**；它已承载故事逻辑、工艺手册、两道判定门与商业事实门，再增即越线。
- 新内容按性质分配：**路由与边界**进本文件；**新的判据族**新开`knowledge/writer/`下的文件并在`## The Roster`登记。
- 越过复核线时按`references/context_budget.md`的`### 瘦身优先序`在**同一次变更内**瘦身；**只把内容搬到另一个文件不算瘦身**。
- 本节的字节数为**实测值**，与登记值差异超过20%即视为过期，须在同一次变更内更新。

## Requirement Router｜需求路由

**这是本层的核心**：agent拿到一份需求后，按左列逐项判定，只读右列命中的节。未命中的一律不读。

| 需求维度（来自已确认事实） | 读哪里 |
|---|---|
| **交付语境**（自制 `self_initiated` / 委托 `client_commissioned`） | 它决定商业事实的**来源归属**与本节其余各项是否适用：`templates/00_project_start_template.md`的 Client Brief 节。`self_initiated`且**无品牌诉求** → 该节整节（含业务目标与主传达目标）写`Not Applicable`、一个字段都不填，按**自制短片**走通用编剧判据；`self_initiated`且**有自有品牌** → 只填自有品牌事实，审批链写`用户（品牌方）`，不产生第二个确认主体；`client_commissioned` → 全节适用，含外部审批链。**不得把"有品牌"等同于"有客户"** |
| **交付物与规格**（客户未指定时） | **客户通常不规定参数**：由制作按目标形式与已提供平台提议并标注`制作建议｜待确认`，在STATE-01 `Production Setup Gate`随媒介与目标形式确认（见`workflows/02_script_analysis_workflow.md`的`### Target Form Confirmation`）；不得留空、不得静默采用。交付参数由制作提议，**平台事实仍由用户提供**：`templates/00_project_start_template.md`的 Client Brief 节 |
| **主传达目标**（多个卖点） | 排序为一条注意焦点链、被降级卖点的承担者、不可执行项的回报：`knowledge/writer/screenplay_development.md`的`## Client Brief And Commercial Fact Gate｜客户与商业事实门`与`knowledge/branded_content/01_brand_requirement_translation.md`的`## Conditions And Anti-Use｜成立条件与反用` |
| **商业形态**（宣传 / 科普 / 产品 / 案例 / 招商 / 雇主品牌） | 该形态"必须让观众看见什么"与科普的结论纪律：`knowledge/branded_content/05_commercial_format.md` |
| **产品在剧情中的角色**（主角型 / 使能型 / 背景型） | `knowledge/branded_content/01_brand_requirement_translation.md`的`## Executable Vocabulary｜可执行词汇`与`knowledge/branded_content/02_product_legibility_and_claims.md` |
| **受监管表述与资质**（功效 / 价格 / 免责声明 / 授权人物或声音） | 只能原样内置或留后期叠加；位置由制作决定、内容由客户提供：`knowledge/writer/screenplay_development.md`的`## Client Brief And Commercial Fact Gate｜客户与商业事实门`第6项与`knowledge/branded_content/index.md`的`## Commercial Fact Discipline｜商业事实纪律` |
| **决策链角色**（决策者 / 使用者 / 影响者 / 代决策者） | 说服路径落点：`knowledge/branded_content/04_commercial_audience.md`；年龄轴优先于角色轴：`knowledge/audience_profiles.md` |
| **目标形式**（短剧 / 竖屏 / 1—3分钟 / 其他） | 命中前三类时：`knowledge/adaptation/short_form_drama_adapter.md`。**加载入口只有两个**——`workflows/02_script_analysis_workflow.md`的`### Adaptation Target Detection`（素材改编路径）与`### Target Form Confirmation`（生产准备路径）；本文件是路由说明，**不是第三个加载入口** |
| **原创 / 已有剧本 / 来源素材** | 入口路由与授权边界：`workflows/02_script_analysis_workflow.md`的`## Screenplay Entry Routing, Creation, Adaptation And Optimization Gate`；C类改编方法见`knowledge/writer/script_adaptation.md` |
| **类型**（已登记时） | `knowledge/genre/index.md`的`## Loading Rule`，再读命中的类型剖面；未登记时不加载、不推定 |
| **媒介形式**（已确认时） | 信息承载方式：`knowledge/medium_profiles.md`的Screenwriter Layer；媒介为`2d_anime`时按它决定什么必须外化为可见动作、符号化表情或OS |
| **受众**（已声明时） | 适宜性、理解难度与表演声音尺度：`knowledge/audience_profiles.md`；未声明时不加载分化表 |
| **需要结构 / 人物 / 场景 / 对白手段时** | `knowledge/writer/screenplay_development.md`的`## Craft Manual｜工艺手册`的对应小节（`### 结构操作`、`### 人物构建`、`### 场景与对白技法`）；**按当前场景只取所需条目**，条目只在其`成立条件`满足时使用 |
| **需要判断删并改排、或已获优化授权时** | `knowledge/writer/screenwriting_optimization.md` |
| **需要导演化处理时** | `knowledge/writer/directorial_interpretation.md` |
| **跨阶段保护（Writer Beat、Setup/Payoff、信息时机）** | `knowledge/writer/screenplay_development.md`的`## Cross-stage Projection`与`## Writer → Director Handoff` |

**路由纪律**：左列每命中一项，右列即成为本次的读取义务；未命中的不读。左列为`Pending`时按`## Return Routing`处理，**不得用"题材相似""时长相近""平台像短视频"之类的近似替代命中的真实事实**。

## Shared File Schema

编剧层每个文件必须齐备以下小节，缺任一项即视为未完成，不得入册：

| # | 小节 | 必须回答 |
|---|---|---|
| 1 | `# Read Scope` | 本文件按什么事项只读哪些节；不得整文件通读 |
| 2 | `## Module Contract` | 本文件拥有什么、Trigger、Not Triggered As、Required Inputs、Output Owner、Downstream Consumers、Conflict Route、Deterministic Invariants |
| 3 | `## Completion Check` | 本文件的工作何时算完成；输出前必须核对什么 |
| 4 | 边界声明 | 不拥有什么、与哪个相邻owner不重合、不创建STATE与Template字段 |

`knowledge/adaptation/short_form_drama_adapter.md`按其自身既有的`## Purpose And Trigger`、`## Acceptance Checklist`与边界声明满足第1—4项，不重复改写。

## Validator-Checkable Invariants

- `## The Roster`登记的文件必须真实存在，且编剧层不得存在未登记的文件（登记项与文件一一对应）。
- 每个登记文件必须齐备`## Shared File Schema`列出的四类小节。
- `## Requirement Router｜需求路由`必须存在，且不得成为短剧Adapter的第三个加载入口。
- 本文件不得复述任何创作判据、阈值、条目正文或秒数。
- 不创建STATE、不新增Template字段、不新建节拍模型的声明必须存在。

## Non-Applicable Rule

- 非叙事项目（纯平面、纯音乐、纯资产返修）不进入本层。
- 品牌诉求、受众、平台、目标形式、类型均未确认时，本层只读`## Requirement Router｜需求路由`以确认缺什么并记录Pending Decision，不加载任何分化表。
- 本层不适用于Storyboard、Poster、MUSIC、AUDIO等辅助模块的既有边界。

## Return Routing

- 品牌诉求、商业事实或受众角色未确认 → `templates/00_project_start_template.md`的`# Client Brief｜客户与商业 brief`与STATE-01 Creation Brief；不得由本层代替用户确认
- 目标形式或媒介未确认 → STATE-01的`Production Setup Gate`的`### Target Form Confirmation`与媒介确认；两者为`Pending`时不得进入STATE-02
- 类型未登记 → STATE-00的项目登记；不得由本层推定类型
- 需求与已锁定剧本冲突 → `knowledge/writer/screenplay_development.md`的`## Proposal And Revision Handoff`
- 创作判据疑问 → `## The Roster`中对应文件的owner
- 归属冲突 → `knowledge/writer/screenplay_development.md`的`## Route Boundary`
