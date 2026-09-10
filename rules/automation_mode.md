# Fast Automation Mode

## Purpose And Owner

本规则是SD Film的唯一自动推进策略owner。它不创建主STATE、最终Template字段、独立项目事实或并行确认Schema；状态合同只保存当前`Automation Policy`，具体执行仍由既有Workflow、Completion Gate、Asset Lock和Review owner负责。

## Activation And Persistence

只有用户当前明确说“开启自动推进”“快速制作模式”“Fast Mode”“尽量少确认”“只在关键节点停”或“自动完成可逆步骤”等无歧义表达时，才将当前项目的`Automation Policy`写为`FAST`。未启用、用户说“关闭自动推进 / 标准模式”，或没有可验证项目状态时为`STANDARD`。模式只改变后续合法步骤的确认方式，不追溯改写既有确认、版本或Accepted Artifact。

每次自动接受必须在当前Artifact或Version History记录`Auto-accepted under FAST`、依据、Revision和时间；用户可随时要求暂停、查看、修改或退回，按现有最小Return Route处理。

## FAST Eligible Work

在输入完整、上游事实已确认且当前QA通过时，FAST可以：

- 自动继续STATE-04、STATE-05的内部设计与合法下一阶段；
- 在STATE-00已确认项目图像模型默认项、当前资产批次已继承且选择Built-in Image时，自动确认STATE-03的当前Prompt Revision，并使用当前环境实际可用的内置图像工具生成当前资产批次；同一资产类型的Candidate References汇总为一次用户批量审阅，而不是逐Prompt停下；
- 在STATE-06和STATE-07的既有Checklist、Preflight和状态写回均通过时，自动接受Detailed Shot Design与Clip Production Plan；
- 在STATE-08完成必需的Final Visual Blocking Assessment后，同轮继续编译当前Clip Prompt。`REF-SKETCH`仍必须通过既有验证，且不得成为Canonical Asset。
- 当前已锁定视频模型与执行Profile、所有相关Execution Clip均已Confirmed且无未决风险时，按Clip顺序自动编译完整视频Prompt；在单轮交付容量不足时，只能在完整Clip之间分批，下一次普通推进直接续交下一批而不再索取内部确认。
- 当前资产批次已继承STATE-00确认的图像模型默认项且为外部模型时，自动确认该批次当前Prompt Revision并交付可提交的外部生成包；不得代替用户向外部服务提交、不得声称已生成，也不得跳过Candidate Image审阅。

FAST只在事实、范围、模型和所需输入都已锁定时行动。任何失败、冲突、缺失、风险超出当前规则、或用户要求查看/修改时，立即回到对应owner，不以自动模式掩盖问题。

资产与`REF-SKETCH`的客观Candidate Output Triage / Cleanup由各自owner在STANDARD与FAST下自动执行；它只弃用不合格或多余的未确认输出，不构成Candidate批准，也不得触碰Hard Stop保护的Canonical / Active图片。

## FAST Continuous Chain

当FAST Eligible Work的QA通过后，系统必须从当前合法位置连续推进STATE-04 → STATE-05 → STATE-06 → STATE-07 → STATE-08，不在这些阶段之间为可逆的内部确认、已锁定模型的重复确认、已验证`REF-SKETCH`或单个Clip交付再停下。连续链只在最近的Hard Stop、缺失关键输入、互斥选择、外部操作、Candidate Image批次审阅、QA失败或用户明确要求查看/修改时停止。

连续链不跳过主STATE、Completion Gate或任何检查；它只消除已通过检查后的人工“继续”往返。视频Prompt的编译与交付不是外部生成提交，仍必须保留每个Clip的完整结构、模型预算和无BGM边界。

## Unified Delivery Packages

`Automation Policy: FAST`默认将同一连续链内已经完成、写回且没有Hard Stop的相邻阶段合并为一次用户交付。标准模式只有用户明确说“统一输出”“合并输出”“一次性制作包”“按包交付”或同义表达时才启用本轮聚合展示；该表达只改变展示切片，不替代任何未展示Artifact的确认。

可使用的包只有既有阶段的顺序组合，包名只是展示封套，不是新STATE、Artifact、Project State字段或最终Template：

- `Preproduction Package`：STATE-04完成的简洁Visual Direction摘要（仅在用户要求查看时展示）→ STATE-05完整Scene Breakdown → STATE-06完整Detailed Shot Design。
- `Execution Package`：STATE-07完整Execution Clip Plan → STATE-08按Clip顺序的完整目标模型Prompt。仅在视频模型/Profile已锁定、Clip Plan可按FAST自动接受且所有逐Clip检查通过时，才能在同一包内交付Prompt。
- `Asset Candidate Package`：同一已锁定图像模型与同类资产批次的Prompt / 生成结果筛选；只展示`KEEP`或`NEEDS_USER_SELECTION`项，并在Candidate Image审阅前停止，绝不延伸到STATE-04。

包内仍必须按原顺序完成每个Workflow的Required Read、QA、Completion Gate和状态写回；每个正式阶段交付物使用其原有完整Template，不能以摘要、"同上"、合并表头或新字段代替。若单轮容量不足，只能在完整Artifact或完整Clip之间分批；下一次普通推进续交同一包的下一完整部分，不重新展示已交付内容。

最近的Hard Stop、缺失关键输入、模型选择、Candidate Image审批、外部提交、QA失败或用户要求查看/修改，立即截断包并只展示最小待决项。不得为了凑齐一个包猜测事实、预先生成最终Prompt、或把未确认的资产 / Clip Plan标记完成。

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
