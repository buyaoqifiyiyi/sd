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

每次生成或重试记录：Run ID、Prompt Revision、Target SHOT/UNIT、Attempt、Execution Risk、Result、Failure Class、Accepted Output、Retry Scope、Stable Downgrade和Review ID。

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

重试只作用于Affected SHOT/UNIT和必要相邻边界。已接受的前序UNIT、资产版本和无关镜头不得重新初始化。

同一失败连续两次：强制应用Stable Downgrade。

同一失败连续三次：返回事实/设计拥有者，不继续同参数盲重试。

---

## Validation Invariants

- Revision ID和Run ID唯一。
- Based On引用存在且无循环。
- Accepted Artifact必须有Validation Result。
- Supersedes只能指向同一Artifact的旧Revision。
- Accepted Output必须绑定生成它的Prompt Revision和Review结果。

