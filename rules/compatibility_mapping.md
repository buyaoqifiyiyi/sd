# Compatibility Mapping

## Purpose

本规则处理旧版State标签、旧Portable Schema和旧Pipeline到当前SD Film主路由的兼容迁移。迁移基于已验证Artifact与Completion Gate，不按旧编号或对话摘要机械复制。

## Preservation Set

迁移必须保留：

- 当前Project ID与项目身份
- Production-Locked Script
- Confirmed Assets、Active Versions与Canonical References
- Visual Direction Lock与用户明确约束
- 已完成Checkpoint、Accepted Artifacts与未受影响Revision
- Review记录、Open Risks与合法Pending Decisions

不得因为路由标签变化重做或重写Accepted Unaffected Artifacts。

## Canonical Route

当前固定主路由为：

```text
STATE-06 Detailed Shot Design
→ STATE-07 Clip Production
→ STATE-08 Clip-based Video Prompt / Video Generation
```

Storyboard只保留为Optional/Auxiliary Artifact；它不是STATE，不计入Completed States，不是Next Workflow，也不得成为STATE-08 Canonical Reference。

## Legacy Storyboard Mislabel Mapping

旧状态把`STATE-07`标为Storyboard时：

- Detailed Shot Design未通过Completion Gate：映射至`STATE-06`与`09_shot_design_workflow.md`。
- 已有Confirmed Detailed Shot Design但没有Confirmed Clip Production Plan：映射至`STATE-07`与`10_clip_production_workflow.md`。
- 已有Confirmed Clip Production Plan：映射至`STATE-08`与`11_video_generation_workflow.md`。

已有Storyboard产物仅登记为Optional/Auxiliary Artifact，不要求重做。

## Legacy Review Checkpoint Mapping

STATE-09 Review是显式调用阶段，因此停“等待实际生成结果”的旧状态按当前语义迁移：

- 用户未要求审核：把`Pending Decision: 等待实际生成结果`与指向Review的Next Workflow迁移为主流程收尾——`Next Workflow: Project Complete / Post`、`Pending Decision: None`；保留已有Review记录、Accepted Take Canon与Open Risks，不因迁移判PASS或失败。
- 用户当前明确要求审核成片，或已带回具体成片问题：迁移到`STATE-09`与`13_review_workflow.md`，按失败驱动档或用户要求的档位继续。

两种迁移都只改路由字段与状态摘要，不重做已确认阶段，也不丢弃Review证据。

## General Mapping Procedure

1. 校验Project ID、Revision与当前可读Artifact。
2. 判断最近一个真正通过Completion Gate的主STATE。
3. 把旧名称、短名、错误Next Workflow和待办标签迁移为当前标准名称。
4. 选择能消费现有Confirmed Artifact的最近当前State / Checkpoint。
5. 只迁移路由字段、状态摘要和必要兼容记录，不修改交付物正文。
6. 在Version History记录原值、映射结果、证据与时间。

旧对话在显式Reload后继续时，历史Skill名称、owner和文件路由只作为待映射输入；Latest Successfully Loaded Current Skill Definition拥有路由权威。映射不得要求项目从STATE-00重启，也不得丢弃Production-Locked Script、Confirmed Assets、Accepted Take Canon / Accepted Canon State、Shot-State Memory、Checkpoint或Accepted Unaffected Artifacts。

## Portable Schema Migration

Portable字段结构由`references/project_state_contract.md`拥有。旧文本出现缺字段、自创区块、自然语言Workflow、`READY / INITIALIZED / ACTIVE / PASSED`作为State Status时，先按Canonical Schema迁移：

- 只迁移有证据的项目事实。
- 无Workflow完成证据的`READY / INITIALIZED`规范化为`NOT_STARTED`。
- Current State只写`STATE-00`至`STATE-09`；完整阶段名写入任务或说明。
- Next Workflow使用实际文件名；主流程收尾时写状态合同允许的终止值`Project Complete / Post`。
- 迁移完成前不得把旧文本当作Valid State Source。
