# Artifact Revision And Dependency Contract

## Purpose

本文件定义项目交付物的Revision、依赖、接受状态、重试隔离和失效传播。

它不替代资产版本；Asset Version服从references/asset_lock_contract.md。

---

## Required Project Ledgers

复杂项目或首次进入STATE-06前建立：

- `<active-project-root>/execution_ledger.md`
- `<active-project-root>/artifact_registry.md`
- `<active-project-root>/generation_runs/`（首次生成或重试时）

简单项目可以在STATE-00只建立空Ledger入口，不要求虚构Revision。

---

## Artifact Record

每个重要交付物记录：

```text
Artifact ID
Artifact Type
Path
Revision ID
Status
Based On
Affected IDs
Created By Workflow
Validation Result
Accepted Result
Supersedes
Invalidates
Created At
```

允许的Status：Draft / Candidate / Accepted / Superseded / Invalidated / Archived。

---

## Dependency Rule

- Based On必须引用存在的Artifact Revision或Asset Active Version。
- 上游Revision发生实质变化时，下游不自动删除；标记Invalidated并登记Recheck Scope。
- 未受影响且已接受的Artifact保持Accepted，符合最小必要修改原则。
- Review必须明确Accepted Unaffected Artifacts。

---

## Generation Run Record

每次生成或重试记录：Run ID、Prompt Revision、Target CLIP/SHOT/UNIT、Attempt、Execution Risk、Result、Failure Class、Planned Start State、Planned End State、Observed Start State、Observed End State、Accepted Output、Accepted Canon State、Retry Scope、Stable Downgrade和Review ID。

Planned State来自Confirmed Clip Production Plan与Prompt边界；Observed State只记录实际生成画面可观察到的状态，不得用计划值代填。只有用户明确接受该Take，且Run ID、Prompt Revision、Review结果与接受证据齐全时，才把该Take的Observed State写为Accepted Canon State。被拒绝、未确认或仅生成未审的Take保留为Attempt记录，但不得改变Canon。

Accepted Canon State是后续Clip瞬时连续性的权威来源：同一维度上覆盖原Planned State。它不得覆盖Active Character / Environment / Prop Canonical References的身份、结构和造型权；Take中出现的脸、服装、环境结构或道具造型漂移不得因接受瞬时动作/站位而升级为新资产事实。

Failure Class只使用：

- Identity Drift
- Spatial / Axis Error
- Motion / Physics Error
- Performance / Lip-sync Error
- Camera / Focus Error
- Lighting / Color Error
- FX / Sound Error
- Coverage Missing
- Template / Platform Error
- Unknown

---

## Retry Isolation

重试只作用于Affected CLIP/SHOT/UNIT和必要相邻边界。已接受的前序Clip / UNIT、资产版本和无关镜头不得重新初始化。

每次重试先执行：`Failure Diagnosis → 选择一个最高影响变量 → 只先修改该变量 → Retake → 与前一Take比较`。变量沿用现有Failure Class与事实拥有者，可落在Identity、Spatial / Blocking、Prop、Motion / Performance、Camera / Focus、Lighting / Color、FX / Sound、Coverage或Prompt Scope / Template。若失败仅为站位错误，第一轮只修Spatial Blocking / 空间关系及必要边界，不整段重写Prompt、不同时更换角色资产、运镜、光线与表演。

只有诊断证据表明根因本身是多变量耦合、单变量修复无法形成合法输入，或用户明确要求整体重做时，才允许一次调整多个变量；必须在Retry Scope记录耦合证据和不采用单变量的理由。后期可修问题优先路由Editing，不为可安全后期处理的局部偏差无必要重新生成。

同一失败连续两次：强制应用Stable Downgrade。

同一失败连续三次：返回事实/设计拥有者，不继续同参数盲重试。

---

## Validation Invariants

- Revision ID和Run ID唯一。
- Based On引用存在且无循环。
- Accepted Artifact必须有Validation Result。
- Supersedes只能指向同一Artifact的旧Revision。
- Accepted Output必须绑定生成它的Prompt Revision和Review结果。
- Accepted Canon State必须来自同一Run的Observed State并有用户接受证据；未接受Take不得改变后续连续性Canon。
