# Runtime Skill Reload / Workflow Re-entry

## Purpose

本规则定义SD Film在普通Chat、已安装Chat Skill与Work/Codex本地环境中的`Runtime Skill Reload Integrity / Chat Hot Reload`与`Workflow Re-entry Integrity`协议。它是显式重新调用的唯一Reload / Re-entry owner，不创建STATE，不改变项目事实，也不拥有任何阶段算法或交付格式。

## Trigger

用户说出下列命令或无歧义等价表达时，必须在状态判断、Project Resume、纯推进命令、Workflow路由或交付物生成之前执行重载：

- `调用SD`
- `调用sd`
- `调用SD流程`
- `重新调用SD`
- `重新调用sd`
- `重新加载SD`
- `重新加载sd`
- `按当前Skill继续`
- `按当前 skill 继续`
- 明确要求使用最新、当前可访问、本地或当前安装版SD Film规则继续

普通的“继续”“下一步”不是重载触发词；它们服从`rules/progression_rules.md`。

### Invocation Classes

- 首次或普通显式`调用SD / 调用sd / 调用SD流程`：执行本轮Reload Gate，再做正常activation、State Source解析与Workflow routing；不存在可恢复项目时按当前Pipeline正常建立入口。
- **Explicit Re-entry Command**：`重新调用SD / 重新调用sd / 重新加载SD / 重新加载sd / 按当前Skill继续 / 按当前 skill 继续`及无歧义等价表达。它固定表示`Runtime Skill Reload + Workflow Re-entry / Re-route`，不能降级成继续沿用上一版结论改写。
- 普通`继续 / 下一步 / 下一个`：不是Explicit Re-entry Command，不执行全量Reload或强制Re-entry，只按`rules/progression_rules.md`继续当前已加载Workflow及其本来要求的Gate。

## Authority

- 当前Chat runtime重新解析后可访问、且本轮成功读取的`SKILL.md`是Current Skill Definition入口；本地安装路径、exposed Skill resource或运行时资源句柄都只是可能的`Loaded Source`，路径被提及不等于已读取。
- `SKILL.md`中的`Skill Version`与`Build ID`是版本唯一真源。
- Skill Definition表示“怎么工作”，允许在显式触发时热重载；Project Context表示“当前项目事实”，包括Production-Locked Script、Confirmed Assets、Active Versions、Canonical References、Accepted Take Canon / Accepted Canon State、Shot-State Memory、已接受Artifact、Checkpoint、Revision与用户明确约束，重载后必须继承。
- Skill规则冲突时固定使用：`Latest Successfully Loaded Current Skill Definition > Old Conversation Skill Description / Cached Skill Rules / historical assistant memory`。旧对话中的Skill描述只能作为历史上下文，不得覆盖或冒充当前资源。
- Project Context与Skill Definition分别解析：重载只刷新Skill Definition，不得因版本、STATE名称、owner或文件路由更新而清空项目、强制从STATE-00重启或重新确认Accepted Unaffected Artifacts。
- 项目状态必须按`rules/state_source.md`选择，旧Skill规则本身不是State Source。

## Reload And Re-entry Sequence

按以下顺序执行，且“知道路径”不等于已读取：

1. 重新解析当前Chat runtime实际可访问的SD Film Skill resources。普通Chat先检查当前runtime提供的installed / exposed Skill resources；Work/Codex在本地文件访问确实可用时可以解析实际安装目录。不得把旧对话里的路径或Skill摘要直接当作本轮资源，也不得把只保存项目事实的Portable State误作Skill Definition。
2. 从本轮解析出的`Loaded Source`完整重新读取当前`SKILL.md`，提取并核对`Skill Version`与`Build ID`。
3. 从该入口重新解析并核对本次基础路由owner：`rules/runtime_reload.md`、`rules/activation_rules.md`、`rules/resource_loading.md`、`rules/state_source.md`、`references/project_workspace.md`、`references/project_state_contract.md`、`workflows/workflow_map.md`；`config.md`只作为入口索引与能力默认值读取，不得覆盖owner规则。
4. 按`rules/state_source.md`重新选择当前项目状态来源；Skill Source与State Source必须分别记录，任何Portable State或Project Context都不能反向证明Skill已重载。重新读取并保留当前Project Context，包括Production-Locked Script、Confirmed Assets / Active Versions / Canonical References、Current Clip或其他Current Object、Accepted Take Canon / Accepted Canon State、Shot-State Memory、Visual Anchor State / Blocking Signature、已接受Artifact、Checkpoint、Revision与用户已确认创作决定。
5. 如旧对话或旧项目使用已变更的STATE名称、owner或文件路由，按`rules/compatibility_mapping.md`基于Artifact与Completion Gate映射，只更新必要路由标签并保留Project Context。
6. 依据当前用户任务、Selected State Source与Completion Gate重新确认固定Main Pipeline、Current STATE和Current Object；用户目标或旧输出中的STATE标签都不能替代本轮确认。
7. 从`workflows/workflow_map.md`重新选择当前任务唯一Workflow owner，只完整读取该Workflow及其Required / Applicable / Conditional Resources；不为证明Reload而全量重读无关Rules、Workflow、Knowledge或Template。
8. 按`rules/resource_loading.md`完成当前任务所需资源加载后，从所选Workflow的正式入口重新执行当前对象；重新运行本轮适用的gates、routing、compiler、validation与Final QA，直到合法Checkpoint或交付结果。不得从上一条assistant输出、上一版Prompt或上一次未验证结论的中间位置直接续写。
9. 只有Workflow Re-entry完成并取得当前Checkpoint后才产出本轮结果；若Gate要求返回上游、等待确认、生成草图或停止，本轮服从该结果，不能为了“重写”而绕过。

普通Chat不是本地文件模式的降级版。只要当前runtime能实际读取Skill入口和必需owner，就直接Reload、Route并执行；Windows本机路径不可读不构成切Work理由。只有用户要求直接编辑/检查本地Skill或项目文件，或当前任务确实必须操作本地文件且Chat runtime没有等价资源访问时，才进入Work。普通制作执行不得默认要求Work。

未命中显式Trigger的“继续 / 下一步”复用当前runtime中最近一次成功加载且仍可用的Skill Definition与Project Context，按需读取当前Workflow资源；不重复执行本Gate，也不得把普通推进表述成一次新Reload。

## Re-entry Input Boundary

Explicit Re-entry的权威输入是`Current Skill + Current Project Context + Current User Task`。Project Context与已确认成果可以继承；Previous Assistant Output、旧Prompt和旧对话摘要只能作为可追溯候选或用户指定的修改对象，不能成为Skill Definition、State Source、Workflow Gate或Completion证据，也不能因为已存在就跳过当前Workflow入口。

重进并不等于重置：Production-Locked Script、Active / Canonical资产、Accepted Take、Accepted Canon State、Shot-State Memory、Confirmed Visual Anchor、Blocking Canon与Accepted Unaffected Artifacts继续有效，除非它们自身的Revision、适用性或owner Gate判定已变化。重进也不等于无条件重做：Workflow重新评估后仍可合法复用未失效的已确认成果。

STATE-08示例：用户说“重新调用sd，优化CLIP-04”时，路由必须是：

```text
Current Skill
→ Current Project Context
→ STATE-08
→ workflows/11_video_generation_workflow.md
→ Reference Selection / Routing
→ Final Visual Blocking Anchor Assessment
→ Prompt Compiler
→ Final QA
→ CLIP-04 Prompt或当前Gate要求的Checkpoint
```

Visual Blocking结果继续唯一服从`knowledge/clip_preflight_check.md`：匹配当前Blocking Signature的Confirmed `REF-SKETCH`可`KEEP`并复用；Blocking发生实质变化必须执行Reassessment；Final=`REQUIRED`且没有匹配Confirmed Anchor时先完成草图Checkpoint，不直接输出Prompt；Final=`NONE`时直接进入编译。Re-entry不得破坏Sketch Persistence / Blocking Canon，也不得以旧Prompt已存在为由跳过该Gate。

## Validation

### Reload Status Contract

`Reload Status`只允许：

- `RELOADED`：已在本次显式调用中从记录的`Loaded Source`实际重新读取当前权威`SKILL.md`，成功取得彼此一致的`Skill Version`与`Build ID`，并重新核对本次基础路由owner pointers及当前任务必需资源。
- `UNAVAILABLE`：当前Skill入口、基础路由owner或完成本次路由所必需的资源实际检索失败；必须同时记录具体失败资源、原因与实际采用的`Fallback Source`。

知道文件路径、沿用对话缓存、读取旧摘要或仅声称“已加载”都不构成`RELOADED`。没有实际重读权威入口并取得版本字段时，禁止报告`RELOADED`或暗示已使用最新安装版；缺少`Loaded Source`与`Owner Files Resolved`证据时，禁止声称“已重新加载当前SD Film Skill”“严格按当前Skill执行”或无歧义同义表达。部分资源失败时不得伪称完整重载成功。

`UNAVAILABLE`时保留Project Context，并按当前可访问的State Source / portable fallback合同继续仍可安全执行的工作；必须如实标明实际来源，例如`Current Accessible Skill Resource`、`Portable State`、`Normalized Project Context`或`Last Successfully Loaded Skill Definition + current Project Context`。旧对话Skill摘要不得标成Current Skill，不能成为`RELOADED`证据。不得仅因本机路径不可见把项目写成`BLOCKED`或默认要求切Work；只有当前Workflow真正缺少外部必要输入时，才按状态合同记录Pending Decision或`BLOCKED`。

### Re-entry Evidence Contract

只有本轮`Reload Status: RELOADED`，且已经重新确认Current STATE、Current Workflow、Current Object并从Workflow Entry执行到合法Checkpoint，才可声称“已重新加载并进入当前Workflow”或无歧义同义表达。仅重读Skill但尚未完成re-route时只能报告Reload事实；`UNAVAILABLE`时即使使用Fallback Source继续安全工作，也必须明确fallback，不能声称已按current Skill完成Re-entry。

显式Re-entry时默认只向用户显示最小证据，不输出完整内部日志：

```text
SD Film: RELOADED — <Loaded Source / Version>
Current STATE: <STATE-XX>
Current Workflow: <workflow owner>
Current Object: <CLIP-04 / SHOT-XX / asset / project checkpoint>
```

字段未知或未证实时必须写实际状态，不能补猜；资源失败时改为`UNAVAILABLE — <failed source>; Fallback: <actual source>`。这些证据是runtime trace，不进入视频Prompt、项目主STATE或最终Template Schema。

重载尝试完成后内部记录：

- Reload Status
- Invocation Marker / Load Timestamp（运行时可提供时）
- Loaded Source
- Loaded Skill Version
- Loaded Build ID
- Owner Files Resolved
- Last Routed State
- State Source
- Last Routed Workflow
- Current Object
- Workflow Entry Checkpoint
- Compatibility Mapping Result（如适用）
- Fallback Source（仅`UNAVAILABLE`或发生fallback时）

这些是轻量调用证据，不建立状态数据库、不写入项目STATE，也不自动污染production输出。用户询问重载结果或系统准备作出“严格按当前Skill”声明时披露必要证据；读取失败时指出具体资源与实际Fallback Source，仅在合法检索机制确实失败后才请求用户提供缺失资源。不得把“本机路径不可访问”本身写成项目`BLOCKED`。
