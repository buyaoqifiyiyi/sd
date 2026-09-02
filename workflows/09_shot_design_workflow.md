# SD Film Detailed Shot Design Workflow

# AI影视电影镜头设计流程


## Workflow Purpose


本Workflow负责：

先为已经完成的影视场景执行 Spatial Blocking Decision，再将其转换为可直接进入 Clip Production 的 `Professional Detailed Shot Script｜专业详细分镜脚本`。


目标：

建立：

以精确时间码和专业分镜表为主交付物的 SHOT 导演镜头资产，以及 Clip Production 所需的起始状态、连续动作、空间/道具关系和稳定结尾边界。

正式用户可见输出不是简化的“景别 + 运镜 + 画面描述”，而是由`templates/08_shot_design_prompt.md`唯一拥有字段与顺序的 Professional Detailed Shot Script。


不是：

生成视频Prompt。


不是：

直接生成视频。



---

# Workflow Position


当前阶段：

STATE-06


进入条件：


STATE-05 Scene Breakdown Complete



---

# Entry Gate


执行前必须确认：


存在：


project_bible.md


asset_registry.md


scene breakdown结果


Sequence Plan，或已记录的Not Applicable理由



并确认：


SCENE已建立。


角色资产已绑定。


环境资产已绑定。


关键道具已绑定。


镜头存在正式FX时，FX Asset已绑定。

Scene Breakdown已提供足以唯一判断的场景边界、固定结构、入口 / 出口、关键家具 / 障碍、人物剧情动作和道具空间事实；缺失时返回STATE-05或相应资产拥有者，不得由Blocking Map猜测补造。

Scene Breakdown中来自原剧本的“镜头1 / 镜头2 / Scene 1 / 段落A / Clip A”只作为Source Script Labels追溯，不是正式SHOT或CLIP。进入本阶段时不得继承任何上游预划Clip、Clip数量或Shot-to-Clip分配。



---

# Required Knowledge


根据镜头内容按需读取：

- knowledge/spatial_blocking_layer.md（所有Scene；在正式分镜生成前完成Spatial Blocking Decision）
- knowledge/director_decision_layer.md（所有Scene / Shot Group；在STATE-06结束前形成内部Director Decision Notes）
- knowledge/action_previs.md（Action-dominant / Mixed，以及需要展开物理动作的Performance-dominant镜头）
- knowledge/camera_language/shot_language_router.md（所有正式SHOT）
- knowledge/camera_language/camera_movement/selection_matrix.md（所有正式SHOT）
- knowledge/camera_language/camera_movement/index.md与被选主运镜对应的原子知识文件（所有正式SHOT；辅助项构成真实运镜时也读取对应原子文件）
- knowledge/quality/shot_qa.md（所有正式SHOT）
- knowledge/quality/execution_risk.md（所有正式SHOT）
- knowledge/quality/continuity_pair_qa.md（所有相邻SHOT）

- knowledge/performance/
- knowledge/sound_language/
- knowledge/fx/
- knowledge/sequence/（存在Sequence Plan时）
- knowledge/camera_language/（所有镜头的景别、角度、运镜、视点与剪辑语言）
- knowledge/transitions/（所有相邻镜头的边界、转场技术、出入镜锚点与降级）

战斗、双主体、对峙、对话、追逐、相向运动或其他依赖双方空间关系的镜头，必须读取并执行`knowledge/camera_language/index.md`中的Relational Screen Geometry Contract；不得只用“面对彼此”描述朝向。

焦段选择必须读取`knowledge/camera_language/lens_language/focal_length_and_perspective.md`；需要七档归并与降级时再读取`focal_length_patterns.md`，连续覆盖读取`focal_length_continuity.md`。


当用户或创意资料使用“压迫式逼近、环绕眩晕、突停凝视、纵深穿堂”等导演化名称时：

先读取 `knowledge/camera_language/director_patterns/index.md`，再回到其中引用的原子知识文件完成技术定义。不得只复制情绪标签作为运镜说明。

当输入包含两种以上运镜、“镜头顺序”、多个景别/机位/视点或一镜到底要求时，必须读取`knowledge/camera_language/movement_combinations/index.md`与`decision_engine.md`，先判定Single-Move、Low-Complexity Compound Path、Coverage Sequence或Transition / FX Sequence，再决定是否拆镜。


这些知识只辅助逐镜设计，不定义STATE-08最终Prompt Schema。


---

# Forbidden Entry


如果不存在：

Scene。

Asset绑定。


禁止执行Shot Design。



返回：

Scene Breakdown。



---

# Core Principle


镜头必须服务于场景。


不能为了生成镜头而生成镜头。



每个Shot必须回答：


为什么拍？

拍什么？

如何拍？

如何运动？



---

# Step 0

# Spatial Blocking Decision｜STATE-06内部前置步骤

在创建正式SHOT或选择机位、焦段、构图和运镜前，必须对每个Scene执行`knowledge/spatial_blocking_layer.md`：

1. 从Scene Breakdown、Active Assets、Sequence Plan（如适用）与已确认首尾帧提取空间事实；
2. 按人物数量、走位、进出场、动作类型、障碍 / 道具复杂度、Clip数量与180度轴线要求判定：`Text-Only / Top-down + Text Recommended / Top-down + Text Default`；
3. 无论采用哪种方式，都先完成Structured Blocking Map与Text Spatial Rules；
4. 双锁场景再准备Top-down Blocking Map Prompt或图像，并与文字规则逐项对照；
5. 形成Confirmed Spatial Blocking Result后，才进入正式Detailed Shot Design。

Spatial Blocking Result至少锁定：

- 场景边界、可通行区域、门窗、桌椅、柱和关键道具；
- A / B / C起点、终点、连续移动轨迹、转向 / 停顿和不可穿越区；
- C1 / C2 / C3位置、朝向、视锥、关系轴 / 主运动轴及所在轴线侧；
- 关键视线或来源 → 路径 → 目标Connector；
- 每个Clip首帧站位、尾帧站位与`Previous Clip End State → Next Clip First Frame Reference`继承方式；
- 角色左右 / 前后、面对方向、谁移动 / 谁不动、不可换边 / 不可越轴，以及道具位置 / 持有状态。

图像生成门槛：

- 当前环境支持图像生成且Decision要求双锁时，先输出完整Top-down Blocking Map Prompt，把STATE-06保持`IN_PROGRESS`并记录`Prompt Awaiting Confirmation`；未经用户确认当前Prompt Revision，不得生成图，也不得进入正式分镜。
- 用户确认后才生成并核对俯视图；标签缺失、路径冲突或与文字规则不一致时，先最小修正或回退Structured Text，不能把错误图当作Confirmed结果。
- 用户明确不想生图、当前任务不需要生图或工具不可用时，输出完整`Structured Text Fallback`与风险说明后可继续；不得声称已存在图像。

Work/Codex把结果写入`<active-project-root>/shots/spatial_blocking/SCENE-xxx_spatial_blocking.md`；普通Chat把它保存为当前STATE-06 Checkpoint。Top-down Map只是Planning Reference，不是Storyboard、Canonical Asset或STATE-08视频参考资产。

该步骤不创建新STATE、SHOT / CLIP ID或Template字段。Confirmed结果必须投影到`templates/08_shot_design_prompt.md`已有的场景 / 美术、画面内容 / 构图、人物动作、摄影机 / 镜头、镜头调度、转场与AI制作备注语义中。

---

# Step 1

# Scene To Shot Conversion


将Scene拆解为镜头。

正式SHOT边界必须由叙事功能、刺激—反应节拍、动作阶段、机位/视点、Coverage、时空边界与可执行性共同决定，不得按Source Script Label数量机械一对一创建SHOT。

本阶段只创建`SHOT-xxx`。不得创建任何Draft、Provisional、Tentative、占位或正式`CLIP-xxx`；Clip Boundary相关信息只用于下游连续性判断，不得预先决定Clip数量或分配。

## Shot Purpose Gate

创建或保留每个SHOT前，必须证明它至少承担一项当前Scene已确认的任务：

- Narrative Change
- Emotional Change
- Relationship Change
- Spatial / Action Progression
- Information Reveal
- Atmosphere Establishment

任务必须写成该镜头产生的具体变化或建立结果，不能只写“有电影感、增加压力、好看、过渡”。一个镜头可以承担多项，但不得为凑任务新增剧情。若完全没有任务，优先与相邻兼容SHOT合并或删除；若它承担必要呼吸、观察、场景建立或剪辑接口，应归入上述对应任务并说明可见 / 可听结果。Shot Purpose Gate是内部导演决策，不新增Template字段，也不进入STATE-08 Prompt。

## Scene / Shot Mode Routing

在动作和表演细化前，对每个Scene / Shot或连续Shot Group选择：

- `Performance-dominant`：主要变化来自注意、情绪、关系、对白倾听或控制/泄漏；执行`knowledge/performance/micro_expression.md`的Performance Progression Engine。
- `Action-dominant`：主要变化来自位移、接触、受力、追逐、多人协调、复杂道具、特技或动作结果；执行`knowledge/action_previs.md`。
- `Mixed`：表演选择会改变动作，或动作后果会改变情绪/关系；联合执行两者，但只保留当前SHOT完成目的所需的信息，并先保证空间、动作因果和容量。

路由可以按Shot变化，不把整场永久贴成“文戏 / 武戏”。它是STATE-06内部编译选择，不创建新STATE、模式ID、用户可见章节或STATE-08字段。


存在Sequence Plan时：

同时读取BEAT、COV、UNIT与State Ledger。


每个正式SHOT必须映射一个或多个COV ID，或明确该镜头只承担已确认的转场/呼吸功能。


Sequence Plan只提供覆盖需求，不决定景别、机位、焦段、运镜或SHOT数量。



依据：


## Establishing Shot


建立：

时间。

地点。

空间关系。



---

## Character Shot


表现：

人物状态。

关系。

动作。



---

## Action Shot


表现：

动作过程。


包括可见起因、物理过程、结果、恢复与下一动作继承。按`knowledge/action_previs.md`选择A1 / A2 / A3最小充分等级；A1只需起点—路径/变化—终点，A2补协调、重心、接触/受力和状态继承，A3启用完整PREVIS与Kinetic Chain。动作复杂度不得自动决定Realistic / Commercial / Stylized-Fantasy视觉风格。



---

## Detail Shot


表现：

关键细节。


例如：

手。

眼神。

道具。



---

## Emotional Shot


表现：

情绪变化。



---

# Step 2

# Shot ID Creation


每个镜头必须拥有唯一ID。

镜号必须重新创建为正式`SHOT-xxx`，不得沿用或改写Source Script Label作为正式镜号。



格式：


SHOT-001



例如：


SHOT-001


场景：

SCENE-001


Coverage:

COV-001（如适用）



---

# Step 3

# Shot Design Parameters


## Professional Detailed Shot Script Schema Gate

每个正式SHOT必须逐项完成`templates/08_shot_design_prompt.md`当前定义的全部专业分镜字段，并严格保留该Template的字段名称、顺序、编号与排版。本Workflow只定义字段语义、生产方法与校验，不复制完整字段骨架。

### Timecode Contract

- 项目已确认帧率时统一使用`HH:MM:SS:FF`；未确认帧率时统一使用`HH:MM:SS.mmm`。同一份分镜不得混用。
- `TC IN`与`TC OUT`必须落在当前Scene / Sequence的剪辑时间轴上；首镜从已确认起始时间码进入，后续镜按正式顺序连续累计，已确认时间跳跃仍通过剪辑时间轴顺序记录，不把剧情时间写进TC。
- `时长(s)`必须精确等于`TC OUT - TC IN`，并能由下一镜`TC IN`复核；小数精度与项目timebase一致。
- 时间码、时长、动作容量、对白口型与结尾稳定窗口不一致时，本SHOT不得确认。

### Professional Field Semantics

- `镜号`使用唯一正式`SHOT-xxx`，不得另建并行编号。
- `景别`只记录可见取景尺度；`焦段`记录确认的焦段或全画幅等效倾向，不用焦段代替景别、摄影机距离或透视结论。
- `场景 / 美术`记录Scene、时间天气、空间区位、环境结构、实用光源、美术状态和本镜可见的关键材质/道具状态，不在这里重做Canonical Asset。
- `画面内容 / 构图`必须在同一Canonical字段内以清楚的独立子项分别写出`画面描述`、`构图`与`人物位置关系`：明确主体位于画面左/中/右及前/中/后景的位置，并按真实空间依据记录前景、中景、背景、负空间、遮挡、反射、内框、引导线、行动路线、焦点主次与景深层次；不适用项写明原因，不得只写“人物居中”“电影感构图”或单层背景虚化。
- `人物动作`必须在同一Canonical字段内以清楚的独立子项分别写出`人物情绪`、`动作重点`与完整动作链：起始状态 → 刺激/注意 → 反应 → 决定/动作 → 稳定结束状态；有人物表演时同时写视线、呼吸、手部/重心、主要微表情、对白口部容量及谁先反应，禁止只写情绪标签。
- `摄影机 / 镜头`记录机位高度、角度、观察方向、视点、摄影机与主体距离、轴线侧、屏幕方向、对焦对象和主镜头类型；多人关系镜头还必须写清A/B左右、朝向、距离、关系轴与可见空间连线。
- `摄影参数`只记录当前镜头执行所需且已有依据的参数：帧率/timebase、快门感、景深/光圈倾向、曝光保护、对焦方式、稳定方式及必要的运动模糊；未知器材事实不得虚构，平台参数不得提前写入STATE-08最终Prompt。
- `镜头调度`必须同时包含四部分：**摄影机运动 + 人物调度 + 两者如何配合/由何触发 + 镜头结束状态**。必须写出摄影机起点、路径、速度、触发、落点，人物起始站位、动作路线、停顿/视线/距离变化，两者的同步或反向关系，以及最终摄影机、人物、空间、动作与焦点停在哪里。只写“慢推、横移、跟拍、固定”等运镜名视为缺失。
- `光线 / 色彩`必须从已确认光源、时间天气、材质与环境颜色出发，记录方向、光质、强度/光比、综合色温、主/辅/强调色、饱和度/明度、肤色与资产固有色保护，以及起始光色态 → 有真实触发的功能性变化 → 稳定结束光色态。它必须说明叙事功能；只写“冷色、暖色、低饱和、电影感”视为缺失。若保持不变，也要说明稳定保护的叙事信息与连续性。
- `画面特效 / 转场`记录已确认FX阶段、参与介质/反射/雨雾等可见效果，以及Boundary Class、主要转场、Outgoing Anchor、Cut Point、Incoming Anchor与Direct Cut降级；没有特效时写“无新增画面特效”，不得用转场新增剧情或资产。
- `台词 / 旁白 / 口播`覆盖所有角色对白、旁白、广告口播与有意无台词；必须标明说话者、完整文本、表演指令与口型容量，禁止使用固定“女声口播”字段。
- `同期声音设计`必须以清楚的独立子项分别记录`环境声`、`同步音效 / Foley / 呼吸 / 剧情内声源`与`声音尾部`。本字段永久禁止背景音乐、配乐、BGM、主题音乐、氛围音乐、歌曲或“无配乐”等音乐说明；用户的配乐请求必须分流至独立MUSIC / SEED-MUSIC模块。
- `AI制作备注`至少记录Start Boundary、End-Frame Constraint、Next-Shot Handoff、Execution Risk / Seedance稳定等级、口型/动作/FX并发负荷、稳定降级、Coverage映射、禁止项，并以独立子项明确`角色一致性`、`环境一致性`、`道具一致性`与`生成风险 / 控制项`；不得把内部Director Decision Notes或Knowledge Reflection写入正式表格。
- `素材 / 资产`逐项列出本镜实际使用的Canonical Character / Environment / Prop / FX / Voice or Audio Reference、合法首尾帧及Active Version/用途；Storyboard、分镜板、拼图或Detailed Shot Design截图不得作为视频参考资产。

Template定义的全部字段属于同一SHOT的统一生产记录，不能用多个互相矛盾的简化描述拼接。内部Camera Language Decision、Execution Risk与Director Decision负责推导和审核；正式用户可见交付只输出Template拥有的专业字段，不暴露内部逐步决策或Knowledge Reflection。


## Per-Shot Structure Parity And Batch Delivery Gate

在正式输出前，先计算Total Shots与每镜预计内容密度，再决定单批或多批交付。该决定只控制每批包含的SHOT范围，不得改变单镜结构。

1. 每个正式SHOT必须逐项完成Template当前定义的全部字段；任一字段为空、被省略、改名、缩写、与其他既定字段合并，或以全局说明代替时，该SHOT不得输出。
2. 每个SHOT还必须通过最低语义覆盖核对：Shot编号、时间、场景、景别、镜头/机位、焦段、构图、人物位置关系、画面描述、人物情绪、动作重点、台词、音效、环境声、光线/色彩、转场逻辑、角色一致性、环境一致性、道具一致性、生成风险/控制项均能在Template指定字段中被独立定位。
3. 单镜与批量使用同一字段顺序、同一完成标准和相同内容密度。禁止只让首镜、样例镜或高风险镜使用完整模板，再把其他镜头降级为“景别 + 机位 + 画面描述 + 台词 + 音效”等简表。
4. 禁止使用“同上”“沿用上一镜”“见前文”“其余一致”“略”或空白单元格。连续事实也要在当前SHOT中明确写出继承状态与本镜锁定；确实不适用时写`不适用`及理由。
5. 一次无法完整容纳全部SHOT时，自动拆成连续批次。默认每批4—5个SHOT；单镜内容特别长时可减少，内容较短且仍能完整保留全部字段时可适度增加。批次边界只能位于SHOT之间，绝不能把一个SHOT拆到两个批次。
6. 每批按`Batch NN / Total｜SHOT-xxx—SHOT-yyy`标识，并重复Template的完整列表头。完成一批后直接从下一个尚未输出的SHOT继续，不询问是否允许压缩；若运行环境要求本轮结束，则保存`Last Fully Delivered Shot`与`Next Undelivered Shot`续批Checkpoint，下一次输出只从该未交付SHOT继续，不重复、不遗漏、不重排已交付镜头。
7. `Timeline And Coverage Summary`只在最后一批全部SHOT交付后输出。中间批只做本批结构、时间码与相邻边界自检，不得用批次摘要替代逐镜内容。

任何批次中只要一个SHOT没有通过上述检查，必须减少本批SHOT数量或继续拆批；唯一允许的调整是批次规模，绝不能压缩单镜结构。


## Camera Language Decision Gate

每个Detailed Shot在写Camera Movement、Camera Speed与最终Visual Description之前，必须先完成Camera Language Decision。不得先套用“缓慢推进/轻微横移”，再倒推理由。

决策顺序：

1. 从Scene、Coverage与Confirmed Spatial Blocking Result提取镜头目的、情绪功能、空间功能、人物运动和节奏阶段；不得在Camera Language Decision中重新摆位、换边或改变轴线。
2. 实际读取`knowledge/camera_language/camera_movement/selection_matrix.md`与`camera_movement/index.md`，按五项输入选择候选。
3. 实际读取被选主运镜对应的原子知识文件；辅助项若构成摄影机物理运动，也读取对应原子文件。
4. 结合关系轴、人物动作容量、焦段、表演可读性和模型复杂度确定Seedance稳定等级、禁止运镜与安全降级。
5. 候选包含两种以上主要运动、多个机位/视点或一镜到底时，进入Movement Combination判定；复杂Orbit / 360、穿墙、无人机或连续越轴还必须进入Advanced Camera Movement门控。

Camera Language Decision至少包含：

- 镜头目的
- 情绪功能
- 空间功能
- 人物运动
- 节奏阶段
- 推荐主运镜，或有叙事理由的Static / Locked-Off
- 可选辅助运镜/支持行为
- 禁止运镜
- Seedance稳定等级
- 选择理由
- 已实际读取的主运镜原子知识文件；适用时记录辅助/组合/高级知识文件

主运镜必须承担清楚的叙事功能，并能够写出起点、路径、速度、人物配合、终点与轴线限制。Camera Language Decision缺失、只写抽象风格词或没有原子知识证据时，本SHOT不得确认。


## Duration


镜头时长。


常规参考范围：

1-15秒。


推荐：

5-8秒。


这不是硬性最短/最长限制。


短插镜、闪切、蒙太奇或动作细节可以短于4秒，并在 STATE-07 与相邻兼容 Shot 组织为4—15秒 Clip。单个 Shot 超过15秒时，必须按自然动作阶段、Coverage、机位/视点或时空边界拆分，不能把不可执行的超长 Shot 留给 Clip Production。


时长必须容纳必要动作、情绪停顿以及结尾稳定窗口，不得为满足参考范围改变剧情或动作结果。



---

## Shot Size


景别：


远景。

大全景。

全景。

中景。

近景。

特写。



---

## Camera Movement


运镜：


固定。

推进。

拉远。

横移。

跟随。

环绕。

升降。


导演模式只作为选择与组合依据。最终仍必须拆解为：

- 唯一主要运镜或明确固定机位
- 角度/视点/构图
- 起点、路径、速度、触发、落点
- 轴线、方向和结束状态
- 高风险模式的基础镜头降级方案

本字段必须执行已确认Camera Language Decision，不得用通用慢推、轻微横移或“动态跟拍”覆盖决策。若执行细化证明原决策与Blocking、轴线或模型容量冲突，返回本步骤重做Decision，不得静默换成习惯模板。

复合路径只允许一次同向、有动机、同轴、同平台的延续；多个景别、机位、视点、观察对象、新反应节拍或新时空必须拆成正式SHOT。



---

## Camera Speed


速度：


缓慢。

平稳。

快速。

急促。


---

## Focal Length Design

每个SHOT必须把Lens Feeling拆成：

- 焦段范围或约XXmm全画幅等效倾向；画幅已确认时才使用严格毫米数
- 摄影机与主体的近/中/远距离、机位高度、侧位及其叙事原因
- 与Shot Size组合后可见的前后尺度、背景叠合/分离、边缘延展和视差
- 对焦对象、锁焦/Rack Focus与必要景深；不把虚化归因于焦段单独作用
- 广角边缘速度/脸部形变风险，或长焦抖动/跟焦/空气介质风险
- 本镜固定焦段、光学变焦或Dolly Zoom的唯一选择及稳定降级

焦段不自动决定景别、透视、情绪或画面质感。缺少摄影机距离时，不得宣称“透视夸张”或“空间压缩”。


---

## Composition Intent

每个SHOT必须说明：

- 一个主构图原子，或一个已拆解且可降级的导演构图模式
- 主体在画面左/中/右和前/中/后景的位置
- 前景、背景、负空间、内框、遮挡、反射、引导线、光区或行动路线的真实来源
- 构图如何服务Coverage、人物关系、动作或情绪变化
- 构图从起始状态到结束状态的变化
- 高风险构图的基础降级方案


禁止只写“高级构图、电影感、压迫感”或模式名称。


## Relational Screen Geometry（适用镜头强制）

先读取Confirmed Spatial Blocking Result，并先于动作细化锁定：

- A、B画面左/右、高低及前/中/后景位置
- A、B分别朝左/朝右、侧身程度、视线目标与距离
- A—B关系轴或主攻击/运动轴，以及摄影机所在轴线侧
- 眼线、攻击、武器、追逐路线、水流、能量或抛射物的来源—路径—目标
- 首帧几何来源与尾帧需要保留的同一组关系

默认选择单一轴线的固定侧面、侧后双人或Over-the-Shoulder。双方同框且相互面对时不得同时完整正脸。没有已建立轴线、明确叙事理由、中性机位/连续可见路径和固定地标时不得设计越轴；高风险时降级为原轴线侧固定机位。



---

## Lighting

按需读取knowledge/lighting/index.md。每个SHOT必须将适用光影拆解为：

- 已确认光源或环境依据，以及光源相对人物、摄影机与空间锚点的位置
- 主光/环境光/实用光源关系与人物受光方向
- 光质、强度/曝光、光比、综合色温关系与衰减
- 介质、遮挡、材质和反射如何让光影可见
- 人物与重要道具的可读受光区
- 起始光态 → 本镜唯一必要变化 → 稳定结束光态
- 与前后镜头的继承、已确认断点或待确认项
- 高风险和基础降级方案

禁止只写“自然光、侧光、逆光、伦勃朗光、电影感”等模式名；禁止用光影新增不存在的窗、灯、火、雾、雨、水或人物情绪。



---

## Color

按需读取`knowledge/color/index.md`。每个适用SHOT必须把色调拆成：

- 已确认资产、时间天气、环境/实用光源、FX和材质提供的颜色来源
- 一个主色调模式或综合色彩结构；内部可使用CLR-01至CLR-09，最终执行描述不得输出编号
- 主色、辅助色、强调色的画面占比、空间位置与人物/背景分离
- 综合色相结构、饱和度层级、明度/黑位/高光和局部对比
- 白平衡/综合色温、绿色—品红偏色，以及肤色/中性色/资产固有色保护
- 材质、湿地、玻璃、金属、水面、烟雾等综合色彩响应
- 起始色态 → 本镜唯一必要变化 → 稳定结束色态及跨镜继承/断点
- 肤色漂移、综合色彩闪变、通道溢出、死黑/过曝和资产换色风险及降级

禁止只写“冷、暖、灰、高饱和、低饱和、暗黑、霓虹、糖果、小清新”；禁止把色调当作人物情绪、光源或题材公式。



---

## Action Execution Goal

每个存在可见物理动作的SHOT必须先读取Confirmed Spatial Blocking Result，再说明：

- Action Execution Level：A1 / A2 / A3，以及为什么这是最小充分等级
- 起始姿态、位置、朝向、支撑与触发
- 可见路径、接触 / 近接触、参与者或道具的先后关系
- A2/A3适用的重心、力源、躯干传递、轨迹、反馈、惯性与恢复
- 稳定结束位置、姿态、持有 / 接触状态和Next-action Carryover
- 关键动作在当前景别、遮挡、时长与摄影机路径下如何可读
- 超出模型或镜头容量时的Stable Downgrade

A1不得被过度工程化。A3关键Beat要尽量写清物理因果，但不机械填满十一环；只有省略会造成瞬移、无来源发力、接触不清或状态重置的链节才强制补齐。不得只写“猛烈攻击、快速躲闪、激烈打斗、优雅舞动”。

## Performance Goal


每个有人物表演的SHOT必须说明：

- 当前基线状态
- 已确认刺激、人物注意到它的时点与视线目标
- 人物对信息的确认/误解/拒绝，以及冲动或控制策略
- 眉眼/眼睑/嘴角/下颌中一个主要面部变化
- 呼吸/肩颈/手部/重心中一个支持变化
- 公开状态与内部泄漏（如有），以及人物最终行动选择
- 表演强度，以及PL1 / PL2 / PL3最小充分载体负荷
- 结束时可继承的视线、呼吸、面部/身体张力、动作与情绪状态


先读取`knowledge/performance/micro_expression.md`执行Performance Progression Engine，再按需读取`facial_action_language.md`、`emotion_dynamics.md`与`expression_patterns.md`。PL1只选1—2个可执行载体；PL2选2—4个递进载体；PL3只在高压、崩溃或重大揭示授权时允许较完整链。禁止把六阶段当所有文戏固定时间轴，禁止只写“悲伤、愤怒、震惊、甜蜜、坚定”或PEX/AU编号，也禁止把瞳孔、脸红、落泪、露齿数和颤抖写成必然结果。


对白镜头还需说明：

说话者、倾听者、对白意图、反应顺序和口型容量风险。

嘴部表情、说话、哭笑、吞咽与呼吸必须排出先后；景别、遮挡和光线必须让关键表演证据可读。


---

## Sound Purpose


每个SHOT确认：

- 主要声音重点
- 持续环境声
- 关键动作声
- 对白或静默需求
- 与前后镜头的声音连接


Shot Design只规划为视频生成准备的生产声音：对白、环境声、动作声、呼吸、Foley与剧情内声源。它不规划后期音乐；只有用户显式调用独立MUSIC / SEED-MUSIC模块后，系统才另行进行专业Spotting、音乐与留白设计。


---

## FX Behavior


镜头存在FX时确认：

- FX ID或Inline Effect标记
- 触发与来源
- 本镜头中的效果阶段
- 对人物、环境、道具与光线的影响
- 结束状态与下一镜继承


---

## Coverage Mapping


存在Sequence Plan时，每个SHOT记录：

- Coverage Requirement IDs
- 本镜提供的可见完成证据
- Required / Supporting / Optional
- 与同一COV其他镜头的分工


禁止为了满足Coverage而新增剧情事实。


---

# Step 4

# Shot Boundary Design


每个SHOT在进入资产绑定前，必须先建立镜头边界合同。


按照rules/04_consistency_rules.md判定：

- Continuous Handoff
- Motivated Discontinuity
- Unresolved Handoff

判定完成后必须读取`knowledge/transitions/decision_engine.md`，只选择一种主要转场技术或保持Unresolved。默认Direct Cut；Match、遮挡、光效、FX或奇幻转场必须有真实锚点和上游依据。


每个SHOT必须设计：

## Start Boundary


首镜头从Scene初始状态建立。


其他镜头继承上一镜头结尾，或依据已确认的场景/时间/剪辑断点重新建立。


## End-Frame Constraint


锁定本镜头最后一帧的人物、空间、道具、动作、情绪、环境和摄影机状态。


禁止为下一镜提前安排动作。

若已有转场方案，还必须锁定Outgoing Anchor、Cut Point以及后期可用的稳定把手；运镜只有在存在明确切点和兼容下一镜锚点时才构成转场。


## Next-Shot Handoff


说明下一镜头如何继承、如何经断点进入，或在下一镜未知时保留什么安全锚点。

已知下一镜时记录一种主要转场技术、Incoming Anchor、继承/重建状态、禁止项和失败时的Direct Cut降级。同期Sound Bridge可辅助，但不得使用背景音乐或配乐。


如果下一镜尚未设计：

不得虚构下一镜内容。


在后续镜头确定时，必须成对复核本镜头结尾与下一镜开头。


---

# Step 5

# Asset Binding


每个SHOT必须绑定资产。


格式：


SHOT-001


Scene:

SCENE-001


Character:

CHAR-001


Environment:

ENV-001


Prop:

PROP-001


FX:

FX-001（如适用）



---

# Step 6

# Cinematic Logic Check


检查：


## Continuity


是否连接上一镜头。



## Motivation


镜头是否通过Shot Purpose Gate，至少形成Narrative、Emotional、Relationship、Spatial / Action、Information或Atmosphere中的一项具体变化 / 建立结果；完全无任务的镜头是否已合并或删除。



## Visual Flow


镜头是否推动剧情。


## Camera Language Integrity

检查：

- 每个SHOT是否先完成Camera Language Decision，且实际读取Selection Matrix、Camera Movement Index与被选主运镜原子文件
- 镜头目的、情绪功能、空间功能、人物运动和节奏阶段是否与推荐主运镜、辅助支持、禁止运镜、稳定等级和选择理由一致
- 是否出现没有独特叙事理由的默认“缓慢推进/轻微横移”，或连续SHOT只替换形容词而保持同一运镜模板

- 景别、机位角度、摄影机物理运动、光学变化、视点和剪辑关系是否分类正确
- Pan 与 Truck、Tilt 与 Crane、Push/Pull 与 Optical Zoom 是否被混用
- OTS、POV、Reverse Shot 是否保持人物身份、眼线与 180 度轴线
- 适用镜头是否已读取Interaction / Eyeline / Action Axis，标记camera safe side，并把左右、朝向、关系轴、摄影机轴线侧和来源—目标空间连线写成可画出的几何，而非抽象“面对对方”；双方同框时是否避免双正脸
- Spatial Blocking Decision是否与场景复杂度一致；Scene Spatial Snapshot是否锁定长期几何与固定环境锚点；双锁场景是否同时具备可读Top-down Map描述 / 图像和Text Spatial Rules，且正式SHOT没有推翻其角色路径、摄影机侧、关键道具或Clip首尾站位
- 反打、双人对话、并排坐、追逐和相向动作是否无意越轴；有意越轴是否使用中性镜头、观众可见的摄影机移动、角色明确换位或插入隔离后建立新轴线等可感知合法过渡，并在新safe side稳定重建方位
- 情绪用途是否有剧情与表演依据，而不是把镜头名称当作固定情绪公式
- Performance-dominant / Action-dominant / Mixed路由是否正确；PL1没有被强制扩成完整递进链，A1没有被强制扩成完整Kinetic Chain，A3关键Beat是否具有明确物理因果、恢复和Next-action Carryover
- 复合模式是否仍只有一个主要路径，并具有可执行降级方案
- “运镜组合”是否已区分一镜路径与多镜Coverage；低复杂度复合路径是否只有一次同向延续，Coverage / Transition Sequence是否已拆镜并交给Transition处理边界
- 构图是否拥有明确主体位置、层次、空间来源、焦点主次和结束几何关系
- 焦段、景别与摄影机距离是否被分别定义；透视、背景尺度和虚化是否有正确因果依据
- 连续覆盖是否保持兼容的脸部几何、摄影距离、背景尺度与对焦状态，焦段变化是否具有动机
- 色彩是否拥有真实来源、主次层级、饱和度与明暗控制、肤色/中性色保护和稳定结束色态
- 连续镜头是否保持综合色温、资产固有色、肤色、强调色位置与材质响应，变化是否有空间/光源/断点依据
- 反射、群体、复杂遮挡、FX与动作构图是否存在身份复制、空间融化、人物融合或剧情越权风险


## Coverage Completion


存在Sequence Plan时检查：

- 所有Required COV是否至少映射到一个SHOT
- 是否有SHOT不承担任何已确认功能
- 是否重复拍摄相同信息而没有新的视角、反应或结果
- UNIT边界是否拥有稳定的Exit与下一UNIT Entry



---

# Step 7

# Director Decision Notes


Professional Detailed Shot Script的全部Template字段、内部Camera Language Decision、Blocking、边界合同与Cinematic Logic Check全部完成后，STATE-06确认结束前必须读取并执行：

`knowledge/director_decision_layer.md`


按Scene / Shot Group生成内部`Director Decision Notes`。Notes必须直接读取本版专业分镜中的时间码、画面内容/构图、人物动作链、摄影机/镜头、摄影参数、镜头调度、光线/色彩、声音、AI制作备注与素材/资产，不得绕过正式分镜根据原剧本重新发明导演方向。Shot Group只表示同一Scene内承担同一主叙事推进、人物关系变化或情绪阶段的一组连续SHOT，不创建新ID、不重排SHOT，也不替代STATE-07的Clip边界。


每组Notes必须锁定十三个维度：

- Narrative Objective
- Audience Experience
- Character Relationship
- Blocking
- Camera Strategy
- Composition Strategy
- Lens / Distance
- Color & Lighting Strategy
- Performance Direction
- Sound Strategy
- Editing / Rhythm
- Continuity Risk
- Seedance Feasibility


并直接回答：

- 观众应知道什么、感受什么、等待什么
- 人物关系如何通过距离、视线、站位与动作变化表达
- 镜头应该动还是停，为什么；运动由什么触发并在哪里停止
- 色彩/灯光是否需要随剧情发生功能性变化；若保持不变，稳定保护什么
- 表演应外放还是克制，谁先泄漏、谁压住
- 声音哪里加强、哪里留白、尾部如何连接下一节拍


Director Decision Notes定义“为什么这样拍”和总体视听方向，不从Knowledge库预选技巧，不替代Camera Language Decision，也不重做已经确认的原子技术定义。若Notes表明现有SHOT的目的、Blocking、动/停、色光、表演、声音或边界不能服务导演意图，必须在STATE-06只修Affected SHOT及相邻边界并重新检查；不得把矛盾交给STATE-07或Prompt文案静默调和。


Notes默认不进入`templates/08_shot_design_prompt.md`的用户可见输出，也不新增Template字段。Work/Codex需要跨轮次持久化时，将其写入Active Project Root的`shots/director_decision_notes.md`或既有Execution Ledger；普通Chat保留在当前Workflow内部上下文。用户明确要求查看时，只另行提供简洁决策摘要，不展示逐步隐式推理。


---

# Completion Requirement


完成Shot Design必须满足：


□ 所有镜头拥有SHOT ID

□ 每个Scene已在正式分镜前完成Spatial Blocking Decision，并保存Decision Factors、Map Mode、Scene Spatial Snapshot、Structured Blocking Map、Text Spatial Rules、Clip Boundary Spatial Ledger与状态

□ 单人无走位 / 简单双人静态只用文字时具有明确理由；双人明显走位、3人以上、打斗 / 追逐 / 多人进出、复杂道具空间、连续多Clip或严格180度轴线场景已优先双锁，或记录用户拒绝 / 工具不可用的Structured Text Fallback与风险

□ 所有Spatial Blocking结果完整标注场景边界、固定环境锚点、A/B/C起终点与路径、C1/C2/C3位置 / 朝向、Interaction / Eyeline / Action Axis、camera safe side、合法越轴方式、关键视线、Clip首尾站位及Previous Clip End State → Next Clip First Frame Reference

□ 每个SHOT已通过Shot Purpose Gate，至少承担一项具体变化 / 建立任务；无任务SHOT已合并或删除，内部任务标签没有进入最终Seedance Prompt

□ 每个SHOT / Group已完成Performance-dominant / Action-dominant / Mixed路由；Performance按PL1/PL2/PL3选择最小充分载体，Action按A1/A2/A3选择最小充分物理展开，Mixed没有机械叠加两套完整链

□ 正式输出为`Professional Detailed Shot Script`，每个SHOT均完整填写`templates/08_shot_design_prompt.md`当前定义的全部字段

□ Artifact Status为Confirmed且具有唯一Artifact Revision；STATE-07只能引用该Artifact与匹配Revision

□ 单镜输出与批量输出结构完全同构；没有因批量交付删字段、合并字段、缩写/改名字段、使用简化表头、空白或“同上/沿用/略”等替代内容

□ 每个SHOT均可独立定位最低语义覆盖：Shot编号、时间、场景、景别、镜头/机位、焦段、构图、人物位置关系、画面描述、人物情绪、动作重点、台词、音效、环境声、光线/色彩、转场逻辑、角色一致性、环境一致性、道具一致性、生成风险/控制项

□ 全部SHOT无法单次完整容纳时已自动按完整Shot分批；默认每批4—5镜并按实际长度调整，批次间无拆镜、遗漏、重复或重排，最后一批之前未用汇总代替逐镜内容

□ 全表使用统一timebase；每镜`TC OUT - TC IN = 时长(s)`，相邻镜时间码可复核，时间码与动作/对白/稳定尾帧容量一致

□ 每镜`画面内容/构图`均明确前景/中景/背景、主体位置、焦点层次及适用的遮挡/反射/景深/负空间；没有只写单层居中或抽象“电影感”

□ 每镜`人物动作`均为可观察的动作与表演链，包含起始、刺激/注意、反应、动作选择与稳定结束状态

□ A3关键动作具有可见触发、动力传递、轨迹、接触 / 近接触、反馈、惯性 / 恢复与Next-action Carryover；A1简单动作保持起点—路径 / 变化—终点，没有无效工程参数

□ 每镜`镜头调度`均完整记录摄影机运动、人物调度、两者配合/触发关系和镜头结束状态；没有只写运镜名

□ 每镜`光线/色彩`均写明真实来源、可见控制、叙事功能、变化触发或稳定理由，以及结束光色态；没有只写冷暖/饱和度标签

□ 每镜`同期声音设计`均完整记录环境声、同步前景声与声音尾部，且没有任何背景音乐、配乐、BGM、主题音乐、氛围音乐、歌曲或“无配乐”说明

□ 每镜`AI制作备注`均保存起始边界、稳定尾帧、下一镜衔接、执行风险/负荷、稳定降级、Coverage与禁止项；每镜`素材/资产`均引用Active Canonical版本与用途


□ 所有镜头绑定Scene


□ 所有镜头绑定资产


□ 所有镜头包含摄影参数

□ 所有镜头均已确认Camera Language Decision，包含镜头目的、情绪功能、空间功能、人物运动、节奏阶段、推荐主运镜、可选辅助、禁止运镜、Seedance稳定等级、选择理由与实际读取的原子知识证据

□ 所有适用运镜组合已完成一镜/多镜分类；每个正式SHOT只有一个主要路径或一次兼容延续，拆镜后Required Coverage没有丢失

□ 所有镜头包含可执行焦段倾向、摄影机距离、空间结果、对焦/景深与运动约束

□ 所有适用镜头包含可执行综合色彩来源、层级、饱和度、明暗/偏色、肤色保护与连续性


□ 所有镜头包含可执行Composition Intent及必要降级方案

□ 所有战斗、双主体、对峙、对话、追逐与相向运动镜头均已完成Relational Screen Geometry锁定；首帧与尾帧几何可复核，攻击/视线/水流等来源—目标方向一致

□ 反打、双人对话、并排坐、追逐与相向运动均保持已建立camera safe side，或记录了可感知、可解释、可连续的合法越轴与新轴线重建；没有把“永不越轴”误作全局禁令

□ Professional Detailed Shot Script已把Confirmed Spatial Blocking Result投影到现有Template字段，没有新增表头，也没有把Top-down Blocking Map列为Canonical / STATE-08参考资产


□ 所有镜头具有动作目标


□ 有人物的镜头具有可观察的表演目标与结束状态


□ 所有镜头已确定声音重点或明确静默/无特殊声音设计


□ 存在FX的镜头已绑定FX并建立本镜头效果阶段与边界状态


□ 存在Sequence Plan时，所有Required COV已映射到SHOT且UNIT边界可执行


□ 所有镜头包含Transition Class、Start Boundary、End-Frame Constraint与Next-Shot Handoff

□ 所有已知相邻镜头只选择一种主要转场技术，具备真实出/入镜锚点与可执行切点；未决镜头没有猜测


□ 相邻镜头已经成对检查，叙事断点没有被误写为连续动作

□ 每个Scene / Shot Group均已生成当前有效的Director Decision Notes，十三个维度完整或具有明确Not Applicable理由

□ 每组Notes均已回答观众知道/感受/等待、关系调度、镜头动/停、功能性色光、表演尺度和声音加强/留白；不存在只写风格标签、技巧名称或“为了电影感”

□ Director Decision Notes与Detailed Shot Design、Camera Language Decision、边界合同和Seedance容量一致；若发生冲突，已在STATE-06完成最小修订

□ Director Decision Notes保持内部可消费，没有成为新STATE、新ID、用户可见固定章节或STATE-08最终字段



---

# State Update


完成后：


更新：

project_status.md

它表示按优先级选定的State Source；普通Chat本机Root不可读时使用Portable State。更新服从references/project_state_contract.md，登记Shot Artifact、Execution Risk结果、Checkpoint与Revision ID，并按环境同步或输出更新后的完整Portable State，执行其`Portable Required Field Writeback`。



状态：


STATE-06 Complete



允许进入：


STATE-07 Clip Production



---

# Forbidden


禁止：


直接生成Seedance Prompt。


直接生成最终视频。


跳过Clip Production阶段。



---

# Output Format

最终输出必须使用：

templates/08_shot_design_prompt.md

Workflow负责Spatial Blocking Decision、镜头判断、参数设计、时间码核算、边界合同、Coverage映射和完成门槛；Template独占Professional Detailed Shot Script的全部用户可见字段、顺序、编号和排版。

单镜交付与批量交付必须执行同一Template结构。多批输出的批次范围、续批Checkpoint和自动继续策略只改变交付切片，不改变Template Schema；默认每批4—5个完整SHOT，可按实际长度调整。

本Workflow中的参数章节只定义必须准备的语义，不得作为另一套输出Schema。

Director Decision Notes属于STATE-06末端内部决策记录，由STATE-07/08读取；它不改变`templates/08_shot_design_prompt.md`的输出Schema，也不随正式Shot Design默认直接展示给用户。

完成后由project_status.md把Next Workflow指向10_clip_production_workflow.md。STATE-06 的 Confirmed Detailed Shot Design 是 STATE-07 的直接输入，不再插入固定 Shot Execution Plan 或 Storyboard 阶段。
