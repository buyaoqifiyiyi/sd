# Fast Automation Mode

# Read Scope

本文件只在使用`Automation Policy: FAST`时读取，**不得整文件通读**：按当前事项只读对应小节。

| 当前事项 | 只读 |
|---|---|
| 启用或判定 FAST | `## Activation And Persistence`、`## FAST Eligible Work` |
| 连续推进与聚合交付 | `## FAST Continuous Chain`、`## Unified Delivery Packages`、`### Delivery Receipt｜交付收据` |
| 边界与冲突 | `## Hard Stops`、`## Conflict And Return Route` |
| 未启用 FAST 时 | **不读本文件**；激活判定由`rules/activation_rules.md`拥有 |
| 不必在运行时读取 | `## Purpose And Owner` |

---

## Purpose And Owner

本规则是SD Film的唯一自动推进策略owner。它不创建主STATE、最终Template字段、独立项目事实或并行确认Schema；状态合同只保存当前`Automation Policy`，具体执行仍由既有Workflow、Completion Gate、Asset Lock和Review owner负责。

**FAST只自动确认，不减少流程与产物。** 被自动接受的是"确认"这一步，不是阶段、检查或交付物本身：每个阶段的Required Read、QA、Completion Gate、状态写回与完整Template交付物一件不少，`rules/05_output_rules.md`的用户可见交付清单也不因FAST而缩短。任何把自动模式解释成"可以少做一个阶段、少跑一次检查或少给一件产物"的用法都无效。

## Activation And Persistence

只有用户当前明确说“开启自动推进”“快速制作模式”“Fast Mode”“尽量少确认”“只在关键节点停”或“自动完成可逆步骤”等无歧义表达时，才将当前项目的`Automation Policy`写为`FAST`。未启用、用户说“关闭自动推进 / 标准模式”，或没有可验证项目状态时为`STANDARD`。模式只改变后续合法步骤的确认方式，不追溯改写既有确认、版本或Accepted Artifact。

每次自动接受必须在当前Artifact或Version History记录`Auto-accepted under FAST`、依据、Revision和时间；用户可随时要求暂停、查看、修改或退回，按现有最小Return Route处理。

## FAST Eligible Work

在输入完整、上游事实已确认且当前QA通过时，FAST可以：

- 自动继续STATE-04、STATE-05的内部设计与合法下一阶段；
- 在Production Setup已确认项目图像模型默认项、当前资产批次已继承且选择GPT Image时，自动确认STATE-03的当前Prompt Revision，并使用当前环境实际可用的GPT Image在同一轮内提交当前资产批次；同一批次的Candidate References汇总为一次用户批量审阅，而不是逐Prompt或逐张停下；`Image Delivery Mode: DIRECT_IMAGE`（由`modules/image-model-selection.md`拥有）在同一资格条件下同样适用本条授权——两个触发指向同一条款，不叠加出新授权，且都不授权自动批准Candidate Image；
- 在STATE-06和STATE-07的既有Checklist、Preflight和状态写回均通过时，自动接受Detailed Shot Design与Clip Production Plan；
- 在STATE-08完成必需的Final Visual Blocking Assessment后，同轮继续编译当前Clip Prompt。`REF-SKETCH`仍必须通过既有验证，且不得成为Canonical Asset。
- 当前已锁定视频模型与执行Profile、所有相关Execution Clip均已Confirmed且无未决风险时，按Clip顺序自动编译完整视频Prompt；在单轮交付容量不足时，只能在完整Clip之间分批，下一次普通推进直接续交下一批而不再索取内部确认。
- 当前资产批次已继承Production Setup确认的图像模型默认项且为外部模型时，自动确认该批次当前Prompt Revision并交付可提交的外部生成包；不得代替用户向外部服务提交、不得声称已生成，也不得跳过Candidate Image审阅。

FAST只在事实、范围、模型和所需输入都已锁定时行动。任何失败、冲突、缺失、风险超出当前规则、或用户要求查看/修改时，立即回到对应owner，不以自动模式掩盖问题。

资产与`REF-SKETCH`的客观Candidate Output Triage / Cleanup由各自owner在STANDARD与FAST下自动执行；它只弃用不合格或多余的未确认输出，不构成Candidate批准，也不得触碰Hard Stop保护的Canonical / Active图片。

## FAST Continuous Chain

当FAST Eligible Work的QA通过后，系统必须从当前合法位置连续推进STATE-04 → STATE-05 → STATE-06 → STATE-07 → STATE-08，不在这些阶段之间为可逆的内部确认、已锁定模型的重复确认、已验证`REF-SKETCH`或单个Clip交付再停下。连续链只在最近的Hard Stop、缺失关键输入、互斥选择、外部操作、Candidate Image批次审阅、QA失败或用户明确要求查看/修改时停止。

连续链不跳过主STATE、Completion Gate或任何检查，也不减少阶段与交付物；它只消除已通过检查后的人工“继续”往返。视频Prompt的编译与交付不是外部生成提交，仍必须保留每个Clip的完整结构、模型预算和无BGM边界。

## Unified Delivery Packages

`Automation Policy: FAST`默认将同一连续链内已经完成、写回且没有Hard Stop的相邻阶段合并为一次用户交付——**合并的只是展示切片，不是阶段本身**。标准模式只有用户明确说“统一输出”“合并输出”“一次性制作包”“按包交付”或同义表达时才启用本轮聚合展示；该表达只改变展示切片，不替代任何未展示Artifact的确认。

可使用的包只有既有阶段的顺序组合，包名只是展示封套，不是新STATE、Artifact、Project State字段或最终Template：

- `Preproduction Package`：STATE-04完成的Visual Direction摘要（最低内容由`workflows/07_visual_development_workflow.md`的`# Visual Direction Summary Contract`唯一拥有：基线行 + Visual Grammar Baseline行 + 四锁各一行）→ STATE-05完整Scene Breakdown → STATE-06完整Detailed Shot Design。摘要只压缩呈现，不替代STATE-04的内部建立与Project Bible写入；用户明确要求查看视觉开发成果时，该槽位必须换成Workflow的完整输出，不得以摘要代替。
- `Execution Package`：STATE-07完整Execution Clip Plan → STATE-08按Clip顺序的完整目标模型Prompt。仅在视频模型/Profile已锁定、Clip Plan可按FAST自动接受且所有逐Clip检查通过时，才能在同一包内交付Prompt。
- `Asset Candidate Package`：同一已锁定图像模型与同类资产批次的Prompt / 生成结果筛选；只展示`KEEP`或`NEEDS_USER_SELECTION`项，并在Candidate Image审阅前停止，绝不延伸到STATE-04。批次本身的构成、分批与两轮交付由`rules/02_asset_rules.md`的`Asset Batch Delivery`拥有，本节只拥有FAST下的聚合展示触发；STANDARD下的同类批次交付不依赖本节。

包内仍必须按原顺序完成每个Workflow的Required Read、QA、Completion Gate和状态写回；每个正式阶段交付物使用其原有完整Template，不能以摘要、"同上"、合并表头或新字段代替。若单轮容量不足，只能在完整Artifact或完整Clip之间分批；下一次普通推进续交同一包的下一完整部分，不重新展示已交付内容。

最近的Hard Stop、缺失关键输入、模型选择、Candidate Image审批、外部提交、QA失败或用户要求查看/修改，立即截断包并只展示最小待决项。不得为了凑齐一个包猜测事实、预先生成最终Prompt、或把未确认的资产 / Clip Plan标记完成。

### Delivery Receipt｜交付收据

聚合交付轮必须在同一轮给出**交付收据**，逐项列出：阶段 → 工件（其完整Template）→ 本轮状态。状态只允许三种：

- `本轮完整输出`：该Template已在本轮实际写出；
- `已在Accepted Artifact`：工件已在项目内存在且Revision一致，收据写明位置与Revision；
- `待交付`：本轮与项目内都没有该工件的完整形态。

判定纪律：

- 用户可见阶段（STATE-05 Scene Breakdown、STATE-06 Detailed Shot Design、STATE-07 Clip Plan、STATE-08 Prompt）**不得只写“已完成×××”**；声称完成却拿不出该Template形态的，一律记为`待交付`，该阶段不得写`State Status: COMPLETE`。
- **生产交付包必须单列一行。** STATE-08交付轮的收据必须包含`生产交付包`条目，写明形态与位置：`目录 + zip`的实际路径，或按`references/asset_package.md`的`## Access Precondition`降级阶梯得到的合法形态（目录无zip / 清单+命名映射 / 命名映射表）并标注`未打包`。包位于Project Root之外、不属于Project State，因此它的状态**不使用`已在Accepted Artifact`**：只允许`本轮完整输出`或合法降级形态。未列出包路径、也未给出降级标注的，该交付轮不得判完成，也不得声称已打包。
- **最终Prompt交付轮的收据必须包含`Prompt纪律自检`条目。** 该轮交付最终Prompt时，收据按`knowledge/quality/prompt_scorecard.md`的`## Discipline Self-Check｜六条执行自检`逐条给出结论：每条只写`过` / `不过` / `不适用`并附一句可观察证据，`不过`的条目同时写入该轮剩余风险。它只提高**可见性**：不改变该交付轮能否判完成、不把自检升为Hard Gate、不新增Project State字段、不替代Template，也不进入最终Prompt正文。
- 收据出现`待交付`时，下一次普通推进必须先续交该完整工件，再继续后续阶段的交付；内部生产可以继续，但不得把`待交付`写成完成。
- 收据只做交付核对，不新增Project State字段、不替代Template、不改变Completion Gate判据（仍由`rules/completion_gate.md`与`references/project_state_contract.md`拥有）。STANDARD下用户显式要求聚合时同样适用。

## Hard Stops

FAST不得自动：

- 锁定Creation / Adaptation / Optimization产生的Production Script Proposal，或扩大既有剧本修改授权；
- 首次确认项目图像模型默认项或项目视频模型偏好，或改变已选择的模型、目标时长和执行模式；
- 为当前资产批次选择不同于项目默认项的例外图像模型；
- 将任何Candidate Image标为Canonical / Active，或替代用户对资产图片的批准；
- 推断真实人物、授权、品牌/Logo、价格、SKU、法务/受监管承诺或缺失的关键事实；
- 调用未授权的外部服务、提交外部生成、使用未知凭据，或把提示词伪称为外部生成结果；
- 将未实际查看的生成视频标为Review PASS。

这些Hard Stops优先于FAST。用户若想改变其中任一边界，必须在当前请求中明确、具体地授权；仍受适用的Workflow与外部操作权限约束。

## Conflict And Return Route

用户当前指令、已确认事实、当前Workflow Gate、Asset Lock、外部权限和Review证据优先于FAST。FAST与任一约束冲突时，保持当前状态并报告最小待决项；不得新建“自动确认”状态、跳STATE或重做无关Accepted Artifact。
