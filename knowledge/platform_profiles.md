# SD Film Platform Profiles

# Read Scope

本文件被多个阶段复用，**不得整文件通读**：按当前事项只读对应小节。

| 当前事项 | 只读 |
|---|---|
| 判定该不该读本文件 | `## Purpose And Boundary`、`## Selection And Ownership` |
| 登记或确认平台事实 | `## Selection And Ownership`、`## Profile Fields｜平台剖面字段` |
| 开场与注意窗口 | `## Note Window Layer｜注意窗口` |
| 完播语义与系列连续性 | `## Completion And Series Layer｜完播与系列` |
| 结尾动作与转化落点 | `## Conversion Landing Layer｜转化落点` |
| 静音、首帧与包装 | `## Silent Playback And Packaging Layer｜静音与包装` |
| 不适用 / 返回路由 | `## Non-Applicable Rule`、`## Return Routing` |
| 不必在运行时读取 | `## Validator-Checkable Invariants` |

---

## Purpose And Boundary

本文件拥有**发布平台剖面**：同一套叙事内核在不同发布平台的注意结构与交付结构下必须如何分化。

它回答一个问题：**在观众离开之前的那个窗口里，故事必须已经交付了什么。**

它**不拥有**：

- **平台事实本身**——任何平台的推荐机制、算法偏好、时长上限、审核与分级条文、画幅尺寸数值、封面尺寸、话题与标签规则、投放与留资要求，都是**外部事实**，必须由用户提供或引用可核对来源。本文件不虚构平台规则、不声称"符合"任何平台的推荐机制，也不提供可以套用的"平台模板"。**它也不是分级或审核制度本身。**
- 剧情事实与故事结构（Writer Owner与`knowledge/screenplay_development.md`）。
- 媒介分化（`knowledge/medium_profiles.md`）、受众适宜性与理解难度（`knowledge/audience_profiles.md`）、类型承诺（`knowledge/genre/index.md`）、时代与地域（`knowledge/period_and_place/index.md`）。
- 目标形式的节拍与硬门：短剧 / 竖屏剧情 / 1—3分钟的Hook窗口与五段模型仍由`knowledge/adaptation/short_form_drama_adapter.md`拥有，本文件不新建第二套节拍模型，也不复述其秒数判据。
- 商业诉求与商业事实（`knowledge/branded_content/index.md`）。
- 画幅构图判据（`knowledge/camera_language/composition_language/vertical_framing.md`）与海报封面判据（`knowledge/poster_design/index.md`）。

它属于**条件性Knowledge**，与`knowledge/medium_profiles.md`、`knowledge/audience_profiles.md`同类：只在交付渠道已由用户或已确认项目材料声明时加载。

## Selection And Ownership

平台不是一个需要被猜出来的值，而是**已确认的交付事实**：它由用户或已确认项目材料给定，登记在`project_bible.md`的`## Delivery Spec｜交付规格`。

判定纪律：

- **不得推定平台**：媒介是动画、题材像广告、时长很短、画风像某一站的内容、客户在某个行业，都不构成"这是给某平台做的"的依据。
- 未声明时记`Platform Profile: PENDING`，**不加载任何分化层**，按既有通用行为继续，也不得登记为已确认的平台剖面。
- **本文件不拥有平台事实**：它只拥有"事实给定之后如何分化"。任一平台的机制、上限、条文或尺寸数值缺失时记Pending Decision，不猜、也不用"这类片子一般是这样"补齐。
- 平台与媒介、类型、受众、时代地域四条轴**正交**：任一轴不得覆盖另一轴，任一轴也不得静默抹掉另一轴。

## Profile Fields｜平台剖面字段

以下字段是**用户或已确认交付规格提供的事实**，不是本文件生成的值。缺失项按Pending Decision记录；其中`平台标识`缺失时整个分化层不加载：

| 字段 | 它是什么 | 缺失时的处置 |
|---|---|---|
| `平台标识` | 发布渠道的准确名称 | 记`Platform Profile: PENDING`，不加载分化层 |
| `注意窗口` | 观众在离开前实际给出的时间 | 不得用"一般是多少秒"代替；按`## Note Window Layer`执行，不自行填值 |
| `完播语义` | 单条独立看完 / 循环 / 需要连续追看 | 未确认时按**单条独立**处理，不预设系列义务 |
| `结尾动作` | 平台内可执行的下一步动作（关注、评论、私信、主页、留资、外链等） | 未给定时不写转化动作，只保留故事层兑现 |
| `静音默认` | 是否默认静音自动播放 | 未确认时按**可能静音**处理 |
| `画幅与安全区` | 交付画幅与界面遮挡区 | 路由到`vertical_framing.md`，本文件不复述其判据 |
| `本批交付量` | 本批需要交付的条数 | 只影响系列连续性判断，不改变单条结构 |

## Note Window Layer｜注意窗口

注意窗口来自`## Profile Fields`，不是本文件设定的秒数。窗口内必须已经成立：

| 维度 | 分化要求 | 写进哪个既有字段 |
|---|---|---|
| 主要矛盾的进入 | 在注意窗口内进入主要矛盾，而不是仍在介绍人物、世界或日常过程 | Writer Beat Map（`knowledge/screenplay_development.md`） |
| 第一屏的建立 | 窗口内的开场必须已建立异常、欲望、危机、关系张力或视觉问题之一；本文件不复制短剧适配器的五类判据与其硬门 | 动作描述、`构图` |
| 建立性信息预算 | 人物、关系、规则与日常过程只保留理解核心事件所需的最小量 | Writer Beat Map、`时长` |
| 核心目标的推迟 | 核心目标与阻力不得因前置说明被推迟到窗口之后 | Writer Beat Map |
| 静音可读 | 按`## Silent Playback And Packaging Layer`处理，不在本层重复 | `声音`、动作描述 |

## Completion And Series Layer｜完播与系列

按`完播语义`分化：

| 完播语义 | 结尾义务 | 边界 |
|---|---|---|
| 单条独立看完 | 结尾完成本段兑现，并留下余韵或收束 | 不强制留下未完成欲望 |
| 循环 | 结尾必须能无损接回开场，且接回后不产生因果矛盾 | 不得为循环牺牲已建立的因果 |
| 需要连续追看 | 结尾保留未完成欲望、信息缺口、新危机或关系升级 | Hook不得凭空推翻已建立因果或Protected Creative Locks |

不论哪一档：**需要连续追看时，每一条仍必须能被单独理解**；单集独立性不得以牺牲本段兑现为代价。系列发行的批量试错策略只在用户目标为系列且明确需要平台测试时记录，不改写单条结构。

## Conversion Landing Layer｜转化落点

本层只处理**结构位置**，不提供任何平台的可执行动作清单：

- **转化动作是Payoff义务，不是落版字卡**：`结尾动作`必须由可见行为或状态收束（完成、交付、使用后的结果、关系变化），不得靠文字落版单独承担。
- **位置固定**：转化动作落在故事兑现**之后**，不得替代兑现，也不得提前泄掉核心悬念。
- **未给定不发明**：`结尾动作`未由用户或已确认交付规格给定时，不写转化动作，也不得自行选择"看起来更好卖"的那一个。
- **文字级元素**：二维码、价格、免责声明、入口文案、精确Logo默认按"优先后期叠加"处理，不写进模型生成承诺；其内容必须由客户提供。
- **不改写剧情**：转化落点不得成为改写Production-Locked Script、Canonical资产或已确认Blocking的理由。

## Silent Playback And Packaging Layer｜静音与包装

| 维度 | 分化要求 | 写进哪个既有字段 |
|---|---|---|
| 静音默认 | 按**可能静音**处理时，注意窗口内的关键信息不得只由台词承载；非实拍媒介下的承载外化仍按`knowledge/medium_profiles.md`执行，本文件不复述其判据 | 动作描述、`声音` |
| 首帧 | 首帧必须与注意窗口内的第一注意目标一致，不得用一个与故事无关的抓眼画面换取停留 | `构图`、第一注意目标 |
| 标题与承诺 | 标题、封面文案不得承诺故事不兑现的内容；与Genre Promise一致 | `主风格`、Genre Profile |
| 封面与封面尺寸 | 路由到`knowledge/poster_design/index.md`；本文件不复述其判据，也不把渠道差异当作受众分化 | 对应Template |
| 画幅安全区 | 按`knowledge/camera_language/composition_language/vertical_framing.md`执行 | `构图` |

## Shared Invariants

平台剖面**不改变**以下任何一项：

- Story First、Asset First、镜头必须服务剧情
- STATE-00至STATE-09主Pipeline、Completion Gate与推进规则
- 资产双确认、Canonical Lock与连续性纪律
- 媒介、类型、受众、时代地域四条轴
- STATE-08最终Prompt字段与Template：不因平台新增任何字段
- 视频Prompt永久禁止非剧情内配乐
- 真实人物、真实机构、真实事件与真实品牌的Hard Stop
- 不得虚构平台规则，不得声称符合任何未确认的平台机制或分级体系

## Return Routing

- 平台事实缺失、冲突或需要确认 → 用户与已确认项目材料 / `project_bible.md`的`## Delivery Spec｜交付规格`；记Pending Decision
- 注意窗口或结尾义务与剧情事实冲突 → Writer Owner；**不得为平台静默改写已锁定剧本**
- 目标形式的Hook窗口与节拍模型 → `knowledge/adaptation/short_form_drama_adapter.md`
- 画幅与安全区构图 → `knowledge/camera_language/composition_language/vertical_framing.md`
- 封面、标题落版与尺寸 → `knowledge/poster_design/index.md`
- 品牌诉求、商业事实与影片形态 → `knowledge/branded_content/index.md`
- 媒介承载分化 → `knowledge/medium_profiles.md`
- 受众适宜性与理解难度 → `knowledge/audience_profiles.md`
- 项目级美学方向 → STATE-04；剧情事实 → Writer Owner

## Non-Applicable Rule

- 平台未声明：不加载任何分化层，按既有通用行为继续；不得登记为已确认的平台剖面，也不得据此在Prompt或剧本里补写平台专属结构。
- 本文件不适用于Poster、MUSIC、AUDIO等辅助模块的既有边界；海报的渠道差异由`knowledge/poster_design/index.md`拥有。
- 本文件不创建STATE、不新增Template字段、不改变任何Model Adapter能力与能力数值。
- 本文件不提供任何平台的算法、审核、时长上限或尺寸数值；这类问题一律返回用户与可核对来源。

## Validator-Checkable Invariants

- `## Profile Fields｜平台剖面字段`、`## Note Window Layer｜注意窗口`、`## Completion And Series Layer｜完播与系列`、`## Conversion Landing Layer｜转化落点`、`## Silent Playback And Packaging Layer｜静音与包装`五节必须同时存在。
- "不得推定平台"与`Platform Profile: PENDING`的声明必须存在。
- "平台事实属外部事实、不得虚构平台规则、不声称符合任何未确认平台机制"的声明必须存在。
- 与媒介、类型、受众、时代地域四条轴正交的声明必须存在。
- "不新建节拍模型、短剧节拍仍由`knowledge/adaptation/short_form_drama_adapter.md`拥有"的声明必须存在。
- "不得为平台静默改写已锁定剧本"的声明必须存在。
- "不新增STATE-08字段、不改变主Pipeline、不改变Model Adapter能力数值"的声明必须存在。
- 视频Prompt永久禁止非剧情内配乐的声明必须存在。
