# SD Film Recovery Guards

> Skill维护层：只在修改本Skill时读取，不参与影视生产。

本文件拥有每次正式修改都必须运行的固定基线：`Legacy Recovery Regression Matrix (LR-R1—LR-R10)` 与 `Standalone Skill Discovery Regression Matrix (SD-R1—SD-R5)`。

## R25 Legacy Recovery Regression Matrix (LR-R1—LR-R10)

本Matrix是`rules/runtime_reload.md`的Legacy Project Recovery Integrity直接回归，并由`references/maintenance_self_check_protocol.md`的`Unconditional Chat Runtime Startup And Recovery Guard`强制触发。每次正式修改SD Film都必须完整运行LR-R1至LR-R10，不论改动文件、模块、风险、是否用户可见或是否仅为拼写修正；不能因Diff未直接修改recovery文件而跳过。凡修改activation / routing、Reload / Re-entry、State Source / Portable State、Project Setup / status schema、Pipeline / STATE owner、Screenwriter、Director、STATE-07/08 Current Object / Clip、USER_GUIDE recovery command或ordinary Chat / Work routing，还必须增加对应直接消费者的定向案例。

### LR-R1 Ordinary Chat Recovery Must Not Default to Work

输入：普通Chat不能读取`C:\Users\...`绝对路径，但Current Accessible / Exposed Skill Definition本轮可读，旧对话中有可验证Project Context。

PASS：Skill Source与Project Source分别解析；以Current Accessible Skill + Current Verifiable Project Context恢复，规范化项目事实、映射当前Workflow并继续，不要求Work。

FAIL：仅因Windows路径不可访问就停住、写BLOCKED、要求Work或要求上传整个本地目录。

### LR-R2 Skill / Project Sources Are Independent

输入：Skill Source是本轮成功读取的Current Accessible Skill；Project State Source分别为有效Portable Project State与Current Verifiable Project Context。

PASS：两种组合都合法继续并分别报告source；Portable / context不反向证明Skill已读取，Skill读取成功也不要求Project必须来自同一路径。

FAIL：source不同即失败、把Portable State当Skill Definition，或因Root缺失清空Project Context。

### LR-R3 Historical Skill Is Never Authority

输入：旧对话存在与Current Skill冲突的旧`SKILL.md`摘要、assistant解释和旧workflow名称。

PASS：Latest Successfully Loaded Current Skill Definition胜出；历史内容只作legacy mapping hint或Project Context事实候选，不能成为Loaded Source、owner或Claim证据。

FAIL：旧摘要覆盖Current Skill、冒充已重载，或把旧workflow描述当Current runtime authority。

### LR-R4 Legacy State Maps Forward

输入：旧STATE / Workflow名已经过时，但存在可验证Artifact、Completion Gate与Checkpoint。

PASS：按`rules/compatibility_mapping.md`映射到能消费现有Artifact的当前Pipeline位置，保留Checkpoint与Accepted Unaffected Artifacts，不从STATE-00重启。

FAIL：按旧编号机械复制、重开项目、重做已完成阶段或把Legacy compatibility变成新主路由。

### LR-R5 Intent Backfill Is Additive

输入：旧项目缺新版Writer / Director Intent，但已有Production-Locked Screenplay、Confirmed Assets、Confirmed Shots与Accepted Take / accepted prompt。

PASS：只对当前Workflow实际需要且可从Canon可靠推导的字段执行`Legacy Intent Backfill`；保留已确认production；Accepted Take / accepted prompt只做compatibility check，不自动失效。

FAIL：回STATE-01重写剧本、重做资产/镜头、完整重建Packet、虚构缺失意图或自动废弃Accepted Take。

### LR-R6 Confirmed Visual Anchors Persist

输入：旧项目已有Confirmed `REF-SKETCH-04`，当前Blocking Signature与其确认Revision一致。

PASS：恢复后Visual Anchor保持有效，Final Assessment得到`KEEP`并复用；不重复生成。若Blocking Signature实质变化，才按current owner执行Reassessment。

FAIL：恢复即清空或重做草图、母版覆盖Current Clip Blocking，或不检查Signature直接假定有效。

### LR-R7 STATE-08 Resume Re-enters Workflow

输入：旧项目位于STATE-08 / CLIP-04，已有Confirmed Clip Plan、资产、Spatial Snapshot、Blocking Canon与可验证Checkpoint。

PASS：映射到current STATE-08 owner后，从entry gate执行`Reference Selection / Routing → Final Visual Blocking Anchor Assessment → Writer + Director Intent Preservation → Prompt Compiler → Final QA`，并继续CLIP-04合法Checkpoint。

FAIL：直接润色旧Prompt、跳过任一Gate、重做已确认上游，或从STATE-00开始。

### LR-R8 Claim Gate Honesty

输入：Current Skill Definition本轮未成功读取；Project Context或Portable State仍可用。

PASS：报告`UNAVAILABLE`、失败资源和真实Fallback Source；可在fallback合同内继续安全工作，但不声称“严格按当前Skill”或“已重新加载当前Skill”。

FAIL：以历史Skill摘要、项目Portable State、缓存版本号或已知路径冒充Current Skill read。

### LR-R9 Work Escalation Only On True Need

输入：A为Portable State或Current Verifiable Project Context足够安全恢复；B为Current Skill及fallback不可访问且最新规则是安全恢复必要条件；C为唯一必要Project Source是未暴露本地文件且portable/context不足；D为用户明确要求修改本地Skill或artifact。

PASS：A继续普通Chat且禁止要求Work；B/C/D才按`Work Escalation Final Fallback`说明真实缺口并要求Work。

FAIL：A升级Work，或B/C/D在无法处理本地必要资源时伪称已安全恢复/修改。

### LR-R10 Plain Next Does Not Force Full Recovery

输入：项目已经成功恢复、Current Workflow与Current Object已验证，用户只说`下一步 / 继续`。

PASS：复用当前成功加载的Skill Definition与Project Context，按`rules/progression_rules.md`推进一个合法Checkpoint；不重复全量reload、source resolution、mapping或backfill。

FAIL：每次`下一步`都重新执行Legacy Project Recovery、生成新Reload Evidence、重建Intent或重做已确认成果。

### R25 Dry-run Coverage

- A `old conversation + current accessible Skill + context only`：LR-R1 / LR-R2 / LR-R3，预期普通Chat恢复成功。
- B `current Skill + portable_project_status`：LR-R2，预期合法恢复。
- C `current Skill unavailable`：LR-R8，预期诚实fallback，无虚假claim。
- D `STATE-08 CLIP-04 + confirmed assets/sketch`：LR-R5 / LR-R6 / LR-R7，预期保留Canon、只补缺失Intent并从current owner重进。
- E `old state names`：LR-R4，预期映射到当前Pipeline。
- F `Director / Screenwriter schema changed`：本Matrix触发合同 + LR-R5，预期仍自动运行完整LR-R1—LR-R10。
- G `only 下一步`：LR-R10，预期不做全量恢复。
- H `all current / portable / context sources insufficient`：LR-R8 / LR-R9，预期只有此时才按真实需要escalate Work。

---

## R26 Standalone Skill Discovery Regression Matrix (SD-R1—SD-R5)

本Matrix由`references/maintenance_self_check_protocol.md`的`Standalone Skill Discovery Guard`拥有触发要求。每次正式修改SD Film都必须运行SD-R1至SD-R5，并与LR-R1至LR-R10一起作为固定基线；它验证独立Skill的发现入口，不把Skill改造成Plugin。

### SD-R1 User-level Canonical Location And Single Authority

输入：当前运行时用户级SD Film安装在`$HOME/.codex/skills/sd-film`，旧`.agents`位置可能仍存在或已迁移。

PASS：只保留一个`name: sd-film`用户级权威副本；实际安装位置为`$HOME/.codex/skills/sd-film`，所有相对引用、Git历史和维护脚本保持可用。

FAIL：两个用户级位置同时存在独立`sd-film`副本、后续修改需要双写，或选择器可能同时显示两份同名Skill。

### SD-R2 Implicit Invocation Metadata Persists

输入：任意Writer、Director、Runtime、Pipeline、Template、Guide或拼写修改完成。

PASS：frontmatter的`name`仍为`sd-film`，description保留六个启动别名，`agents/openai.yaml`仍声明`policy.allow_implicit_invocation: true`。

FAIL：别名被优化掉、description只剩能力摘要、openai.yaml缺失，或隐式调用被改为`false`。

### SD-R3 Codex Explicit Invocation And Chat At-Sign Boundary

输入：用户在Codex中需要确定性启动SD Film，或在当前普通Chat中查看`@`选择器。

PASS：Codex使用`$sd-film`；当前普通Chat的`@`选择器只显示Plugin时，如实说明本机独立Skill没有`@`入口。`interface.display_name`与`allow_implicit_invocation`只提供元数据/隐式策略，不冒充Plugin注册。

FAIL：宣称用户可以用`@`加显示名调用本机独立Skill，把`display_name`误当作`@`注册，或为了获得`@`入口擅自把Skill改成Plugin。

### SD-R4 Local Skill Product Boundary Is Honest

输入：用户尝试在网页端、移动端或无法读取本机Skill目录的宿主中使用本机独立Skill。

PASS：说明本机独立Skill能被Codex从本地目录发现；普通Chat只有在当前宿主实际暴露本机Skill时才可能隐式使用。不虚假承诺移动目录后普通Chat、网页端或移动端会自动可用，也不擅自改做Plugin。

FAIL：声称`.agents/skills`能让所有ChatGPT客户端读取本机文件，或仅因宿主边界就复制、上传、插件化Skill。

### SD-R5 Metadata Refresh Does Not Create A Second Route

输入：Skill文件已更新，但当前旧Chat尚未显示新的名称、描述或调用行为。

PASS：先重启桌面应用或新建Chat复测；Runtime / Recovery owner保持`rules/runtime_reload.md`，Discovery Guard只管发现元数据与安装唯一性。

FAIL：为解决缓存另建第二套activation、第二个同名Skill、平行Runtime Router或Plugin副本。

---
