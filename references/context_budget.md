# SD Film Context Budget And Size Ledger

## Purpose

本文件是SD Film**自身体量预算**的唯一权威来源。它只服务Skill维护，不是影视制作Pipeline的一部分：不创建STATE，不写入项目状态，不影响用户可见交付，也不得成为新Prompt字段或Template的依据。

它回答一个问题：**文件长到什么程度开始损害“规则被读到、被遵守”**。

## Why Size Is A Correctness Issue

Skill分三层加载：`description`常驻、`SKILL.md`在被调用时整体注入、其余文件按需读取。文件过长时，代价从“慢”变成“错”：

- **高频必读文件超长**：规则仍在文件里，但落在中段，遵循率显著下降。门禁型规则因此静默失效——文件没坏，行为坏了。
- **检索成本随文件数上升**：找不到应该读哪个文件时，结果是漏读、错读或跳步，而不是报错。
- **同一事实双写**：长文件更难逐项比对，改动只同步一处即产生冲突。

因此本预算检查的是**可读性纪律**，不是磁盘占用，也不是写作风格。

## Budget Tiers

行数按文件实际换行数统计，不区分EOL。

| Tier | 阈值 | 要求 |
|---|---|---|
| Entry | `SKILL.md` ≤ 120 行 | 只保留身份、版本、入口、主路由、全局不变量与索引；不得复制细粒度规则、算法或Template字段 |
| Target | 单文件 ≤ 800 行 | 超过必须登记在下方Size Ledger |
| Ceiling | 单文件 ≤ 3000 行 | **任何文件都不得达到**；达到即视为结构性失控，必须拆分后再提交 |

`SKILL.md`还同时受`scripts/validate_sd_film.py`既有字节上限约束。

## Size Ledger

超过Target的文件必须逐条登记。登记是**债务记录，不是豁免证明**：它记录“当前为什么还没拆”和“什么时候必须重新评估”，不改变Target的适用，也不豁免Ceiling。

未登记的超Target文件、已降到Target以下但仍留在此表的条目、以及指向不存在文件的条目，都会使Validator失败。

| File | Owner | Lines (r50) | Why It Still Stays Whole | Review By |
|---|---|---|---|---|
| references/regression_scenarios.md | Skill维护QA | 1508 | 回归场景矩阵，按R*/LR-R*/SD-R*编号顺序检索；拆分会产生跨文件引用与编号断链 | 2026-10-11 |
| references/module_contracts.md | Skill维护QA | 925 | 维护QA与模块接口的唯一权威来源；已识别出“Checklist短卡 + 详细合同”的拆分方向，未在本轮执行 | 2026-10-11 |
| USER_GUIDE.md | 用户文档 | 906 | 面向人的使用说明，未被任何Workflow列为Required Resource，不参与运行时读取；不得被当作运行时规则来源 | 2026-10-11 |
| workflows/09_shot_design_workflow.md | STATE-06 | 1157 | STATE-06详细镜头设计的单一owner；内部按Shot字段分组，拆分会使字段归属跨文件 | 2026-10-11 |
| workflows/13_review_workflow.md | STATE-09 | 1032 | 三层Review与逐镜逐边界覆盖台账的单一owner；覆盖矩阵需要完整上下文才能核对 | 2026-10-11 |
| knowledge/11_seedance_adapter.md | Model Adapter知识 | 1833 | 与`adapters/seedance-2.0.md`存在能力事实双写风险；正确处置是收敛为单一owner，属独立变更 | 2026-10-11 |
| rules/03_prompt_rules.md | Prompt Rules | 1447 | 22条Prompt规则按编号引用，拆分会使跨规则引用失效 | 2026-10-11 |
| workflows/07_visual_development_workflow.md | STATE-04 | 2330 | 全库最长文件，距Ceiling余量最小；含Aesthetic Decision Lock Gate与多层视觉Gate，是最优先的拆分候选 | 2026-10-11 |
| workflows/01_project_setup_workflow.md | STATE-00 | 1389 | 项目初始化与Project Model Selection Gate的单一owner | 2026-10-11 |

## Ledger Maintenance

- **新增必登记**：任何修改使文件超过Target时，必须在同一次变更中登记，写明Owner、当前行数、留存理由与复审日期。
- **瘦身必摘牌**：文件降到Target以下时，必须在同一次变更中移除条目。不允许保留已经达标的僵尸条目。
- **复审到期必重估**：到达`Review By`时重新判断，要么拆分、要么更新理由与新的复审日期。不得默认续期。
- **拆分优先于扩表**：登记不是长期解法。同一Owner连续两次复审仍未拆分时应视为未处理的技术债。

## Change Interaction

- 本预算不构成新增文件的理由。新增或拆分文件时，`references/module_contracts.md`的`Rule Ownership Check`仍然优先；只有确认现有权威位置不合适才允许新增。
- 本文件的数值与Ledger不与任何其他文件重复：`references/module_contracts.md`的`Context Budget Check`只引用本文件，不复制阈值。
- 读取顺序、按需读取与复用纪律仍由`rules/resource_loading.md`拥有；本文件不重复定义运行时加载行为。
