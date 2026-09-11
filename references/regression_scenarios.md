# SD Film Regression Scenarios

## Regression File Index

为控制单次读取成本，本回归集按编号族拆为四个文件。每个文件内部编号保持连续，可按编号直接定位；只读需要的那一个，不整集通读。

| File | 覆盖范围 | 用途 |
|---|---|---|
| `references/regression_scenarios.md`（本文件） | R00—R14 与 Deterministic Expectations | 管线、资产、预算、Runtime Reload 与准入的基础场景；总期望清单 |
| `references/regression_scenarios_craft.md` | R15—R23 | Prompt 编译、表演、阻断、剧本与导演端到端 |
| `references/regression_scenarios_system.md` | R24、R27—R35、R48—R54 | 写作、Runtime、模型适配、FAST、交付校验、美学锁与维护 |
| `references/recovery_guards.md` | R25（LR-R1—R10）、R26（SD-R1—R5） | 每次正式修改都必须运行的固定基线 |

## Purpose

以下场景用于修改Rules、Workflows、Knowledge、Templates或Validator后的生产回归检查。每类至少保留一个PASS和一个FAIL样例。

---

## R00 STATE-01 Optimization Decision Gates

### R00-A Rough Script Reports And Stops

输入：`调用SD + 一份存在开场慢、对白重复和高潮偏弱的普通粗略剧本`。

PASS：先执行`Script Input → Script Diagnosis → Optimization Opportunity Report → User Decision Gate`；报告逐项覆盖开场钩子、核心冲突进入时机、信息重复、台词效率、动作可视化、人物记忆点、节奏、高潮力度、情绪价值、结尾Hook、时长适配、场景/人物复杂度；结论为B或C档；只说明问题、影响和方向；以“是否执行轻度优化？”或“是否进入结构优化？”结束；`Script Status: Source Material`、STATE-01 `IN_PROGRESS`并停止。

FAIL：同轮输出改写后的剧本正文、替换台词、Adaptation Draft、Screenwriting Optimization结果、Directorial Interpretation结果或Production Script Proposal；自动进入STATE-02。

### R00-B Reject Optimization Locks Original

续接R00-A，用户明确回复“不优化，保留原稿”。

PASS：不修改原稿，不执行Script Adaptation、Screenwriting Optimization或Directorial Interpretation；完成只读Script Analysis；将用户原始版本登记为`Production-Locked`，STATE-01通过Completion Gate后进入STATE-02；报告风险仅作为制作注意项保留。

FAIL：拒绝后仍润色台词、补场、重排、自动改编，或继续等待Production Script Proposal确认。

### R00-C Explicit Optimization Stops At Proposal Confirmation

续接R00-A，用户明确回复“进入优化”。

PASS：A/B类执行`Screenwriting Optimization → Directorial Interpretation → Production Script Proposal`；Class C按必要性先执行`Adaptation Target Detection → Script Adaptation → Adaptation Draft`再进入同一优化链。Proposal输出后写`Script Status: Optimized Proposal`、STATE-01 `IN_PROGRESS`、`Pending Decision: 等待Production Script Proposal确认`并再次停止。当前Proposal已展示且可核对时，用户随后使用推进表达即确认Proposal，随后Production-Lock并进入STATE-02。

FAIL：把单独“继续 / 下一步 / 好的”当作优化授权或Proposal确认；Proposal输出后直接Production-Lock或进入STATE-02。

---

## R01 Simple Single Shot

单人、简单动作、固定或单一运镜。应为Execution Risk L1，Sequence Planning Not Applicable，边界和稳定结尾仍不得缺失。

## R02 Two-Person Dialogue

检查左右、轴线、说话者/倾听者、Exact Line、自然停顿、误口型和相邻镜眼线。

## R03 Chase / Action Coverage

检查Required Coverage、屏幕方向、动作结果、Camera Class与L3/L4降级，禁止把多视点伪装成一镜。

## R04 FX Lifecycle

检查FX来源、阶段、人物/环境/道具交互、残留后果、光色与声音尾部。

## R05 Multi-Unit Sequence

检查SEQ/BEAT/COV/UNIT命名空间、Entry/Exit Anchor、State Ledger和重试隔离。

## R05A Detailed Shot Design To Clip Production

输入包含连续对话、动作接力、场景断点与不同逐镜时长的Confirmed Detailed Shot Design。检查所有正式Shot按原顺序且仅进入一个CLIP-xxx；Seedance 2.0每个Clip由用户选择4—15秒，Seedance 2.5由用户选择4—30秒，16—30秒只在严格预检PASS时成立；未知网关状态不得将2.5预先压缩为15秒。连续低复杂度Shot可合并，跨时空/资产断点和不满足模型窗口的候选被拆分或返回正确上游边界；Clip内保留起始状态、连续动作、空间/道具/摄影机连续性与结尾状态。跨Clip固定执行`上一Clip生成完成 → 判断是否需要严格承接 → 若需要则请求用户截取尾帧 → 上传并命名REF-TAIL → 加入当前Clip参考资产 → 首帧明确引用 → 当前Clip生成 → 当前Clip尾帧限制 → 下一Clip承接`；STATE-08按CLIP→G一对一输出一条连续Prompt，即使Clip包含多个Shot也不拆Prompt；任何Storyboard视觉材料均不得进入参考资产。

## R05B Source Script Label Namespace

输入剧本自带“镜头1—镜头5”或“Clip A—Clip E”标题。PASS路径必须先把这些标题登记为Source Script Labels，STATE-05建立SCENE，STATE-06按叙事功能、动作阶段、机位/视点、Coverage与边界创建正式SHOT，STATE-07才根据Confirmed Detailed Shot Design建立CLIP。以下任一情况均为FAIL：在STATE-05或STATE-06完成前创建暂定/占位/正式CLIP；把Source Script Label直接改名或一对一映射为SHOT、UNIT、CLIP或G段；只声明Source Revision但不存在可关联的Confirmed Detailed Shot Design Artifact或Portable Checkpoint。

## R06 Scene / Time Discontinuity

检查Motivated Discontinuity，只重建剧情授权状态，不伪造过渡动作。

## R07 Image-To-Video Reference

检查首/尾帧用途、Asset Active Version、边界冲突和Template 11到Template 10的单向投影。

## R08 Review Revision Loop

PASS允许完成；REVISE/REBUILD保持STATE-09 IN_PROGRESS，记录Affected IDs、Return Route、Accepted Unaffected Artifacts和Recheck Scope。

## R09 STATE-03 Double-Confirmation Closure

以下三个最小案例必须完成正式资产的Registry状态闭环。当前agent具备直接生图能力时，默认在`Image Generated`停止；当前agent不具备能力或用户要求Prompt时，才在`Prompt Draft`和`Image Generated`各停止一次。示例中的“用户确认”是测试事件，不代表实际项目批准。

### R09-C Character

输入：`CHAR-001 林遥，28岁女气象工程师，短黑发，灰蓝防水工作服，冷静克制；有对白；无剧情状态变体。`

当前agent具备直接生图能力时，首次输出为一张外观参考图并等待用户确认外观；不展示Prompt，也不得把这张外观参考图写入Candidate / Canonical References、Active Version或下游视觉输入。当前agent不能直接生图或用户明确要求Prompt时，外观参考图Prompt至少包含：

- 角色定义只包含视觉身份与剧情事实；“有对白”不得触发角色音色描述、Voice Profile、Seed Audio Prompt或Voice Reference字段。
- 正式角色资产设定图Prompt：`角色设定表，28岁东亚女性气象工程师林遥，椭圆脸、平直眉、深棕眼、鼻梁自然、薄而清晰的唇形、真实轻微皮肤纹理、短黑发齐耳并露出双耳，身高约168厘米、匀称偏瘦体型；穿灰蓝色连帽防水工作服、深灰工装裤、黑色防滑短靴，不佩戴首饰。纯浅灰无缝背景，一张4:3横幅画布固定为清晰四分区：从左至右三个等比例、等高度全身区域为正面自然站姿、严格右侧、背面；右侧第四区为正面头肩面部特写，平静中性表情、视线略高于镜头。四区必须为同一角色、同一年龄感、同一发际线和发型、同一服装接缝/口袋/拉链/帽型/鞋型/配色；柔和中性棚拍光，真实电影角色概念设计，清晰材质与结构，高分辨率。禁止拆为两张图，禁止改变脸型、年龄感、身体比例、发型长度、服装结构与配色；禁止透视夸张、动态姿势、额外人物、文字、水印、拼错肢体、美颜塑料皮、夸张妆容、笑容、首饰或五官漂移。`
- 状态变体：`Not Required—剧本未确认额外视觉状态。`
- `Awaiting User Confirmation: Appearance Reference Prompt`；不得生成图片。

模拟用户确认外观后，当前agent具备直接生图能力时直接生成一张正式合成角色资产图；不能直接生图或用户要求Prompt时，先输出并确认正式资产Prompt。生成后仅登记`Candidate References: char-001-asset-sheet-c01.png`，状态为`Image Generated`，不得出现Canonical References或Active。模拟用户确认该一张合成角色资产图后，最终记录必须为`Visual Production Status: Asset Confirmed`、`Status: Active`、`Active Version: v001`，并把该已批准Candidate Reference升级为Canonical Reference；整个案例不创建声音资产，也不因缺少声音资产阻塞。

### R09-E Environment

输入：`ENV-001 海边气象站主控室，近未来但可现实建造，暴雨夜；需要主空间、入口反向视角与控制台关键区域。`

Prompt Draft至少包含：

- 主参考图Prompt：`近未来海边气象站主控室，长方形单层空间，画面左侧为面向海面的连续抗风玻璃窗，画面右后方为唯一金属气密入口，中央两排低矮控制台沿房间长轴排列，前端大型天气雷达屏，天花暴露式线性灯与检修轨道；湿冷暴雨夜，窗外海浪与远处警示灯可见，室内主要由4000K线性顶灯和青绿色仪表屏照明，灰色防滑地面、哑光铝板墙、深灰橡胶包边。摄影机位于入口内侧约1.6米高度，24mm等效大全景，清楚展示入口—控制台—海窗的可行走动线与尺度；真实电影美术概念图，16:9，高分辨率。锁定窗、入口、两排控制台和雷达屏的相对位置；禁止改变房间骨架、增加楼梯或第二入口、赛博朋克霓虹堆叠、人物、文字、水印。`
- 多视角Prompt：从海窗方向反看入口与两排控制台的完整独立Prompt，保持同一布局、材质、暴雨夜与光源锚点。
- 关键区域Prompt：控制台操作区中景完整独立Prompt，明确按钮、屏幕、椅位、通行宽度与材质。
- `Visual Production Status: Prompt Draft`并等待确认。

模拟Prompt确认、生成`env-001-main-c01.png / env-001-reverse-c01.png / env-001-console-c01.png`、图片确认后，三图才可进入Canonical References；最终必须为`Asset Confirmed + Active`。任一步缺少Prompt确认或图片确认均为FAIL。

### R09-D Prop Discovery Completeness

输入：Production-Locked Script包含三项可见物件：角色从桌上取走并在下一Scene交给同伴的黄铜钥匙；只在书房背景出现的两盏台灯；以及角色翻阅后放回原处的无特写普通报纸。

PASS：STATE-02只将黄铜钥匙识别为`Important Prop Candidate`，因交接、近景信息揭示和跨Scene持有连续性路由为`PROP Core`。两盏台灯与普通报纸没有承担剧情/信息、关键动作、状态连续性或用户指定需求，不进入台账、Registry或STATE-03待办。钥匙未确认图片时STATE-03保持`IN_PROGRESS`。

FAIL：只列角色和环境后将STATE-02标记完成；因为钥匙只出现一次而不作路由决定；将所有可见物件（包括台灯和报纸）强制列为道具资产；用空白Prop清单替代`No important PROP asset required`；或在STATE-06/08临时设计未进入STATE-03的正式重要道具。

### R09-P Prop

输入：`PROP-001 手持风暴数据记录器，掌上工业仪器；正常与屏幕报警两种状态，需要接口细节。`

Prompt Draft至少包含：

- 主参考图Prompt：`一张1×4横版道具设定图，手持风暴数据记录器，掌上工业仪器，约18厘米高、8厘米宽、3厘米厚，深灰色防滑橡胶包边，拉丝铝合金正面框，顶部短天线，正面上半部为无品牌矩形屏幕，下半部四枚实体防水按键，右侧橙色密封数据接口盖，背面可拆电池盖与腕带孔；从左至右四个等宽区依次为正面、严格右侧、背面、右侧橙色密封接口盖的关键细节近景。前三格以同一比例完整展示同一道具，四格保持同一结构、材质、基础状态、白灰无缝背景与柔和棚拍主光和轮廓光；真实可制造产品设计，高分辨率。锁定尺寸比例、天线、屏幕、四按键、橙色接口盖和电池盖位置；禁止拆成四张图、不同设计、文字标签、品牌文字、额外按键、透明悬浮界面、夸张科幻装饰、人物、水印、结构漂移。`
- 状态Prompt：屏幕由正常数据变为红色报警界面，外壳结构、按键、天线与接口位置完全不变；完整包含同样的构图、光影、背景和限制。
- 细节Prompt：`Not Required — covered by Main 1×4 Prop Sheet`；右侧橙色密封接口盖的关键细节已在第四格锁定。若剧本后来要求打开接口盖的内部机械状态，才为该新状态单独出图。
- `Visual Production Status: Prompt Draft`并等待确认。

模拟Prompt确认、生成`prop-001-main-sheet-c01.png / prop-001-alarm-c01.png / prop-001-port-c01.png`、图片确认后，三图才可进入Canonical References；其中`prop-001-main-sheet-c01.png`必须为正面 / 侧面 / 背面 / 关键细节的1×4横版。最终必须为`Asset Confirmed + Active`。生成图被拒绝时保持Candidate，不能进入Registry确认态。

---

## R10 Canonical Character Appearance / Form Inheritance

项目已有经用户确认的`CHAR-005@v002 孔老板`Active角色资产：孔雀本体、固定冠羽与羽色、真实孔雀躯干和双足结构、无手臂、非人形比例；Canonical References分别锁定Identity、Scale与Costume/Adornment。用户随后只要求制作新的挥翅动作状态图、双人场景示意、Storyboard、电影海报、Detailed Shot Design、Clip和Seedance Prompt，并提供一张构图很好但把孔老板画成人形孔雀头角色的风格参考。

PASS路径必须在所有阶段继续引用`CHAR-005@v002`及适用Canonical References；只继承新参考的构图或镜头关系，不继承其人形结构；动作图只改变挥翅姿势，海报与场景图保持孔雀本体，Shot/Clip/Prompt明确锁定无手臂、孔雀躯干与原羽色，最终视频Review逐项检查物种与身体结构。风格参考、动作参考或新生成结果与Active资产冲突时，Active资产胜出，冲突结果被拒绝或重生。

以下任一情况均为FAIL：孔老板出现人形躯干、手臂、人类身高比例或半人形站姿；冠羽、羽色、体型、服装/装饰基础无授权变化；因动作、机位、构图、风格或模型适配重新设计外貌；把Storyboard、海报或漂移生成结果登记为新角色Canonical Reference；把两套外貌混合折中；未走STATE-03 Candidate Version与用户批准就改变Active角色资产。

---

## R11 Reference Budget / 参考资产预算控制

所有案例先执行Visual Input Eligibility、删除非当前Clip出场角色、未使用环境/道具/动作图并去重，再判定A/B/C。A/B标记`Tail Frame Required = YES`，尾帧无论是否已上传都预留1个Projected位，并在`参考资产：`直接列统一`REF-TAIL`名称、对应用途与真实状态；未上传时写“待用户提供/待上传、未确认”，不计入已提交图片，Prompt可交付但实际提交生成前补图。C标记`NO`，不列或预留上一尾帧。真实视觉条目必须存在且已确认；其他已经确定需要用户实际补入的视觉参考图必须写明具体图像对象、实际投喂用途与“待用户补充/待上传、未确认”，计Projected位但不冒充已提交图片，也不得绕过正式Canonical资产确认。Projected Final Count与已提交图片数均≤9；整合只允许在超限风险触发后作用于非角色信息。

### R11-A Seven Candidates

当前Clip有7张真实、独立、相关参考图，无额外连续性帧需求。PASS：不整合，最终7张。FAIL：为了“统一”或因为已有总设定图而主动替换/合并独立图。

### R11-B Eight Candidates Without Reservation

当前Clip有8张真实、独立、相关参考图，已确认不需要上一Clip尾帧、当前首帧或其他额外图片位。PASS：不整合，最终8张。FAIL：默认整合或无依据预留导致丢失高精度独立图。

### R11-C Nine Candidates Plus Previous Tail

当前Clip已有9张候选，Previous-Clip Continuity Decision为A Direct或B Reference-Only，因此`Tail Frame Required = YES`。无论上一实际尾帧图是否已经上传，Projected Final Count均按10张计算并至少释放1位；【参考资产】必须以`REF-TAIL-XX｜CLIP-XX尾帧参考`列出尾帧，A标“同镜头连续承接用途”，B标“空间/站位/景别参考用途”。若尚未提供，PASS必须标记“待用户提供/待上传、未确认”，不计入已提交图片；Prompt可交付但实际提交生成前补图。FAIL：因尾帧暂缺把需求改为NO、遗漏`REF-TAIL`声明、声称待补充资产已上传/已确认、B误用A固定直接承接句、仍声称9张通过、超过9张或合并核心角色图。

### R11-D Twelve Candidates

当前Clip有12张真实候选。PASS：删除无关项、去重；仅在仍超限时用真实已确认的环境多视角/道具组/空间或动作关系总图替代完整覆盖的零散图；仍超限按保留优先级裁剪，最终≤9。FAIL：默认全部合并、虚构不存在的总图，或最终仍>9。

### R11-E Multi-Core-Character Independence

多角色场景中有多个当前Clip核心角色。PASS：每个核心角色各自保留独立正式角色资产设定图（面部特写 + 三视图）或角色锁定图；动作/互动图只负责动作关系；非角色信息承担必要的整合压力。FAIL：把多个核心角色合并成角色总表、共用一个角色位，或用动作图替代任一角色外貌基准。

### R11 Retention Priority

整合后仍需裁剪时，从高到低保留：当前Clip出场核心角色独立图 > 当前主要环境 > 当前关键道具 > 当前关键动作/互动关系 > 上一Clip尾帧/当前首帧连续性参考 > 特殊一次性道具/次要角色。已经判定为Direct / Reference-Only且实际存在、可访问、已确认的连续性帧属于硬需求，必须先释放其他位置，不得静默删除后仍声明连续继承。

---

## R12 Runtime Skill Reload / Workflow Re-entry

以下案例覆盖新Chat、旧对话、重复Reload、Workflow Re-entry、资源不可访问、非Reload推进和Work边界。Reload / Re-entry成功判定只服从`rules/runtime_reload.md`；这些案例不创建新的测试协议。

### R12-A Stale Conversation Pipeline vs Current Installed Pipeline

输入：旧对话缓存声称`STATE-07`对应`Storyboard`，磁盘当前`SKILL.md`却声明`STATE-07 Clip Production`并包含更新的Skill Version / Build ID。

PASS：按`rules/runtime_reload.md`重新解析当前runtime可访问资源，重新完整读取Current Skill `SKILL.md`，记录`Reload Status: RELOADED`、Loaded Source、Skill Version / Build ID与Owner Files Resolved；当前Skill Pipeline覆盖旧对话的Skill描述；再只读取状态owner、映射后Workflow与其适用依赖。

FAIL：继续把Storyboard当作固定STATE-07；用历史摘要覆盖磁盘Skill；未实际重读却声称`RELOADED`；强制用户新建对话或项目。

### R12-B Preserve Progress And Map To Current Workflow

输入：旧项目停在标注为`Storyboard`的`STATE-07`，已有Confirmed Detailed Shot Design，无Confirmed Clip Production Plan，并有可验证Last Successful Checkpoint。

PASS：按`Active Project Root/project_status.md > portable_project_status.md > 当前可验证Project Context`选择状态；如使用第三级则先规范化为Portable State；把项目映射到当前`STATE-07 Clip Production`和`10_clip_production_workflow.md`；保留Detailed Shot Design、Checkpoint、已完成States与Storyboard Optional Artifact；只继续尚未完成的Clip Production。

FAIL：回退STATE-00；重做已确认Detailed Shot Design；将旧Storyboard作为STATE-08参考资产；仅按旧STATE编号硬复制而不检查Artifact / Completion Gate。

### R12-C Preserve Production Lock And Confirmed Assets

输入：项目已有`Script Status: Production-Locked`、Confirmed Core / Support Assets、Active Versions、Canonical References、已接受Artifact Revision与用户明确的“不改剧本、不改角色外观”约束。

PASS：Reload后上述项目事实全部保留；只更新Skill Definition和必要路由标签；后续Workflow仍从Active / Canonical资产与Production-Locked Script读取真源。

FAIL：把Script Status降回Source Material；丢失Confirmed Assets、Active Version或Canonical References；因Skill重载重新要求用户确认已接受结果；忽略用户锁定约束。

### R12-D New / Ordinary Chat Uses Current Accessible Skill Resources

输入：新普通Chat中用户说“调用sd”，当前runtime能读取exposed / installed SD Film resources，但不能访问Windows本机路径。

PASS：先从当前Chat runtime可访问资源重读`SKILL.md`与基础路由owner，记录真实Loaded Source并继续State Source / Workflow路由；不要求Work，不要求用户上传本机Skill目录。

FAIL：仅因`C:\Users\Lenovo\.agents\skills\sd`不可读就停止、声称BLOCKED、要求切Work，或未读取当前资源便声称严格按当前Skill。

### R12-E Repeated Reload, Current Owner And Re-entry Evidence

输入：Skill更新后，用户再次说“重新调用sd”；上一轮已有Reload Evidence与Project Context。

PASS：生成新的Invocation Marker / Load Timestamp（运行时可提供时），重新读取当前Loaded Source，核对当前Skill Version / Build ID与Owner Files Resolved；版本、来源或owner变更时证据随之变化，未变化时也能证明本轮发生实际读取；Project Context保持；重新确认Current STATE / Workflow / Object，并从当前owner入口执行到合法Checkpoint后才报告已重进Workflow。

FAIL：复用上一轮Evidence、只回显缓存版本、继续使用更新前owner、未实际读取却称已重新加载/已重进，或把Reload当作项目重置。

### R12-F Current Skill Unavailable Uses Truthful Fallback

输入：用户显式“重新加载SD”，但当前Skill入口或必需owner实际不可访问；存在有效Portable State或可验证Project Context。

PASS：记录`Reload Status: UNAVAILABLE`、失败资源/原因和实际Fallback Source；保留项目并继续fallback合同允许的安全工作，不声称`RELOADED`、最新安装版或严格按当前Skill，不因本机路径不可见默认切Work。

FAIL：用旧对话Skill摘要冒充Current Skill、隐瞒fallback、清空项目，或仅因路径不可见报告项目BLOCKED。

### R12-G Plain Continue Does Not Force Full Reload

输入：当前runtime已有一次成功loaded Skill Definition和有效Project Context，用户只说“下一步”。

PASS：复用当前loaded definition，按需读取当前Workflow与依赖并推进一个合法Checkpoint；不全量重读Skill，不产生新的Reload Evidence，也不把“下一步”当作显式Reload。

FAIL：每一步无意义重读全部Rules / Workflows / Knowledge，或伪称本轮再次RELOADED。

### R12-H Work Is Only For Local File Operations

输入A：普通制作请求“调用sd，继续CLIP-003”；输入B：用户要求修改本机`C:\Users\Lenovo\.agents\skills\sd`文件。

PASS：A先使用当前Chat可访问Skill资源并正常路由，不默认Work；B进入具备本地文件能力的Work/Codex并遵守Skill维护流程。

FAIL：A强制切Work，或B在无法直接操作本地文件的环境中伪称已经修改。

### R12-I Old Prompt Does Not Bypass STATE-08 Entry

输入：旧对话含CLIP-04旧Prompt、旧Skill摘要与上一次未验证结论；Project Context中已有Confirmed Clip Plan、Current Clip与已确认资产。用户说“重新调用sd，重写CLIP-04”。

PASS：重新读取Current Skill并保留Project Context，重新确认STATE-08与`workflows/11_video_generation_workflow.md`，从Workflow入口依次执行Reference Selection / Routing、Final Visual Blocking Anchor Assessment、Prompt Compiler与Final QA；旧Prompt只作为待比较/修改对象，不成为Gate证据或唯一编译输入。

FAIL：直接润色旧Prompt、沿用旧Skill摘要、跳过Reference Routing / Visual Blocking Gate / Final QA，或因重载清空Confirmed Project Context。

### R12-J Confirmed Sketch Survives Re-entry When Blocking Is Stable

输入：CLIP-04已有与当前Blocking Signature匹配的Confirmed `REF-SKETCH-04`；用户显式重新调用并只要求压缩措辞或优化Prompt，Blocking未实质变化。

PASS：re-entry重新执行Final Assessment并得到`KEEP existing sketch`，复用同一草图、Revision与图片位，不重新生成草图；随后从Prompt Compiler与Final QA产生当前CLIP-04结果。

FAIL：把re-entry解释为重置草图、重复生成`REF-SKETCH`、调用母版替换已确认Anchor，或跳过Assessment直接假设旧图有效。

### R12-K Material Blocking Change Forces Reassessment

输入：CLIP-04原为双人并排共坐，已有Confirmed `REF-SKETCH-04`；用户显式重新调用并把Blocking改为一人起身走到另一人面前，改变Topology、Position与Movement Path。

PASS：保留旧草图Revision追溯，但re-entry重新执行Visual Blocking Anchor Reassessment并只得到`REPLACE / RETIRE / CREATE`中的适用结果；Final=`REQUIRED`且新Anchor尚未确认时停在草图Checkpoint，不沿用旧图或直接输出Prompt。

FAIL：因旧图已存在而`KEEP`、只改Prompt文字掩盖Blocking冲突、跳过草图验证，或删除旧Revision追溯。

---

## R13 Cross-Clip End-State And Reference Routing

以下三例均先从上一Clip的Entry / 内部状态链 / Exit / Handoff归并八组`Clip End-State Record / Next-Clip Carryover`，再按当前Clip目标与Continuity Risks路由最小充分参考资产；不得把整个Registry、上一Clip全部资产或所有Eligible条目机械复制到下一Clip。

### R13-A Same-Shot Direct Continuation

上一Clip结束时：林夏坐在钢琴凳画左、身体朝右前方，右手压住乐谱；许栀坐画右、与林夏肩距约20厘米；两人位于同一关系轴北侧，摄影机C1在轴线南侧中景，雨天窗光从画右进入。下一Clip继续同一镜头、同一动作阶段。

PASS：八组记录完整保留人物坐姿/朝向/距离、乐谱持有与位置、轴线和C1机位、雨天光态及未完成动作；判定A Direct与`Tail Frame Required = YES`。Reference Selection选择各自身份风险所需Character Canonical、钢琴区域结构风险所需Environment Canonical、乐谱造型风险所需Prop Canonical与`REF-TAIL-XX｜CLIP-XX尾帧参考（同镜头连续承接用途）`；Spatial Blocking仅作文字几何约束，不把Top-down Map当视觉资产。尾帧缺图时条目写“待用户提供/待上传、未确认”，Prompt仍可完整交付但实际提交生成前补图；`首帧参考：`使用固定Direct句并逐项继承，不重置坐姿、不重播压住乐谱动作。

FAIL：缺少任一八组状态导致人物/道具/相机/光态重置；把B/C误判为A；省略REF-TAIL、用途错误、用文字End State冒充图片，或因预算有空位加入不相关角色/道具资产。

### R13-B New Shot With Tail Position Reference

上一Clip具有与R13-A相同End-State，但下一Clip另起OTS新镜头：允许摄影机从C1改为轴线同侧C2、景别改为近景；人物坐姿、左右、朝向、肩距、乐谱位置、雨天窗光方向与钢琴空间关系必须保持。

PASS：八组记录把“必须保持”与“允许改变”分开；判定B Reference-Only与`Tail Frame Required = YES`。Reference Selection保留解决身份/环境结构/乐谱造型风险的对应Canonical资产，并选择`REF-TAIL-XX｜CLIP-XX尾帧参考（空间/站位/景别参考用途）`锁定站位、距离和空间；`首帧参考：`明确另起新镜头重新构图、允许C1→C2与中景→近景，不使用A的固定Direct句。其他已确认但与本Clip无关的资产不选。

FAIL：把新OTS误写为同镜头续拍；使用A固定句；尾帧用途未写或写错；无授权跨轴、左右翻转、人物/道具重置；为了“更稳”把全部Registry资产塞入参考清单。

### R13-C New Shot Without Tail Reference

下一Clip切到同一教室门外的单人门把手特写，人物不入画；新构图不依赖上一尾帧的两人站位，但仍需保持已确认教室门结构、雨天状态和门把手造型。

PASS：八组记录明确上一人物状态暂不进入画面、剧情仍有效但不作视觉首帧锚定；判定C Not Required与`Tail Frame Required = NO`。Reference Selection不列、不预留`REF-TAIL`，只选择门结构风险所需Environment Canonical与门把手造型风险所需Prop Canonical；雨天光态若只有文字场景视觉基准则写入`环境一致性 / 首帧参考 / 起始状态`，只有实际已确认合格的场景状态图存在时才作为视觉参考。Spatial Blocking继续提供文字方向约束，Top-down Map不进入参考资产。

FAIL：机械要求截图或把旧尾帧、两名角色图、钢琴/乐谱等无关资产塞入；把旧人物构图和光线画面强行继承到新特写；遗漏门结构或门把手这一实际风险所需资产。

---

## R14 Reference Asset Eligibility / 参考资产准入

输入清单：

```text
参考资产：
1. 林夏.png｜林夏-基础形象
2. 许栀.png｜许栀-基础形象
3. ENV-02｜窗台钢琴区域教室全景
4. REF-TAIL-02｜CLIP-02尾帧参考｜用途：镜头延续、参考人物坐姿延续、参考人物在同一张板凳上的左右站位、参考肩膀距离、参考手臂搭放位置、参考钢琴与窗户空间关系、参考雨天光线与环境状态
5. 乐谱参考资产｜用途：固定乐谱纸张尺寸、材质、印刷内容与旧化程度；作为本Clip“被风吹落的乐谱”造型依据
6. 板凳参考说明｜用途：锁定两人共坐同一张板凳；不是两把椅子，不是两张琴凳，不允许拆分座位
```

PASS：逐项执行“这是不是一张实际会被投喂/引用的视觉资产？”；1—5号保持不动，6号判定`NOT ELIGIBLE`并从`参考资产：`删除。其正向事实迁移为`空间关系：两人始终共坐同一张双人板凳，林夏在左、许栀在右，保持已确认肩膀距离。`或等价`道具状态`约束；“不得拆成两把椅子/两张琴凳”可在`道具状态`正向锁定并把高风险错误写入`反向提示词`。如果项目实际存在双人钢琴凳视觉图，则以真实`PROP-BENCH-01｜双人钢琴凳`及其文件/受控ID进入参考资产，而不是保留6号文字说明。

FAIL：保留6号；仅因加入“参考说明/用途”就把它算作图片位；删除或重写1—5号视觉条目；把约束迁移到新字段；虚构`PROP-BENCH-01`或其图片路径；把待补正式Canonical道具图当作占位绕过STATE-03。

---

## Deterministic Expectations

- Skill、Registry、Project、Asset、Artifact、Execution、Sequence、Clip、Poster、STATE-08和Review Validator通过合法样例。
- 缺字段、重复ID、非法时间轴、背景音乐、内部模式ID泄漏、无Return Route和第三次盲重试被拒绝。
- 主Pipeline仍只有STATE-00至STATE-09。
- STATE-08最终Schema仍只由templates/10_video_prompt.md拥有。
- R09-C/E/P均验证`Prompt Draft → Prompt Confirmed → Image Generated → Asset Confirmed`，且Prompt确认前不出图、图片确认前不Active/Canonical。
- R10验证Canonical Character Appearance And Form Lock从Asset、Visual Development、Storyboard/Poster、Shot Design、Clip、Prompt Generation、Final Video到Review的全阶段继承，并覆盖非人角色禁止未授权拟人化。
- R11-A至R11-E验证条件性整合阈值、9张加必需尾帧的真实计数、12张自动压缩到≤9、实际资产存在性和多核心角色独立图硬门槛。
- R12-A至R12-K验证旧对话缓存不能覆盖Latest Successfully Loaded Current Skill Definition、旧STATE按当前Artifact / Completion Gate映射、Project Context在Reload后不丢失、显式重新调用会从当前Workflow入口重跑而非润色旧Prompt、Confirmed草图按Blocking Signature复用或重评，以及普通Chat优先当前可访问Skill resources、重复Reload产生本轮证据、资源不可访问时诚实报告fallback、“下一步”不强制全量重载、Work只用于本地文件操作。
- R13-A至R13-C验证尾帧需求先于资产可用性判定、严格承接主动请求截图与草案/最终版边界，以及非严格承接不强制截图。
- R14验证纯文字“板凳参考说明”从参考资产删除并迁移到既有空间/道具/反向字段，1—5号视觉资产保持不动，真实双人钢琴凳图只以正式资产ID引用。
- R15-A至R15-L验证文学意图可执行转译、工程级数据按视觉价值压缩、Canonical资产释放Prompt注意力、导演/电影级标签首次出现时的项目特定展开、已锁定项目风格的后续Clip delta压缩、动作复杂Clip中的风格让位、正文正向化、通用负向项末尾唯一收束、局部物理连续性约束保留、CLIP-03字段唯一归属与事故历史式反向段压缩，以及本次调整不破坏Voice opt-in；最终Template结构保持不变。
- R16-A至R16-E验证Canonical来源携带已锁定状态、Generation Budget先于五维、Accepted Observed State覆盖Planned瞬时状态、`REF-TAIL`不越权覆盖身份，以及站位失败优先单变量复拍；全部复用现有Pipeline、Execution Ledger与Template结构。
- R17-A至R17-C验证角色声音身份严格opt-in、常规STATE-08 Prompt完全省略声音身份文字、显式声音设计进入独立Seed Audio兼容模板，以及已有Confirmed Voice Source不会在只请求Clip Prompt时被自动序列化。
- R18-A至R18-D验证Scene Spatial Snapshot与合法越轴、PL1克制表演、A3动作动力因果和A1简洁降级；四类均不得新增主STATE、Template字段或Prompt内部标签。
- R19-A至R19-D验证每Clip必检查但不必出草图、首次Required Clip先草图后Prompt、Pose Hierarchy / Relationship Topology漂移、Confirmed Anchor持久复用、Blocking重构四种Reassessment结果、简单单人NONE与A3综合草图；草图不得覆盖Canonical资产或污染最终Prompt。
- R20-A至R20-F验证母版只拥有Sketch Presentation Authority、Current Clip独占Blocking内容、钢琴双人 / 三人围桌 / A3统一使用无性别技术人偶、任何Character Appearance Leakage硬失败、简单单人NONE不受母版可用性影响、Prompt Rewrite复用当前草图且母版不进入最终视频参考资产或图片预算。
- R21-A至R21-C验证逐角色Performance Arc、Pre-action / In-action / Post-action Residue、Intentional Hold、多人相对表演层级和Clip Performance / Emotion Check；固定剧情、SHOT / Clip结构与STATE-08字段保持不变。
- R22-A至R22-H验证Creation Brief与Existing Script / Material双入口、Idea-to-Screenplay、明确直接优化授权、Proposal修订/确认、Directable Screenplay QA、导演思维向STATE-05/06传递，以及STATE-02至09、Storyboard、Voice、Music、REF-SKETCH与Prompt Compiler隔离不回归。
- R23-A至R23-N验证Director Module从Project / Script到资产、Scene / Sequence / Shot / Clip / Prompt / Editing / Review的持续传递、Visual Dramaturgy、Visual Grammar Baseline与Scene Delta、Project Color Reference的条件性模型输入、Scene Camera Strategy、固定Shot决策顺序、Dramatic Execution Unit、双女主钢琴Prompt、Action-dominant路由、Technical与Director's Cut Review、Runtime Continue隔离、三镜功能差异、FX / Sequence / Clip / Prompt的显式消费与多阶段Clip的观察层次；最终Prompt Schema、Voice opt-in和现有连续性系统保持不变。
- R34-A至R34-D验证STATE-00模型默认/偏好减少重复确认，但STATE-06/07仍按模型真实参考能力复核；Final=`REQUIRED`的草图在兼容模型中成为真实提交图片输入、计入预算，在文件缺失、Signature失配、预算不足或H3模式不兼容时诚实阻断；NONE、复用与替换不回归。
- R35-A至R35-C验证用户“已有资产”属于可用性声明而非提交义务：STATE-02照常输出完整清单并标注`已有（用户声明）` / `待制作`，不索取、不催交、不逐项盘问、不写BLOCKED；声明不构成Existing File Check、Candidate / Canonical Reference或Active Version；缺失由用户主动说明或由清单承载。
- R24-A至R24-K验证Screenwriter Module持续维护人物/故事因果、Scene Value、Writer Beat、Subtext、Setup-Payoff、Information Architecture与Arc，经Writer → Director Handoff传递到Shot / Clip / Prompt / Editing / 三层Review；Genre不被固定公式全局化，Writer不拥有Camera，双入口、Runtime / Reload、Voice / Music、Accepted Take Canon、Shot-State Memory与STATE-08 Schema不回归。
- R27-A至R27-E验证无动机机位跳变与连续长镜头中途换轴失败、耳镜反光现实→玉境Match Cut可通过、有动机剪辑缺切点或切后稳定重建失败，以及容量不足返回STATE-07拆分Clip；STATE-08固定字段不变。
- R48-A至R48-H验证交付物校验器与Skill维护校验器职责互不替代、未授权音色字段被拒、Review台账逐镜逐边界全覆盖且不得留空、`画幅：`分镜总数声明与实际数量一致、大全景尺度可由现实关系复算、人物必须响应环境光区、参考代际劣化按顺序处理且不放开线稿/Storyboard禁令，以及经验必须带P/O/C分类与触发条件、步骤、失效信号、例外、反例且耦合来源不得升级为P或不作措辞级结论；STATE-08固定Schema、R11预算硬门槛与Voice opt-in保持不变。
- R49-A至R49-C验证STATE-04 Aesthetic Decision Lock在四个维度各要求排他性选择与被放弃的选项、无取舍的默认做法不构成决定、决定沿STATE-06与STATE-08继承并由Prompt Scorecard Hard Gate审计；四项决定不新增Project Bible竞争区域、平行Schema或STATE-08字段，逐镜参数仍由STATE-06拥有。
- R50-A至R50-B验证STATE-04 Aesthetic Decision Lock经STATE-08 Required Resources与Global Projection Matrix进入Prompt编译、四项决定落到既有`主风格`／`画面描述`／`环境一致性`字段、且不被Delta压缩抹除；不新增任何Prompt字段。
- R51-A至R51-D验证Skill体量预算：超Target未登记、超Ceiling、僵尸台账条目、指向不存在文件的台账条目均使Validator失败；已登记且未超Ceiling的超Target文件通过；`SKILL.md`保持在Entry行数预算内；预算本身不构成新增文件的理由，也不与`rules/resource_loading.md`的运行时读取规则重叠。
- R52-A至R52-D验证维护自检已从模块合同抽取为可独立读取的短卡与判据真源：必读路径不再需要通读超长合同文件；`module_contracts.md`不得重新长出并行检查副本（其自身作为`COMPOSITE`体量债仍在Size Ledger待拆）；`USER_GUIDE.md`为非运行时文件；模型能力数值只由Adapter拥有，知识层不再复述原始窗口。
- R53-A至R53-D验证体量以UTF-8字节而非行数判定、`COMPOSITE`文件必须拆分而`INTEGRAL`文件保留并写明按章节读入口、Ceiling不可被Ledger豁免且已实际执行（132.7 KB回归集被拆为四个文件）、拆分后编号连续且由原文件提供Index、引用方全部更新。
- R54-A至R54-D验证长期体量维护方案的三层可执行：事前不新增无归属文件、不先加后登、新文件不超Target的60%；事中由Validator独立强制字节阈值、类别与Ledger一致性；事后按周期产出体检报告并对过期台账判失败；`COMPOSITE`是待拆队列而非豁免。
- R54-E验证“减”的通道必须被实际评估：`Duplicate Rule Check`除查重复外还要判定是否存在可合并或可退役的既有规则，`Additive By Default`不得被解释成规则总量只增不减。
- LR-R1至LR-R10验证普通Chat不因Windows路径不可读默认要求Work、Skill / Project双source独立、Current Skill压过历史摘要、Legacy STATE向前映射、Intent Backfill只增补、Confirmed `REF-SKETCH`持久、STATE-08从current owner entry重进、Claim Gate诚实、Work只在真实必要时升级，以及普通`下一步`不重复全量恢复。
