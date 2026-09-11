# SD Film Maintenance Self-Check（Per-Change Run Card）

## Purpose

本文件是Skill维护QA的**执行入口与每次正式修改的必读清单**。它拥有**执行顺序、检查项与判定输出格式**；每一项的完整判据、边界、反例与处置要求由`references/maintenance_self_check_protocol.md`拥有。两者冲突时，判据以protocol为准。

它属于Skill维护层：不是影视制作Pipeline的STATE，不写入项目状态，不进入用户视频Prompt，也不得被复制成另一套并行检查规范。

生产系统的**模块接口合同**由`references/module_contracts.md`拥有，本文件不重复定义任何模块合同；Skill自身体量的**数值阈值与Size Ledger**由`references/context_budget.md`拥有，本文件只引用其一。

## Trigger

每次对Skill作任何正式修改后都必须执行，包括修改`SKILL.md`、Rules、Workflows、Knowledge、Templates、References、Validator、测试、用户文档、模块增删、Prompt结构、路由、Gate、STATE规则、资产规则、连续性规则、Review规则以及纯拼写修正。

轻量语义检查可以与改动风险匹配，但`Standalone Skill Discovery Guard`与`Unconditional Chat Runtime Startup And Recovery Guard`**永远不能省略**。

## Mandatory Maintenance Chain

```text
Read current rules
→ Locate related rules
→ Classify existing coverage
→ Apply minimal change
→ Run the 15 Check Dimensions below
→ Run Standalone Skill Discovery Guard
→ Run Unconditional Chat Runtime Startup And Recovery Guard
→ Classify and resolve every finding by risk
→ Run targeted regression for the requested change and every repaired finding
→ Sync USER_GUIDE when user-facing behavior changed
→ Final change report
```

## Check Dimensions

逐项判据、边界与反例见`maintenance_self_check_protocol.md`的同名条目。

| # | Dimension | 检查什么 |
|---|---|---|
| 1 | Duplicate Rule Check | 是否出现语义相同、措辞不同的并行规则，或本应单一来源却复制的完整协议 / Schema |
| 2 | Conflict Check | Pipeline、STATE编号、Gate、优先级、默认行为与辅助模块边界是否互相冲突 |
| 3 | Terminology Drift Check | 正式术语与ID是否漂移、失控，或出现同义命名 |
| 4 | Rule Ownership Check | 归属是否符合Authority Matrix；入口是否复制了细粒度规则 |
| 5 | Prompt Pollution Check | 新增内部控制是否会膨胀最终Prompt |
| 6 | Routing Integrity Check | 新模块的入口、触发与返回路由是否完整，且未把显式模块变成默认必经 |
| 7 | Template Consistency Check | Workflow声明的Output Owner、字段语义与当前Template是否一致 |
| 8 | Reference Integrity Check | 所有显式文件、模块、Template与脚本路径是否真实存在且名称一致 |
| 9 | State / Continuity Compatibility Check | STATE-00至STATE-09与各项连续性事实是否被破坏 |
| 10 | User Guide Sync Check | 用户可见行为变化时`USER_GUIDE.md`是否已同步 |
| 11 | Regression Check | 是否选用了最少但有效的正反例回归，并覆盖自检附带修复项 |
| 12 | Change Classification Check | 最终变更分类是否与实际操作一致 |
| 13 | Runtime Claim / Legacy Recovery Check | Runtime Reload、Workflow Re-entry与Legacy Recovery是否仍由唯一owner定义 |
| 14 | Standalone Skill Discovery Check | 独立Skill的发现入口、别名与单一用户级权威副本是否完好 |
| 15 | Context Budget Check | 是否仍守Entry / Target / Ceiling预算，且Size Ledger未被腐化 |

## Required Verification

- `scripts/validate_sd_film.py --skill-root <skill-root>`：确定性结构与引用检查
- `scripts/test_validate_sd_film.py`：完整测试入口
- `references/recovery_guards.md` 的 `Legacy Recovery Regression Matrix (LR-R1—LR-R10)`
- `references/recovery_guards.md` 的 `Standalone Skill Discovery Regression Matrix (SD-R1—SD-R5)`

上述四项是每次正式修改的固定基线，不因改动小、未触及runtime或“本轮只改文案”而跳过。脚本只负责确定性结构、不变量与引用检查；语义判据由维护者实际阅读比较完成，**脚本通过不等于全部维度自动PASS**。

## Findings Disposition

每个真实发现项必须在本轮标记为`FIXED`、`WARN`或`FALSE_POSITIVE`，并记录所有者、影响与处理依据；误报必须说明为什么不构成问题，不能用总体`PASS`掩盖单项发现。

风险分级（`SAFE_LOCAL` / `CONTROLLED_CROSS_MODULE` / `HIGH_RISK / DECISION_REQUIRED`）的判定门槛与处置要求见protocol。

## Required Self-Check Summary

每次正式修改后的最终报告必须简短列出：

```text
Skill Update Self-Check

Change Classification: no_change / optimize_existing / merge_existing / add_new / deprecate/remove
Findings Disposition: FIXED <count> / WARN <count> / FALSE_POSITIVE <count>
Duplicate Rules: PASS / FIXED / WARN
Conflict Rules: PASS / FIXED / WARN
Terminology: PASS / FIXED / WARN
Rule Ownership: PASS / FIXED / WARN
Context Budget: PASS / FIXED / WARN
Prompt Pollution: PASS / FIXED / WARN
Routing: PASS / FIXED / WARN
Template Sync: PASS / FIXED / WARN
Reference Integrity: PASS / FIXED / WARN
State / Continuity: PASS / FIXED / WARN
Runtime Claim Integrity: PASS / FIXED / WARN
Legacy Recovery Regression: PASS / FAIL / WARN
Chat Runtime Startup Guard: PASS / FAIL / WARN
Standalone Skill Discovery: PASS / FAIL / WARN
Writer / Director Compatibility: PASS / FIXED / WARN
Regression: PASS / FAIL / WARN
USER_GUIDE Sync: YES / NOT REQUIRED
Warnings: NONE / <concise unresolved warnings>
```

报告同时说明原机制位置、覆盖缺口、实际改动文件、运行过的验证，以及全部发现项的风险等级和处置。只有实际执行过的检查才能标记`PASS`；发现并修复后标记`FIXED`；只有达到`HIGH_RISK / DECISION_REQUIRED`门槛且本轮不能安全解决时才标记`WARN`，并附证据、影响、建议方案和下一步，不能再使用“与本次修改无关”作为延期理由。
