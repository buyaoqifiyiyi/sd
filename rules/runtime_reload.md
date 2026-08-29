# Runtime Skill Reload / Hot Reload

## Purpose

本规则定义SD Film在Work/Codex本地环境与已安装Chat Skill环境中的运行时重载协议。它是全局运行协议，不创建STATE，不改变项目事实，也不拥有任何阶段交付格式。

## Trigger

用户说出下列命令或无歧义等价表达时，必须在状态判断、Project Resume、纯推进命令、Workflow路由或交付物生成之前执行重载：

- `调用SD`
- `调用sd`
- `重新调用SD`
- `重新加载SD`
- `按当前Skill继续`
- 明确要求使用最新、本地或当前安装版SD Film规则继续

普通的“继续”“下一步”不是重载触发词；它们服从`rules/progression_rules.md`。

## Authority

- 当前实际安装并成功读取的`SKILL.md`是Skill Definition入口。
- `SKILL.md`中的`Skill Version`与`Build ID`是版本唯一真源。
- 对话缓存、旧摘要、旧版Skill文本和历史路由说明不得覆盖当前已安装资源。
- 重载只刷新Skill Definition；Project Context、Production-Locked Script、Confirmed Assets、Active Versions、Canonical References、已接受Artifact、Checkpoint、Revision与用户明确约束必须保留。
- 项目状态必须按`rules/state_source.md`选择，旧Skill规则本身不是State Source。

## Reload Sequence

按以下顺序执行，且“知道路径”不等于已读取：

1. 完整重新读取当前已安装的`SKILL.md`。
2. 提取并核对`Skill Version`与`Build ID`。
3. 读取`config.md`和`SKILL.md`外部规则索引指向的全局规则。
4. 读取`references/project_state_contract.md`与`references/project_workspace.md`。
5. 按`rules/state_source.md`重新选择当前项目状态来源。
6. 如状态标签来自旧Pipeline，按`rules/compatibility_mapping.md`基于Artifact与Completion Gate映射。
7. 读取`workflows/workflow_map.md`，再完整读取当前Workflow及其声明的必需/适用依赖。
8. 按`rules/resource_loading.md`完成当前阶段资源加载后才继续执行。

本地Work/Codex优先读取当前安装目录中的实际文件；其他安装式运行时使用该运行时提供的资源检索机制。不得要求普通Chat提供本机Skill路径，除非实际资源检索已经失败且该资源对当前Workflow确属必需。

## Validation

### Reload Status Contract

`Reload Status`只允许：

- `RELOADED`：已在本次执行中实际重新读取权威`SKILL.md`，并成功取得彼此一致的`Skill Version`与`Build ID`。
- `UNAVAILABLE`：权威入口或完成本次路由所必需的安装资源实际检索失败；必须同时记录具体失败资源与原因。

知道文件路径、沿用对话缓存、读取旧摘要或仅声称“已加载”都不构成`RELOADED`。没有实际重读权威入口并取得版本字段时，禁止报告`RELOADED`或暗示已使用最新安装版。部分资源失败时不得伪称完整重载成功；应记录`UNAVAILABLE`，同时保留Project Context并继续执行仍可安全执行的fallback，不得仅因本机路径不可见把项目写成`BLOCKED`。

重载尝试完成后内部记录：

- Reload Status
- Loaded Skill Version
- Loaded Build ID
- Current State
- State Source
- Active / Next Workflow
- Compatibility Mapping Result（如适用）

用户询问重载结果时披露这些信息。读取失败时指出具体资源；仅在实际检索失败后才请求用户提供缺失资源。不得把“本机路径不可访问”本身写成项目`BLOCKED`。
