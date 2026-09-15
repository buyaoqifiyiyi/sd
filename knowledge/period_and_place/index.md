# SD Film Period And Place｜时代与地域

# Read Scope

本文件是时代与地域层的中枢入口，**不得整文件通读**：按当前事项只读对应小节。

| 当前事项 | 只读 |
|---|---|
| 判定该不该读本域 | `## Purpose And Boundary`、`## Loading Rule` |
| 定位当前需要哪个原子 | `## The Roster` |
| 区分"已确认事实 / 推断 / 不可确认" | `## Evidence Discipline｜考据纪律` |
| 写新的原子文件 | `## Shared Atom Schema`、`## Validator-Checkable Invariants` |
| 不适用 / 返回路由 | `## Non-Applicable Rule`、`## Return Routing` |
| 不必在运行时读取 | `## Validator-Checkable Invariants` |

---

## Purpose And Boundary

本域拥有**已确认的时代背景与地域如何约束画面上的可见事实**：器物与技术可用性、服装形制与材料、文字与标识、照明与交通通讯条件、称谓与身体语言、习俗与日常器物，以及**时代错置（anachronism）**的判据与不确定性的标注方式。

**它不拥有**：剧情事实、World Setting（项目事实由用户与已确认项目材料拥有，记录在`templates/01_project_bible_template.md`的`# 2. World Building`）、视觉风格与美学方向（STATE-04）、媒介分化（`knowledge/medium_profiles.md`）、类型呈现（`knowledge/genre/index.md`）、资产身份（对应资产owner），以及任何STATE、Template字段或STATE-08最终Schema。

**与`knowledge/visual_styles/`的边界**（两者极易被误当重复）：

- 风格层说的是**风格纪律**：不要因为引用了某个导演就把项目改成古装、雨夜或武士片——那是"不得擅自添加时代符号"。
- 本域说的是**事实纪律**：项目已确认是这个时代与地域时，画面里**什么能出现、什么不能出现**。

两者互补：风格层禁止无依据地引入符号，本域约束已确认前提下的可见物。任何一条都不得被另一条替代。

它属于**条件性Knowledge**，与`knowledge/medium_profiles.md`同类：只在时代或地域已登记时加载。

## Loading Rule

**触发**：`templates/01_project_bible_template.md`的`# 2. World Building → ## Time Period`（时代背景）或`## Location System`（主要地点）已登记时加载——登记值来自用户或已确认项目材料。

**未登记**：记`Period And Place: PENDING`，不加载任何原子，也不得**从媒介、类型、平台、导演风格名、参考片或资产外观推定**时代与地域。目标形式或题材相似不构成推定依据。

**读取范围**：只读当前命中的原子，按各原子的章节标题定点读取；不整域通读。时代与地域都有登记时，两个原子都读，但以**时代**约束硬事实、以**地域**约束习惯与语境，冲突时时代优先并记录让位。

## Evidence Discipline｜考据纪律

本域所有结论必须落在下列三类之一，混类是主要失败来源：

| 类别 | 定义 | 使用方式 |
|---|---|---|
| **已确认来源** | 用户提供、已确认项目材料或可核对的公开参考 | 可写成项目事实，进入资产与Prompt |
| **合理推断** | 由已确认时代/地域常识性推导，但无给定来源 | **必须显式标注为推断**；可用于设计，不得写成"史实" |
| **不可确认** | 具体年号与纪年、真实机构与官职、真实人物、真实事件、真实品牌、精确器物型号与工艺参数 | 不得写成事实；需要时改为不指向真实的等价物 |

- **不得把常识当史实。** 观众能识破的错误（现代物件、字体、标志、工艺）比"不够考据"伤害更大。
- **真实历史人物、真实机构、真实事件与真实品牌是一等禁项**，与`rules/automation_mode.md`的Hard Stop同一口径：不因"时代需要"而放宽。
- 不确定时按"不指向真实"的方向降级，并在内部记录该降级；不得用虚构的精确细节冒充考据。

## The Roster

| # | Atom | File | 拥有什么 |
|---|---|---|---|
| 1 | 时代的可见约束 | `knowledge/period_and_place/01_era_visibility.md` | 器物与技术可用性、服装形制、文字与标识、照明与交通通讯条件在画面上的允许与禁止 |
| 2 | 地域与文化 | `knowledge/period_and_place/02_place_and_culture.md` | 空间组织、称谓与语言、身体语言与社交距离、日常器物与习俗的可见面 |
| 3 | 时代一致性与错置 | `knowledge/period_and_place/03_period_consistency.md` | 时代基线向CHAR / ENV / PROP / 声音的投影、跨镜一致性、时代错置判据 |

本表是原子的**唯一登记处**：新增原子必须同时在此登记，文件与登记项一一对应。

## Shared Atom Schema

每个原子文件必须按下列固定小节组织，缺任一小节即视为未完成，不得入册：

| # | 小节 | 必须回答 |
|---|---|---|
| 1 | `## Purpose And Owner` | 本原子回答什么、边界在哪、与哪个相邻owner不重合 |
| 2 | `## Visible Constraints｜可见约束` | 维度 → 该时代/地域的允许与禁止 → **写进哪个既有字段** |
| 3 | `## Conditions And Anti-Use｜成立条件与反用` | 每条约束的成立条件、不成立时怎么办 |
| 4 | `## Uncertainty Marking｜不确定项标注` | 本原子涉及的推断项如何标注、不可确认项如何降级 |
| 5 | `## Failure Signals｜失败信号` | 可观察的失效表现 |

## Shared Invariants

时代与地域**不改变**以下任何一项：

- Story First、Asset First、镜头必须服务剧情
- **反刻板**：地域不得靠符号清单表达（灯笼、斗笠、和服、纱窗一类单件符号既可能时代不符，也会把地域压成标签），优先用空间关系、称谓、身体距离与日常器物；展开见`knowledge/period_and_place/02_place_and_culture.md`
- STATE-00至STATE-09主Pipeline、Completion Gate与推进规则
- 资产双确认、Canonical Lock与连续性纪律
- 媒介剖面、类型剖面与导演风格三条轴：与时代地域**正交**，任一条不得覆盖另一条
- STATE-08最终Prompt字段与Template：不因时代新增任何字段
- REF-TAIL A/B/C、REF-SKETCH边界、Voice opt-in，以及**视频Prompt永久禁止非剧情内配乐**
- 真实人物、机构、事件与品牌的Hard Stop

## Return Routing

- 时代或地域未登记、冲突或无法确认 → STATE-00的项目登记与`templates/01`的World Building字段；不得由本域代替用户确认
- 剧情事实、世界设定本身 → Writer Owner与已确认项目材料
- 项目级美学方向 → STATE-04
- 资产身份与形制细节的最终仲裁 → 对应资产owner与`references/asset_lock_contract.md`
- 媒介表达在非实拍档不成立 → `knowledge/medium_profiles.md`
- 时代符号与导演风格的冲突 → `knowledge/visual_styles/index.md`（风格层只作研究来源，不改写时代事实）

## Non-Applicable Rule

- 时代与地域均为`PENDING`：不加载任何原子，不写`Period And Place`结论，也不得按某个默认时代（"现代"）推进——现代同样是需要确认的事实；需要时代才能成立的资产、服装、道具或照明选择记为待定并返回登记处补正。
- 现代题材同样适用：当代项目的时代约束表现为**技术、服饰、标识与语言必须与当下一致**，不是"无需考据"。
- 本域不适用于Poster、MUSIC、AUDIO等辅助模块的既有边界；音乐的时代/地域框架由`knowledge/music_score/music_bible_and_cues.md`拥有。
- 本域不创建STATE、不新增Template字段、不改变任何Model Adapter能力与能力数值。

## Validator-Checkable Invariants

- `## The Roster`登记的原子文件必须真实存在，且`knowledge/period_and_place/`下不得存在未登记的原子文件（登记项与文件一一对应）。
- 每个原子必须齐备`## Shared Atom Schema`列出的五个小节。
- `## Evidence Discipline｜考据纪律`必须存在，且必须包含三类证据划分与真实人物/机构/事件/品牌的一等禁项。
- 与`knowledge/visual_styles/`的边界声明必须存在（风格纪律 vs 事实纪律）。
- 不新增STATE-08字段、不改变主Pipeline的声明必须存在。
- "不得推定时代与地域"的声明必须存在。
