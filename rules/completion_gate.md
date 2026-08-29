# Completion Gate And State Transition

## Purpose

本规则拥有“何时允许进入、完成、推进、退回或通过Review”的全局决策原则。各Workflow拥有本阶段具体Completion Checklist；`references/project_state_contract.md`拥有决策作出后的字段变更与持久化写回；Template只拥有最终交付格式。

## Completion Decision

阶段只有在以下条件全部满足时才能写`COMPLETE`：

1. 当前Workflow声明的Required Inputs已验证。
2. Required Resources已在本次执行中实际读取；适用的Conditional Resources也已读取。
3. Workflow所有必需步骤与本阶段质量检查已完成。
4. 需要用户确认的Prompt、图片、Production Script、Clip Plan或其他Artifact已获得明确确认。
5. 输出通过当前Template完整性检查，且没有竞争Schema。
6. 当前状态、Artifact、Revision、Checkpoint、Pending Decision与Next Workflow已按状态合同成功写回；失败时不得伪称阶段完成。

路径存在、文字说明、历史摘要、草稿或内部分析不等于Completion Gate通过。任何必需项未通过时保持`NOT_STARTED`、`IN_PROGRESS`或真正适用的`BLOCKED`，并指出最近可继续的Checkpoint。

## Transition Decisions

- `ENTER`：当前Workflow合法、前置状态与必需输入允许进入时作出；进入本身不等于完成。
- `COMPLETE`：只有本规则的Completion Decision与当前Workflow Checklist全部通过时作出。
- `AUXILIARY_NOT_APPLICABLE`：辅助Workflow确实不适用时作出，不得改变主STATE或伪造生产完成。
- `REVIEW_RETURN`：Review为REVISE / REBUILD时作出，必须携带最小Return Route与复核范围；修复后仍须返回Review。
- `REVIEW_PASS`：只有实际审核结果通过时作出；未查看生成结果不得作出。

本规则只决定允许哪一种Transition Decision，不重复定义字段清单、Revision写法或Root / Portable同步顺序。所有字段变更与同步行为由`references/project_state_contract.md`执行。

## Confirmation Boundaries

- STATE-01只有`Script Status: Production-Locked`才能完成。
- STATE-03必须完成Prompt确认与图片确认双闭环；Image Generated不等于Asset Confirmed。
- STATE-07必须有Confirmed Clip Production Plan并通过逐ClipPreflight与Reference Budget。
- STATE-08必须消费Confirmed Clip Production Plan，并按`workflows/11_video_generation_workflow.md`与`templates/10_video_prompt.md`完成逐Clip验证。
- 用户只要求下一步时不得把未来阶段或待确认资产提前标记完成。

## Persistence Gate

Transition Decision只有在`references/project_state_contract.md`完成对应写回后才算落地。写回失败不得伪称成功；具体Root / Portable顺序、字段和失败语义只由状态合同定义。
