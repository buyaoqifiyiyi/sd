# SD Film Production Delivery Package

# Read Scope

本文件被多个阶段复用，**不得整文件通读**：按当前事项只读对应小节。

| 当前事项 | 只读 |
|---|---|
| 图片文件名怎么起、锁定时机 | `## Asset Image Naming`, `## Naming Lock And Rename` |
| 打包时机、交付什么 | `## Package Timing And Delivery`, `## Package Contents` |
| 哪些东西才允许进包 | `## Package Admission｜只收已认可的` |
| 当前环境能不能打包、不能时给什么 | `## Access Precondition` |
| 包放在哪、原文件动不动 | `## Package Location And Source Rule` |
| 与最终视频 Prompt 的一一对应 | `## Final Prompt Correspondence` |
| 校验与失效 | `## Verification And Invalidation` |
| 可选工具 | `## Optional Interoperable Tooling` |
| 不必在运行时读取 | `## Purpose`, `## Final Principle` |

---

## Purpose

本文件拥有**生产交付包**（Production Delivery Package）的构成、资产图片文件名规范、来源规则与对应性校验；它是“把用户已认可的生产物分类打包”这一件事的唯一权威。

它不创建STATE、不创建Artifact、不新增项目状态字段、不新增最终Prompt字段，也不替代`asset_registry.md`、任何阶段Workflow或任何Template。包是**交付视图**：只收用户实际认可、已确认的文件，按类别集中一次交付，不改内容、不错位、不虚报——**不是**当前项目所有生产物的总汇，也不是Registry或Project Root的镜像。

---

## Package Timing And Delivery

包在**Clip 表（Confirmed Clip Production Plan）确认之后、最终视频 Prompt 之前**一次性生成；执行环境另有前提，见`## Access Precondition`。生产物按已确认阶段顺序产出，Clip 表是最后一项在Prompt之前需要确认的生产物；此时包内各类别才有可打包的真实文件。

- 构建包是STATE-03资产确认与STATE-07 Clip表确认之后的**交付动作**，不是新STATE，也不是进入STATE-08的前置Gate。
- 用户明确要求打包时立即构建。此外，当包的门条件全部满足、且当前阶段没有未决风险时，交付最终视频Prompt的那一轮必须附上包（或明确给出包路径与“已生成”证据）；不得声称已打包而实际未生成。
- 与`rules/automation_mode.md`的`Unified Delivery Packages`正交：后者的包名是**展示封套**，本文件的包是**真实文件集合**。两者不得互相定义，也不得把一个的实现写进另一个。
- 门条件未满足时：报告还缺哪一类、缺在哪个Gate，不生成空包，也不把缺失类别静默省略。

**门条件**（`final-prompt-ready`）：

1. 当前项目应制作的CHAR / ENV / PROP / FX视觉资产全部为`Asset Confirmed`，且每条已确认资产都有符合命名规范的文件名绑定；
2. Clip表已确认，且其参考资产路由已完成；
3. 每个`Applicable`类别都有对应真实文件。项目确实不需要的类别写`Not Applicable`并写明依据，不得因缺文件而静默丢弃类别。

`## Access Precondition`不通过时，本节的门条件即使全部满足也不构建包；两类条件是AND关系。

## Package Admission｜只收已认可的

包内每一项都必须**同时**满足两个条件：**有可回查的确认记录**，且**其真实文件存在并通过本文件的命名/来源检查**。只满足其一的一律不进包。

**入选证据**：

- 用户在本轮确认了具体对象（该Checkpoint、该批次、该Artifact、该图片），按`rules/progression_rules.md`的`Confirmation Input Semantics`记录；
- **用户未指出问题而给出推进表达**：按该规则的`Exception-Based Batch Confirmation`，这**构成确认**——只要该批次已经真实展示、且逐项能核对到具体对象与Revision。用户没提异议就是认可，不额外索要“确认 / 批准”措辞；
- `Auto-accepted under FAST`：按`rules/automation_mode.md`留下了依据、Revision与时间。

包内每一条都标注接受依据`Approval Basis`：`User Confirmed`、`Confirmed (batch, no objection)`或`Auto-accepted under FAST`。批次确认与逐项确认可以分别标注，但都属用户确认；FAST自动接受项必须与用户确认区分标注，不得合并表述。用户要求“只要我本人确认过的”时，排除FAST自动接受项。

**不作为入选证据**：出现在Asset Registry或对话里、路径存在、Prompt已完整、被下游阶段消费过。这些都不是认可。另有两类边界不因沉默而成立——**从未真实展示过的内容**（用户没有机会提异议）、**用户没看到或范围无法逐项核对的内容**；把沉默当成不展示的理由同样无效。Asset候选图、被弃用图、仅用于设计决策的外观参考图、Storyboard与Top-down Blocking Map按各自既有规则不进包。

**排除必须可见**：`00_INDEX.md`列出`未确认／未打包`清单，逐项写原因（从未展示、未确认、已否决、缺确认记录、非Canonical、文件不可读）。排除数量与原因不得省略或概括成“其余项目”。

**不得事后补确认**：不得为了让某项进包而回填`Approval Basis`、把未确认项标成已确认，或用“打包需要”当补确认的理由。排除是过滤，不是删除：原文件留在Project Root。

**Not Applicable须有依据**：类别确实不适用时写`Not Applicable`并写明依据；不得用它掩盖“其实有产出但未确认”。

## Access Precondition

**打包只在具备真实文件访问能力的运行环境中执行**，即`references/project_workspace.md`与`rules/state_source.md`定义的**Work / Codex 本地模式**（ChatGPT 桌面应用 / Codex CLI / IDE 等能读写本机目录的宿主），并且只能由**当前轮实际验过**的能力判定。

判据是能力，不是平台名：不得用用户自我声明、产品名、历史会话、其他平台或上一次运行的能力推断本轮可打包。三项能力必须在本轮构建前逐项核验：

1. **读**：Active Project Root 可访问，且确认资产图片的真实文件可读；
2. **写**：包位置（Project Root 之外）可创建目录并写入文件；
3. **压缩**：可生成zip。只有第3项允许降级——它只影响搬运形态，不影响包本身。

### 普通 Chat / Portable 模式

普通 Chat 的 Portable 模式（本机目录不可读）**不具备**上述能力。此时**不产zip、不产包目录**，也不得声称已打包。改写为交付纯文本的：

- `00_INDEX`：六类清单、每类文件名与来源；
- `00_MANIFEST`：`文件名 ↔ Asset ID ↔ 用途 ↔ Active Version ↔ 类别`映射表；
- 目录骨架文本：用户按它在自己的环境里建目录、重命名、压缩。

该文本形态必须明确标注“未打包”，且每个条目写真实来源；用户回传真实文件后才按本文件打包。

### 降级阶梯

| 本轮实际能力 | 交付 |
|---|---|
| 读 + 写 + 压缩 | 包目录 + zip（完整） |
| 读 + 写，不能压缩 | 包目录 + 完整清单，明确说明未生成zip |
| 读，不能写 | 完整清单 + 命名映射，由用户自行落盘 |
| 不能读 | 只交付命名映射表，每项标`待用户重命名`，明确“未打包” |
| 部分可读 | 打包可读项，逐项列出不可读项与原因；不因单项失败放弃整包 |

任何降级都不得用文件名、清单或空目录**伪造**包已生成、图片已上传或已确认。降级不是`BLOCKED`：它是当前能力下的合法交付形态，按上表如实报告即可。

## Package Contents

包的类别与顺序固定。每类都有自己的清单文件，清单只记录包内实际内容。下表是**类别容器**，不是“有产出就装”的许可：每项内容仍须先通过`## Package Admission`。

| 类别 | 目录 | 内容（均须已认可） | 不适用时 |
|---|---|---|---|
| Script | `01_script/` | 用户确认过的Production-Locked剧本与剧本分析 | 项目无锁定剧本时不生成包 |
| Assets | `02_assets/` | 资产登记表 + 每条`Asset Confirmed`的图片 | 无该类已确认资产时写`Not Applicable`并写明依据 |
| Visual Development | `03_visual_development/` | 用户确认过的`Project Style Baseline` / Aesthetic Decision Lock / `Project Color Reference`；只由STATE-04内部持有、未经确认的方向性材料不进包 | 无该类已确认项时该目录写`Not Applicable`并写明依据。该`Not Applicable`**只描述打包入选，不构成跳过STATE-04的依据**；STATE-04的建立与完成要求由`workflows/07_visual_development_workflow.md`拥有 |
| Scenes | `04_scenes/` | 用户确认过的Scene Breakdown与适用Sequence Plan | 无该类已确认项时该目录写`Not Applicable`并写明依据 |
| Shots | `05_shots/` | 用户确认过的Detailed Shot Design与适用Storyboard | 无该类已确认项时该目录写`Not Applicable`并写明依据 |
| Clips | `06_clips/` | 用户确认过的Clip Production Plan | 未确认则不打包（见门条件） |

```text
<Project ID>_<Project Name>_ProductionPackage_v<NNN>/
├── 00_INDEX.md
├── 00_MANIFEST.md
├── 01_script/
├── 02_assets/          （CHAR / ENV / PROP / FX 子目录与各自 _MANIFEST.md）
├── 03_visual_development/
├── 04_scenes/
├── 05_shots/
└── 06_clips/
```

`06_clips/`是最后一项：包在Clip表确认后生成，包内**不含**最终视频Prompt；Prompt仍由STATE-08按当前Template独立交付。

- `00_INDEX.md`：类别清单、每类文件名与来源、包Revision、构建时间与已完成类别的Gate证据。
- `00_MANIFEST.md`：每个打包文件的`文件名｜类别｜Asset ID或Artifact ID｜版本或Revision｜来源`，以及内容清单（文件字节数与SHA-256）、`Supersedes`与未打包的`待补充`条目。
- 类别清单使用`_MANIFEST.md`后缀（例如`CHAR_MANIFEST.md`），记录本类别全部已确认资产及其文件名。

## Asset Image Naming

资产图片必须使用**稳定、可机械判定**的文件名，使最终视频Prompt的每个参考条目都能一对一落到包内一张真实文件。这是命名的唯一权威。

命名形态：

```text
<Asset ID>｜<Purpose>.ext
```

- `Asset ID`：已登记的稳定实体ID（`CHAR-001`、`ENV-002`、`PROP-003`、`FX-004`）。Asset ID已含类别前缀，文件名不再重复类别前缀。
- `Purpose`：该文件在Registry里登记的Canonical用途；枚举由`references/asset_lock_contract.md`的`Canonical Reference Rule`唯一拥有（Identity / Costume / Scale / Layout / Material / State / FX Phase）。文件名里写作`Identity`、`Costume`、`Scale`、`Layout`、`Material`、`State`、`FX Phase`。
- `.ext`：图片真实格式（`.png`、`.jpg`、`.jpeg`、`.webp`）。
- **一个环境空间只对应一个Environment Asset**：`ENV-01`…`ENV-04`是该Asset的多个Canonical Reference图，共用一个Asset ID，只由View Code区分（与下方`ENV-002｜Layout_ENV-01.png`的例子同源，正确形态为`ENV-002｜Layout_ENV-01.png`…`ENV-002｜Layout_ENV-04.png`）。不得为每个View另铸一个Asset ID，也不得让View Code与Asset ID的序号一一绑定；否则Environment View Set、Spatial Lock与逐View几何校验在下游都无法表达，且同一空间的资产身份被拆成互不相干的四个。
- 环境View在Purpose后用下划线接View Code：`<Asset ID>｜<Purpose>_<View Code>.ext`，例如`ENV-002｜Layout_ENV-01.png`、`ENV-002｜Layout_ENV-03.png`。View Code继续使用`knowledge/environment_multi_view_reconstruction.md`既有的View ID（`ENV-01` Master Establishing / `ENV-02` Reverse / `ENV-03` Lateral / `ENV-04` Top-Down），适用扩展View写`EXT`；不得为文件名另造一套视角词汇。下划线是Purpose与View Code的专用分隔符，因此Purpose本身不得含下划线；多词Purpose（如`FX Phase`）用空格并整体匹配，不得塞进View位。
- Support Board文件使用板与项：`<Board ID>｜<Item ID>.ext`，例如`BOARD-CHAR-001｜A-02.png`；它在Board内的Item ID与下游`<Board Name> / <Board ID> / <Item ID>`引用一致。
- 版本号不进入文件名：版本继续由`asset_registry.md`的Active Version唯一拥有。同一Asset ID换Version即换内容，此时按`## Naming Lock And Rename`生成新文件，而不是原地改名。
- 分隔符统一使用全角`｜`，与既有`资产ID｜资产名`引用写法一致；文件名不得使用空格、括号、斜杠或任何会与引用分隔符混淆的字符。

**允许的用途**（不得为绕开枚举而自创用途）：

| 资产类别 | 允许的Purpose |
|---|---|
| CHAR | Identity / Costume / Scale / State |
| ENV | Layout / Material / State（用View Code区分视角） |
| PROP | Identity / Material / Scale / State |
| FX | FX Phase / State |
| Support Board | 板与项ID；不写Purpose |

## Naming Lock And Rename

命名在**批次图片确认**时锁定：把该文件名写入`asset_registry.md`对应资产的Canonical References（路径或受控外部ID、用途、绑定Version）之后，`Asset ID → 文件名`映射即稳定，不得原地改名或复用旧名。

- 资产内容或版本更新：新建符合规范的新文件并在Registry切换Active Version；旧文件与旧名保留为历史，记录`Supersedes`。不得覆盖旧文件、不得让两个不同内容共用同一文件名。
- 已确认资产的文件名不得因风格、审美或整理方便而更改；改名会使已交付Prompt的参考条目失效。
- 候选图、被弃用图、线稿、拼图、Storyboard与Top-down Blocking Map不是Canonical资产，不进入资产图片命名体系，也不进包内资产目录。

## Package Location And Source Rule

包位于Active Project Root之外的交付位置：

```text
<project-root>/../<project_id>_packages/<version>/
```

- 包目录与zip不属于Project State，不被任何Workflow当作Required Resource，也不得反向改写`asset_registry.md`或任何Accepted Artifact。
- 打包**只复制真实已确认文件**：不改内容、不转码、不重命名已确认资产图片、不移动Project Root内原文件。Project Root仍是唯一生产真源。
- 不伪造路径、受控ID、上传或确认状态。未提供的文件（例如A/B所需`REF-TAIL`）在manifest记为`待补充`，不计入包内文件数。
- 包内每份文件必须记录来源（Project Root内相对路径或用户提供路径）。来源缺失或不可读时报告为阻塞项，不得凭文件名推断内容。

## Final Prompt Correspondence

最终视频Prompt的`参考资产：`（Seedance 2.5为`多模态参考资产：`，MiniMax H3为对应参考字段）为每个实际投喂的视觉条目写出该资产的稳定引用名`<Asset ID>｜<资产名>`；环境View在其后以下划线补View Code（如`ENV-001｜面馆主视图_ENV-01`）。**以Asset ID为键**：每个引用名都必须能一对一落到`02_assets/`中的一张真实文件——一个Asset ID只对应一张Canonical图时写`<Asset ID>｜<资产名>`即可，一个Asset ID对应多张图（环境View、State、Costume、Material等）时必须补足以区分是哪一张的View Code或Purpose，否则视为不可机械核验。只写资产名、只写中文标签或写平台附件位（`图片1`）而不含Asset ID的条目一律不合格。对应关系必须是**一对一且可机械核验**：

- 每个入选的已确认资产条目，其文件名与包内`02_assets/`中的真实文件一一对应；
- 包内每张被列为Canonical的资产图，都能在引用它的Clip的`参考资产：`中找到对应条目；仅按`knowledge/environment_multi_view_reconstruction.md`登记为**按方位校验用途、默认不进入画面参考位**的View（典型为`ENV-04`俯视校验）豁免本项，但必须在`00_MANIFEST.md`写明其校验用途与“默认不进入参考位”的依据，不得静默留一张无解释的孤儿图；
- 不虚构文件名，不使用未打包、未确认或来源不明的图片，不把同一文件重复列为两个不同资产；
- 该对应只决定“条目落到哪个文件”，不改变Reference Selection / Routing、Reference Authority Map、Reference Budget或任何Prompt字段语义。

## Verification And Invalidation

构建包之前逐类核对门条件与Gate证据。出现以下任一情况必须停止并逐项报告，不得静默跳过、改名绕开或伪造补齐：

- 同一Asset ID映射到多个文件名，或多个Asset ID映射到同一文件名；
- Registry登记的文件名不符合本规范；
- Registry登记的Canonical Reference文件不存在或不可读；
- 已交付Prompt引用了包内不存在的文件；
- 某`Applicable`类别没有真实文件，或某类别被跳过而未写`Not Applicable`依据。

包内不写系统无法验证的话：`00_MANIFEST.md`只记录实际打包的真实文件与其校验和，不替代`asset_registry.md`的确认状态。

包的失效条件：任何打包资产的Active Version变化、任何被引用文件的名称或内容变化、或Clip表被判需重跑。失效不等于已交付Prompt自动失效——系统必须报告“包已失效”，并按最小修正处理已交付的参考条目，不静默重发。

## Optional Interoperable Tooling

`scripts/build_asset_package.py`是部分环境下的**可选加固**：它按本文件规范复制文件、生成清单、产出zip，并执行本节的自动化核验（含对已编译的Prompt文件做反向对应性检查）。

- 工具只做确定性文件与格式检查，不判断剧情、资产身份或Prompt质量。
- 工具不调用任何图像或视频模型，也不向外部服务提交任何内容。
- 没有Python、没有该脚本或换到别的运行环境，都不构成跳过本文件要求的理由；按本文件手工执行同样的分类、命名、来源与对应性判定即可。

## Final Principle

```text
只打包用户已认可的：有确认记录 + 真实文件存在，两者缺一不进包
未进包的要逐项报告原因，不静默丢弃
打包前提：具备真实文件访问能力的 Work / Codex 本地环境，按本轮实际能力判定
普通Chat / Portable 模式不产zip，只交付清单与命名映射，并明说“未打包”
资产图片文件名稳定且可机械判定
最终Prompt的每个参考条目都能落到包内一张真实文件
包是交付视图，不是新STATE、不是状态真源、不改任何已确认事实
```
