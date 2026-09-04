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

### Current-Object Fast Path

当项目已有可验证的当前对象（例如外部角色图、环境图或道具图）时，先只读取Selected State Source、当前对象记录、对应Workflow、对应Template与资产锁合同；不得先读取其他资产类别、其他篇章目录或整套Knowledge库。对已有文件执行最小来源、可读性与身份匹配检查，随后进入该对象的确认或最小补充步骤；只有发现缺失、冲突或需重新设计时才扩展读取范围。

已有外部视觉文件默认登记为Candidate Reference。若用户明确要求“使用现有资产/跳过制作”，可跳过新图生成分支，直接进入Candidate Reference确认门；不得跳过用户确认、Canonical Reference登记或Active Version锁定。

当前Workflow的Required Resources列表是该阶段执行资源的权威清单；`knowledge/00_knowledge_index.md`只负责分类和发现，不得维护与Workflow竞争的资源门槛。尤其STATE-08以`workflows/11_video_generation_workflow.md`的资源声明为准。

## Actual Read Gate

- 路径被提及、文件曾在旧轮次读取、或SKILL中记录说明，不等于本次已读取。
- 显式Reload必须产生`rules/runtime_reload.md`要求的本轮读取证据；非显式推进只需保有可验证的当前loaded definition，不伪造新Reload证据。
- 必需资源读取失败时，明确列出资源和失败原因；先尝试当前运行时的合法检索机制。
- 只有实际检索失败后才能请求用户提供资源。
- 资源缺失导致当前Workflow无法继续时，按状态合同记录Pending Decision或真正适用的`BLOCKED`，不得虚构执行结果。

## Verified Reuse Register

本节只优化同一runtime内对**未失效、已验证事实**的重复读取和重复推导；它不创建新的State Source、项目缓存、Completion Gate或最终输出Schema。唯一owner仍是本文件。

### Reuse Record

对当前任务实际使用过的资源，可在runtime内部保留最小`Verified Reuse Record`：

- Resource：实际读取的唯一文件或已确认Artifact。
- Scope：Project ID、STATE、Current Object及适用的Revision / Version / Blocking Signature。
- Evidence：本轮成功读取、解析或验证的简短证据。
- Dependencies：会使该结果失效的上游事实或Artifact。
- Result Type：`SOURCE FACT`、`ROUTING DECISION`、`GATE RESULT`或`DERIVED NOTE`。

这是轻量运行记录，不写入Project State、Portable State、Template或用户可见交付；不得用它冒充“本轮已重新读取”或`RELOADED`证据。

### Safe Reuse Rules

1. 每次Workflow开始、恢复、保存、推进或重载仍必须按`rules/state_source.md`实际选择State Source；不得复用旧选择跳过可访问性、Project ID、Revision或Checkpoint核验。
2. 显式Reload仍完整遵守`rules/runtime_reload.md`；必须重新读取`SKILL.md`和该规则指定的基础owner，不能以Reuse Record声称`RELOADED`。
3. 当前Workflow、其Template、Completion Gate、用户本轮指令以及所有Required Resources仍必须实际满足该Workflow的读取与验证要求。Reuse只允许避免对**同一、仍有效的事实**重复做无新增信息的解释性推导。
4. 已确认的Production-Locked Script、Active Asset Version、Canonical Reference、Accepted Artifact、Spatial Snapshot、Blocking Signature、Shot-State Memory或上一阶段Gate Result，只有在其唯一owner的Version / Revision与依赖均未变化时才能复用。复用时仍须确认其标识、适用范围与来源可追溯。
5. `DERIVED NOTE`永远不是事实来源、State Source或Completion证据；它只能作为加速当前分析的候选。输出或关键决策前必须回指对应的`SOURCE FACT`或`GATE RESULT`。

### Mandatory Invalidation

遇到任一情况，立即废弃受影响记录并按当前owner重新读取或重新执行；不确定是否受影响时默认废弃：

- 用户修改当前目标、创作约束、剧本事实、资产外观、参考图、Scene / Shot / Clip边界或确认状态。
- Project ID、Revision、Checkpoint、Active Version、Canonical Reference、Visual Anchor State或Blocking Signature变化，或无法核对。
- 当前STATE、Current Object、Workflow、Template、Skill Version / Build ID或适用规则发生变化。
- 资源读取失败、来源不可访问、Artifact状态不是Confirmed / Accepted、或存在冲突的事实来源。
- Workflow要求重新执行Gate、Review要求REVISE / REBUILD，或任何依赖检查报告风险。

### Operating Sequence

1. 先执行当前Workflow要求的State Source、路由与Required Resource Gate。
2. 对每项后续事实检查是否有Scope与Dependencies完全匹配的Verified Reuse Record。
3. 匹配时复用已验证的事实或Gate结果，并只补充本轮Delta；不匹配或不确定时重新读取 / 重算。
4. 输出前仍执行当前Workflow的Completion Checklist、`rules/completion_gate.md`和Template完整性检查。

因此，优化对象是“未变化事实的重复解释”，不是生产步骤、确认边界、最终验收或用户可见内容。

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
