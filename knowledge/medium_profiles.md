# SD Film Medium Profiles

# Read Scope

本文件被多个阶段复用，**不得整文件通读**：按当前层级只读对应小节。

| 当前事项 | 只读 |
|---|---|
| 剧本层 | `## The Three Profiles`、`## Selection And Ownership`、`## Screenwriter Layer` |
| 导演层 | `## Director Layer`、`## Shared Invariants` |
| 视觉层 | `## Aesthetic Layer`、`## Cross-Medium Asset Rule` |
| 不适用 / 返回路由 | `## Non-Applicable Rule`、`## Return Routing`、`## Validator-Checkable Invariants` |
| 不必在运行时读取 | `## Purpose And Boundary` |

---

## Purpose And Boundary

本Knowledge定义**媒介剖面**：同一套叙事内核在不同画面生成基础下必须如何分化。

它回答一个问题：**镜头、表演与美学语言中，哪些随媒介改变、哪些不改变。**

它**不拥有**：故事结构、剧情事实、资产身份、STATE推进、Completion Gate、任何Template字段或STATE-08最终Prompt Schema。

它属于**条件性Knowledge**，与`knowledge/adaptation/short_form_drama_adapter.md`同类：只在媒介已确认时加载，未确认时不加载、不猜测、不默认。

## The Three Profiles

| Profile ID | 画面生成基础 | 摄影机的存在 |
|---|---|---|
| `live_action` | 真实光穿过光学镜头，被感光介质记录 | 物理摄影机 |
| `3d_animation` | 几何体与材质被虚拟摄影机渲染 | 虚拟摄影机（物理规律成立） |
| `2d_anime` | 线条与色块被绘制成版面 | **不存在摄影机** |

三档沿「**摄影 → 绘画**」排列，但**间距不相等**：`3d_animation` 与 `live_action` 共享"画面由光生成"这一前提，差距小；`2d_anime` 不共享该前提，差距大。

因此本文件对三档的处理强度不同：

- `live_action` 是基准，既有知识全部适用。
- `3d_animation` 只覆盖少数维度，其余继承既有实拍知识。
- `2d_anime` 覆盖最多维度，并**禁用**一批实拍专有参数。

## Selection And Ownership

媒介由STATE-00确认并存于`project_bible.md`的`Project Information → 媒介形式`字段；本文件拥有该字段的**值域**与三档分化规则。

判定：只记录用户直接提供或可从素材直接确认的媒介；不得从Genre、题材、平台或画风标签推定。用户只说“动画”而未指明维度时写`Pending`并询问一次。

未确认时保持`Pending`，按`live_action`的既有行为继续，但不得登记为已确认真人剧。

**媒介与Genre正交。** Genre（爱情/动作/悬疑）不决定媒介，媒介也不改变Genre承诺。两者不得互相覆盖。

## Screenwriter Layer

信息由什么承载：

| 维度 | `live_action` | `3d_animation` | `2d_anime` |
|---|---|---|---|
| 信息主载体 | 表演：微表情、停顿、潜台词 | 表演：绑定表现力 | **外化**：可见动作、表情、OS |
| 留白容忍 | 高 | 中 | **低** |
| 内心与OS | 例外手段 | 少用 | 常规手段 |
| 对白密度 | 可稀疏 | 可稀疏 | 须高密度，或逐句转为可见动作 |
| 硬边界 | 不写演员演不出的 | 不写绑定做不出的 | **不写画不出的** |

`2d_anime` 下，任何依赖微表情层次、沉默留白或未言明潜台词承载的信息，必须改写为可见动作、符号化表情或OS。写了但画不出来、或画出来观众读不到，等同于信息缺失。

`3d_animation` 下的表演边界由**绑定表现力**决定，不由演员决定；不得把真人表演细节直接写成执行要求。

## Director Layer

镜头语言建立在什么约束上：

| 维度 | `live_action` | `3d_animation` | `2d_anime` |
|---|---|---|---|
| 焦段 / 景深 | 成立（光学） | 成立（虚拟光学） | **不适用**；注意引导改用主体大小对比与画面疏密 |
| 光比 | 成立 | 成立（打光） | **不适用**；明暗关系改用色块明度对比 |
| 摄影机运动 | 成立 | 成立 | **降级为版面位移**（推拉摇移的版面等效） |
| 构图 / 景别 / 轴线 | 成立 | 成立 | 成立（抽象规则，跨媒介有效） |
| 时间表达 | 快门、帧率、运动模糊 | 帧率、渲染运动模糊 | **帧感**：关键帧—中割取舍；静止即停格 |
| 独有手段 | 景深虚化、镜头瑕疵 | 超物理运动、无重力 | smear frame、impact frame、版面切割、留白 |

**`2d_anime` 禁止项**：不得为该档镜头指定焦段毫米数、光比比值、轨道/摇臂设备、稳定方式或真实景深。这些在绘制媒介中没有对应物，写入只会污染Prompt并误导生成，必须改用本表给出的等效表达。

`3d_animation` 的例外：摄影机必须遵守虚拟空间物理（除非剧本授权超物理运动），且"光的性质"从捕捉变为设计——打光与渲染属于本档，不属于`live_action`的既有光比语言。

## Aesthetic Layer

美学参数用什么维度描述：

| 维度 | `live_action` | `3d_animation` | `2d_anime` |
|---|---|---|---|
| 核心参数 | 光与材质 | 材质与渲染 | 线与色 |
| 词表示例 | 胶片颗粒、色温、光比、肤质 | 材质质感、着色风格、环境光遮蔽 | 线宽、色指定、上色法、网点 |
| 一致性锚 | 五区角色资产图 + Immutable Traits | 模型 + 材质 + 绑定 | 角色设定集 + 画风锚 |
| 典型失败 | 生成漂移、脸崩手崩 | 恐怖谷、材质塑料感 | 画风漂移、线宽不一致、色指定失真 |
| “低饱和”的落法 | 低饱和胶片 + 灰调光 | 低饱和材质 + 去饱和渲染 | 低饱和色指定 + 灰调上色 |

同一美学意图在三档下必须**换词表达**。不得把 `live_action` 的词表直接用于另外两档：`2d_anime` 不承认胶片颗粒、次表面散射或镜头暗角作为美学载体，其对应物分别是网点/笔触、上色法与留白。

**资产形态也随媒介分化**：`live_action` / `3d_animation` 的角色正式资产为五区资产图；`2d_anime` **不套用**该结构，其角色资产是设定集与画风锚。结构与判据细节归`templates/04_character_asset_prompt.md`，本文件只声明适用档位。

## Shared Invariants

媒介剖面**不改变**以下任何一项：

- Story First、Asset First、镜头必须服务剧情
- STATE-00至STATE-09主Pipeline、Completion Gate与推进规则
- 资产双确认、Canonical Lock与连续性纪律——**载体**按档切换，纪律不变
- STATE-08最终Prompt字段与Template：不因媒介新增任何字段
- REF-TAIL A/B/C、REF-SKETCH边界、Voice opt-in与视频Prompt永久无BGM
- Writer / Director职责分工

## Cross-Medium Asset Rule

一个媒介的资产**不得静默用于**另一个媒介。跨档复用必须重建资产或经用户明确确认，因为：

- `live_action` 与 `3d_animation` 的角色身份可由图像参考延续，但材质与绑定事实需要重建。
- `2d_anime` 的角色一致性锚是设定集与画风，实拍五区角色资产图不构成其Canonical依据。

## Return Routing

- 媒介决定本身缺失或冲突 → STATE-00（`媒介形式`字段的写入owner）
- 资产身份或Canonical冲突 → 对应资产拥有者
- 逐镜镜头语言冲突 → STATE-06
- 项目级美学方向冲突 → STATE-04

## Non-Applicable Rule

- 未确认媒介：记`Medium Profile: PENDING`，不加载本文件的分化表，按`live_action`既有行为继续。
- 本文件不适用于Storyboard、Poster、Sequence、MUSIC、AUDIO等辅助模块的既有边界；它们各自既有owner不变。
- 本文件不创建STATE、不新增Template字段、不改变任何Model Adapter能力。

## Validator-Checkable Invariants

- 三档ID固定为`live_action`、`3d_animation`、`2d_anime`，不得新增第四档或改名。
- 三张分层表（Screenwriter / Director / Aesthetic Layer）必须同时存在。
- `2d_anime`禁止项必须显式列出。
- 与Genre正交的声明必须存在。
- 不改变STATE-08 Schema的声明必须存在。
