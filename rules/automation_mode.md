# Fast Automation Mode

## Purpose And Owner

本规则是SD Film的唯一自动推进策略owner。它不创建主STATE、最终Template字段、独立项目事实或并行确认Schema；状态合同只保存当前`Automation Policy`，具体执行仍由既有Workflow、Completion Gate、Asset Lock和Review owner负责。

## Activation And Persistence

只有用户当前明确说“开启自动推进”“快速制作模式”“Fast Mode”或无歧义同义表达时，才将当前项目的`Automation Policy`写为`FAST`。未启用、用户说“关闭自动推进 / 标准模式”，或没有可验证项目状态时为`STANDARD`。模式只改变后续合法步骤的确认方式，不追溯改写既有确认、版本或Accepted Artifact。

每次自动接受必须在当前Artifact或Version History记录`Auto-accepted under FAST`、依据、Revision和时间；用户可随时要求暂停、查看、修改或退回，按现有最小Return Route处理。

## FAST Eligible Work

在输入完整、上游事实已确认且当前QA通过时，FAST可以：

- 自动继续STATE-04、STATE-05的内部设计与合法下一阶段；
- 自动确认STATE-03的当前Prompt Revision，并使用当前环境可用的内置图像工具生成当前资产批次；同一资产类型的Candidate References汇总为一次用户批量审阅，而不是逐Prompt停下；
- 在STATE-06和STATE-07的既有Checklist、Preflight和状态写回均通过时，自动接受Detailed Shot Design与Clip Production Plan；
- 在STATE-08完成必需的Final Visual Blocking Assessment后，同轮继续编译当前Clip Prompt。`REF-SKETCH`仍必须通过既有验证，且不得成为Canonical Asset。

FAST只在事实、范围、模型和所需输入都已锁定时行动。任何失败、冲突、缺失、风险超出当前规则、或用户要求查看/修改时，立即回到对应owner，不以自动模式掩盖问题。

## Hard Stops

FAST不得自动：

- 锁定Creation / Adaptation / Optimization产生的Production Script Proposal，或扩大既有剧本修改授权；
- 首次选择视频模型，或改变已选择的模型、目标时长和执行模式；
- 将任何Candidate Image标为Canonical / Active，或替代用户对资产图片的批准；
- 推断真实人物、授权、品牌/Logo、价格、SKU、法务/受监管承诺或缺失的关键事实；
- 调用未授权的外部服务、提交外部生成、使用未知凭据，或把提示词伪称为外部生成结果；
- 将未实际查看的生成视频标为Review PASS。

这些Hard Stops优先于FAST。用户若想改变其中任一边界，必须在当前请求中明确、具体地授权；仍受适用的Workflow与外部操作权限约束。

## Conflict And Return Route

用户当前指令、已确认事实、当前Workflow Gate、Asset Lock、外部权限和Review证据优先于FAST。FAST与任一约束冲突时，保持当前状态并报告最小待决项；不得新建“自动确认”状态、跳STATE或重做无关Accepted Artifact。
