# Skill Experience Contract

> 本文件是运行时资源，由需要它的Workflow按其Required Resources读取；本节仅声明该读取关系。

## Module Identity

- Module Name: `Skill Experience Module`
- Module Type: 跨项目持久Knowledge层 + Review/失败复盘后的候选确认机制
- Main STATE: 不创建新STATE；候选产生点位于STATE-09 Review与项目Resume/Retry复盘之后
- Knowledge Owner: `knowledge/skill_experience.md`
- Contract Owner: 本文件

## Trigger Boundary

触发：STATE-09 Review完成、REVISE / REBUILD返回、生成失败复盘，或用户明确要求总结/记录/使用技能经验。

不触发：新项目启动、普通项目状态读取、项目发现或查找、单次Prompt润色、未完成的即时推理、项目专属事实整理、用户未要求的自动Skill写入或自动经验检索。

## Knowledge Classification

每条候选与经验必须先归入以下一类，分类决定它能否跨项目复用、以及是否必须带日期：

- `P｜Cross-Project Principle`：由多个独立案例验证、跨模型仍成立的方法。无有效期，可跨项目复用。
- `O｜Operational Parameter`：模型版本、时长与秒数窗口、参考输入上限、分辨率、价格、成功率、重试次数等会随平台与版本变化的操作参数。**必须写明`valid_as_of`日期**，不得表述为跨项目原则，也不得在未复测的情况下继续引用。参数变化时标记`REVIEW`并重新取证。
- `C｜Project Configuration`：特定角色、场景、叙事视点、美术或连续性决定。只属于该项目，默认不进入通用Skill；项目特殊口味写入项目风格档案。

证据门槛：一次成功或失败只记观察；同一对象多次随机结果可形成模型倾向，仍属`O`；至少两个独立镜头或场次出现同样因果，或用户明确将其定为创作规范，才可形成候选`P`或`C`；跨模型仍成立且无关键反例时才升级为高置信`P`。模型版本、参数、时长、价格与成功率始终为`O`。

## Candidate Schema

每个候选至少包含：

- `Experience Candidate ID`
- `Class: P / O / C`
- `Observation`（观察到什么，症状与成功点分开写）
- `Evidence`（Review ID、Failure Pattern、用户反馈或重复案例）
- `Triggers`（什么条件下适用：镜头类型、空间条件、资产类型、模型或阶段）
- `Procedure`（具体怎么做，可复现的步骤，而不是结论句）
- `Failure Signals`（出现什么可观察信号说明这条经验正在失效或不适用）
- `Exceptions`（什么情况下不该用，已知边界）
- `Counter-examples`（已知反例；没有时写`None observed`，不得省略该字段）
- `Applicability`
- `Proposed Practice`
- `Expected Impact`
- `Source Variable`（`single_variable` 或 `coupled_uncharacterized`）
- `Confidence: LOW / MEDIUM / HIGH`
- `Scope: output / project_iteration / both`
- `valid_as_of`（`Class = O` 时必填；`P` 可留`None`）
- `Conflict Check`
- `User Decision: PENDING / ACCEPT / REJECT`

`Source Variable`固定取值：单变量修改记`single_variable`；同时改变多个变量且无法分离归因时记`coupled_uncharacterized`。**`coupled_uncharacterized`不得升级为`P`，也不得据此宣称某一措辞、某一词或某一风格必然有效**；它最多作为`O`或`C`的观察记录，需要单变量复测后才能重新归类。先保留反例，不只收集成功样本。

候选仅存在于当前响应、Review/复盘记录或用户指定的草稿位置；`PENDING`不得进入Skill经验库。

## Confirmed Experience Record

用户确认后，经验记录至少包含：

- `Experience ID`（独立于CHAR / ENV / PROP / FX / SCENE / SHOT / CLIP等命名空间）
- `Class: P / O / C`
- `Statement`
- `Triggers`
- `Procedure`
- `Failure Signals`
- `Exceptions`
- `Counter-examples`
- `Applicability`
- `Evidence`
- `Confidence`
- `Validated Count`
- `valid_as_of`（`Class = O` 时必填）
- `Created / Last Validated`
- `Status: ACTIVE / REVIEW / RETIRED`
- `Conflict / Supersedes`（无则None）

`O`类经验在`valid_as_of`到期、模型版本变化或平台能力变更时必须转为`REVIEW`；未复测前不得作为当前依据引用。缺少`Failure Signals`、`Exceptions`或`Counter-examples`字段的条目不得入库。

Skill经验库路径为Skill根目录下的`knowledge/skill_experience/experience_ledger.md`；不得写入任何Project Root、`portable_project_status.md`或项目兼容入口。

## Application To Output

仅在本合同的显式触发条件成立后，才筛选ACTIVE经验，并记录内部 `Experience Application`：命中的适用条件、采用的建议、未采用原因（如有）与验证结果。不得用项目名称、题材、素材或相似度自动检索历史项目/经验。经验只投影为当前Template允许的语义，不新增最终输出字段，不覆盖用户当前指令、项目事实、Rules、Workflow或Template。

## Application To Project Iteration

经验命中时可生成 `Iteration Recommendation`，但必须返回对应事实/设计Owner。只有该Owner流程与用户确认通过后，才可修改项目交付物并按项目Revision规则记录；经验本身不能直接修改Production-Locked Script、Confirmed Asset、Accepted Take、Shot、Clip或Prompt。

## Conflict And Retirement

与硬规则、当前用户指令或已确认项目事实冲突时，优先级固定低于它们；经验标记`CONFLICT`并暂停应用。被新证据推翻、长期未复核或适用条件消失时标记`REVIEW`或`RETIRED`，不得静默删除历史证据。

## Deterministic Invariants

- 候选未获用户确认不得写入Skill经验库。
- Skill经验不出现在Project State、Portable State或主Pipeline STATE列表中。
- 经验不占用现有实体ID命名空间。
- 经验应用不改变Template Schema、不绕过Completion Gate、不跳过主Pipeline。
- 所有Skill经验写入均产生Skill版本变更并触发完整Skill Update Self-Check。
