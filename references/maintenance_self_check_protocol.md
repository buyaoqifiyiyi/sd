# SD Film Maintenance Self-Check Protocol

## Purpose

本文件是Skill维护QA的**判据真源**：它拥有`references/maintenance_self_check.md`中15个检查维度每一项的完整判据、边界、反例与处置要求，以及两个固定Guard的完整协议。

执行入口、维护链顺序与报告格式由`references/maintenance_self_check.md`拥有。本文件不重复定义执行流程，也不定义任何模块合同（那是`references/module_contracts.md`）或Skill可达性判据（那是`references/context_budget.md`）。

**本协议是纯文本、人工可执行的。**每条判据都写成可由任何Agent或人直接对照文件完成的判断，不依赖`scripts/`下的验证器、不依赖特定平台、不依赖网络。`scripts/`只是某些环境下的可选加固；换到没有这些工具的环境时，按本文件逐条人工执行即可，不得以“缺少工具”为由降低检查强度——能被工具挡住的错误，也必须能被读者挡住。

本文件属于Skill维护层，不是影视制作Pipeline的STATE，不写入项目状态，不进入用户视频Prompt，也不得被复制成另一套并行检查规范。

## Change Classification

开始修改前先搜索当前权威来源和同类机制，完成后把本次变更标记为以下一种：

- `no_change`：现有机制已完整覆盖，未修改文件。
- `optimize_existing`：权威原规则存在但覆盖不完整，在原位置补足。
- `merge_existing`：同类规则零散分布，合并到一个权威来源，其他位置只保留引用或路由。
- `add_new`：确认没有合适权威位置后才新增最小模块或文件。
- `deprecate/remove`：移除已废弃、冲突或被权威来源替代的内容，并清理全部引用。

## Dimension Criteria

1. **Duplicate Rule Check**：搜索语义相同但措辞不同的并行规则，以及本应由单一来源拥有却复制到`SKILL.md`、Rule、Workflow、Knowledge、Template、Reference或Validator的规范。保留一个权威来源，其他位置只保留必要路由、引用或不变量，不复制完整协议或Schema。
   本项还**必须显式判定是否存在可合并或可退役的既有规则**：本次新增是否使某条既有规则过时、被覆盖、被吸收或不再有触发条件；结论为“无”时必须写明依据。`Additive By Default`保护的是既有字段与已确认行为不被破坏，**不是规则总量可以无限增长**——`merge_existing`与`deprecate/remove`是既有变更分类，若长期从未被使用，说明本项已退化为“只查重复、不查冗余”，这一点本身必须作为发现项上报。
2. **Conflict Check**：核对Pipeline、STATE编号、Gate、优先级、默认行为与辅助模块边界。重点排除显式调用与默认必经并存、Storyboard Auxiliary与固定STATE并存、Shot/Clip/Prompt单位关系冲突，以及同一Template字段被不同文件定义。
3. **Terminology Drift Check**：复用当前正式术语与ID，包括Shot、Clip、Prompt、Voice Profile、Accepted Take、Accepted Canon State、Shot-State Memory、Reference Selection / Routing、REF-TAIL、Visual Blocking Anchor、Visual Anchor State与Blocking Signature。新名称只有在代表新概念且不会形成同义命名时才允许。
4. **Rule Ownership Check**：按本文件Authority Matrix检查归属。`SKILL.md`只保留身份、版本、入口、主路由、全局硬规则和索引；详细算法、门槛、知识、Schema与合同分别留在Workflow、Rules、Knowledge、Templates和References。不得为提高可见性而在入口复制细粒度规则或Template字段。
5. **Prompt Pollution Check**：确认新增内部控制不会直接膨胀最终Prompt。检查重复、冲突、抽象语义模板、否定词堆叠、资产重述、无效精密参数、跨镜头残留、风格堆叠与优先级淹没；内部QA、分数、Issue ID、路由说明和维护术语不得进入最终Prompt。
6. **Routing Integrity Check**：确认新模块有正确入口、触发和返回路由；显式调用模块未变为默认必经；Optional/Auxiliary Workflow未写入主Pipeline；Legacy Compatibility未成为新项目主路由；普通“继续”未被误判为Reload、AUDIO或MUSIC授权。主Workflow的STATE自证、`workflows/workflow_map.md`作为路由唯一owner、阶段顺序与**他阶段Workflow文件名**未被各Workflow复述（标题、行内字段与代码块三种形态同等对待）、以及收尾块**有且仅有一个**`# Completion Gate`、写回块**不得回退为退役名**`# State Update`（正名为`# Status Update`），由`scripts/validate_sd_film.py`的`check_workflow_routing`确定性执行；写回块**是否存在**不在脚本的确定性检查范围内，其完备性仍须由维护者逐个人工确认，脚本通过不替代它；语义部分（入口是否合理、辅助模块是否被误升为必经）仍由维护者判断，脚本通过不替代它。
7. **Template Consistency Check**：核对Workflow声明的Output Owner、字段语义与当前Template；废弃字段不得残留。Template继续唯一拥有用户可见字段、顺序、必填性和排版。音色未显式投影时，常规STATE-08输出不得默认保留声音身份或“音色特征”字段。
8. **Reference Integrity Check**：验证所有显式文件、模块、Template、Knowledge与脚本路径真实存在且名称一致；新增资源已被合法路由发现；删除或改名后没有悬空引用。**同时反向检查孤儿内容**：新增的字段、规则或知识必须能被某个消费者读到——被某个Workflow列为Resource、被某个Template使用、或被某个上游事实引用；定义了却无人引用的内容等于已经丢失，必须在本轮补上消费者或移除它。运行`scripts/validate_sd_film.py --skill-root <skill-root>`执行可确定的结构与引用检查。生产交付物校验由独立owner`scripts/validate_prompt_package.py`承担：它在STATE-08交付前对已编译的`# CLIP-X｜…` Package做确定性结构断言（全局字段存在与顺序、分镜或阶段编号连续且数量与声明一致、`REF-TAIL`用途声明、终段位置与固定无BGM句、未授权`音色特征：`）。两者职责互不替代：前者守护Skill自身，后者守护本次交付；后者不进入本Checklist的维护QA执行owner。
9. **State / Continuity Compatibility Check**：确认STATE-00至STATE-09、Shot-State Memory、Accepted Take、Accepted Canon State、Reference Selection / Routing、REF-TAIL A Direct / B Reference-Only / C Not Required、Visual Anchor State / Blocking Signature、Spatial Blocking、资产锁、Revision与Checkpoint不被破坏；维护QA不得创建新主STATE或项目事实。
10. **User Guide Sync Check**：如果修改改变用户该如何下指令、默认行为、用户可见输出结构、模块入口、opt-in边界或停止点，必须同步`USER_GUIDE.md`；仅内部知识或实现优化且不改变调用和输出时标记`NOT REQUIRED`，不得为机械同步复制内部规则。
11. **Regression Check**：根据影响范围选择最少但有效的案例，并同时包含适用的正例和反例。路由变更验证正确模块与不触发路径；Prompt变更验证Schema与污染；连续性变更验证REF-TAIL三模式；音色变更验证未调用时省略、显式调用时进入Seed Audio；资产变更验证Core / Support与Reference Asset Eligibility。优先复用`references/regression_scenarios.md`与现有Validator / tests；如果自检同时修复了其他历史问题，必须为每个修复项增加对应的直接回归，不得因为它与原始请求无关而省略验证。
12. **Change Classification Check**：复核最终分类与实际操作一致，并记录为什么不是其他类别；新增文件前必须能说明现有权威位置为何不合适。**迭代粒度按对话计**：同一对话内的多次修改累积为**一次**正式迭代，只在维护者确认该批改动定稿时才递增`Skill Version`与`Build ID`；不得为单个任务各升一版，也不得用版本号数量代替改动质量的判断。
13. **Runtime Claim / Legacy Recovery Check**：核对Runtime Skill Reload、Workflow Re-entry与Legacy Project Recovery仍由唯一owner定义；Skill Source / Project State Source独立；历史Skill永不成为Current authority；Claim Gate诚实；Work只在真实必要时escalate；Legacy Intent Backfill只增补不重做；STATE-08从current owner entry重进；普通`下一步`不触发全量恢复。必须运行`references/recovery_guards.md`中的`Legacy Recovery Regression Matrix (LR-R1—LR-R10)`及现有Validator / tests。
14. **Standalone Skill Discovery Check**：核对当前运行时用户级权威副本位于`$HOME/.codex/skills/sd-film`、同名`sd-film`没有第二份用户级副本、`SKILL.md` frontmatter保留启动别名、`agents/openai.yaml`与Skill名称一致、`policy.allow_implicit_invocation`为`true`，且用户文档只把Codex `$sd-film`作为本机独立Skill的确定性显式入口。在当前用户客户端中，普通Chat的`@`选择器只显示Plugin；不得宣称本机独立Skill可通过`@`加显示名调用，也不得把网页/移动端读取本机Skill误写为受支持能力。
15. **Context Budget Check**：`references/context_budget.md`是可达性判据、文件类别与Size Index的唯一owner，本项只引用它，不复制数值。**越线不是违规**：复核线与Ceiling的区别就是“提示”与“阻断”的区别。按`Maintenance System Map`定义的三层节奏执行本项：
    - **事前（Prevent）**：新增内容先归位到既有owner，不因“方便”而新建文件；新建Markdown不得超过复核线的60%（30 KB）；本次变更若使文件越过复核线，必须在同一次变更内给出它的读取入口或拆分它。
    - **事中（Enforce）**：`SKILL.md`仍在Entry阈值内且未复制细粒度规则；Size Index每条都写明读取入口；已落回复核线以下的条目已移除；`NON_RUNTIME`文件不在管辖内；没有任何文件达到Ceiling；索引的`Size`列与实测差异不超过20%。
    - **事后（Audit）**：越过复核线但未登记的文件由`--report`列出，在周期复核时补齐；`Review By`到期的条目必须重估；`COMPOSITE`条目是待拆队列，不得长期挂账；周期性全库体检只负责发现累积，不替代前两层。
    **本项的目标是细节能否被读到，不是文件够不够小。** 越线但不影响读取方式，不构成发现项；未越线却无人引用、没有读取入口，才是真实失效。
16. **Claim / Evidence Credibility Check**：核对**用来判断这次改动是否成立的那份证据本身**是否可信。本项不评价改动内容，只评价支持它的证据。四类必查：
    - **宣称 vs 实现**：任何文件声称某项检查“由脚本 / Validator / Gate确定性执行”时，必须打开该工具核对其**实际射程**。**以实现的射程为准**；宣称过宽即缺陷——实现只做了一半却写成全做，会让下一个维护者以为已经查过而跳过人工判定。反向同样算缺陷：工具确实执行了某项检查，却没有任何owner写明它，读者同样无从得知。
    - **测量工具先自证**：用工具（脚本、统计、采样、检索）判断改动效果前，先确认它**能区分目标与非目标**、**前后使用同一尺度与单位**、并对已知样本给出正确结论。工具自身有缺陷时，它的“无变化 / 无问题”结论一并作废。实测教训：一个把`目录/index.md`误判为整目录引用的正则，让改动前后的对比稳定显示“毫无变化”，几乎导致“改动无效”的错误结论。
    - **权威来源核对，不以渲染输出为据**：字节数、换行符、编码、二进制内容这类事实，用能给出原始字节的来源核对（`git cat-file`、`git ls-files --eol`、直接字节计数），**不以终端管道的渲染结果、行拼接或格式化输出为据**——管道与格式化会吞掉`\r`一类不可见字符，并据此给出错误的归属结论。
    - **实测与投影必须分开标注**：结论中凡不是本轮直接量得的数字，必须标为投影 / 推算并写明假设；不得把推算写成结论，也不得对可实测项用“估计”代替测量。

    另有一条删除前置：**删除或移动任何文件之前，先普查它是否含有别处不存在的独有内容**（未被版本控制的本地数据、被Git忽略目录里的产物、独有历史）。普查结论必须写进报告；未普查即删除，视为未执行本项。

## Skill-Wide Detection And Risk-Based Repair

- **Detection scope is Skill-wide**：每次完整自检都检查整个Skill在十六个维度上的可见问题，不以本次Diff、修改文件或直接消费者为发现边界。已经发现的问题不得仅因“与本次修改无关”而跳过、隐藏或从报告中删除。
- **Every finding requires disposition**：每个真实发现项必须在本轮标记为`FIXED`或`WARN`，并记录所有者、影响和处理依据；误报必须说明为什么不构成问题，不能用总体`PASS`掩盖单项发现。
- **SAFE_LOCAL**：权威来源明确、影响局部、行为保持不变且可通过确定性检查或直接回归验证的问题，本轮必须修复，即使它是历史遗留或与原始请求无关。例如悬空引用、重复定义、失效索引、确定的术语漂移、版本不一致和无消费者的竞争副本。
- **CONTROLLED_CROSS_MODULE**：涉及多个文件或消费者，但所有者、影响边界和回归路径明确的问题，原则上也在本轮修复；同步更新所有直接消费者并扩展定向回归。文件数量或是否属于原始Diff本身不是延期理由。
- **HIGH_RISK / DECISION_REQUIRED**：可能改变用户已确认的重要行为、主Pipeline、STATE、资产锁、项目事实、最终Schema、外部兼容，或需要无法在本轮可靠验证的大规模迁移时，不得静默修改。标记`WARN`，写明证据、影响、权威所有者、建议修复方案与所需用户决定；若会使本次更新不安全，则在完成前升级为明确阻塞或请求决定。
- 风险分级是为了决定如何处理，不是缩小检查范围。禁止把“不要全面重构”解释成只修本次相关问题；同时也不得把自优化变成无边界重写。优先逐项、可回滚、可验证地清零问题，只有达到`HIGH_RISK / DECISION_REQUIRED`门槛才允许延期。
- 不允许为了“统一”删除用户已确认的重要行为、改变Production-Locked事实、清空Confirmed Assets / Accepted Artifacts，或扩大当前授权范围。
- 语义检查由维护者实际阅读和比较完成；Validator只负责确定性结构、不变量和引用检查。Validator通过不等于全部语义维度自动PASS。

## Targeted Regression Selection

回归选择以所有实际修复项及其直接消费者为边界，而不只看原始请求的Diff：先验证每个修改文件，再验证它引用或被引用的直接模块，最后验证对应关键不变量。若修复横跨多个所有者，分别验证各自Template / Workflow合同；若只改内部说明且无行为变化，不机械运行无关的全生产回归，但不得漏掉自检附带修复的直接回归。

模块接入或路由变更至少继续检查：

- 主Pipeline仍只包含STATE-00至STATE-09。
- 原有Template仍拥有原有阶段Schema。
- 新ID命名空间没有冲突。
- 新Workflow有明确触发、不触发与Not Applicable / Return Route。
- 新输出只写入合法的Active Project Root或对应可移植状态位置。
- 所有显式内部文件引用均存在。
- 正常样例通过Validator；缺字段、重复ID、越权ID或错误路由样例被拒绝。

## Runtime Recovery Regression Protection

`Unconditional Chat Runtime Startup And Recovery Guard`是每次正式Skill修改的固定基线，而不是按Diff选择的可选回归。无论修改任何文件、模块、文案、Template、Knowledge、测试、Validator或仅修正拼写，都必须运行`references/recovery_guards.md`中的完整`Legacy Recovery Regression Matrix (LR-R1—LR-R10)`，验证普通Chat activation、Current Skill resource解析、双source独立、Claim Gate、Work边界、legacy mapping、intent backfill、STATE-08 re-entry与plain-next隔离；不能以改动小、未触及runtime或“本轮改的不是recovery文件”为由跳过。

以下区域仍视为高风险触发面；命中时除固定基线外，还必须根据直接消费者增加定向恢复案例：

- `SKILL.md` activation / routing
- Runtime Reload / Workflow Re-entry
- State Source / Portable State
- Project Setup / project status schema
- Pipeline / STATE rename、owner或filename变化
- Screenwriter Module / WRITER INTENT PACKET
- Director Module / DIRECTOR INTENT PACKET
- STATE-07 / STATE-08 Current Object、Clip state、Reference / Blocking / Prompt entry
- `USER_GUIDE.md` recovery commands
- ordinary Chat vs Work routing

执行owner固定为`scripts/validate_sd_film.py --skill-root <skill-root>`与`scripts/test_validate_sd_film.py`。这两项验证始终检查LR-R1—LR-R10的静态合同和防篡改用例，因此每次正式修改都必须运行它们；如果未来脚本owner改名或迁移，必须在同一次变更中把本文件、执行入口与测试入口一起迁移，不能只删掉检查。语义演练仍由维护者按Matrix逐项核对，脚本通过不替代语义判断。

## Standalone Skill Discovery Guard

本Guard属于现有Skill维护QA，不是Plugin机制、不是主Pipeline STATE，也不建立第二套Runtime Router。它只保护独立Skill在支持本机Skills的ChatGPT桌面应用、Codex CLI与IDE中的发现入口；不得据此声称网页端或移动端能直接读取本机目录。

每次正式修改都必须运行以下固定检查，不允许因“本轮只改Writer / Director / Runtime / Template / 文案”而跳过：

- `SKILL.md` frontmatter的`name`仍为`sd-film`，`description`前置保留`调用sd`、`调用SD`、`用SD Film`、`重新调用sd`、`恢复旧项目`、`继续之前的项目`等高价值启动词；隐式调用只以当前description作发现提示，不以旧对话Skill摘要补位。
- `agents/openai.yaml`存在，`interface.display_name`为`SD Film`，`interface.default_prompt`显式提及`$sd-film`，`policy.allow_implicit_invocation`为`true`；Writer、Director、STATE Workflow和USER_GUIDE不得覆盖该调用策略。
- 当前运行时用户级权威安装采用`$HOME/.codex/skills/sd-film`。权威副本只允许存在**一份物理文件**；其他宿主各自的Skill根（如`$HOME/.agents/skills`）只允许以**指向该同一物理副本的Junction**存在，不得保留第二份**独立**`sd-film`副本。**判据是“本次改动是否需要双写”，不是“同名目录出现了几次”**——删除一根指向唯一物理副本的Junction不会消除任何重复，只会让该宿主失去本Skill。运行时安装根发生迁移时执行一次迁移，不维持双写或两个独立副本。
- 发现器会递归读取Skill根目录下的`SKILL.md`；因此Git忽略`tmp/`不等于运行时忽略它。临时打包或推送副本必须放在Skill根目录之外，或在完成前移除其`name: sd-film`入口；Validator必须拒绝根目录内的第二个同名入口。
- Codex中的确定性显式入口是`$sd-film`。在当前用户客户端的普通Chat中，`@`选择器只显示Plugin或Plugin内含能力，本机独立Skill不得承诺以`@`选择显示名的入口；普通Chat只有在宿主实际暴露本机Skills时，才可能通过`description`对`调用sd`作隐式选择。`agents/openai.yaml`的`display_name`与`allow_implicit_invocation`不会把独立Skill注册成Plugin，也不证明普通Chat已有`@`入口。
- Skill变更通常应被Codex自动检测；如果当前Codex会话未刷新元数据，要求重启桌面应用或新建Codex任务后复测。普通Chat的`@`列表没有SD Film时，不得把它误诊为Skill内容错误，也不得为迎合`@`而创建Plugin、复制Skill或弱化Runtime规则。

可执行owner仍为`scripts/validate_sd_film.py --skill-root <skill-root>`与`scripts/test_validate_sd_film.py`；它们必须检查元数据、别名、隐式调用开关、单一用户级权威副本、禁止虚假`@`显式调用声明及`references/recovery_guards.md`中的`Standalone Skill Discovery Regression Matrix (SD-R1—SD-R5)`。安装位置、普通Chat是否暴露本机Skill以及客户端刷新属于运行环境证据，脚本之外仍需在最终报告中如实记录。
