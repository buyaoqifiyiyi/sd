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

## Metric

**主度量是 UTF-8 字节数，不是行数。**

模型的上下文成本按 token／字符计算，不按行。本库Markdown空行占比在31%–57%之间，用行数会把体量高估近一倍，并系统性地漏判段落密集的文件。实测教训：一个395行的文件实为57 KB（全库第4），而一个2330行的文件实为33 KB（中等）——按行数排名会把这两者判反。

行数只作为`SKILL.md`的辅助约束，不作为其他文件的阈值。

## Budget Tiers

| Tier | 阈值 | 要求 |
|---|---|---|
| Entry | `SKILL.md` ≤ 12 KB 且 ≤ 120 行 | 只保留身份、版本、入口、主路由、全局不变量与索引；不得复制细粒度规则、算法或Template字段 |
| Target | 单文件 ≤ 50 KB | 超过必须登记在下方Size Ledger |
| Ceiling | 单文件 ≤ 100 KB | **任何文件都不得达到**；达到即视为结构性失控，必须先拆分再提交 |

## File Classes

超过Target的文件必须登记，并归入以下一类。类别决定“能不能留着不拆”：

| Class | 含义 | 处置 |
|---|---|---|
| `COMPOSITE` | 合集型：由并列的独立小节组成，任何一次使用只需要其中一两节 | **应拆**。登记只是拆分前的过渡，不得长期保留 |
| `INTEGRAL` | 整体型：由一条连贯的推理链或流程组成，使用时必须整块读完 | 允许保留在Target以上；但必须靠`rules/resource_loading.md`的Read Budget按章节读，并写明该边界 |
| `NON_RUNTIME` | 非运行时文档，不参与运行时读取 | 豁免Target；但文件自身必须声明为非运行时文件 |

判定方法：看小节之间是否互相依赖。小节可独立成立 → `COMPOSITE`；缺一节就读不懂整条链 → `INTEGRAL`。**只看体量不看结构会拆错文件**：整体型文件拆开后，单次使用反而要读更多文件。

## Size Ledger

超过Target的文件必须逐条登记。登记是**债务记录，不是豁免证明**：它记录“当前为什么还没拆”和“什么时候必须重新评估”，不改变Target的适用，也不豁免Ceiling。

未登记的超Target文件、已降到Target以下但仍留在此表的条目、以及指向不存在文件的条目，都会使Validator失败。

| File | Class | Size (r53) | Why It Stays | Review By |
|---|---|---|---|---|
| USER_GUIDE.md | NON_RUNTIME | 64.7 KB | 面向人的使用说明，文件顶部已自证为非运行时文件，未被任何Workflow列为Required Resource | 2026-10-11 |
| knowledge/prompt_compilation/state08_projection.md | INTEGRAL | 57.3 KB | STATE-08编译链，缺任一Gate都会漏投影，拆分会让每个Clip多读一个文件；按章节读：Global/Per-Shot Projection Matrix、Serialization Rules、Applicability Gate为常用入口 | 2026-10-11 |
| workflows/09_shot_design_workflow.md | INTEGRAL | 51.4 KB | STATE-06 Step 0—7线性流程，Shot字段之间互相约束；按章节读：Professional Detailed Shot Script Schema Gate与Completion Requirement为常用入口 | 2026-10-11 |

## Ledger Maintenance

- **新增必登记**：任何修改使文件超过Target时，必须在同一次变更中登记，写明Class、当前体量、留存理由与复审日期。
- **瘦身必摘牌**：文件降到Target以下时，必须在同一次变更中移除条目。不允许保留已经达标的僵尸条目。
- **COMPOSITE不得长期挂账**：`COMPOSITE`类条目连续两次复审仍未拆分，视为未处理的技术债。
- **复审到期必重估**：到达`Review By`时重新判断，要么拆分、要么更新理由与新的复审日期。不得默认续期。
- **拆分必须按编号／职责边界**：拆分后每个文件的编号或命名空间保持连续，并由原文件提供Index；不得为压体量而切断互相依赖的链条。

## Long-Term Maintenance

体量问题不会因为一次拆分而结束——只要还在迭代，文件就还会增长。所以本预算分三层执行，缺任何一层都会退化回“越写越长”。

### 1. Prevent｜写之前

- **先归位，再新增**：新增内容默认补进既有owner；先按`Rule Ownership Check`确认，确认不了才允许新增文件。
- **不得先加后登**：如果本次变更会让任一文件**超过Target**，或把一个已在Target以上的文件再推高**10%以上**，必须在同一次变更内处理（拆分／合并／删除冗余），不得靠登记台账蒙混过关。
- **新文件不得一出生就是大文件**：新建Markdown不得超过Target的60%（30 KB）。超过即说明它本应是既有文件的一节，或本身就该再分。
- **正文不复制**：引用其他文件只写路由或不变量，不复制完整协议或Schema（见`Duplicate Rule Check`）。

### 2. Enforce｜改的时候

- `scripts/validate_sd_film.py`以**字节阈值、文件类别与Ledger一致性**做确定性检查，不依赖维护者自觉。
- `Skill Update Self-Check`的`Context Budget Check`维度按本文件判定，结果写进必交的报告模板。

### 3. Audit｜周期性

- **周期性全库体检**：按固定节奏运行`scripts/validate_sd_film.py --skill-root <skill-root> --report`，输出字节排名、Ledger一致性、复审到期项与最接近Ceiling的文件。
- **体检只负责发现累积**，不替代事前与事中；发现项按风险分级在当轮修复。
- **台账随体量走**：Ledger的`Size`列必须反映最近一次实测值；实测与登记值差异超过20%即视为台账过期，Validator会失败。
- **到期必须重估**：到达`Review By`时重新判定，要么拆分、要么更新理由与新的复审日期。`COMPOSITE`类连续两次复审仍未拆分，按未处理技术债上报。

### 4. Debt Policy

- `COMPOSITE`条目是**待拆队列**，不是长期状态。
- `INTEGRAL`条目必须写明“按章节读”的入口；不写入口的`INTEGRAL`视同未登记。
- 宁可拆一个文件，也不要为了凑阈值删掉已确认的规则、字段归属或回归场景。

## Change Interaction

- 本预算不构成新增文件的理由。新增或拆分文件时，`references/maintenance_self_check_protocol.md`的`Rule Ownership Check`仍然优先；只有确认现有权威位置不合适才允许新增。
- 本文件的数值与Ledger不与任何其他文件重复：`references/maintenance_self_check_protocol.md`的`Context Budget Check`只引用本文件，不复制阈值。
- 读取顺序、按需读取与复用纪律仍由`rules/resource_loading.md`拥有；本文件不重复定义运行时加载行为。
