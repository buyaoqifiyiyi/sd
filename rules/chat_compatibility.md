# Chat-Compatible Execution

## Purpose

普通Chat不是缩减模式。除状态持久化位置和项目输入来源不同外，它在生产运行时必须执行与Work/Codex相同的STATE-00至STATE-08主Pipeline（STATE-09 Review按`rules/activation_rules.md`显式调用）、Workflow、Completion Gate、资产确认闭环、Director Decision Layer、Knowledge Reflection、Clip规则和Template合同。

## Inputs

普通Chat可从以下来源建立或恢复Project Context；Work/Codex中的`Active Project Root`仍是本地状态与交付物的持久化目标：

- 用户本轮提供的文本、附件和明确确认
- 当前对话中仍可验证的项目事实与Artifact
- 完整`portable_project_status.md`
- 运行时能够实际检索的已安装Skill资源

Skill Definition与Project Context是两类独立来源。显式“调用 / 重新调用 / 重新加载SD”先按`rules/runtime_reload.md`重新解析当前Chat runtime实际可访问的installed / exposed Skill resources；随后才按`rules/state_source.md`选择项目事实。Portable State可恢复项目，但不能证明当前Skill已经重载，也不是Skill Definition副本。

不得因为无法读取`C:\Users\Lenovo\.agents\skills\sd`或本地项目Root而停止、报错、默认要求切Work或要求用户上传整个目录。需要规则、Workflow、Knowledge或Template时，先通过当前运行时实际可用的Skill资源机制检索；只有实际检索失败且资源确属当前步骤必需时，才请求用户提供该资源。Work只用于用户要求直接编辑/检查本地Skill或项目文件，或任务确实需要本地文件操作而普通Chat没有等价访问能力的情况；普通制作执行本身不要求Work。

## Portable Execution

- 按`rules/state_source.md`选择Portable State或把当前可验证Project Context规范化为Canonical Portable State。
- Portable State结构与字段由`references/project_state_contract.md`唯一拥有。
- 每次进入、完成、退回、恢复Workflow或确认资产后，在内部更新完整Portable State；只有用户明确要求保存、导出、恢复核对或查看项目状态时，才在回复中输出完整Portable State。普通制作交付不得因状态镜像占用对话篇幅。
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

## 联想控制｜讨论阶段的措辞纪律

讨论Prompt、拆分镜或选风格时，用户自己的用词与模型补全的内容都会成为后续Prompt的素材。本节只约束**讨论与草案阶段如何选用措辞**；产物侧的归因索引与登记位由`knowledge/quality/prompt_scorecard.md`的`## 联想事故归因与禁用词登记`拥有，本节不复制其症状表。

**先输出本轮对话契约，再加内容。** 涉及Prompt、分镜或风格的产出轮，先只写清本轮要覆盖的字段范围、必须出现项与禁止出现项，再补内容；内容不得反过来扩展这个范围。这个"轮次契约"与Template固定输出契约是两件事，不得互相替代。

**唯一锚点。** 同一意图只给一条主锚点，并列多个方向要标明各自代价，不得把互不兼容的联想项堆成一个"参考"。**单次回应不堆叠三个以上可选方案**；超过三个改用一句话说明取舍方向，由用户选定后再展开。

**不得靠联想补全事实。** 高共现词——导演名、流派名、题材风格名、情绪标签、名场面、平台名、器材与品牌名——出现时必须判定它是**当前项目的必要身份**，还是只在调用默认视觉包。默认视觉包不得自动补入场景、服装、道具或光源；判定与拆解仍按`knowledge/prompt_compilation/state08_projection.md`的`执行Semantic Template Decomposition`段。

**不把否定当约束。** "不要X"会把X带进后续素材，与`rules/03_prompt_rules.md` `### Prompt Pollution Control`第4类同源。讨论中先写正向目标状态；确需保留的否定，在写入任何工件前收束到`rules/03_prompt_rules.md` `# Negative Prompt Boundary Rule`规定的位置。

**不承接自己的措辞。** 上一轮自己写出的说法不构成事实依据；新写入的每条约束必须能指向一个上游依据。没有依据、又无法确认的，标为待确认或删除；不得因"已经说过"而进入工件。

**归因失败时换角度，不继续沿原方向加料。** 同一方向连续两轮无效或反复触发同类错误时，停下来重新判断是哪一类联想被触发——回写口径按`knowledge/quality/prompt_scorecard.md`的归因表逐行判定；不得继续在同一方向上追加描述、举例或改写。
