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

PASS：A/B类执行`Screenwriting Optimization → Directorial Interpretation → Production Script Proposal`；Class C按必要性先执行`Adaptation Target Detection → Script Adaptation → Adaptation Draft`再进入同一优化链。Proposal输出后写`Script Status: Optimized Proposal`、STATE-01 `IN_PROGRESS`、`Pending Decision: 等待用户确认Production Script Proposal`并再次停止。只有用户随后明确确认Proposal，才Production-Lock并进入STATE-02。

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

输入包含连续对话、动作接力、场景断点与不同逐镜时长的Confirmed Detailed Shot Design。检查所有正式Shot按原顺序且仅进入一个CLIP-xxx；每个Clip为4—15秒；连续低复杂度Shot可合并，跨时空/资产断点和超过15秒候选被拆分或返回STATE-06；Clip内保留起始状态、连续动作、空间/道具/摄影机连续性与结尾状态。跨Clip固定执行`上一Clip生成完成 → 判断是否需要严格承接 → 若需要则请求用户截取尾帧 → 上传并命名REF-TAIL → 加入当前Clip参考资产 → 首帧明确引用 → 当前Clip生成 → 当前Clip尾帧限制 → 下一Clip承接`；STATE-08按CLIP→G一对一输出一条连续Prompt，即使Clip包含多个Shot也不拆Prompt；任何Storyboard视觉材料均不得进入参考资产。

## R05B Source Script Label Namespace

输入剧本自带“镜头1—镜头5”或“Clip A—Clip E”标题。PASS路径必须先把这些标题登记为Source Script Labels，STATE-05建立SCENE，STATE-06按叙事功能、动作阶段、机位/视点、Coverage与边界创建正式SHOT，STATE-07才根据Confirmed Detailed Shot Design建立CLIP。以下任一情况均为FAIL：在STATE-05或STATE-06完成前创建暂定/占位/正式CLIP；把Source Script Label直接改名或一对一映射为SHOT、UNIT、CLIP或G段；只声明Source Revision但不存在可关联的Confirmed Detailed Shot Design Artifact或Portable Checkpoint。

## R06 Scene / Time Discontinuity

检查Motivated Discontinuity，只重建剧情授权状态，不伪造过渡动作。

## R07 Image-To-Video Reference

检查首/尾帧用途、Asset Active Version、边界冲突和Template 11到Template 10的单向投影。

## R08 Review Revision Loop

PASS允许完成；REVISE/REBUILD保持STATE-09 IN_PROGRESS，记录Affected IDs、Return Route、Accepted Unaffected Artifacts和Recheck Scope。

## R09 STATE-03 Double-Confirmation Closure

以下三个最小案例必须依次通过四个Registry状态，且每个案例在`Prompt Draft`和`Image Generated`各停止一次。示例中的“用户确认”是测试事件，不代表实际项目批准。

### R09-C Character

输入：`CHAR-001 林遥，28岁女气象工程师，短黑发，灰蓝防水工作服，冷静克制；有对白；无剧情状态变体。`

Prompt Draft输出至少包含：

- 角色定义与角色音色描述：中低音域、清晰克制、自然语速、短停顿后再强调关键词。
- 三视图Prompt：`角色设定表，28岁东亚女性气象工程师林遥，椭圆脸、平直眉、深棕眼、短黑发齐耳并露出双耳，身高约168厘米、匀称偏瘦体型；穿灰蓝色连帽防水工作服、深灰工装裤、黑色防滑短靴，不佩戴首饰。纯浅灰无缝背景，同一画布从左到右为正面全身自然站姿、严格右侧全身、背面全身，三个视图等比例等高度，服装接缝、口袋、拉链、帽型、鞋型与颜色完全一致；柔和中性棚拍光，真实电影角色概念设计，清晰材质与结构，4:3横幅，高分辨率。禁止改变脸型、年龄感、身体比例、发型长度、服装结构与配色；禁止透视夸张、动态姿势、额外人物、文字、水印、拼错肢体。`
- 面部特写Prompt：`林遥面部角色参考，28岁东亚女性，椭圆脸、平直眉、深棕眼、鼻梁自然、薄而清晰的唇形、真实轻微皮肤纹理、短黑发齐耳并露出双耳；正面头肩特写，平静中性表情，视线略高于镜头，浅灰无缝背景，柔和中性棚拍主光加弱填充，肤色准确，真实电影角色概念设计，1:1，高分辨率。严格继承三视图的脸型、年龄感、发际线、发长与发色；禁止美颜塑料皮、夸张妆容、笑容、首饰、额外人物、文字、水印、五官漂移。`
- 状态变体：`Not Required—剧本未确认额外视觉状态。`
- `Visual Production Status: Prompt Draft`与`Awaiting User Confirmation: Image Prompts`；不得生成图片。

模拟用户确认`Prompt Revision: P-v001`后，状态变为`Prompt Confirmed`。生成后仅登记`Candidate References: char-001-turnaround-c01.png; char-001-face-c01.png`，状态为`Image Generated`，不得出现Canonical References或Active。模拟用户确认两张图片后，最终记录必须为`Visual Production Status: Asset Confirmed`、`Status: Active`、`Active Version: v001`，并把两张已批准Candidate References升级为Canonical References。

### R09-E Environment

输入：`ENV-001 海边气象站主控室，近未来但可现实建造，暴雨夜；需要主空间、入口反向视角与控制台关键区域。`

Prompt Draft至少包含：

- 主参考图Prompt：`近未来海边气象站主控室，长方形单层空间，画面左侧为面向海面的连续抗风玻璃窗，画面右后方为唯一金属气密入口，中央两排低矮控制台沿房间长轴排列，前端大型天气雷达屏，天花暴露式线性灯与检修轨道；湿冷暴雨夜，窗外海浪与远处警示灯可见，室内主要由4000K线性顶灯和青绿色仪表屏照明，灰色防滑地面、哑光铝板墙、深灰橡胶包边。摄影机位于入口内侧约1.6米高度，24mm等效大全景，清楚展示入口—控制台—海窗的可行走动线与尺度；真实电影美术概念图，16:9，高分辨率。锁定窗、入口、两排控制台和雷达屏的相对位置；禁止改变房间骨架、增加楼梯或第二入口、赛博朋克霓虹堆叠、人物、文字、水印。`
- 多视角Prompt：从海窗方向反看入口与两排控制台的完整独立Prompt，保持同一布局、材质、暴雨夜与光源锚点。
- 关键区域Prompt：控制台操作区中景完整独立Prompt，明确按钮、屏幕、椅位、通行宽度与材质。
- `Visual Production Status: Prompt Draft`并等待确认。

模拟Prompt确认、生成`env-001-main-c01.png / env-001-reverse-c01.png / env-001-console-c01.png`、图片确认后，三图才可进入Canonical References；最终必须为`Asset Confirmed + Active`。任一步缺少Prompt确认或图片确认均为FAIL。

### R09-P Prop

输入：`PROP-001 手持风暴数据记录器，掌上工业仪器；正常与屏幕报警两种状态，需要接口细节。`

Prompt Draft至少包含：

- 主参考图Prompt：`手持风暴数据记录器，掌上工业仪器，约18厘米高、8厘米宽、3厘米厚，深灰色防滑橡胶包边，拉丝铝合金正面框，顶部短天线，正面上半部为无品牌矩形屏幕，下半部四枚实体防水按键，右侧橙色密封数据接口盖，背面可拆电池盖与腕带孔；45度三分之四产品展示视角，白灰无缝背景，柔和棚拍主光与轮廓光，真实可制造产品设计，1:1，高分辨率。锁定尺寸比例、天线、屏幕、四按键、橙色接口盖和电池盖位置；禁止品牌文字、额外按键、透明悬浮界面、夸张科幻装饰、人物、水印、结构漂移。`
- 状态Prompt：屏幕由正常数据变为红色报警界面，外壳结构、按键、天线与接口位置完全不变；完整包含同样的构图、光影、背景和限制。
- 细节Prompt：右侧橙色密封接口盖打开的微距结构图，锁定铰链、密封圈与接口尺度；其余结构不改变。
- `Visual Production Status: Prompt Draft`并等待确认。

模拟Prompt确认、生成`prop-001-main-c01.png / prop-001-alarm-c01.png / prop-001-port-c01.png`、图片确认后，三图才可进入Canonical References；最终必须为`Asset Confirmed + Active`。生成图被拒绝时保持Candidate，不能进入Registry确认态。

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

多角色场景中有多个当前Clip核心角色。PASS：每个核心角色各自保留独立三视图/角色锁定图；动作/互动图只负责动作关系；非角色信息承担必要的整合压力。FAIL：把多个核心角色合并成角色总表、共用一个角色位，或用动作图替代任一角色外貌基准。

### R11 Retention Priority

整合后仍需裁剪时，从高到低保留：当前Clip出场核心角色独立图 > 当前主要环境 > 当前关键道具 > 当前关键动作/互动关系 > 上一Clip尾帧/当前首帧连续性参考 > 特殊一次性道具/次要角色。已经判定为Direct / Reference-Only且实际存在、可访问、已确认的连续性帧属于硬需求，必须先释放其他位置，不得静默删除后仍声明连续继承。

---

## R12 Runtime Skill Reload / Hot Reload

三个案例均以用户在已工作的旧对话中输入“调用SD，按当前安装最新版Skill继续当前项目”为触发。

### R12-A Stale Conversation Pipeline vs Current Installed Pipeline

输入：旧对话缓存声称`STATE-07`对应`Storyboard`，磁盘当前`SKILL.md`却声明`STATE-07 Clip Production`并包含更新的Skill Version / Build ID。

PASS：按`rules/runtime_reload.md`重新完整读取当前安装`SKILL.md`，记录`Reload Status: RELOADED`及磁盘版Skill Version / Build ID；当前安装Pipeline覆盖旧对话的Skill描述；再读取config、适用Rules、状态References、映射后Workflow与其依赖。

FAIL：继续把Storyboard当作固定STATE-07；用历史摘要覆盖磁盘Skill；未实际重读却声称`RELOADED`；强制用户新建对话或项目。

### R12-B Preserve Progress And Map To Current Workflow

输入：旧项目停在标注为`Storyboard`的`STATE-07`，已有Confirmed Detailed Shot Design，无Confirmed Clip Production Plan，并有可验证Last Successful Checkpoint。

PASS：按`Active Project Root/project_status.md > portable_project_status.md > 当前可验证Project Context`选择状态；如使用第三级则先规范化为Portable State；把项目映射到当前`STATE-07 Clip Production`和`10_clip_production_workflow.md`；保留Detailed Shot Design、Checkpoint、已完成States与Storyboard Optional Artifact；只继续尚未完成的Clip Production。

FAIL：回退STATE-00；重做已确认Detailed Shot Design；将旧Storyboard作为STATE-08参考资产；仅按旧STATE编号硬复制而不检查Artifact / Completion Gate。

### R12-C Preserve Production Lock And Confirmed Assets

输入：项目已有`Script Status: Production-Locked`、Confirmed Core / Support Assets、Active Versions、Canonical References、已接受Artifact Revision与用户明确的“不改剧本、不改角色外观”约束。

PASS：Reload后上述项目事实全部保留；只更新Skill Definition和必要路由标签；后续Workflow仍从Active / Canonical资产与Production-Locked Script读取真源。

FAIL：把Script Status降回Source Material；丢失Confirmed Assets、Active Version或Canonical References；因Skill重载重新要求用户确认已接受结果；忽略用户锁定约束。

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

---

## Deterministic Expectations

- Skill、Registry、Project、Asset、Artifact、Execution、Sequence、Clip、Poster、STATE-08和Review Validator通过合法样例。
- 缺字段、重复ID、非法时间轴、背景音乐、内部模式ID泄漏、无Return Route和第三次盲重试被拒绝。
- 主Pipeline仍只有STATE-00至STATE-09。
- STATE-08最终Schema仍只由templates/10_video_prompt.md拥有。
- R09-C/E/P均验证`Prompt Draft → Prompt Confirmed → Image Generated → Asset Confirmed`，且Prompt确认前不出图、图片确认前不Active/Canonical。
- R10验证Canonical Character Appearance And Form Lock从Asset、Visual Development、Storyboard/Poster、Shot Design、Clip、Prompt Generation、Final Video到Review的全阶段继承，并覆盖非人角色禁止未授权拟人化。
- R11-A至R11-E验证条件性整合阈值、9张加必需尾帧的真实计数、12张自动压缩到≤9、实际资产存在性和多核心角色独立图硬门槛。
- R12-A至R12-C验证旧对话缓存不能覆盖当前安装Skill、旧STATE按当前Artifact / Completion Gate映射，并且Production-Locked Script、Confirmed Assets、Checkpoint、Accepted Artifacts与用户约束在Reload后不丢失。
- R13-A至R13-C验证尾帧需求先于资产可用性判定、严格承接主动请求截图与草案/最终版边界，以及非严格承接不强制截图。
- R14验证纯文字“板凳参考说明”从参考资产删除并迁移到既有空间/道具/反向字段，1—5号视觉资产保持不动，真实双人钢琴凳图只以正式资产ID引用。
- R15-A至R15-C验证文学意图可执行转译、工程级数据按视觉价值压缩，以及Canonical角色/环境资产释放Prompt注意力给当前动作、空间、镜头与状态承接；最终Template结构保持不变。
