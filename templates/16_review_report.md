# Review Report Template

## Template Ownership

本Template是STATE-09 Review Report最终结构的唯一拥有者。

Review判断逻辑属于 `workflows/13_review_workflow.md`；质量知识只提供检查方法；本Template不推进STATE。

---

## Review Identity

Review ID：REVW-XXX

Project ID：

Project Name：

Reviewed Revision：

Reviewed Artifact：

Review Date：

---

## Overall Result

Result：PASS / REVISE / REBUILD

Disposition：KEEP / RE-EDIT / REGENERATE / REDIRECT

Failure Class：NONE / WRITING FAILURE / DIRECTING FAILURE / GENERATION FAILURE / EDITING FAILURE / UPSTREAM FACT FAILURE

Failure Origin：None / Writing / Generation / Editing / Directing / Upstream Fact

Hard Gate Result：PASS / FAIL

Prompt Quality Score（如适用）：/100

Summary：

Story Review Summary（Causality / Motivation / Scene Value / Writer Beat / Conflict-Stakes / Subtext / Setup-Payoff / Arc / Ending Payoff / Information Architecture）：

Technical Review Summary：

Director's Cut Review Summary（Intent vs Result / Audience Attention / Performance Truth / Relationship Readability / Information Timing / Shot Necessity / Rhythm / Emotional Residue）：

---

## Story Review

| Scene / Writer Beat | Causality / Motivation | Scene Value Change | Conflict / Stakes | Dialogue / Subtext | Setup / Payoff | Character / Relationship Arc | Information Architecture | Ending Payoff | Result / Return Route |
|---|---|---|---|---|---|---|---|---|---|

Writer Beat不是Shot；本表不得规定Shot Count或Camera Language。无有意义State Change且无不可替代Setup / Hold / Transition功能的场景标记为weak / replaceable。

---

## Affected IDs

Shots：

Assets：

Sequences / Units：

Boundaries：

---

## Shot-Level QA

| Shot | Result | Story / Coverage | Asset Lock | Space / Action | Performance / Lip-sync | Camera / Lighting / Color | Sound / FX | Seedance Stability | Problem | Return Route |
|---|---|---|---|---|---|---|---|---|---|---|

`Space / Action`对战斗、双主体、对峙、对话、追逐、相向运动必须检查：A/B左右与前后、分别朝向、视线目标、距离、唯一关系轴、摄影机轴线侧、Connector来源—路径—目标，以及双方相对同框时是否避免同时完整正脸。

---

## Adjacent-Shot Continuity QA

| Boundary | Class | Outgoing Anchor | Cut Point | Incoming Anchor | Inherited State | Authorized Change | Result | Problem |
|---|---|---|---|---|---|---|---|---|

每个适用边界必须成对复核Outgoing Tail Frame与Incoming First Frame的镜头几何；无授权跨轴、左右交换、朝向翻转、双正脸或攻击/视线/水流等Connector反向均为Hard Gate失败，返回STATE-06；仅Clip组织或尾帧用途错误时返回STATE-07。

---

## Coverage And Unit QA（如适用）

| COV / UNIT | Required Evidence | Present | Accepted Result / Revision | Retry Isolation | Result |
|---|---|---|---|---|---|

---

## Problems And Corrective Actions

| Issue ID | Severity | Affected IDs | Fact Owner | Problem | Minimum Necessary Fix | Return Workflow | Recheck Scope |
|---|---|---|---|---|---|---|---|

Severity：P0 Blocker / P1 Major / P2 Minor。

技术连续性正确但人物行为无动机属于WRITING FAILURE；Writer事实正确而情绪/信息呈现提前属于DIRECTING FAILURE；现有素材可通过剪辑恢复时选择EDITING FAILURE + RE-EDIT，否则按根因选择REGENERATE或REDIRECT，不得选择KEEP。

---

## Return Control

Return Route：

Next Workflow：

Recheck Scope：

Accepted Unaffected Artifacts：

Must Not Change：

---

## Completion Decision

- PASS：所有硬门槛通过，允许STATE-09 Complete。
- REVISE：局部可修复，STATE-09保持IN_PROGRESS并返回指定Workflow。
- REBUILD：上游事实或设计严重错误，STATE-09保持IN_PROGRESS并返回事实拥有者。

Disposition映射：KEEP→PASS；RE-EDIT→REVISE并进入Editing；REGENERATE→REVISE并只重试Affected Clip；REDIRECT→REVISE或REBUILD并返回Director / Scene / Shot / Clip owner。

不得同时选择多个结果。
