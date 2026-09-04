# Skill Experience Module

## Purpose

本模块维护跨项目、可复用的技能经验。它记录经过实际结果或用户反馈验证的工作规律，用于改善后续产出与项目迭代；它不是项目经验、Project State、Project Bible或Asset Registry。

## Operating Model

1. 在 STATE-09 Review 或生成失败复盘后，系统可自动提出一个或多个 `Experience Candidate`。
2. 候选必须说明观察、证据、适用条件、预期影响与不确定性；候选不会自动写入经验库。
3. 用户明确确认后，按 `references/skill_experience_contract.md` 写入经验库并生成新经验版本。
4. 已确认经验只在用户明确要求“使用历史经验 / 调用经验库”，或当前Review/失败复盘明确处理经验时读取，作为只读建议参与产出决策；不得在新项目启动、普通Workflow路由或制作交付前自动查询、匹配类似项目或应用。当前用户指令、项目事实、Rules、Workflow与Template始终优先。
5. 项目迭代时，经验只能形成可追踪的 `Iteration Recommendation`，由对应事实/设计Owner和用户确认后修改项目交付物；不得直接改写Production-Locked Script、Confirmed Asset、Accepted Take、Shot、Clip或Prompt。

## Experience Quality

- 经验必须来自可核对的Review结果、失败模式、用户明确反馈或重复观察。
- 单一项目的一次性事实、个人偏好、未经验证的猜测和临时Prompt不得直接升级为技能经验。
- 经验应尽量描述“在什么条件下采取什么策略、观察到什么结果”，避免绝对化为所有项目都适用的规则。
- 发现经验与现有规则或已确认项目事实冲突时，经验标记为 `CONFLICT / RETIRE`，返回对应Owner；不得用经验掩盖冲突。

## Application Record

内部应用时保留：`Experience ID`、命中的条件、采用/不采用决定、影响的产出或项目迭代范围，以及验证结果。默认不把内部经验库全文复制到最终Prompt或Review模板。

## Boundary

本模块不创建STATE、不拥有阶段最终Schema、不改变Completion Gate、不替代Screenwriter、Director、Camera、Asset、Continuity或Review Owner，也不自动触发AUDIO / MUSIC模块。

它也不是项目发现机制：不得用经验Ledger、历史项目名称、题材、素材或相似度来决定当前项目、建立项目登记或延迟首次剧本交付。
