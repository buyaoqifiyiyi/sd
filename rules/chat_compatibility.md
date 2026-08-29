# Chat-Compatible Execution

## Purpose

普通Chat不是缩减模式。除状态持久化位置和项目输入来源不同外，它必须执行与Work/Codex相同的STATE-00至STATE-09 Pipeline、Workflow、Completion Gate、资产确认闭环、Director Decision Layer、Knowledge Reflection、Clip规则和Template合同。

## Inputs

普通Chat可从以下来源建立或恢复Project Context；Work/Codex中的`Active Project Root`仍是本地状态与交付物的持久化目标：

- 用户本轮提供的文本、附件和明确确认
- 当前对话中仍可验证的项目事实与Artifact
- 完整`portable_project_status.md`
- 运行时能够实际检索的已安装Skill资源

不得因为无法读取`C:\Users\Lenovo\.codex\skills\sd`、本地项目Root或`project_registry.json`而停止、报错或要求用户上传整个目录。需要规则、Workflow、Knowledge或Template时，先通过当前运行时的已安装资源机制检索；只有实际检索失败且资源确属当前步骤必需时，才请求用户提供该资源。

## Portable Execution

- 按`rules/state_source.md`选择Portable State或把当前可验证Project Context规范化为Canonical Portable State。
- Portable State结构与字段由`references/project_state_contract.md`唯一拥有。
- 每次进入、完成、退回、恢复Workflow或确认资产后，在回复中输出更新后的完整Portable State；不得只给路由摘要或自创简化状态。
- 普通Chat写`Portable State Availability: READY`、`Portable Sync Status: PORTABLE_ONLY`，并保留真实Project ID、Revision、Checkpoint、Completed States、Confirmed Assets和Next Workflow。
- 用户在后续对话提供更新后的Portable State时，先校验与迁移Schema，再恢复执行。

## Behavior Parity

普通Chat仍必须：

- 完成STATE-01剧本分类、改编/优化决策与Production Lock门槛。
- 完成STATE-03 Prompt确认→生成→图片确认的双确认闭环；工具不可用时保持`IN_PROGRESS`，不得把文字描述当成Confirmed Asset。
- 在STATE-06/07/08执行适用的镜头、Clip、连续性、Preflight、Reference Budget和Template门槛。
- 遵守单Clip默认交付、用户确认、Review退回和最小必要修订。
- 仅在用户显式请求声音身份资产时激活AUDIO / SEED-AUDIO模块。

本规则不允许虚构本地文件已写入、资产已生成或用户已确认。无法持久化本机文件时，用Portable State和当前回复中的完整交付物保持可恢复性。
