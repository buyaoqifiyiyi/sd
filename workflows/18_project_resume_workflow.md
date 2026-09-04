# Project Resume And Retry Workflow

## Purpose

从已验证Checkpoint恢复中断项目，并对生成失败执行可控重试。

本Workflow是辅助Workflow，不创建主STATE，不跳过Pipeline，不重新初始化项目。

---

## Trigger Gate

以下任一情况触发：

- 用户要求继续、恢复或断点续作。
- 上次任务中断、工具失败或对话切换。
- Review返回REVISE / REBUILD。
- SHOT或UNIT需要重试。
- Active Artifact与project_status.md记录不一致。
- 用户在旧对话中继续项目，并命中`rules/runtime_reload.md`定义的Runtime Reload Trigger。
- 用户命中`rules/runtime_reload.md`定义的Explicit Legacy Recovery Command。

正常连续执行且状态清楚时不触发。

---

## Required Resources

- `rules/runtime_reload.md`与Current Accessible Skill Definition（触发Runtime Reload时必须从本轮解析的Loaded Source重读）
- config.md与当前路由适用的rules/
- references/project_workspace.md
- references/project_state_contract.md
- references/artifact_revision_contract.md
- references/asset_lock_contract.md
- knowledge/quality/execution_risk.md（生成重试时）
- references/skill_experience_contract.md与knowledge/skill_experience.md（生成失败复盘形成跨项目经验候选时）
- project_manifest.json（可访问时）
- 按优先级选定的project_status.md或portable_project_status.md
- asset_registry.md
- execution_ledger.md（存在时）
- artifact_registry.md（存在时）
- templates/17_execution_ledger.md
- templates/18_artifact_revision_ledger.md

---

## Step 1: Resolve Project

如当前输入触发Runtime Skill Reload或Legacy Project Recovery，先完整执行`rules/runtime_reload.md`对应的Integrity协议并取得合法Reload Status，再进入项目解析。本Workflow不维护触发词、Skill Definition Source优先级、加载顺序、Work escalation、Legacy Intent Backfill字段表或成功判定。

先由`references/project_workspace.md`解析Active Project候选，再按`rules/state_source.md`选择唯一State Source。本Workflow只消费选择结果并验证恢复证据，不复制优先级、fallback、Project ID冲突或Chat运行差异的全局规则。

---

## Step 2: Validate Identity And State

检查所有可访问资料与Selected State Source的Project ID、State Schema、Revision ID、Active Workflow和Next Workflow，并验证所有持久路由字段及Pending Tasks使用当前主Pipeline标准名称。Portable模式不因本机Manifest、Bible或Registry不可读而失败。

Portable候选若使用READY / INITIALIZED、缺少Required Header / Sections或使用自然语言Workflow别名，先按`references/project_state_contract.md`的Canonical Portable State Schema与`rules/compatibility_mapping.md`迁移；没有生产Workflow完成证据时保持STATE-00 NOT_STARTED。迁移完成前不得把该候选当作有效Checkpoint。

如发现 STATE-06 / STATE-08 使用非标准短名、STATE-07 被标成 Storyboard，或待办表仍按 Shot Design、Storyboard、Video Generation 三项连续排列，先按`rules/compatibility_mapping.md`迁移。映射以可验证Artifact和Completion Gate为准；Storyboard只保留为Optional/Auxiliary Artifact，不得据旧状态直接选择Storyboard Workflow。

迁移与Reload必须保留当前项目、Production-Locked Script、Confirmed Assets / Active Versions / Canonical References、Accepted Take Canon / Accepted Canon State、accepted prompt、Shot-State Memory、Blocking Canon / Spatial Snapshot、Confirmed `REF-SKETCH`、已完成Checkpoint、Accepted Unaffected Artifacts与用户明确约束。只更新旧路由标签和必要状态摘要，不得因Skill升级、STATE名称、owner/file routing或Writer / Director schema变化强制重开或重做。

Legacy项目缺少新版Writer / Director intent时，调用`rules/runtime_reload.md`唯一拥有的`Legacy Intent Backfill`，只消费`knowledge/screenplay_development.md`与`knowledge/director_decision_layer.md`定义的字段语义，并把结果作为当前Workflow所需的内部source data。不得在本Workflow重定义Packet、回STATE-01重写已锁定剧本、重做资产/已确认镜头，或自动失效Accepted Take / accepted prompt。Confirmed `REF-SKETCH`在Blocking Signature未变时继续有效。

不一致时不合并猜测；记录Recovery Item并返回事实拥有者。

---

## Step 3: Find Last Safe Checkpoint

只接受已落盘、依赖存在、通过确定性校验且未被上游Revision失效的Checkpoint。

对话中的未保存分析不算Checkpoint。

---

## Step 4: Build Resume Scope

记录：

- Resume From
- Required Inputs
- Affected IDs
- Accepted Unaffected Artifacts
- Must Not Change
- Next Workflow
- Return After Completion

---

## Step 5: Retry Decision

生成失败时读取Generation Attempts：

- 第一次：最小修正后重试。
- 同类失败第二次：必须应用Stable Downgrade。
- 同类失败第三次：停止盲重试，返回Asset / Detailed Shot Design / Clip Production / Video事实拥有者。

重试不得改变已接受前序UNIT或无关镜头。

完成失败归因后，可按`references/skill_experience_contract.md`自动提出跨项目`Experience Candidate`，但不得自动写入Skill。用户确认后，该经验才可作用于后续产出与项目迭代；当前项目的实际修改仍须通过对应Owner与Revision流程。

---

## Step 6: Record And Resume

使用可用的templates/17_execution_ledger.md和templates/18_artifact_revision_ledger.md更新Ledger记录，然后进入Selected State Source指定的合法Workflow。记录恢复决策后同步或输出完整Portable State，并执行references/project_state_contract.md的`Portable Required Field Writeback`。

本Workflow不生成该阶段最终交付物。

---

## Completion Gate

- 可访问的Active Project唯一，或普通Chat已唯一选择Portable项目身份。
- Last Safe Checkpoint可验证。
- Resume Scope和Must Not Change明确。
- 依赖Revision存在。
- 重试次数与降级策略已记录。
- Next Workflow合法且没有跳过前置阶段。
- 如本次触发Reload，已内部确认Reload Status、Loaded Source、Loaded Skill Version、Loaded Build ID、Owner Files Resolved、Last Routed State、State Source、Last Routed Workflow、Current Object与Workflow Entry Checkpoint；显式Re-entry已从该Workflow入口执行到合法Checkpoint后才声称完成重进；如为`UNAVAILABLE`，另有具体失败资源与Fallback Source，且没有作出“严格按当前Skill”声明。
- 如本次为Legacy Project Recovery，已记录Skill Source、Project State Source、Mapped Current STATE、Current Workflow、Current Object、Canon Preserved、Backfill Needed与Next Workflow；STATE-08恢复已从current owner entry执行Reference Selection / Routing → Final Visual Blocking Anchor Assessment → Writer + Director Intent Preservation → Prompt Compiler → Final QA，而不是直接润色旧Prompt。
