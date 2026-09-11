# SD Film Regression Scenarios

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

## R15 Prompt Attention / Translation / Physical Data

三个案例都必须保持`templates/10_video_prompt.md`固定结构，不新增五维字段，不恢复旧七字段G01；内部执行`Director Intent / Literary Intent → Visual Translation → Physical Anchoring → Prompt Compression → Final Clip Prompt`。

### R15-A Literary Camera Intent

输入：`镜头像终于鼓起勇气一样靠近她。`

PASS：保留“逐渐靠近人物内心、克制而迟疑”的情绪功能，并转译为类似`眼平中近景起镜；人物保持原姿态，摄影机在她短暂停顿后沿单一路径缓慢推进至近景；她在靠近过程中轻微垂眼、呼吸变浅，摄影机减速停住，不横移、不环绕，稳定落在双眼焦点`的可见执行语义。具体动作只能使用上游已确认内容；示例不强制垂眼或呼吸变化。

FAIL：只保留原文学句；机械删除文学意图只剩“慢推”；叠加横移、环绕和变焦；没有人物反应、触发、终点或稳定结尾。

### R15-B Over-Engineered Camera Data

输入：`摄影机1.37m高、距离人物2.43m、以0.137m/s推进，焦距53mm。`

PASS：若小数精度没有用户/模型特定依据且不改变可见结果，压缩为`眼平机位，中景起镜，约5秒沿单一路径缓慢推进至中近景，保持人物双眼对焦与稳定轴线；约50mm等效倾向`或等价可执行关系。内部记录这些数字只表达视觉倾向，不承诺严格测量。

FAIL：原样堆叠全部小数并声称模型会精确执行；删除全部摄影信息导致机位/速度/起止景别丢失；把推进、变焦与焦段变化混为一条互相冲突指令。

### R15-C Canonical Assets Free Prompt Attention

输入：当前Clip已有`CHAR-001@v003`正式角色参考与`ENV-002@v002`正式环境参考，二者真实存在、Confirmed/Active并已列入`参考资产：`；本Clip真正变化的是角色从门边走到桌前、摄影机同轴跟随、最后停在角色手放到桌面的稳定状态。

PASS：`人物一致性`与`环境一致性`只保留资产ID/版本、当前状态、不得改变项及本Clip特有风险的最小确认；不复述整段五官、服装、建筑布局与材质。Prompt注意力集中在起点、行走路径、摄影机跟随距离/轴线、手部动作顺序、桌面接触结果与稳定尾帧；Spatial Blocking、REF-TAIL、Two-Tier与Reference Routing继续按既有合同执行。

FAIL：在全局与每个分镜重复长篇角色外貌和环境结构；因资产已锁定而遗漏动作路径、摄影机行为或结束状态；删除Canonical资产引用；把Five-Dimensional Prompt Control Matrix打印成五个最终大字段。

### R15-D Director Style Label Expansion

输入：`岩井俊二式青春电影氛围。`

PASS：最终Prompt可以保留`岩井俊二式青春电影氛围`；该重要标签首次出现时，在同一`主风格`段紧跟其Project-specific Style Meaning与当前Clip必要的3—5个（或更少）高价值carriers，例如本项目将其定义为柔散自然窗光、低饱和灰绿与米白色关系、克制观察式镜头、人物以停顿/呼吸/同步反应/细微眼神变化表达关系。实际选择服从当前Clip事实，不机械复制全部示例，也不自动加入校园、校服、樱花、海边、夏日奔跑或其他未确认青春场景包。名称完全冗余时允许省略，但具象化后不默认删除。

FAIL：只写“岩井俊二式青春电影氛围”；解释仍只是“清透、唯美、克制、青春感”等抽象词；把导演名当作精准复现参数；规定carriers足够后必须删除导演名；机械复制整段风格说明；无依据增加校园/樱花/海边/奔跑；风格描述淹没主体、动作、空间、摄影机或状态承接。

### R15-E Cinematic Live-action Label Expansion

输入：`电影级真人青春短片质感。`

PASS：最终Prompt可以保留`电影级真人青春短片质感`；首次出现时在同一风格段具体解释为当前Clip最需要的3—5项（或更少），例如真实演员自然肤质与皮肤细节、自然曝光关系和真实暗部层次、浅景深、轻微胶片颗粒、受控高光或克制的镜头动态。选择必须与已确认媒介、资产、光源、动作和Generation Budget一致，不把示例整段固化成模板。

FAIL：只保留“电影级 / 真人感 / 青春感”；用“高级、真实、有质感”等同级抽象词循环解释；堆叠8K、ARRI、award winning等器材/质量词；无依据新增商业布光、黑金配色或广告式摆拍；为了填满维度而制造冲突。

### R15-F Stable Project Style Delta

输入：CLIP-001已在Confirmed Visual Direction / Project Bible与Canonical角色、环境资产中锁定`岩井俊二式潮湿夏日青春氛围`的项目特定含义；CLIP-002为直接连续段，只增加窗外雨势变弱、人物关系由回避变为短暂同步反应，其他项目风格不变。

PASS：CLIP-002按`Source Carries State, Prompt Carries Delta`在`主风格`保留标签或已确认风格锚点，只补“雨势变弱后的柔散窗光保持、两人以一次同步抬眼建立关系”等当前delta与风险；不复制CLIP-001的完整光线、综合色彩、肤质、颗粒、镜头和表演说明。同一标签在本Prompt中不重复解释。若正式Style Source不可访问或含义发生变化，则重新展开受影响部分。

FAIL：每个连续Clip完整复制同一长篇Visual Bible；只因是“后续Clip”就在没有正式Style Source时写裸标签；省略当前Clip真实变化的光态、表演或风险；在主风格和每个分镜反复解释同一标签。

### R15-G Action-Heavy Clip Style Compression

输入：一个动作复杂Clip已经需要锁定双人身份、追逃前后关系、单一摄影机路径、道具换手顺序、环境障碍、动作Endpoint与下一Clip Handoff，同时上游还给出多个导演/流派/情绪标签。

PASS：主体、动作、空间、时间顺序、摄影机路径、道具状态与Handoff优先；风格自动压缩到能直接帮助读懂当前Beat的1—3个或更少高价值carriers，例如稳定的冷灰综合色彩、克制手持和足够景深。一个仍有统一锚定价值的重要标签可以保留并用这些carriers简短解释；完全冗余、无关或冲突的其他标签允许省略，但不存在“具象化后默认删除导演名”的硬规则。固定Template字段仍完整，Generation Budget与Five-Dimensional Matrix不变成最终栏目。

FAIL：为保留风格而删减动作步骤、空间方向、道具状态或Endpoint；同时堆叠多个导演、赛博朋克、黑帮感、广告感、胶片感与器材名；要求风格必须占满3—5项；以压缩为由删除Template字段。

### R15-H Positive Specification And Unified Negative Prompt

输入：`岩井俊二式潮湿夏日青春气质；禁止夸张微笑、甜宠式表演、广告摆拍、MV慢动作与炫技运镜。`

PASS：`主风格：`可以保留并展开`岩井俊二式潮湿夏日青春气质`，但以柔散自然窗光、低饱和灰绿/米白、安静观察式摄影、克制含蓄表演、细小停顿/视线/手部动作与简洁自然镜头调度等当前Clip必要的正向carriers执行；不在正文重复原负向清单。只有仍属当前高风险、正向描述难完全锁定的残余错误经过合并压缩后进入末尾唯一`反向提示词：`。

FAIL：在`主风格 / 人物一致性 / 画面描述 / 人物动作与情绪`继续散布“禁止 / 不要 / 避免”清单；把原句完整复制到多个字段；删除风格标签但没有建立执行carriers；末尾反向段与正文同义重复或比动作/空间/镜头正文更长更抢权重。

### R15-I Multi-Shot Single Final Negative Prompt

输入：一个包含三个分镜的Confirmed Clip，三个分镜共享角色一致性、克制表演和空间轴线风险。

PASS：三个分镜正文分别写清当前动作、空间与连续性正向状态，不重复通用负向清单；整个Clip只有一个`反向提示词：`，位于最后一个分镜全部字段之后，并且是当前Clip最终段落，其后无任何备注或正文。

FAIL：每个分镜各写一次反向清单；出现两个或更多`反向提示词：`；反向段出现在分镜之间；末尾反向段之后仍有尾帧说明、音色字段、备注或补充正文。

### R15-J Local Physical Continuity Constraint

输入：某分镜要求`左手始终握住伞柄，不能换手`，且换手会破坏上一镜到下一镜的动作连续性。

PASS：在该分镜的`起始状态 / 人物动作与情绪 / 道具状态 / 镜头结尾状态`中适用位置保留最小、指代清楚的连续性约束，优先写成`左手持续握住伞柄，整个动作链与结尾状态均保持左手持有`；不把它扩展成局部通用负向清单。跨镜通用高风险项仍只在末尾唯一反向段收束。

FAIL：为了统一负向位置而把持伞手约束全部移走，导致具体动作链不清；在每个字段重复“不能换手”；把雨伞约束扩展成长串通用负向词；用反向提示词掩盖上游持有者或左右手事实冲突。

### R15-K Voice Omission Survives Negative Placement Change

输入：角色有对白，用户只要求普通Seedance Clip Prompt，没有明确要求当前视频模型使用声音/音色控制。

PASS：本次正向优先与反向段调整不改变Voice opt-in边界；最终Prompt完全省略`音色特征：`、Voice Profile、Voice/Audio Reference和声音资产状态文字；`反向提示词：`仍为最后字段。

FAIL：为了统一字段位置而重新加入`音色特征：`或占位语；把声音资产状态塞到反向提示词之后；把固定禁BGM句误当作声音身份授权。

### R15-L CLIP-03 State Ownership / Negative Compression

输入：真实回归样本CLIP-03《落下的乐谱与四个单音》。已确认两名角色身份、ENV-02旧音乐教室与唯一横向长琴凳、REF-TAIL-02承接、乐谱视觉资产；Clip内发生“从前态调整为共坐正常坐姿 → 乐谱落地但无人拾取 → 两人交替完成四个独立单音”。用户没有显式要求声音身份控制。上游风格锚点包含`岩井俊二式潮湿夏日青春氛围`。

PASS：

- 先建立Ownership Map：`参考资产`只声明真实Source及用途；`首帧参考`权威定义起始左右/姿态/共用长琴凳与Direct承接；`人物一致性`只保留身份/年龄/发型/服装/比例；`环境一致性`只保留教室结构、唯一长琴凳结构与阴雨光态基线；逐镜只写新增动作、状态变化和局部物理关系；`尾帧限制`权威定义结束坐姿、乐谱状态、四音完成状态与carryover。
- “同一张长琴凳 / 林夏左许栀右 / 乐谱不捡 / 四个单音”各有唯一完整定义；其他位置只在状态变化、首尾接口或局部高风险时写`保持该状态 / 乐谱留在地面 / 完成下一次单音`等最短Delta，不在6—9个字段全文重复。
- 正文把座椅、左右、手部和演奏范围写成正向可执行状态；只保留必须贴近动作链的最小局部物理约束。
- 雨声、风声、窗帘、纸张滑落/落地和四个钢琴单音进入各分镜`音效`；最终完全没有`音色特征：`、Voice Profile、Voice/Audio Reference或声音资产状态文字。
- 最终只有一个末尾`反向提示词：`。固定禁BGM首句之后只保留当前Clip少量高风险类别，例如座椅结构分裂/人物左右互换、人物离座或拾取乐谱、肢体异常、演奏范围自动扩展、身份/环境漂移与夸张表演/摄影偏移；相近错误合并，不逐项复述正向状态。
- 删除猫、吉他、手机、磁带等历史事故物、未来Clip事件和当前未出场资产；反向段不成为事故历史清单，也不压过主体、动作、空间、镜头、时间状态与Handoff。
- `岩井俊二式`标签可保留，并在首次出现的同一`主风格`段给出当前项目可执行解释；Style Label Expansion不因去重失效。
- REF-TAIL继续按A Direct用途存在，Reference Asset Eligibility、Accepted Take Canon与Shot-State Memory不被State Once去重削弱；首帧与尾帧仍足以复算连续性。

FAIL：把唯一长琴凳、左右、乐谱和四音规则在参考用途、首尾帧、人物/环境一致性、每个分镜与反向段全文重复；正文仍散布通用`禁止/不得/不要`清单；用`音色特征：`承载雨风纸张或钢琴声；反向段包含事故历史、未来剧情或与当前Clip无关资产；去重后首帧/尾帧不足以复算A Direct连续性；删除或孤立风格标签而不做Style Label Expansion。

---

## R16 Delta / Budget / Scope / Canon / Authority / Retake

以下案例必须沿用现有STATE-07 Clip Contract、八组Shot-State Memory、Reference Selection / Routing、Execution Ledger、STATE-09 Review与`templates/10_video_prompt.md`固定结构；不得新增主STATE、Clip Registry、平行Project State或最终Prompt字段。

### R16-A Canonical Sources Carry State, Prompt Carries Current Delta

输入：已有Confirmed / Active角色与环境正式资产；当前Clip只发生角色从门边走到桌前、摄影机同轴跟随并停在手触桌面的Endpoint。

PASS：`参考资产`保留正式ID/版本/Primary Role，`人物一致性 / 环境一致性`只作当前状态、风险和不得改变项的最小确认；Prompt主体集中描述行走、摄影机路径、手部接触、时间顺序与稳定Endpoint。模板字段完整但不重复长篇五官、服装、建筑结构与材质。

FAIL：删除正式资产引用；在多个字段重复完整角色/环境设定；因压缩而丢失当前动作、镜头Delta或Endpoint。

### R16-B Generation Budget Allocation

输入：同一候选Clip要求完美身份、复杂奔跑打斗、五人群体、繁忙雨景、环绕运镜、多人对白口型、强FX和变化灯光。

PASS：内部先明确一个Primary Spend（例如双主角身份与核心攻防Beat）、最多一至两个Secondary（例如主空间关系与单一路径跟随），并把群体活动、复杂环绕、非必要口型、额外FX或光色变化写入Economized / Safe Downgrade；Five-Dimensional Matrix只高控制必要未锁定项。若仍超载则返回STATE-07/06拆分。

FAIL：五维全部补满；Primary不唯一；Economized为空；把`Primary Spend / Secondary Spend / Economized`打印成最终Prompt字段。

### R16-C Accepted Take Overrides Planned Transient State

输入：CLIP-03 Planned End为“左手搭手背”，实际Take的Observed End为“右手搭手腕”，用户明确接受该Take；Run、Prompt Revision、Review与接受证据齐全。

PASS：Execution Ledger分别保存Planned与Observed；Accepted Canon State采用“右手搭手腕”。CLIP-04从右手/手腕状态继续，不无过程纠回左手/手背，也不重播接触动作；正式角色/环境/道具资产身份仍不变。

FAIL：未记录Observed；下一Clip强行按原计划恢复左手；把未接受Take写入Canon；因接受动作结果而改变正式资产身份。

### R16-D REF-TAIL Identity Drift Is Not Identity Authority

输入：上一Accepted Take / `REF-TAIL`的脸部略漂移，但Active Character Canonical Reference正确；下一Clip需要继承尾帧姿态、站位与动作阶段。

PASS：角色Canonical Reference声明Identity Authority，`REF-TAIL`声明Transient State Primary Role；下一Clip保持正式角色身份，只从尾帧/Accepted Canon继承姿态、站位、朝向、人物距离与动作阶段，并把脸部漂移列为Continuity Risk。

FAIL：让尾帧覆盖正式脸部身份；完全丢弃尾帧导致站位/动作阶段重置；不写Primary Role / Purpose；把漂移尾帧升级为角色Canonical资产。

### R16-E Single-Variable Retake For Blocking Error

输入：生成结果只有人物站位错误，身份、动作、镜头、光线、道具与其他连续性均正确。

PASS：Review诊断为Spatial / Blocking，选择它为最高影响变量；第一轮只修Affected Clip的空间关系/Blocking与必要相邻边界，保留其他已接受内容；Retake后只比较站位及其边界是否改善。若可后期安全修复则路由Editing并说明范围。

FAIL：整段Prompt全部重写；同时更换角色资产、动作、运镜、光线与道具；没有前后Take比较；以“整体感觉”直接REBUILD。

---

## R17 Voice Identity Opt-In And Prompt Isolation

### R17-A No Voice Request

输入：角色有对白，用户只要求继续主Pipeline或输出当前Seedance Clip Prompt，没有提出音色制作或当前视频声音控制要求。

PASS：不进入AUDIO模块；默认外部已有可用角色音色资源；STATE-02/03/08均不阻塞；视频Prompt完全省略`音色特征：`、Voice Profile、Voice/Audio Reference及“已有/缺失/无需音色”等状态文字。台词只保留准确文本与必要Dialogue Performance。

FAIL：要求补建Voice Profile；创建Not Applicable；返回STATE-03；输出`No Voice Asset`或无对白占位；把音色描述写进视频Prompt。

### R17-B Explicit Voice Design

输入：`为女主设计音色。`

PASS：Router返回`AUDIO / SEED-AUDIO Voice Asset`，从当前项目阶段独立进入音色模块；输出独立Voice Profile和明确标记为“SD Film为Seed Audio 1.0组织的兼容模板”的Prompt。Prompt描述speaker，分离稳定Voice Identity与当前Dialogue Performance，并只按需输出Voice Description、Emotional Tone、Delivery / Prosody、Dialogue、Timing、Ambience、Key Sound Effects、Scene Progression和获授权Reference Audio；不强行并入视频Prompt。

FAIL：继续普通Character Asset；把声音交付塞进STATE-08；冒充官方唯一字段模板；固定要求15秒、八条`No...`声明或无关视觉描述。

### R17-C Confirmed Voice Exists But User Requests Only CLIP-03 Prompt

输入：Active CHAR Version已有Confirmed Voice Profile或Voice Audio Reference；用户只说`输出CLIP-03 Seedance提示词。`

PASS：Confirmed声音资产只作为Source State存在，不投影到CLIP-03视频Prompt；`音色特征：`和Voice/Audio Reference均省略。主流程按STATE-08其他Gate继续。

FAIL：自动复制Voice Profile；写“由参考音色锁定”；仅因已有声音资产就把Reference列入`参考资产：`；把先前AUDIO授权外推到当前请求。

---

## R18 Spatial / Performance / Action PREVIS Minimal Integration

### R18-A Two-Person Dialogue And Bench Axis Continuity

输入：同一教室连续场景，A与B并排坐在唯一横向长凳上，A始终在观众画面左、B在画面右；先给双人建立镜，再做同一轴线侧的正反打。中段导演有意让A起身绕到B另一侧，并要求越轴后继续对话。

PASS：Scene Spatial Snapshot锁定长凳、门、窗、钢琴等Fixed Environment Anchors、A/B起始位置、Eyeline Axis与camera safe side；普通正反打保持相反眼线与同侧机位。A换位时记录`Start Position → Visible Movement Path → End Position`，通过角色镜内明确换位并以固定地标建立新轴线侧，随后屏幕左右翻转被判为合法；Environment Canonical继续锁空间身份，不因人物换位重做环境资产。Shot-State Memory记录换位后的局部状态，A/B/C `REF-TAIL`仍按边界需要选择。

FAIL：下一镜A/B无过程换边；把所有屏幕左右当成场景东/西；只写“创意越轴”而没有可感知过渡；或把合法新轴线一律判错并强迫永不越轴。

### R18-B Restrained Youth Drama Uses Minimal Carriers

输入：4秒青春片反应镜头。角色听见朋友轻声道别，选择不挽留；剧本要求克制，没有崩溃、哭喊或重大揭示。

PASS：路由为Performance-dominant，使用PL1；只选择1—2个载体，例如视线停在对方手上后短暂移开、呼吸停半拍再缓慢恢复，并以手指停止动作或肩膀保持不动作为可选支持。保留“想挽留但压住”的公开状态/局部泄漏与稳定余韵，不强制完整递进链，不自动加入落泪、吞咽、瞳孔变化或大幅后退。

FAIL：机械输出触发—瞳孔—下颌—吞咽—指尖发白—呼吸粗重—失控哭泣的完整链；或仍只写“她悲伤而复杂地看着对方”。

### R18-C A3 Choreographed Action Has Physical Causality

输入：一段经过剧情授权的复杂格挡—转身—反制动作，起始双方站位、主Action Axis、道具状态与最终“攻击者失衡、主角稳定防守架”结果已确认。

PASS：路由为Action-dominant并选择A3；Action PREVIS写清Trigger、Preparation、Weight Shift、Ground / Foot Drive、Hip / Torso Transfer、Limb / Prop Trajectory、Contact / Near-contact、Force Response、Follow-through、Recovery / End State与Next-action Carryover中的必要链节。景别与Coverage让支撑、轨迹、接触和结果可见；结尾把攻击者失衡方向、主角支撑脚/朝向、道具持有与摄影机safe side写入Shot-State Memory，供下一Shot或Accepted Canon继承。

FAIL：只写“主角猛地反击、双方激烈打斗”；接触、受力和结束状态缺失；下一镜双方恢复初始架势；或因为A3自动加入玄幻FX、0.5秒硬撞、机枪式对招和高潮定格。

### R18-D A1 Simple Action Stays Simple And Prompt Stays Clean

输入：角色从桌面拿起一封信，转身看向门口，Clip内没有追逐、对抗、复杂道具、FX或高强度表演。

PASS：路由为Action-dominant或Mixed中的低复杂度动作，选择A1，只写右手从桌边起始、沿短路径握住信封、信封离开桌面并稳定保持在右手、角色转头后视线落向门口的Start / Path / End；不添加完整动力链、精密角度、速度、受力参数或复杂运镜。STATE-08不输出A1、Kinetic Chain、PL等级、Shot Purpose、QA或路由标签，继续按`Source Carries State, Prompt Carries Delta`只保留当前Clip必要Delta。

FAIL：为拿信加入蹬地、腰胯、脊柱传导、空气反馈、接触力数值与多段摄影机；或把内部11环、六阶段和Purpose列表逐项塞进最终Prompt。

---

## R19 Visual Blocking Sketch / Clip Prompt Gate

### R19-A CLIP-04 First Prompt Requires One Confirmed S+P Anchor

输入：CLIP-04中林夏在左、许栀在右，共坐同一张长琴凳，共同面向钢琴 / 窗外；许栀仅允许`Gaze + LIMITED Head`，Position / Torso / Shoulder / Distance锁定；林夏持续弹琴且不转头。用户首次请求`输出CLIP-04提示词`或只说`下一个`。

PASS：STATE-07已记录Visual Blocking Risk Pre-Assessment；STATE-08 Final Assessment判`HIGH / REQUIRED`，本轮先生成中性S+P综合草图，核对role mapping、林夏左 / 许栀右、Side-by-side、Same Bench、Shared Facing、许栀Gaze→林夏、`Head LIMITED`、Pose Hierarchy、Eyeline Axis与Camera Safe Side。林夏与许栀必须使用同一套无性别技术人偶，只靠蓝 / 红角色标签、姓名和左右位置区分，不以长发 / 短发、裙装 / 裤装或身体曲线区分。通过后注册`REF-SKETCH-04｜CLIP-04空间与姿态调度草图`，说明`草图人物为无性别调度人偶，仅用于空间 / 姿态 / 机位关系，不作为人物外观参考。`加入当前Clip参考资产并更新预算，本轮不输出Prompt。用户下一次继续且Signature未变时才输出Prompt。即使A/B左右未换，Side-by-side漂成Face-to-face仍判Blocking Drift。

FAIL：第一次请求直接输出Prompt；生成草图后未验证或未列入参考资产；把草图当角色 / 环境Canonical；用性别、发型、服装或体型区分林夏 / 许栀；让“许栀看林夏”自动导致全身转向；或认为左右没交换所以Face-to-face不算漂移。

### R19-B Prompt Rewrite Reuses Anchor; Blocking Reconstruction Reassesses

输入：CLIP-04已经有Confirmed `REF-SKETCH-04`。用户连续多次要求压缩措辞、优化主风格、整理反向提示词、调整台词 / 音效，Blocking不变；随后大幅重构为许栀起身走到林夏面前。

PASS：普通改写每次只比较Current Revision与Blocking Signature，结果为KEEP并复用同一草图 / 图片位，不重复生成。起身、移动到面前使Same Bench、Position、Topology、Distance、Movement Path与Clip End Blocking实质变化，触发Reassessment并得到`REPLACE with REF-SKETCH-04-v2`或`RETIRE + CREATE`；新草图重新验证后才输出重构Prompt。

FAIL：每次措辞优化都重新出图；Prompt改写导致草图版本自身漂移；或大幅Blocking重构仍盲用旧图且不重新评估。

### R19-C Simple Single Person Is NONE

输入：单人原地站立，只做普通转头；固定机位，无共享空间结构、换位、复杂道具、跨轴、复杂前中后景或A2/A3动作。

PASS：每Clip检查仍执行，但Final Assessment=`NONE`；不生成、不预留`REF-SKETCH`，直接编译Prompt。

FAIL：为了流程统一强制生成P-SKETCH或Formal Keyframe。

### R19-D A3 Action May Use A-SKETCH Or Combined Anchor

输入：A3复杂格挡—转身—反制动作，双方起点、主Action Axis、道具、接触 / 近接触、受力方向、恢复终点与Next-action Carryover已确认，但单纯文字仍存在路径 / 接触漂移风险。

PASS：Final Assessment可判`ACTION HIGH / REQUIRED`，选择A-SKETCH或S+P+A综合草图；双方使用同一套无性别技术人偶，以箭头、轴线、接触点和受力方向锁定Start / Path / Contact / Force / End / Carryover。只有动作可达性必需的身体比例可以表达，仍不恢复性别、脸、发型、服装或角色体型身份。通过Sketch Validation与Character Appearance Leakage Check后作为受限Visual Blocking Anchor进入参考资产。角色、环境与道具身份继续由各自Canonical资产控制；Prompt正文只保留当前动作Delta与必要局部约束。

FAIL：A3一律强制多张正式Keyframe；草图带入写实五官、正式服装 / 灯光 / 画风并覆盖Canonical；或把全部动力链和草图标注复制进Prompt。

---

## R20 REF-SKETCH-MASTER Presentation Authority

### R20-A Piano Pair Uses Technical Blocking Sheet Language

输入：CLIP-04仍为林夏左 / 许栀右、Side-by-side、Shared Facing、Same Bench，许栀只有`Gaze + LIMITED Head` Delta；`REF-SKETCH-MASTER`注册为真实可读视觉输入，示例图本身也包含两女与钢琴内容。

PASS：Final=`REQUIRED`时把母版只作为Sketch Presentation Authority输入，当前Blocking Signature作为内容权威。输出是自适应Technical Director Blocking Sheet，Main Blocking、Spatial / Top-down、Camera Information、Permission与Usage区能直接证明林夏左 / 许栀右、Side-by-side、Shared Facing、Same Bench、许栀Gaze→林夏和`Head LIMITED`；两人使用同一套无性别人偶，只由蓝 / 红角色标签、姓名与位置区分，不继承母版或Character Asset中的性别、发型、服装、体型。当前`REF-SKETCH-04`通过验证后进入视频参考资产；母版本身不进入。

FAIL：提示词核心仍是唯美铅笔Storyboard、雨天青春电影或人物插画；以长发 / 短发、裙装、脸或身体曲线区分两人；缺少Topology / Facing / Gaze / Camera证明；或因为案例内容与母版相似就把母版本身当当前Clip Blocking Authority。

### R20-B Three People Around A Table Has No Template Content Leakage

输入：Current Clip是A / B / C三人围圆桌交谈，环境为干燥会议室，无钢琴、长琴凳、窗边雨景或乐谱；需要锁定三人座位、共同视线中心、Camera Safe Side和发言者局部转头。

PASS：继承母版的信息层级和技术标注语言，但Main Blocking与Top-down重新布局为三人环桌Topology；三人使用同一套无性别技术人偶，只靠A / B / C角色标签、技术颜色和座位位置区分；角色数量、位置、环境锚点和Camera完全来自Current Clip。Template Content Leakage Check确认没有两女、钢琴、琴凳、窗户、乐谱、雨景、母版文字、示例发型 / 服装或示例光色；Character Appearance Leakage Check确认没有任何身份化外观。

FAIL：复制两个人物、钢琴 / 琴凳、窗户、乐谱、雨线、黑板文字或示例人物造型；用三种发型、服装、性别或体型区分A / B / C；为贴合母版把三人删成两人；或像素级复刻版式导致三人关系不可读。

### R20-C A3 Action Remains Technical Previs

输入：A3武打Clip需要A-SKETCH或S+P+A；Current Clip已确认双方起点、Action Axis、道具路径、接触 / 近接触、受力方向、恢复终点与Next-action Carryover。

PASS：母版只提供Technical Director Blocking Sheet表达，双方使用同一套无性别技术人偶，以Start / Path / Contact / Force / End箭头、轴线、Camera side与动作Permission完成技术预演；布局可为动作路径重新分区，必要身体比例只表达可达性 / 接触 / 受力约束。没有性别化体态、角色外貌重绘、高燃海报、能量爆炸、姿势美术定稿、电影光效或无依据FX；Canonical角色 / 环境 / 道具身份不受影响。

FAIL：生成高燃概念插画、武打海报或动作Key Art；根据Character Asset恢复双方脸、发型、服装、性别或体型身份；用母版的静态双人并排版式压扁动作路径；或把技术颜色标记当最终服装 / 光色设计。

### R20-D Simple Head Turn Still Returns NONE

输入：单人固定位置、固定机位，只做普通转头；母版文件已经注册且可读。

PASS：母版可用性不改变Assessment；Final=`NONE`，不调用母版、不生成 / 预留`REF-SKETCH`，直接进入Prompt编译。

FAIL：因为母版已安装就强制生成P-SKETCH、把母版列入视频参考资产或占用图片预算。

### R20-E Prompt Rewrite Reuses Current Sketch Without Recalling Master

输入：当前Clip已有经母版辅助生成并确认的`REF-SKETCH-04`，Blocking Signature不变；用户只要求压缩措辞、调整主风格或整理反向提示词。

PASS：结果为KEEP，复用现有`REF-SKETCH-04`与同一图片位，不重新调用母版、不重新生成草图；最终视频`参考资产：`只列当前草图及其他实际视频输入，不列`REF-SKETCH-MASTER`。只有Blocking-affecting Revision才执行KEEP / REPLACE / RETIRE / CREATE，REPLACE / CREATE时才重新按注册状态使用母版或Text Contract Fallback。

FAIL：每次Prompt Rewrite都重新读取母版并生成新草图；母版成为持续视频参考；或Blocking重构后仍盲用旧草图。

### R20-F Character Appearance Leakage Is A Hard Failure

输入：候选S-SKETCH / P-SKETCH / A-SKETCH版式、标签、箭头、Camera和Blocking均正确，但任一人物出现写实五官、具体长短发、具体服装设计、明显胸腰臀性别体态、年龄 / 美貌 / 气质身份，或根据Character Asset重画外观。

PASS：实际视觉检查把`character_appearance_leakage`记录为`true`或无法确认`neutral_mannequin_representation=true`；`scripts/validate_sd_film.py sketch`固定返回`FAIL = Character Appearance Leakage / Identity Contamination`。候选保持`FAILED / REVISE`并沿同一Technical Visual Blocking Sketch route重做，不注册Confirmed、不进入Clip参考资产，也不通过修改Character Asset或Blocking事实迁就草图。

FAIL：因为版式与Blocking正确就忽略人物外观泄漏；用“只是代理”解释后仍注册；或把中性人偶QA扩写进最终Seedance Prompt的反向提示词。

---

## R21 Performance Arc / Emotion Preflight

### R21-A Restrained Character Changes Across Shots Without Extra Coverage

输入：同一Scene有三个已确认SHOT。角色先冷静检查异常，第二镜确认目标，第三镜完成处理并恢复克制；剧情、SHOT数量、机位、时长和动作结果均已锁定，不允许加镜头。

PASS：STATE-06建立同一角色的Performance Arc Map：Inherited Baseline为专业冷静；第一镜通过视线先移、一次短暂停眼或呼吸变浅表现疑惑；第二镜在确认刺激后眼神稳定、下颌或手部张力略增并选择行动；第三镜动作完成后先复核结果、缓慢释放肩颈/呼吸，再回到新的受控Settled State。每镜只承载当前可见段，`Previous Settled State = Current Inherited Baseline`，STATE-07/08 Performance / Emotion Check为PASS，最终只写入既有`人物动作 / 人物动作与情绪 / 镜头结尾状态 / Performance State`语义，不新增SHOT、Clip、STATE或Template字段。

FAIL：三镜都只写“角色始终冷静从容”；每镜从默认脸重新开始；为了补情绪增加无必要特写/反应镜；或在STATE-08用“更有情绪、更生动”形容词替代上游表演链。

### R21-B Ensemble Uses Relative Amplitude And Reaction Order

输入：同一Clip含克制处理者、受惊逃跑者、刚解除痛苦的委托者与旁观者。剧情要求处理者始终最克制，受惊者最外放；委托者只在确认危险解除后放松，旁观者延迟反应。

PASS：每个Beat只有一个清楚Primary Performer；受惊者可使用Open / Heightened并承担大幅逃跑，处理者用PL1/PL2眼神、呼吸或动作后停顿承接，委托者从谨慎倾听到确认安静再肩膀放松，旁观者作为Listener / Background Holder先保持低幅、收到共享刺激后才升级。视觉重点交接由刺激、视线或动作结果触发，四个角色各有不同Arc Endpoint和Next-shot Carryover。

FAIL：所有人同时瞪眼、张嘴、后退；所有人都用同一`紧张→放松`模板；为保持主角“高冷”让处理者完全无注意/呼吸/停顿变化；或让背景人物无刺激抢走视觉重点。

### R21-C Intentional Hold Is Active, Not Frozen

输入：4秒近景中角色必须保持面无表情以隐藏真实反应，只听完一句关键信息，不说话、不移动位置。

PASS：表演被定义为Intentional Hold：视线先停在说话者、关键字后眨眼短暂停止或呼吸轻微受抑，手部原动作停住，延迟一拍后恢复控制但视线未完全放松；Post-action Residue进入镜头结尾。动作/口型容量没有被无关微表情堆满。

FAIL：只写“全程面无表情”；或为了避免面瘫同时加入挑眉、瞪眼、吞咽、握拳、后退、落泪和转身。

---

## R22 Screenplay Creation / Existing Script Dual Entry

### R22-A Idea Enters Screenplay Generation

输入：`调用sd，写一个雨夜双女主重逢短片。`

PASS：STATE-00登记`Creation Brief`，STATE-01进入Director-first Screenplay Development；不要求先提供完整剧本，不对尚不存在的文本输出Optimization Opportunity Report。Proposal具有视觉动作、关系变化、信息层次、表演机会、空间潜力与AIGC Directability，并在用户确认Gate停止。

FAIL：把创意归为Existing Class C后要求先批准改编；要求去普通Chat写完剧本；或直接进入Shot Design。

### R22-B Uploaded Script Enters Diagnosis Without Rewrite

输入：用户上传完整剧本并说`调用sd`，没有允许修改。

PASS：登记`Existing Script / Material + Class A/B`，先输出Optimization Opportunity Report并等待决定；没有改写正文或误进Creation Brief。

FAIL：从零重写、静默优化、跳过诊断，或因题材像创意而误走Creation。

### R22-C Explicit Direct Optimization Does Not Re-ask Authorization

输入：`调用sd，直接优化这个剧本；保持世界观、人物身份和结局。`

PASS：先完成诊断和Opportunity证据，再在同一轮按明确授权进入适用Optimization / Adaptation路径；不重复询问“是否优化”。Production Script Proposal输出后仍等待最终确认。

FAIL：省略诊断证据、重复请求同一改写授权，或把改写授权误当最终Proposal确认。

### R22-D Confirmed Screenplay Advances Without Regeneration

输入：Creation或Existing分支的当前Proposal已被用户明确确认并记录`Script Status: Production-Locked`，用户随后说`下一步`。

PASS：STATE-01 Completion Gate通过后进入STATE-02 Asset Discovery；不重复生成剧本，不停回Proposal Gate。

FAIL：重新写剧本、重新做Opportunity Report，或跳过STATE-02进入资产制作/Shot。

### R22-E Scene Revision Stays In Script Development

输入：当前`Script Status: Optimized Proposal`，用户说`修改这一场：让她不要直接表白。`

PASS：保持STATE-01 IN_PROGRESS，只修指定场与必要相邻因果，重跑受影响Scene Director Intent与Directable Screenplay QA，再次等待Proposal确认。

FAIL：进入STATE-05/06、重写全稿、把`下一步`当确认，或保留旧Proposal为Production-Locked。

### R22-F Director-first But Not Pre-shot

输入：从零生成一支情感短片剧本。

PASS：剧本通过Scene Purpose、Audience Experience、Character Objective / Conflict、Relationship Change、Visual Action、Performance Opportunity、Spatial Dramaturgy、Information Strategy、Rhythm Curve与AIGC Directability十项内部QA；最终文本是可独立阅读的剧本，没有35mm、特写、推镜、摇镜、机位、SHOT / CLIP或分镜表字段。

FAIL：只写说明性对白和内心独白；把十项QA机械输出成剧本正文；或在STATE-01预先锁定摄影机。

### R22-G Existing Diagnosis Regression

输入：Class B初稿，无明确改写授权。

PASS：原有A/B/C分级、十二项Optimization Opportunity Report、User Decision Gate、No Revision、Optimization Rejected、Adaptation Draft与第二次Proposal确认全部仍可用。

FAIL：因新增Creation route而自动改写Existing Script，或取消既有保护Gate。

### R22-H Downstream Isolation Regression

输入：运行Skill静态与定向回归。

PASS：主Pipeline仍只有STATE-00至STATE-09；Storyboard仍Optional/Auxiliary；Voice仍Explicit-only；视频Prompt仍永久禁配乐；REF-SKETCH、Prompt Compiler、STATE-02至09及四种Script Status保持原合同。Director Intent从STATE-00/01开始，Scene Director Intent经STATE-05投影、在STATE-06具体化为Director Decision Notes、在STATE-07/08消费，但不成为最终Prompt字段。

FAIL：新增主STATE、让Storyboard进入主路由、自动触发Voice/Music、改变STATE-08 Schema，或让内部Director Intent污染剧本/Prompt。

---

## R23 Director Module / Camera Language End-to-End

### R23-A Script — Rainy-night Two-woman Reunion

输入：`调用sd，写一个雨夜双女主重逢短片。`

PASS：STATE-00建立最小Project Director Baseline；STATE-01仍走Creation Brief → Idea-to-Screenplay，形成Audience Experience、Information Strategy、Visual Action、Performance Opportunity、Spatial Potential、Rhythm与camera-language opportunity。剧本可以写“先让观众看到她没有回头，随后才意识到另一人一直看她”等可镜头化信息顺序，但最终仍是可独立阅读的剧本，不出现Shot List、35mm、特写、低机位、推拉摇移、SHOT或CLIP字段。

FAIL：只记录平台/画幅；没有观众体验或信息策略；或在剧本阶段直接生成镜头表和摄影参数。

### R23-B Visual Development — Distance, Approach, Restraint

输入：同一双人关系弧为“疏远→靠近→再次克制”。

PASS：STATE-04形成Visual Dramaturgy / Mise-en-scène与Visual Arc：负空间、共享空间、前中后景、人物距离、对比/色光和环境压力先分离、再接近、最后重新保留克制边界；各变化有剧情/空间/真实光源依据。输出投影到现有Project Bible字段。

FAIL：只写“全片低饱和冷色电影感”、每场相同色调，或提前锁定每个Shot的焦段和运镜。

### R23-C Scene Breakdown — 40-second Two-person Scene

输入：40秒双人场景，含重逢、回避、怀疑、确认与再次克制。

PASS：STATE-05按Dramatic / Relationship / Information / Performance Beat拆解，建立Dramatic Geography、Spatial Evolution、Reveal / Withhold timing与Beat-to-beat rhythm；形成“先观察并隐藏反应→信息泄漏时保持→确认后才允许靠近→结尾压住”的Scene Camera Strategy。没有创建SHOT / CLIP或具体镜头参数。

FAIL：按台词句数机械拆段；只列地点和人物；或把Scene Camera Strategy写成85mm、特写、慢推清单。

### R23-D Shot Design — Glance Beat Is Derived, Not Decorated

输入：同一个“偷看”Beat；人物A保持向前，人物B只以一次视线偏移泄漏在意，A尚未确认。

PASS：STATE-06按`Shot Purpose → Audience Attention → POV / Audience Position → Relationship & Blocking → Composition Strategy → Shot Size → Lens → Camera Position → Camera Movement → Duration / Hold → Cut Motivation`推导。构图先保护共同朝前与A未察觉，B的眼神成为第二注意目标；Camera在泄漏前保持固定，是否在Beat后运动取决于确认/压力功能，并具有Trigger / Stop。可回答删除本Shot后观众会失去“B先泄漏而A未知”的信息差。

FAIL：无论Blocking与信息时序都默认“85mm特写+慢推+浅景深”，或先选技术再补理由。

### R23-E Clip Production — Suspicion To Confirmation Stays Intact

输入：两个相邻Shots共同完成“怀疑→证据→确认”，单独生成会破坏反应积累，合计时长与复杂度仍在4—15秒内。

PASS：STATE-07把它们作为一个Dramatic Execution Unit，保留Start→End dramatic delta、critical performance / blocking、information timing、Camera Continuity / Visual Rhythm与稳定Endpoint；不因技术便利拆开。若合并导致互斥时空、状态重置或模型过载，则返回拆分而不是强行合并。

FAIL：一Shot一Clip机械拆分，或为了情绪连续把超时/过载/跨世界内容强塞进同一Clip。

### R23-F Prompt — Piano Pair Director Intent Preservation

输入：现有双女主钢琴类Clip；两人同坐一张长琴凳、共同朝前，只有一人短暂gaze-only泄漏，另一人延迟反应，信息不能提前确认。

PASS：最终Prompt继续严格使用`templates/10_video_prompt.md`原Schema；先锁共同朝前和关系距离，再以动作顺序、活动幅度、焦点/遮挡建立First Look / Second Look；包含gaze-only leakage、Hold / Pause / Delayed Reaction、Composition Function、Camera Movement Trigger或有理由Static、Information Delay与稳定余韵。遵守Source Carries State, Prompt Carries Delta，不显著变长，不输出Director理论、Packet、dominance、BUILD/HOLD/PEAK/RELEASE、PL等级或未调用Voice Profile。

FAIL：两人同时转头互看、每镜慢推+浅景深、提前确认关系、长篇解释“为什么这样拍”、改变模板字段，或出现`音色特征：`/Voice资产状态。

### R23-G Action Case — Action-dominant Wuxia Clip

输入：武侠格挡—转身—反制Clip，双方起点、Action Axis、武器路径、接触/受力和恢复状态已确认。

PASS：选择Action-dominant + Action PREVIS A3；Camera Language优先脚下支撑、武器/身体轨迹、接触点、力线、受力结果、屏幕方向与空间可读性，复杂运镜在动作负荷前降级。表演只保留影响动作选择或结果的最小信息，不用青春微表演逻辑压制动作。

FAIL：为了情绪特写切碎动作因果，遮挡接触点、越轴、双方并排合影，或把完整微表情链与复杂Camera同时拉满。

### R23-H Review — Technically Correct, Dramatically Early

输入：实际结果身份、道具、Blocking和技术连续性全部正确，但人物在设计的延迟揭示前已经看向对方并暴露确认情绪。

PASS：Technical Review通过相应项，Director's Cut Review判Information Timing / Performance Truth失败；绝不Disposition=`KEEP`。现有素材能通过切点、顺序、Reaction Priority或声音连接恢复时选择`RE-EDIT`；模型没有生成合法延迟表演且上游设计正确时`REGENERATE`；上游导演/Prompt意图本身提前暴露时`REDIRECT`。同时标记Failure Origin，不把所有情况都当生成瑕疵。

FAIL：因技术连续性正确而PASS / KEEP，或不区分generation failure与directing failure。

### R23-I Runtime — Continue Is Not Reload

输入：当前Workflow与Project Context已验证，用户只说`下一步`或`继续`。

PASS：沿当前Checkpoint继续一个合法步骤，按需读取当前Workflow与Director Intent投影；不触发全量Runtime Reload，不清空Packet、Confirmed Assets、Accepted Take Canon或Shot-State Memory。明确`重新调用sd / 按当前Skill继续`时才按既有Reload / Re-entry合同重读当前版本。

FAIL：普通继续每次全量reload、重建导演Packet、重新生成剧本/分镜，或跳过当前确认Gate。

### R23-J Camera Language — Three Shots Have Three Functions

输入：同一场戏需要三个Shot依次完成空间建立、信息隐藏/泄漏、关系确认后的压住/释放。

PASS：三个Camera Language Decision分别承担建立、隐藏/泄漏、确认后的压住或释放；景别、构图、机位、距离、运镜/Static和Hold / Cut由功能差异推导。可刻意重复同一摄影逻辑，但必须说明如何累积信息/关系；不得为了多样随机堆运动。

FAIL：三镜都无理由“慢推+浅景深”，或三镜为了不同而随机环绕、升降、甩镜并破坏轴线/表演。

### R23-K Cross-stage Director Consumption — FX, Sequence, Clip And Prompt

输入：一个项目具有已确认Scene Director Intent；其中包含需遮挡Reveal并留下后果的FX、需要跨Scene组织Coverage的Sequence，以及覆盖多个SHOT的Execution Clip。

PASS：STATE-03 FX从当前Director Intent只读取视觉重点、遮挡/Reveal与后果呈现功能，不创建Camera或剧情；条件性Sequence Planning只消费已确认Scene Director Intent、Information Presentation与Rhythm Intent来组织BEAT / COV / UNIT，不创建SHOT或Camera参数；STATE-07将匹配的Director Decision Notes投影为Clip Dramatic Function、关键表演/Blocking、节奏与信息时机；STATE-08在编译前核验当前Clip Director Intent / Notes一致，并只把1—3项已确认导演优先级交给Projection。任一缺失或冲突均返回最小事实owner。

FAIL：FX或Sequence绕过导演呈现约束自行创造镜头/剧情；STATE-07只写笼统“保持导演意图”而不形成Clip投影；或STATE-08仅凭旧Prompt、Adapter或模型偏好重写导演方向。

### R23-L Multi-stage Clip — Observation Hierarchy Is Not Flat Follow

输入：一个Seedance 2.5、20秒的Clip依次承载相遇、共同完成小动作、关系靠近、信息确认与余韵；草案要求“同一台摄影机自然跟随、保持前进方向”，所有阶段都是平视中景和轻微推进，但没有连续长镜的叙事理由。

PASS：STATE-06对不同Shot Purpose / Audience Attention / 关系与信息阶段执行Adjacent Observation Contrast；STATE-07 Long-duration Preflight与Clip Movement Plan记录阶段间的观察层次，或明确连续长镜理由、受保护注意力对象、解除条件与稳定终点。若无法成立，返回STATE-07拆分Clip或使用有动机剪辑；STATE-08仅把已确认层次转为既有字段语义，不输出内部标签；STATE-09能区分“Clip Plan缺设计”与“Plan正确但Prompt / 生成压平”。

FAIL：为了避免单调随机堆叠越轴、环绕、升降、甩镜或强制每镜不同；或把多阶段内容默认写成同一平视跟拍、同一路径前进和无触发的轻微推进。

### R23-M Visual Grammar — Baseline Holds, Scene Delta Serves Drama

输入：一个项目已确认克制、潮湿、低对比的海边小镇视觉世界；同一角色分别进入“等待的站台”“共同生活的厨房”“关系确认的海堤”。草案把三场都写成相同灰蓝色、同一平视中景与同一路径跟随；另一草案为了变化无依据加入红色霓虹与舞台顶光。

PASS：STATE-04先建立不含逐Shot参数的Visual Grammar Baseline，明确可用色谱、强调色的出现条件、真实光源、材质/空间气质和摄影机介入倾向；STATE-05为每场标记空间的戏剧功能与有事实依据的Scene Delta；STATE-06再把当前主信息与关系转成镜头选择；STATE-09既能拒绝把统一机械拍成相同，也能拒绝为变化而破坏Baseline。STATE-08只继承已锁定Baseline与当前delta，不增加最终Prompt Schema。

FAIL：把某位导演、某种题材或“低饱和”固化为所有项目的默认审美；让颜色只因好看出现、改写资产固有色或虚构光源；或在STATE-04以Visual Grammar名义预写逐Shot焦段、机位与运镜。

### R23-N Project Color Reference — Conditional Model Input, Never Asset Authority

输入：用户提供一张可访问的海边小镇色卡，并确认它用于本项目的综合色彩基线；夜景Clip存在暖色强调比重漂移风险，角色、环境、道具与首尾帧均已有更高优先级的Canonical参考。

PASS：STATE-04把色卡作为`Project Color Reference`记录在既有Color System，不注册为CHAR / ENV / PROP / FX或Canonical Asset；STATE-07仅因当前光色漂移风险选入并计入Reference Budget；STATE-08在既有模型参考字段写真实来源、唯一Primary Role与“仅控制综合色相 / 明度 / 饱和度 / 强调色占比”。角色、环境、道具、构图、光源、镜头与最终画风继续服从其原owner。无真实色卡、未确认色卡、没有当前风险或有更具体场景状态参考时，色卡不进入模型输入，只有文字Color System继续生效。

FAIL：把色卡当人物、环境、道具或最终画风资产；让它覆盖Canonical外观/结构、虚构光源、强制每个Clip投喂，或对仅有Hex/文字需求伪造图片输入与确认状态。

---

## R24 Screenwriter Module / Writer Intelligence End-to-End

### R24-A Idea — Rainy-night Two-woman Reunion

输入：`调用sd，写一个雨夜双女主重逢短片。`

PASS：Creation Brief进入Screenwriter Module，先以最小充分方式建立双方Want / Objective / Hidden Objective、阻力、关系弧、Dramatic Question、Information Architecture和Setup / Payoff，再生成Production Script Proposal与Writer → Director Handoff；剧本不出现焦段、机位、运镜、SHOT / CLIP或Shot Count。

FAIL：只按氛围生成对白；先写35mm / 特写 / 慢推；或强制用户填写完整WRITER INTENT PACKET。

### R24-B Existing Script — Diagnose Before Rewrite

输入：用户上传完整剧本，没有授权改写。

PASS：先诊断causality、motivation、scene necessity / value change、Writer Beat progression、conflict / stakes、subtext、setup / payoff、information architecture、character / relationship arc与ending payoff，并映射到现有Opportunity Report；停在User Decision Gate，不改正文。

FAIL：自动重写、只做导演镜头分析、跳过Writer Diagnosis或把`下一步`当改写授权。

### R24-C Motivation — Convenience Action Rejected

输入：人物没有前因地“突然坐到对方身边”。

PASS：追溯并要求`Trigger → Character Interpretation → Desire / Intention → Decision → Action → Consequence → New State`；缺任一使动作不成立的核心环节时标记motivation / causality问题，不直接接受剧情便利动作。

FAIL：因为后续剧情需要就保留，或用Camera / 表情装饰掩盖缺失动机。

### R24-D Dialogue — Subtext Opportunity, Not Mechanical Deletion

输入：角色说`我一直很想你`，但既定性格与当场目标不支持直说。

PASS：检查`Dialogue → Surface Meaning → Subtext → Hidden Objective`，指出可通过试探、回避、动作、沉默或道具承载的机会；只在角色与场景逻辑要求时改写，并保留对白可能性。

FAIL：机械删掉所有直白对白，或不检查角色目标就把台词当合格信息说明。

### R24-E Scene — No State Change

输入：一场戏从头到尾没有Information / Relationship / Decision / Power / Emotional / Expectation变化，也无不可替代Setup / Hold / Transition功能。

PASS：标记`weak / replaceable scene`，说明缺失的Value Change并路由到Writer Diagnosis；不靠增加漂亮镜头伪装场景价值。

FAIL：只因场景有气氛或对白就保留，或强制每场必须正负价值翻转而不允许必要Breath / Setup。

### R24-F Setup / Payoff — Timing Survives Production

输入：前场Planted Detail在后场形成Payoff。

PASS：Writer Packet记录Setup / Payoff obligation与信息时机；Scene / Clip / Prompt / Editing保持它，既不遗漏也不提前暴露；Review可追溯到具体义务。

FAIL：Clip边界切断回收、Prompt提前展示真相、Editing交换顺序，或后场重新发明无来源Payoff。

### R24-G Writer Beat Is Not Shot

输入：一个“认出旋律”的Writer Beat。

PASS：Writer只定义Trigger、Interpretation、Decision / Response与New State；Director可用一个Shot、多个Shot或与相邻Beat同处一个长镜头表达，依据观众体验、表演、空间与可执行性决定。

FAIL：Writer强制Shot Count / 特写，或Shot Design无法追溯到Writer Beat / 合法Director Purpose。

### R24-H Prompt — Preserve Both Authorities

输入：已确认Writer Intent与Director Decision的关系场景进入STATE-08。

PASS：最终Prompt保留角色意图、潜台词、Beat order、Setup / Payoff、Information timing与Relationship Delta；Camera仍只来自Director Decision。固定STATE-08 Schema不变，Writer Packet及内部标签不输出。

FAIL：潜台词被压扁成直白台词/表情，Beat顺序改变，Writer越权生成镜头参数，或Director Camera被Writer规则覆盖。

### R24-I Review — Unmotivated Behavior Is Writing Failure

输入：技术画面正确、导演呈现合理，但人物行为没有动机。

PASS：Story Review判`WRITING FAILURE`并返回STATE-01 Screenwriter Module；不判Prompt / Generation failure，不要求只重写Prompt。

FAIL：因画面和导演层通过而KEEP，或把缺失动机路由到STATE-08。

### R24-J Genre — No Universal Conflict Formula

输入：分别运行动作片、商业短剧与青春文艺片案例。

PASS：动作片优先物理目标/阻力与动作因果；商业短剧可按已识别目标加载可选hook / escalation adapter；青春文艺片允许克制、信息不对称与关系压力。三者不共享强制冲突密度、对白密度、固定Beat数或三幕百分比。

FAIL：全局套用短剧爽点、固定15 Beat、强制每场反转，或用青春微表演规则压制动作可读性。

### R24-K Runtime — Continue / Reload / Re-entry Preserved

输入：已验证Project Context后分别说`下一步`、`继续`与`重新调用sd / 按当前Skill继续`。

PASS：普通继续沿合法Checkpoint推进且保留Writer / Director Packet、Confirmed Assets、Accepted Take Canon与Shot-State Memory；显式Reload按现有合同重读Skill Version / Build ID和owner，不重建已确认剧本。

FAIL：新增STATE、普通继续触发全量重载、丢失Writer Packet、跳过确认Gate，或显式Reload沿用旧owner定义。

---

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

## R27 Clip Execution Mode Acceptance

### R27-A Unmotivated Camera Jump Fails

输入：两个相邻Shot被标记为`多Shot有动机剪辑`，但只有“切到近景”或无动机机位跳变，没有叙事功能、切点、视觉媒介或切后重建。

PASS：STATE-07 Clip Preflight判`FAIL`，不得把随机跳变包装成导演剪辑；返回拆分或补齐上游Director Decision。

FAIL：仅因总时长合格就把两个Shot合进同一Clip。

### R27-B Mid-Take Axis Change Fails

输入：`多Shot连续生成`在无可感知越轴过程、角色换位或隔离镜头的情况下中途换轴。

PASS：连续生成判`FAIL`；维持同一轴线，或改为已确认的有动机剪辑并在新机位稳定重建。

FAIL：把“连续长镜头”当作可任意跳转摄影机的许可。

### R27-C Ear-Mirror Match Cut Passes

输入：现实中角色举起耳镜；耳镜玉光占满画面，作为明确切点与视觉媒介；切后在玉境中重新建立角色、环境、道具、摄影机与稳定构图。耳镜玉光和抬手是保留锚点，世界与机位是允许改变锚点。

PASS：Director确认“揭示耳中玉境”的叙事功能后，可标为`多Shot有动机剪辑`；既有`起始状态 / 画面描述 / 镜头结尾状态`承载切前、切点和切后信息，不新增STATE或STATE-08字段。

FAIL：没有玉光遮幅、切前结束或切后稳定构图就直接换到玉境。

### R27-D Incomplete Motivated Cut Fails

输入：Clip声明`多Shot有动机剪辑`，但缺少切点/视觉媒介，或切后没有新世界、角色、环境、道具、摄影机与稳定构图的重建状态。

PASS：Validator与Clip Preflight失败，并要求补齐既有生成合同内的切镜合同。

FAIL：以“导演意图”或“有电影感”代替可执行切镜信息。

### R27-E Capacity Downgrade Returns STATE-07

输入：一个已具备有动机切镜合同的Clip同时要求高身份保真、复杂多角色动作、口型、FX、世界切换和摄影机重建，模型容量不支持。

PASS：不编译STATE-08，`Return Route = STATE-07 / 拆分Clip`；保留已确认剧情与导演意图，在多个Clip中重建边界。

FAIL：继续生成、删除必要故事信息，或用无原因跳变掩盖容量不足。

---

## R28 Seedance 2.5 Compatibility Regression

Compatibility marker: R20-D A3 Action Remains Technical Previs is not a distinct execution rule; its technical-previs coverage belongs to R20-C, while R20-D remains the simple-head-turn case.

### R28-1 Seedance 2.0 Default Short Clip

输入：当前批次锁定`Seedance 2.0`，未选择其他模式。

PASS：仅一次Lock后使用4—15秒Standard Clip、≤9图片预算、既有A/B/C `REF-TAIL`和固定STATE-08模板；不出现2.5字段、时间码或额外Prompt栏目。

### R28-2 Seedance 2.5 Standard Clip

输入：Lock=`Seedance 2.5`，目标时长10秒，未作任何Long-form选择。

PASS：默认仍使用4—15秒Standard Clip、最小充分参考与既有连续性风险降级；30秒不是默认时长。

### R28-3 Seedance 2.5 Long-form Clip

输入：Lock=`Seedance 2.5`，用户选择目标时长20秒；镜头链、空间关系、表演和动作密度均通过严格预检，网关状态未知。

PASS：无需用户额外选择Long-form，计划自动使用16—30秒内部路由；仅严格预检失败时才重跑STATE-07拆分为短Clip，不回退已确认Detailed Shot Design。未知网关状态不触发15秒限制；实际平台拒绝才触发最小调整。

### R28-4 Seedance 2.5 Video Extension

输入：Lock=`Seedance 2.5`，用户选择Video Extension并提供实际上一段成片。

PASS：将该成片登记为受控`REF-VIDEO`，同时保留Canonical资产、首/尾帧、End-State与A/B/C规则；不得以视频输入替代它们。

### R28-5 Seedance 2.5 Targeted Edit

输入：Lock=`Seedance 2.5`，用户明确要求修改既有视频的一段内容。

PASS：只在既有分镜正文的适当字段写受控时间段语义；不新增时间轴/目标模型字段。非Targeted Edit仍拒绝时间码、逐秒分段和帧率描述。

### R28-6 Clay Render Authority Isolation

输入：一个已验证、无性别`REF-SKETCH`作为2.5 Clay Render / 白模空间调度参考。

PASS：只消费位置、朝向、距离、拓扑、机位、姿态、视线和动作路径；Character外观/服装/年龄、Environment材质、灯光、色彩和最终画风仍由Canonical Authority控制。

### R28-7 High Reference Capability Uses Minimal Sufficiency

输入：2.5网关可确认支持高于9张图片、视频或音频参考。

PASS：先按当前Clip风险筛选最小充分集合，只有超过实际有效上限才整合/裁剪；不机械填满30图、10视频或10音频；音频仍须当前用户明确opt-in。

### R28-8 Lock Before Clip Integration

输入：STATE-06已完成，Project State没有Target Video Model。

PASS：在任何STATE-07 Clip整合之前询问一次2.0/2.5；不得等到STATE-08最终Prompt才问。

### R28-9 Locked Model Does Not Re-prompt

输入：Project State和Confirmed Clip Plan均为同一LOCKED模型与执行Profile。

PASS：STATE-07/08直接消费该Profile，不重复询问。

### R28-10 Pre-confirmation Model Switch Scope

输入：Clip Plan确认前用户从2.0切换到2.5或反向切换。

PASS：只使受影响STATE-07/08执行产物重跑；Production-Locked Script、Confirmed Assets、Scene Breakdown和Detailed Shot Design保持Accepted。

### R28-11 MiniMax H3 Standard Clip

输入：Lock=`MiniMax H3`，目标时长12秒，当前Clip有两个实际已确认角色参考图，用户要求中文对白与口型一致。

PASS：只选择`adapters/minimax-h3.md`，保持12秒单Clip并按最小充分原则使用真实参考图；将准确台词和最小口型/中文语义写入既有`台词：`字段，保留当前Clip风险的简洁负面提示词、永久无BGM禁令及`非叙事性音乐：N/A`；不写Seedance Video Extension、Seedance时码式Targeted Edit或未验证的上传上限。

FAIL：把Seedance 2.5的30秒、Video Extension、Clay Render或时码式Targeted Edit移植给H3；忽略H3支持的首/尾帧、全能参考或已有视频编辑；把未上传的图片写成已投喂；仅因存在对白就自动写入音色身份。

## R29 Model Compilation Template Router Regression

### R29-1 Seedance 2.0 Stable Compiler

输入：Lock=`Seedance 2.0`，已确认一个10秒Clip。

PASS：内部Profile选择且只选择`Seedance 2.0 Stable Compiler`，沿用短Clip、≤9图片和既有连续性合同；不要求2.5参考映射或任务语义，最终Template无模型/Compiler字段。

### R29-2 Seedance 2.5 Native Compiler

输入：Lock=`Seedance 2.5`，Clip使用已确认的参考素材。

PASS：内部Profile选择且只选择`Seedance 2.5 Native Compiler`并读取2.5 Profile；素材映射只在内部记录来源、用途与Authority，最终Template字段、顺序和排版保持不变。

### R29-3 Native Reference And Frame Semantics Do Not Leak

输入：2.5 Clip使用合法首/尾帧、Clay Render空间草图和实际`REF-VIDEO`延展输入。

PASS：内部语义分别保留首尾帧、草图Authority和延展输入，仍不取代Canonical / REF-TAIL / End-State；最终Prompt不出现上传顺序、内部角色、API字段、Target Model、Execution Mode或Compiler字段。

### R29-4 Targeted Edit Is Conditional

输入：2.5用户明确编辑既有视频，随后另给一个Standard Clip。

PASS：前者只在既有分镜正文表达受控编辑范围与保持项，后者不含时间码或逐秒区间；两者共用固定最终Schema。

---

## R30 FAST Continuous Chain Regression

### R30-A Explicit Low-Confirmation Language Enables FAST Only

输入：项目已有合法State Source，用户说“尽量少确认，只在关键节点停，自动完成可逆步骤”。

PASS：写入`Automation Policy: FAST`并读取唯一owner `rules/automation_mode.md`；不新建模式、STATE或Schema。表达不锁定Production Script Proposal、不选择模型、不批准Candidate Image、不提交外部服务，也不构成Review PASS。

FAIL：把用户的低确认偏好解释为全部授权，或因为措辞未包含“Fast Mode”而仍强制STANDARD。

### R30-B FAST Carries Verified Internal Work Through Prompt Delivery

输入：STATE-04起的事实、资产、视频模型和Execution Profile均已锁定；STATE-04/05/06/07的QA均通过；三个Execution Clip均Confirmed，其中CLIP-02需要`REF-SKETCH`。

PASS：连续推进STATE-04→05→06→07→08，自动接受Detailed Shot与Clip Plan；CLIP-02的草图验证、注册后同轮编译Prompt；三个完整Prompt按顺序交付，单轮容量不足时仅在完整Clip之间分批，下一次普通推进直接续交。每一阶段仍完成既有QA、预算、无BGM和状态写回。

FAIL：要求用户在STATE之间逐次确认、草图后额外等待、仅因多Clip就停止在第一个Prompt，或跳过QA / Completion Gate。

### R30-C FAST Stops At Non-Reversible Boundaries

输入：FAST项目在资产图像模型未选、外部Midjourney Prompt已编译、Candidate Image已回传、或准备提交视频生成时继续推进。

PASS：首次/变更模型时请求选择；已锁定Midjourney批次只自动交付外部提交包；回传Candidate后停在批次审阅，用户批准后才Active / Canonical；外部视频生成由用户显式提交；未实际查看视频不得Review PASS。

FAIL：替用户选择模型、代投Midjourney或视频服务、把Prompt写成生成结果，或自动把Candidate升级Canonical。

---

## R31 Candidate Output Triage And Cleanup Regression

### R31-A Asset Run Keeps One Valid Candidate And Removes Extras

输入：CHAR-001正式资产Prompt预期一张四区角色设定图；本次内置生成返回三张：C01正确、C02为重复画布、C03是错误角色且带水印。三个未确认输出均位于当前运行可验证的临时目录。

PASS：视觉核验后只将C01登记并展示为`KEEP` Candidate，报告“保留 C01，仍待图片确认”；C02 / C03标为`DISCARD`、报告最短原因、从Candidate References / Registry / 下游参考移除并删除其已核验临时文件。不得要求用户从错误或重复图中选择，C01也不得因此自动Canonical / Active。

FAIL：把三张都显示为候选、只说“有错误”却不指明保留项、把C02 / C03计入预算，或删除C01 / 已确认资产。

### R31-B Valid Aesthetic Alternatives Need One User Choice

输入：ENV-001回传两张均满足当前Prompt、资产ID和空间结构的单图候选，差异仅是同等可用的阴天光照细微倾向，系统没有客观依据判断哪张更符合用户偏好。

PASS：只展示这两张`NEEDS_USER_SELECTION`候选，标明ID与可见差异；不删除任一项，不将其自动升级Canonical / Active，等待用户的图片选择与批准。

FAIL：用FAST替用户做审美选择、把两张都登记为Active，或将未确认的合格图直接删除。

### R31-C Sketch Failure Is Removed Before Registration

输入：CLIP-04需要`REF-SKETCH`，生成结果一张通过所有技术验证，另一张含角色发型、服装和电影光效。

PASS：只保留并报告技术合格草图；泄漏图为`DISCARD`，从Candidate Evidence、Confirmed Visual Anchor、参考资产与图片预算移除；临时本地文件归属明确时直接删除，否则说明无法物理删除但不会再引用。合格草图仍须完成原有验证和注册，不成为角色资产。

FAIL：把失败草图也展示或登记、只报告“草图有问题”不说保留哪张、因自动清理而跳过Sketch Validation，或删除已Confirmed草图。

---

## R32 Unified Delivery Package Regression

### R32-A FAST Aggregates Preproduction And Execution Without Flattening Artifacts

输入：核心资产、Production-Locked Script和事实已确认；视频模型/Profile已锁定；STATE-04至STATE-08所需输入完整且所有QA通过。用户启用FAST并要求继续。

PASS：内部按STATE-04→05→06→07→08依序读取、检查、写回；对外以`Preproduction Package`交付可查看的Visual Direction摘要、完整Scene Breakdown与完整Detailed Shot Design，再以`Execution Package`交付完整Clip Plan和每个Clip的完整目标模型Prompt。每个Template原字段、顺序和内容保持完整；不得将多个阶段压为一张新总表或用“同上”替代。每个Clip仍执行预检、参考预算和无BGM边界。

FAIL：把包名写进Project State或最终Prompt字段、跳过中间QA、只交摘要、先输出Prompt后形成Clip Plan，或因聚合改写Script / Director Intent / Canonical资产。

### R32-B Hard Stop Truncates The Package At The Nearest Boundary

输入：FAST项目完成STATE-06，但尚未选择视频模型；另一项目在资产Candidate Image审阅前要求一次性完成全流程。

PASS：前者可以结束`Preproduction Package`，随后只展示首次模型选择；不得虚构Execution Package。后者只交付`Asset Candidate Package`的筛选结果并停在候选图确认，不进入STATE-04。用户要求统一输出不替代模型选择或Candidate / Canonical批准。

FAIL：为了交付完整包默认挑选模型、把候选图升级Canonical、跳过STATE-03，或把外部提交当作包内自动步骤。

### R32-C Standard Mode Aggregates Only Already-Legal Results

输入：STANDARD项目说“按包交付”，但当前Detailed Shot尚未被确认，且没有FAST自动接受资格。

PASS：可以将已经合法完成的相邻成果组合展示，但在当前Detailed Shot确认Checkpoint停止；不得用“按包交付”把未展示Shot或Clip Plan视为确认，更不得提前编译STATE-08 Prompt。

FAIL：因为用户要求合并展示就绕过Confirmation Input Semantics、Completion Gate或Hard Stop。

---

## R33 Model-Specific Main Style Regression

### R33-A Seedance 2.5 Has A Dedicated Main Style Field

输入：Seedance 2.5的CLIP-02继承已确认的低饱和海边Visual Grammar Baseline，当前剧情需要人物在暮色中靠近，且时间线已有动作与镜头设计。

PASS：`尾帧限制：`后、`全局叙事与画面设定：`前存在独立`主风格：`；它写项目特定风格含义与当前Clip必要的少量可见载体，例如真实暮光来源、低饱和灰蓝关系、克制观察机位与表演尺度。`全局叙事与画面设定：`只写主体、地点、事件、主题和核心镜头意图，不重复完整风格段；时间线继续承载当前动作、摄影机与光色变化。

FAIL：把风格只隐含在全局叙事或时间线、在多个字段机械重复，或因新增风格字段删掉多模态参考 / 时间线 / 无BGM边界。

### R33-B H3 Keeps Three-Part Structure With Main Style First In Core Idea

输入：MiniMax H3的CLIP-03使用已确认青春片Visual Grammar Baseline，要求人物在厨房内完成一个克制反应。

PASS：顶级结构仍只有`参考素材说明：`、`核心创意：`、`画面过程说明：`与既有末尾限制；`核心创意：`的第一行固定为`主风格：`，写项目特定含义和最小充分的可见载体，第二行再写主体、地点、事件与必要运镜。不得新增与三段式竞争的顶级风格段。

FAIL：只写孤立风格标签、将风格藏在第二行后、增加H3顶级`主风格：`段、混入Seedance 2.5时间线或删除`非叙事性音乐：N/A`。

---

## R34 Required Sketch Submission Binding Regression

### R34-A Project Model Choice Is Early, Clip Capability Is Late-Bound

输入：新项目在STATE-00确认`Built-in Image + MiniMax H3`；STATE-03新建角色与环境资产；后续CLIP-04为H3 Start-End模式且Final=`REQUIRED`。

PASS：STATE-03直接继承Built-in Image而不逐批重复提问；STATE-06/07复核H3 Start-End无法提交Required草图，只给出改为H3 All-Reference、改选兼容模型或返回上游降低Blocking的最小路径。不得为了兑现项目偏好把`REF-SKETCH`伪装为首/尾帧，也不得重做剧本、资产或导演设计。

### R34-B Required Sketch Is A Real Submitted Input For Every Compatible Model

输入：`REF-SKETCH-04`已验证、Confirmed、Signature匹配且其真实文件/受控ID可访问；CLIP-04的Final=`REQUIRED`，预算仍有一个图片位。

PASS：Seedance 2.0的`参考资产：`列出`REF-SKETCH-04｜真实文件/受控ID｜实际提交图片输入`；Seedance 2.5的`多模态参考资产：`有其真实`@图片N`；MiniMax H3 All-Reference的`参考素材说明：`有其真实`@图片N`。三者都把它计入实际图片预算，且唯一Authority为Position / Facing / Distance / Topology / Axis / Camera / Pose / Gaze / Action Path；Canonical角色、环境、道具、材质、灯光、色彩与最终画风不受草图控制。

### R34-C Missing Or Incompatible Sketch Input Cannot Be Claimed

输入：Final=`REQUIRED`，但`REF-SKETCH-04`文件/受控ID不可访问，或其Signature过期，或2.0/2.5预算已满，或H3仍为Start-End / Video Edit。

PASS：`REF-SKETCH Submission Compatibility=FAIL`，Prompt Pending并给出恢复输入、腾出预算、改H3 All-Reference、改模型或返回Blocking的最小路径。最终文字不得写“已使用 / 已提交草图”，不得作为输入就绪生成包交付。

### R34-D None, Rewrite And Replacement Boundaries

输入：Final=`NONE`的简单Clip；以及一个Signature不变的Prompt Rewrite与一个Blocking重构后的REPLACE。

PASS：NONE没有草图空槽位、占位或图片预算；Rewrite复用同一实际`REF-SKETCH`输入但不重复生成或计数；REPLACE从输入与预算移除旧草图，绑定新的可访问、Signature匹配草图后再编译。

## R35 Declared-Existing Asset Handling Regression

### R35-A Declared Assets Are Listed, Not Solicited

输入：用户在STATE-00 / STATE-02说明“角色和环境资产我这边已经有了”，未提供任何文件或路径；项目仍需判定CHAR / ENV / PROP / FX。

PASS：STATE-02照常输出完整资产清单、Tier判定与Support Board计划，已声明条目标注`已有（用户声明）`、其余标注`待制作`；不要求用户上传、发送、粘贴、提供路径、文件名或自有素材清单，不重复追问，不写BLOCKED，不把停止点放在素材索取上；Registry仍为`Prompt Status: Not Started / Image Status: Not Generated / Confirmed Status: No`。

FAIL：要求用户先交资产或上传参考图；把资产清单变成逐项缺口盘问；因文件未提供或不可读而停住；或在用户未说明前虚构其持有 / 缺失状态。

### R35-B Declaration Is Not Registration

输入：用户声明“角色图已有”后未提供文件，随后要求继续到STATE-03。

PASS：`已有（用户声明）`不满足`Existing Asset Fast Path`触发前提，角色仍走Asset Design → Prompt → Image双确认；只有用户实际提供文件、给出可访问受控ID或明确要求登记时才进入Existing File Check → Candidate Reference Registration → User Confirmation → Canonical Reference / Active Version。

FAIL：把声明当已确认资产直接用于下游Prompt或视频参考；跳过Prompt / Image确认；或以“用户已有”为由跳过Tier判定与Registry状态语义。

### R35-C Missing Items Come From The List Or The User

输入：清单已输出，用户未说明缺失项，也未提供任何补充。

PASS：Skill按清单继续当前可推进步骤，不逐项盘问缺失；只有某缺口会改变当前对象身份或阻断当前制作步骤时，才一次性指出该**具体**缺口并给最小路径。

FAIL：连续追问“哪些没有”“请逐项确认是否已有”“请提供素材清单”；或把未声明资产写成缺失、把用户声明过的资产写成待制作。

## R48 Deliverable Validation, Coverage And Scale Regression

### R48-A Delivery Validator Accepts And Rejects

输入：一个符合`templates/10_video_prompt.md`的`# CLIP-X｜…` Package，以及同一Package的破损版本（字段错序、分镜编号不连续、字段空值、JSON格式、缺少固定无BGM句）。

PASS：`scripts/validate_prompt_package.py <prompt-file> --model seedance-2.0`对合规包返回VALID并以0退出；对每个破损版本返回对应INVALID原因并以1退出。2.5与H3分支分别校验阶段递进无重叠与`非叙事性音乐：N/A`末行。

FAIL：校验器只接受`--skill-root`、无法校验已编译Package；或把`validate_prompt_package.py`写成`validate_sd_film.py`的替代品，或把它列为Skill更新维护QA的执行owner。

### R48-B Unauthorized Voice Field Is Rejected

输入：Package中出现`音色特征：`，但用户未明确要求把声音控制写入当前视频模型Prompt。

PASS：校验器返回INVALID并指明该字段只在显式授权时插入；用户明确要求并追加`--allow-voice-field`时通过。

FAIL：把对白、已有音色资源或Active Voice Profile当成插入该字段的理由。

### R48-C Review Ledger Coverage Is Complete

输入：一次含N个SHOT的Review，其中只有部分SHOT被写入`Shot-Level QA`，或某维度留空。

PASS：每个受审SHOT与每个受审边界各占一行，每一列都有结论；通过写`PASS`或`无风险`，不适用写`N/A`并写明理由；结论为`PASS`时`Problem`写`无`、`Return Route`写`不适用`。

FAIL：只列有问题的SHOT、用一段总体评价替代逐镜记录、任一维度留空，或在该状态下仍作出`PASS`并进入Completion Gate。

### R48-D Shot Count Declaration Matches Shots

输入：一个Seedance 2.0 Clip，`画幅：`声明分镜总数，逐分镜区块数量与之不一致；以及一个模型可能扩写单镜的情形。

PASS：`画幅：`声明的分镜总数与逐分镜实际数量完全一致；存在扩写风险时`反向提示词：`保留与声明一致的数量兜底句，且数量限制不只写在反向提示词。

FAIL：缺少总数声明、虚报数量，或新增独立字段承载数量声明而改变STATE-08固定Schema。

### R48-E Full Shot Scale Contract

输入：大全景中出现人物、门、车辆与建筑。

PASS：按门高、头顶到屋顶余量、人物与车辆的位置关系、建筑层高倍数写出相对比例，并可由现实关系复算。

FAIL：只用“宏大”“电影感构图”描述尺度，人物被缩小、门被放大或层高失真，或把比例错误当成画质/后期问题处理。

### R48-F Character Responds To Environment Light

输入：人物穿过不同光区，或反打镜头改变受光分布。

PASS：面部亮度、色温、方向与反射随位置、遮挡、距离或朝向变化同步改变；面部可读性通过光源关系、反射结果或构图提升。

FAIL：写入与环境无关的固定面部补光或均匀打亮“美颜光”，导致人物像贴在背景上或在镜头间无来源地受光漂移。

### R48-G Reference Provenance And Degradation

输入：同一资产连续多轮图改图，输出出现塑料感、脏高光与细碎噪点。

PASS：先合并修改需求减少迭代；发现劣化时退回原始图或结构图重新生成；只在原图不可用时从最近干净版本分叉并重新合成已确认正确的局部。控制强度按用途选择。

FAIL：在已劣化的衍生图上继续叠加修改；或借本机制把线稿、白模、多格拼图或Storyboard登记为Canonical Reference、STATE-08视频输入。

### R48-H Experience Classification And Coupled Attribution

输入：一条候选经验，来源为同时改变多个变量且无法分离归因的观察。

PASS：候选与确认记录带`Class: P / O / C`；`O`类带`valid_as_of`且到期后转`REVIEW`；`Triggers`、`Procedure`、`Failure Signals`、`Exceptions`、`Counter-examples`齐全；耦合来源记为`coupled_uncharacterized`且不升级为`P`，不据此宣称某一措辞必然有效。

FAIL：只有结论句而缺适用条件、步骤、失效信号或反例的条目入库；把`O`类模型参数写成跨项目原则；用耦合改动宣称某词已获验证。

## R49 Aesthetic Decision Lock Regression

### R49-A Four Dimensions Require Exclusive Choices

输入：一个已完成STATE-03核心资产的短项目进入STATE-04，剧本主题与Director Intent已锁定。

PASS：在写入Project Bible前完成Aesthetic Decision Lock；反差与光比结构、色彩对抗关系、构图主张、视觉母题与变化轨迹四个维度各给出选择、被放弃的选项、事实依据与可观察的可见后果；四项落在既有Overall Visual Style、Color System、Lighting Style、Composition Rules与Continuity区域；视觉母题写明至少三次可出现、变化或反转的轨迹。

FAIL：只写“低饱和、电影感、高级感”等标签或只给色调名；只写选择而没有被放弃的选项；用“为了电影感”充当依据；新增Project Bible竞争区域、平行Schema或STATE-08新字段。

### R49-B Decoration Without Trade-off Is Not A Decision

输入：某项目在四个维度都写了正向描述，但没有说明放弃哪一类常规做法。

PASS：判定Aesthetic Decision Lock未成立，不写入Project Bible，不进入STATE-05；返回STATE-04补齐被放弃的选项与依据。

FAIL：把“统一柔和光比”“自然色调”“标准三分法”这类无取舍的默认做法记为已做出的决定并通过Completion Check。

### R49-C Lock Is Inherited And Audited Downstream

输入：一个已锁定四项决定的项目推进到STATE-06与STATE-08，某个Clip重新引入与锁定构图主张相反的画面组织。

PASS：STATE-06在Composition Strategy中保留已锁定构图主张；STATE-08 Prompt落入已锁定的光比结构、色彩对抗与构图主张；STATE-08 Prompt Scorecard的Hard Gate检查该Clip是否继承并执行Aesthetic Decision Lock，漂移时该项不通过并回到STATE-04或STATE-06。

FAIL：用“更好看”“更有电影感”在STATE-08另起一套临时审美；让Scorecard只按文字华丽程度给摄影与光影两项高分；把Lock写成逐镜参数或在STATE-04提前产出Shot List。

## R50 Aesthetic Decision Lock Projection Regression

### R50-A Lock Reaches The Prompt Compiler

输入：一个已在STATE-04锁定四项美学决定的项目推进到STATE-08，当前Clip只携带1—3条导演优先级。

PASS：STATE-08的Required Resources包含`project_bible.md`的已确认Aesthetic Decision Lock；Prompt Compiler在Global Projection Matrix中按`Aesthetic Decision Lock（STATE-04）→ 主风格；画面描述；环境一致性`投影；`主风格`写出光比程度与色彩对抗关系，逐镜`画面描述`写出本镜相对锁定值的构图与母题Delta。

FAIL：STATE-08只拿到导演优先级而没有美学决策入口；把四项决定写成风格标签；在STATE-08另起一套临时审美。

### R50-B Lock Is Not Erased By Delta Compression

输入：项目风格已由Visual Direction锁定，第二个及之后的连续Clip按`Source Carries State, Prompt Carries Delta`只写差异。

PASS：`主风格`仍保留可核查的光比结构、色彩对抗关系与构图主张锚点；本镜真实发生光比、色彩或构图变化时写明变化；视觉母题在已确认的出现、变化或反转节点上出现，未到节点不重复。

FAIL：把“已由视觉开发锁定”当作省略理由，导致后续Clip的`主风格`只剩风格标签、`画面描述`只剩动作；或每镜机械重复整段项目Visual Bible。

## R51 Skill Context Budget Regression

### R51-A Oversized File Must Be Registered Or Split

输入：一次变更使某个Workflow、Rule或Knowledge文件继续增长，越过单文件Target阈值。

PASS：在同一次变更中把该文件登记进`references/context_budget.md`的Size Ledger，写明Owner、当前行数、留存理由与复审日期；或直接拆分到阈值以内。`scripts/validate_sd_film.py`对超Target未登记的文件报告失败。

FAIL：让文件静默增长；用“内容确实重要”代替登记理由；把登记当作永久豁免；或为了压行数删除已确认的规则、字段归属、Template字段或回归场景。

### R51-B Shrunk File Must Be Unregistered

输入：某文件经拆分或压缩后降到Target以下，但Size Ledger仍保留其条目。

PASS：同一次变更中移除该条目，Validator随即通过。

FAIL：保留已达标条目，使Ledger退化为长期豁免名单，下一次增长不再触发任何检查。

### R51-C Ceiling Is Not Waivable

输入：某文件达到或超过Ceiling阈值。

PASS：判定为结构性失控，先拆分为多个单一职责文件，同步更新全部引用与路由后再提交；拆分后重新核对文件引用完整性。

FAIL：在Ledger中登记后照常提交；或以“本轮只改文案、与超长无关”为由延期。

### R51-D Budget Does Not Justify New Files

输入：一次优化中发现多个文件超长，考虑通过新增文件降低单文件行数。

PASS：先按`Rule Ownership Check`确认现有权威位置；只有拆分确实需要新的单一职责载体时才新增，并同步更新所有引用、路由与回归。

FAIL：以“降低行数”为由新增平行规则文件，形成第二套并行检查规范或竞争owner。

## R52 Maintenance Self-Check Extraction Regression

### R52-A Must-Read Path Stops Being A Long File

输入：一次维护优化需要修改Skill，按`SKILL.md`入口执行维护自检。

PASS：`SKILL.md`直接指向短卡`references/maintenance_self_check.md`（15项检查项、执行链与报告模板齐全），判据真源在`references/maintenance_self_check_protocol.md`；`references/module_contracts.md`只保留模块接口合同与一个指针，已回到单文件Target以内并从Size Ledger摘牌。

FAIL：维护自检仍只能通过通读一个超长合同文件才能找到；或抽取后`module_contracts.md`同时保留一份可执行的并行副本。

### R52-B Module Contracts Does Not Re-Grow The Checklist

输入：后续修改在`references/module_contracts.md`中再次写入检查维度、维护链或报告模板。

PASS：判定为Duplicate Rule，保留单一权威来源；`scripts/validate_sd_film.py`检测到合同文件重新出现维护自检标题即失败。

FAIL：允许合同文件与维护QA文件并行维护同一套检查。

### R52-C Non-Runtime Documents Are Not Runtime Authority

输入：某个Workflow或规则需要引用用户用法说明。

PASS：`USER_GUIDE.md`顶部声明自身为非运行时文件；运行时读取按`rules/resource_loading.md`的Read Budget执行，用户说明只用于确认用户可见行为。

FAIL：把`USER_GUIDE.md`当作规则、恢复、路由或Schema来源；或为让它“更权威”而把内部规则复制进用户文档。

### R52-D Capability Numbers Have One Owner

输入：模型时长窗口或参考预算发生变化。

PASS：只修改对应Adapter的能力数值；知识层不再复述原始窗口，只引用Adapter的`duration`并说明超出稳定窗口时的预检条件。

FAIL：知识层保留一份独立的窗口数值，使一次能力变更必须在多个文件同步。

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
- R52-A至R52-D验证维护自检已从模块合同抽取为可独立读取的短卡与判据真源：必读路径不再需要通读超长合同文件；`module_contracts.md`不得重新长出并行检查副本并已从Size Ledger摘牌；`USER_GUIDE.md`为非运行时文件；模型能力数值只由Adapter拥有，知识层不再复述原始窗口。
- LR-R1至LR-R10验证普通Chat不因Windows路径不可读默认要求Work、Skill / Project双source独立、Current Skill压过历史摘要、Legacy STATE向前映射、Intent Backfill只增补、Confirmed `REF-SKETCH`持久、STATE-08从current owner entry重进、Claim Gate诚实、Work只在真实必要时升级，以及普通`下一步`不重复全量恢复。
