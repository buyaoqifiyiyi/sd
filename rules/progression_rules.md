# Progression And Anti-Duplication

# Read Scope

本文件被多个阶段复用，**不得整文件通读**：按当前事项只读对应小节。

| 当前事项 | 只读 |
|---|---|
| 收到纯推进命令 | `## Advance Gate` |
| 判定用户确认语义 | `## Confirmation Input Semantics` |
| 判定授权边界 | `## Authorization Boundary` |
| Review 退回或断点恢复 | `## Revision And Resume` |
| 不必在运行时读取 | `## Purpose` |

---

## Purpose

本规则处理“下一步”“继续”“下一个”“往后做”等纯推进命令，防止重复已完成工作或误触发生成行为。

## Advance Gate

收到纯推进命令时，必须依次：

1. 按`rules/state_source.md`解析当前State Source。
2. 核验Current State、State Status、Last Successful Checkpoint、Completed States、Active Artifacts、Pending Decision与Review Return Route。
3. 对当前Workflow执行`rules/completion_gate.md`；未完成时只继续最近未完成步骤。
4. 当前阶段已完成时，路由到合法Next Workflow，不重复输出已完成交付物；若当前`Automation Policy: FAST`或用户本轮明确要求统一交付包，按`rules/automation_mode.md`的`Unified Delivery Packages`聚合符合资格的相邻阶段。
5. STATE-08多Clip项目按默认单Clip交付制，只输出下一个尚未交付Clip；除非用户本轮明确要求批量或全部输出，或当前`Automation Policy: FAST`命中`rules/automation_mode.md`的连续链资格。
6. 状态变化后按`references/project_state_contract.md`写回。

当`Automation Policy: FAST`时，先读取`rules/automation_mode.md`。对其明确列出的Eligible Work，当前Workflow完成必需QA后必须按FAST Continuous Chain在同一轮自动继续、写回并按Unified Delivery Packages聚合展示；不得跳过State、Hard Stop、外部权限或事实冲突处理。未命中FAST资格时仍按本规则的最近Checkpoint停止。

## Confirmation Input Semantics

本规则是所有主STATE与辅助Workflow的用户确认输入语义唯一owner。只要当前轮已展示一个可核对、版本和范围明确的确认检查点，任何语义上表示继续推进的表达（包括但不限于`下一步`、`下一个`、`继续`、`往后做`、`接着做`、`next`、`proceed`、`好的`）即为确认当前检查点，并授权完成该检查点后的合法下一生产步骤；不再额外要求“确认 / 批准 / 锁定”等同义措辞。所有Workflow、Rule、Template和Reference中“用户确认”“明确确认”“明确批准”“等待确认”均按本节解释，除非其拥有者明确说明该步骤不是确认而是选择、缺失输入或外部操作授权。

该语义不替用户在多个互斥选项中作选择，不虚构缺失事实或文件，不提交外部服务，不授予真实人物、品牌、法务、受监管内容等额外权限，也不使未展示、版本不明或范围含混的Artifact得到确认。出现这些情形时，只呈现最小必要选项、输入或风险；用户的纯推进命令本身不解决它们。确认后的写回仍必须保留Artifact、Revision、时间和确认范围证据。

### Exception-Based Batch Confirmation｜例外式批次确认

当当前检查点已经展示一个**范围、Revision 与逐项对象都能核对**的多项批次（多个资产的Prompt、多张Candidate Image、多个Clip或其他同类交付物）时，用户的确认输入按例外式判读：

- 用户指出其中不满意的**具体项**（例如“第3张重做”“CHAR-002换掉”“其余可以”）时，该输入构成对其余已展示项的确认；被指出项按其owner的最小Return Route退回，不牵连同批已确认项。
- 用户明确**否决整批**（例如“全部重做”“都不行”）时，整批退回，不产生项目级确认。
- 用户**未指出问题**而给出推进表达时，构成对该批次全部已展示项的确认。

例外式判读的前提不可省略：只有已经真实展示、且每项都能被核对到具体对象与Revision的批次才可被确认。未展示、未生成、范围不明或无法逐项对应的内容不因用户沉默或笼统推进而获得确认，也不得以“用户没有提出异议”替代展示。被退回项仍服从各自的Hard Gate与客观Triage，不因同批其他项已确认而被跳过。

批次如何构成、如何分批与如何应用，由交付物owner定义；本节的确认语义对资产批次与Clip批同等适用。资产批次的构成与两轮交付见`rules/02_asset_rules.md`的`Asset Batch Delivery`。

## Authorization Boundary

纯推进命令只授权继续已确定的下一生产步骤，不自动授权：

- 把Creation或Optimization分支的Production Script Proposal标记为Production-Locked
- 批量输出全部Clip
- 激活Storyboard或AUDIO / SEED-AUDIO辅助模块
- 跳过当前Completion Gate
- 重做已接受且未受影响的Artifact

若下一步骤本身需要用户确认、外部输入或生成授权，输出当前检查点与待确认项后停止；当前确认检查点的纯推进输入按本规则的`Confirmation Input Semantics`处理。`Automation Policy: FAST`中由`rules/automation_mode.md`明确授权的Prompt自动确认、GPT Image/外部图像批次、STATE-06/07自动接受、同轮`REF-SKETCH`后Prompt编译和完整Clip之间的Prompt批量交付除外。不得把用户最终目标误解释为本轮立即交付全部后续成果。

STATE-08的Before-Single-Clip-Prompt Gate是本规则的窄范围例外：用户请求指定Clip或说“下一个 / 下一步 / 继续”时，已授权系统执行该Clip的Final Visual Blocking Anchor Assessment。Final=`REQUIRED`时，生成并验证一张受限`REF-SKETCH`属于当前Prompt的自动内部生产步骤，不等同于STATE-03资产生图、Storyboard激活或Candidate确认；无需另行把纯推进命令解释为资产Prompt确认。`STANDARD`本轮停在草图、注册与用途说明，下一次推进才输出Prompt；`FAST`在草图验证、注册和用途说明后同轮编译，并按Continuous Chain继续其余符合资格的Clip。任何角色 / 环境 / 道具 / FX资产图、Formal Keyframe或非Gate图片仍服从原授权边界。

## Revision And Resume

- Review退回或用户局部修改时，只恢复受影响的最小范围，保留Accepted Unaffected Artifacts。
- 同一生成失败第二次必须降级，第三次返回事实或设计拥有者；禁止盲重试。
- 项目中断、跨轮继续或Checkpoint恢复调用`workflows/18_project_resume_workflow.md`，但不创建新STATE。
