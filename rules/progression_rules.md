# Progression And Anti-Duplication

## Purpose

本规则处理“下一步”“继续”“下一个”“往后做”等纯推进命令，防止重复已完成工作或误触发生成行为。

## Advance Gate

收到纯推进命令时，必须依次：

1. 按`rules/state_source.md`解析当前State Source。
2. 核验Current State、State Status、Last Successful Checkpoint、Completed States、Active Artifacts、Pending Decision与Review Return Route。
3. 对当前Workflow执行`rules/completion_gate.md`；未完成时只继续最近未完成步骤。
4. 当前阶段已完成时，路由到合法Next Workflow，不重复输出已完成交付物。
5. STATE-08多Clip项目按默认单Clip交付制，只输出下一个尚未交付Clip；除非用户本轮明确要求批量或全部输出。
6. 状态变化后按`references/project_state_contract.md`写回。

## Authorization Boundary

纯推进命令只授权继续已确定的下一生产步骤，不自动授权：

- 在STATE-03跳过Prompt确认并调用图片生成工具
- 把Candidate图片标记为Confirmed / Canonical
- 把Creation或Optimization分支的Production Script Proposal标记为Production-Locked
- 批量输出全部Clip
- 激活Storyboard或AUDIO / SEED-AUDIO辅助模块
- 跳过当前Completion Gate
- 重做已接受且未受影响的Artifact

若下一步骤本身需要用户确认、外部输入或生成授权，输出当前检查点与待确认项后停止。不得把用户最终目标误解释为本轮立即交付全部后续成果。

STATE-08的Before-Single-Clip-Prompt Gate是本规则的窄范围例外：用户请求指定Clip或说“下一个 / 下一步 / 继续”时，已授权系统执行该Clip的Final Visual Blocking Anchor Assessment。Final=`REQUIRED`时，生成并验证一张受限`REF-SKETCH`属于当前Prompt的自动内部生产步骤，不等同于STATE-03资产生图、Storyboard激活或Candidate确认；无需另行把纯推进命令解释为资产Prompt确认。本轮必须停在草图、注册与用途说明，下一次推进才输出Prompt。任何角色 / 环境 / 道具 / FX资产图、Formal Keyframe或非Gate图片仍服从原授权边界。

## Revision And Resume

- Review退回或用户局部修改时，只恢复受影响的最小范围，保留Accepted Unaffected Artifacts。
- 同一生成失败第二次必须降级，第三次返回事实或设计拥有者；禁止盲重试。
- 项目中断、跨轮继续或Checkpoint恢复调用`workflows/18_project_resume_workflow.md`，但不创建新STATE。
