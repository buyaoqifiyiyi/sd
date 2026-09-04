# Skill Experience Contract

## Module Identity

- Module Name: `Skill Experience Module`
- Module Type: 跨项目持久Knowledge层 + Review/失败复盘后的候选确认机制
- Main STATE: 不创建新STATE；候选产生点位于STATE-09 Review与项目Resume/Retry复盘之后
- Knowledge Owner: `knowledge/skill_experience.md`
- Contract Owner: 本文件

## Trigger Boundary

触发：STATE-09 Review完成、REVISE / REBUILD返回、生成失败复盘，或用户明确要求总结/记录技能经验。

不触发：普通项目状态读取、单次Prompt润色、未完成的即时推理、项目专属事实整理、用户未要求的自动Skill写入。

## Candidate Schema

每个候选至少包含：

- `Experience Candidate ID`
- `Observation`
- `Evidence`（Review ID、Failure Pattern、用户反馈或重复案例）
- `Applicability`
- `Proposed Practice`
- `Expected Impact`
- `Confidence: LOW / MEDIUM / HIGH`
- `Scope: output / project_iteration / both`
- `Conflict Check`
- `User Decision: PENDING / ACCEPT / REJECT`

候选仅存在于当前响应、Review/复盘记录或用户指定的草稿位置；`PENDING`不得进入Skill经验库。

## Confirmed Experience Record

用户确认后，经验记录至少包含：

- `Experience ID`（独立于CHAR / ENV / PROP / FX / SCENE / SHOT / CLIP等命名空间）
- `Statement`
- `Applicability`
- `Evidence`
- `Confidence`
- `Validated Count`
- `Created / Last Validated`
- `Status: ACTIVE / REVIEW / RETIRED`
- `Conflict / Supersedes`（无则None）

Skill经验库路径为Skill根目录下的`knowledge/skill_experience/experience_ledger.md`；不得写入任何Project Root、`portable_project_status.md`或项目兼容入口。

## Application To Output

执行相关产出前按需筛选ACTIVE经验，并记录内部 `Experience Application`：命中的适用条件、采用的建议、未采用原因（如有）与验证结果。经验只投影为当前Template允许的语义，不新增最终输出字段，不覆盖用户当前指令、项目事实、Rules、Workflow或Template。

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
