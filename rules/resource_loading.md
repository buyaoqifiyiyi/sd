# Resource Loading And Ownership

## Purpose

本规则定义SD Film的资源读取顺序和单一职责边界。它不拥有阶段算法或最终输出Schema。

## Loading Order

每次执行按需、渐进式读取：

1. 若命中重载触发，先执行`rules/runtime_reload.md`，由它重新解析并重读Current Skill Definition及基础owner pointers。
2. 未命中重载触发时，复用当前runtime最近一次成功加载且仍可访问的`SKILL.md`定义；若本runtime尚无已验证入口则读取一次并确认版本、主Pipeline和路由索引，但不得把这次普通初始化声称为用户触发的`RELOADED`。
3. 读取`config.md`及当前行为实际需要的全局规则，不为“保险”或普通“继续 / 下一步”全量重读所有Rules。
4. 读取`references/project_state_contract.md`与`references/project_workspace.md`，按`rules/state_source.md`选定状态。
5. 读取`workflows/workflow_map.md`和当前Workflow全文。
6. 读取当前Workflow列出的Required Resources、Applicable / Conditional Resources及必要索引。
7. 只读取当前阶段需要的Knowledge文件与当前最终交付对应Template；不得为“保险”加载整个知识库。
8. 输出前执行Workflow验证、`rules/completion_gate.md`和Template完整性检查。

当前Workflow的Required Resources列表是该阶段执行资源的权威清单；`knowledge/00_knowledge_index.md`只负责分类和发现，不得维护与Workflow竞争的资源门槛。尤其STATE-08以`workflows/11_video_generation_workflow.md`的资源声明为准。

## Actual Read Gate

- 路径被提及、文件曾在旧轮次读取、或SKILL中记录说明，不等于本次已读取。
- 显式Reload必须产生`rules/runtime_reload.md`要求的本轮读取证据；非显式推进只需保有可验证的当前loaded definition，不伪造新Reload证据。
- 必需资源读取失败时，明确列出资源和失败原因；先尝试当前运行时的合法检索机制。
- 只有实际检索失败后才能请求用户提供资源。
- 资源缺失导致当前Workflow无法继续时，按状态合同记录Pending Decision或真正适用的`BLOCKED`，不得虚构执行结果。

## Responsibility Boundaries

- `SKILL.md`：身份、版本、系统角色、主Pipeline、STATE总览、全局优先级、Activation/Reload入口、Workflow路由和外部索引。
- `config.md`：运行默认值、索引路径和能力开关；不复制行为规则。
- `rules/`：跨阶段约束与全局行为。
- `workflows/`：阶段输入、步骤、依赖、Completion Checklist和错误路由。
- `knowledge/`：专业判断方法，不拥有路由或最终格式。
- `templates/`：用户可见阶段交付Schema的唯一所有者。
- `references/`：状态、项目空间、资产锁和模块接口合同。

## Template Uniqueness

任何规则、Workflow、Knowledge、示例或Validator都不得维护另一套完整最终字段、字段顺序或排版骨架。它们可以声明语义约束和映射义务，但最终字段名称、顺序、必填性和格式只引用当前Template。

STATE-08最终Schema唯一由`templates/10_video_prompt.md`拥有；图生视频时`templates/11_image_to_video_prompt.md`只提供Source Data和边界约束，不创建竞争Seedance Schema。
