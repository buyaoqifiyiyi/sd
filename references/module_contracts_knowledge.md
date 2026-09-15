# SD Film Module Contracts — Knowledge Contracts

> Skill维护层：只在修改本Skill时读取，不参与影视生产。

本文件是模块接口合同的一部分；Authority Matrix 与 Stable Interface Rules 留在 `references/module_contracts.md`。本文件不拥有归属判定，也不得复制该框架。

## Performance Expression Knowledge Contract

Module Type：STATE-04、STATE-06至STATE-09辅助Knowledge。

触发：镜头包含人物注意、反应、情绪变化、对白倾听、压抑/伪装、哭笑、群体反应、身体状态影响表演，或Scene / Shot Group / Clip需要核对跨镜Performance Arc与相对表演层级。

输入拥有者：Script / Scene事实、Character Asset与基线、人物关系、Shot Purpose、Action / Blocking、Dialogue / Sound、Camera / Composition、Lighting与边界状态。

输出拥有者：STATE-04由Project Bible表演字段拥有；STATE-06由Shot Design Template拥有；STATE-08由Selected Model对应的唯一Template拥有。

下游消费者：Detailed Shot Design、Clip Production、Video Generation、Review。

不变量：

- 内部表演模式只使用PEX-01至PEX-36，最终Prompt不得输出PEX或AU编号
- 每个情绪变化必须有已确认刺激、注意变化、至少一项可见反应、行动选择与稳定结束状态
- 每个相关角色在Scene / Shot Group层使用内部Performance Arc Map核对Inherited Baseline、Trigger、Pre-action / In-action / Post-action Residue、Arc Endpoint与Next-shot Carryover；单SHOT只投影当前可见段，不创建Template字段
- Intentional Hold必须保留注意目标、压制/延迟、呼吸/姿态或行动证据；静态情绪标签与固定脸完成动作不构成有效表演
- 多人场景必须明确Primary Performer、Secondary Reactor / Listener / Background Holder、反应顺序、相对幅度与视觉重点交接；除非剧情授权，不得全员同强度表演或全员同脸冻结
- 连续镜头继承视线目标、呼吸、面部/身体张力、泪液/红肿等可见后果与控制/泄漏状态
- 表演语义映射到现有Template字段，不创建Expression或Performance最终字段

禁止：

- 把喜怒哀乐或模式名称当作完整表演指令
- 把固定脸型、瞳孔、脸红、露齿数、落泪或颤抖当作情绪必然结果
- 用表情新增人物关系、心理诊断、剧情刺激、台词、动作结果、光线或色调
- 与Character Asset、Action / Blocking、Dialogue / Sound、Lighting建立重复原子定义

冲突时：项目表演尺度返回STATE-04；角色身份/基线返回Character Asset拥有者；动作、对白容量、景别或逐镜表演节拍返回STATE-06。

---

## Camera Movement Selection Matrix Knowledge Contract

Module Type：STATE-06至STATE-09辅助Camera Knowledge，不创建新STATE。

触发：所有正式SHOT的Camera Language Decision、所有Clip Movement Plan、STATE-08运镜语义投影与STATE-09 Camera Language QA。

不触发：不独立改写剧情、资产、导演风格、Shot Purpose、SHOT / CLIP顺序或Seedance最终Schema。

输入拥有者：Shot Purpose、情绪/表演、人物运动、Blocking / Relational Screen Geometry、空间任务、节奏阶段、Visual Direction、模型复杂度与边界合同分别由对应上游事实和设计拥有者提供。

输出拥有者：STATE-06由`templates/08_shot_design_prompt.md`拥有；STATE-07由`templates/20_clip_plan.md`拥有；STATE-08由Selected Model对应的唯一Template拥有。

允许读取：`knowledge/camera_language/camera_movement/selection_matrix.md`、Camera Movement Index、被选主/辅助运镜原子文件，以及适用的Movement Combination / Advanced Camera Movement。允许写入：当前阶段拥有者管理的Detailed Shot Design、Clip Production Plan与内部Projection / QA结果。

下游消费者：STATE-06 Detailed Shot Design、STATE-07 Clip Production、STATE-08 Clip-based Video Prompt / Video Generation与STATE-09 Review。

不变量：每SHOT先做Camera Language Decision；每Clip有主导镜头语言与重复/复杂度控制；超过4个Shot时通常至少2种运镜逻辑；同类主运镜连续3次以上需要逐镜叙事理由；不强制每镜不同；基础稳定运镜优先；复杂Orbit / 360、穿墙、无人机和多段一镜到底受叙事必要性、模型容量与降级门控。

禁止：未检索就默认“缓慢推进/轻微横移”；随机堆叠运镜；把稳定等级、Decision或Clip Movement Plan变成STATE-08新字段；用运镜选择静默修改轴线、剧情、资产或Shot Purpose。

冲突时：逐镜目的、Blocking、轴线、动作容量或主运镜返回STATE-06；Clip编排返回STATE-07；仅执行转译问题留在STATE-08；资产或剧情事实返回其拥有者。

---

## Transition Knowledge Contract

Module Type：跨镜头边界与转场选择Knowledge。

输入拥有者：`rules/04_consistency_rules.md`判定的Boundary Class，以及Detailed Shot Design、Clip Production Plan、Sequence和已确认资产/FX事实。

输出拥有者：Shot Design的边界合同与`templates/10_video_prompt.md`现有字段。

必须：

- 先判定Continuous Handoff、Motivated Discontinuity或Unresolved Handoff，再选择一种主要转场技术
- 记录Outgoing Anchor、Cut Point、Incoming Anchor、继承/重建状态、禁止提前动作与Direct Cut降级
- 投影到上一G段前置【尾帧限制】、下一G段【首帧参考】、按空间/动作连续性条件决定的【参考资产】正式引用，以及上一镜“镜头结尾状态”和下一镜“起始状态”；跨场景时上一尾帧通常不进入下一段【参考资产】，只作人物与视觉连续性核对
- 同期声音桥只使用对白、环境声、动作声、呼吸、Foley或剧情内声源
- 同一Clip内使用逐镜状态链；跨Clip明确A/B/C。A/B在下一Package【参考资产】列统一`REF-TAIL`、对应用途与真实状态，缺图时标“待用户提供/待上传、未确认”，Prompt可交付但生成前补图；A使用Direct固定句，B明确另起新镜头且不使用该句；C不列`REF-TAIL`并使用Canonical资产、Spatial Blocking与文字End State承接或重建

禁止：

- 新增STATE-08“转场”字段或输出TRN内部ID
- 改写Boundary Class、剧情、资产、站位、道具或镜头目的
- 把普通运镜直接命名为转场
- 无依据新增光源、介质、FX、魔法或场景变形
- 使用背景音乐、配乐或歌曲建立STATE-08声音转场

---

## Shot Size And Framing Knowledge Contract

Module Type：STATE-04、STATE-06至STATE-09辅助Camera Knowledge，不创建新STATE。

触发：需要确定取景尺度、景别名称、信息距离、特写与局部的裁切范围，或核对连续镜头的景别继承与尺度一致性。

输入拥有者：Shot Purpose、Audience Attention、Composition Strategy、Camera Position / Distance、Blocking / Spatial Lock、Focal Length与资产身份分别由对应上游事实和设计拥有者提供。

输出拥有者：STATE-04由Project Bible摄影方向拥有；STATE-06由`templates/08_shot_design_prompt.md`的`景别`字段拥有；STATE-07由`templates/20_clip_plan.md`拥有；STATE-08由Selected Model对应的唯一Template拥有。

下游消费者：Detailed Shot Design、Clip Production、Optional Storyboard、Video Generation与Review。

不变量：

- 规范景别的唯一owner是`knowledge/camera_language/lens_language/framing_and_scale.md`；其他文件只引用它，不维护平行景别清单
- 规范景别为大全景 / 远景 / 全景 / 中景 / 中近景 / 近景 / 特写 / 大特写；局部镜头与细节插入镜头是并列的取景类型
- 景别只记录可见取景尺度，不决定摄影机运动、焦段或情绪
- 同一景别可由静态机位、真实位移或剪辑获得，三者必须在Shot Design中分开说明
- 景别越近，身份来源、眼线、裁切范围与动作数量越需要明确；近不等于复杂
- 大全景与远景必须写出人物与门、车辆、建筑之间可复算的相对比例

禁止：

- 只写“人物居中”“电影感构图”，或用“特写”指代未说明的拍摄方式
- 把景别当作情绪的固定公式，或把焦段当作景别的同义词
- 用极端裁切掩盖未确认的身份、空间或轴线事实
- 为匹配景别语义新增人物、地点、动作或资产事实

冲突时：项目级摄影方向返回STATE-04；逐镜景别、机位、距离、对焦或动作容量返回STATE-06；Clip编排返回STATE-07；资产身份或空间事实返回其拥有者。

---

## Focal Length Knowledge Contract

Module Type：STATE-04、STATE-06至STATE-09辅助Camera Knowledge。

触发：需要确定焦段倾向、摄影机距离、同景别透视、景深/对焦、边缘安全、长焦叠层或焦段连续性。

输入拥有者：Visual Direction、Shot Purpose、Shot Scale、Camera Position / Movement、Composition、Blocking、Lighting、Performance与空间连续性。

输出拥有者：STATE-04由Project Bible摄影方向拥有；STATE-06由Shot Design Template拥有；STATE-08由Selected Model对应的唯一Template拥有。

下游消费者：Detailed Shot Design、Clip Production、Video Generation、Review。

不变量：

- 内部焦段模式只使用FLN-01至FLN-07，最终Prompt不得输出FLN编号
- 未确认画幅时，毫米数只作为全画幅等效倾向，不作为硬件事实
- 焦段选择必须与摄影机距离、景别、空间效果、对焦/景深和运动约束共同定义
- 透视由摄影机位置决定；虚化由多项变量共同决定；焦段不自动提升质感
- 焦段语义映射到现有Template字段，不创建Lens或Focal Length最终字段

禁止：

- 把焦段当作景别、情绪、透视、压缩、虚化或电影感的单一原因
- 为匹配附件示例新增人物、地点、动作、情绪或器材事实
- 与Camera Movement、Composition、Lighting、Performance或Optical Zoom重复定义
- 用随机焦段变化破坏脸部几何、背景尺度、眼线、轴线和连续性

冲突时：项目级焦段体系返回STATE-04；逐镜景别、机位、运动、对焦或动作容量返回STATE-06；资产或空间事实返回其拥有者。

---

## Color Knowledge Contract

Module Type：STATE-04、STATE-06至STATE-09辅助Knowledge。

触发：项目或镜头需要综合色彩体系、主辅强调色、饱和度、明度/对比、白平衡/偏色、肤色/中性色保护、材质综合色彩响应或跨镜色态连续性。

输入拥有者：已确认Character / Environment / Prop / FX Asset、Visual Direction、Lighting、Shot Purpose、时间/天气、材质与边界状态。

输出拥有者：STATE-04由Project Bible Color System拥有；STATE-06由Shot Design Template拥有；STATE-08由Selected Model对应的唯一Template拥有。

下游消费者：Detailed Shot Design、Clip Production、Video Generation、Review。

不变量：

- 内部模式只使用CLR-01至CLR-09，最终Prompt不得输出CLR编号
- 每个适用色调必须同时定义综合色彩来源、色相层级、饱和度、明度/对比、白平衡/偏色、肤色/中性色保护和稳定结束色态
- 连续镜头保持资产固有色、肤色、中性色、综合色温、饱和度与材质响应连续
- Color语义映射到现有Template字段，不创建Color或色调最终字段

禁止：

- 把色调名称当作固定情绪、题材、人物状态或完整Prompt
- 用调色新增光源、环境、服装、道具、FX或改变资产固有色
- 把暗调写成欠曝、把高饱和写成全局拉满、把糖果/清透写成过曝磨皮
- 与Lighting、Exposure、Texture、Asset或Performance重复定义原子职责

冲突时：项目级色彩体系返回STATE-04；资产固有色返回对应资产拥有者；光源/曝光返回Lighting；逐镜色态与动作容量返回STATE-06。

---

## Camera Movement Combination Knowledge Contract

Module Type：STATE-06至STATE-08辅助Camera / Coverage Knowledge。

触发：镜头描述包含两种以上摄影机运动、多个景别/机位/视点、“镜头顺序”、一镜到底、动作Coverage或跨时空组合。

输入拥有者：Shot Purpose、Coverage Requirement、Camera原子、Blocking、Performance、Lens、FX、Sequence与Transition Boundary。

输出拥有者：STATE-06由Shot Design Template拥有；STATE-08由Selected Model对应的唯一Template拥有。

不变量：

- 内部模式只使用CMG-01至CMG-16，最终Prompt不得输出CMG编号
- 先判定Single-Move、Low-Complexity Compound Path、Coverage Sequence或Transition / FX Sequence
- 每个正式SHOT默认只有一个主要摄影机路径；复合路径最多包含一次同向、有动机、同轴、同平台的延续
- 多景别、多视点、新刺激—反应节拍、换侧/越轴、时空变化或不同FX阶段必须拆镜
- 组合语义映射到现有Template字段，不创建Movement Combination最终字段

禁止：

- 把景别、机位、视点、对焦、慢动作、FX或剪辑全部命名为运镜
- 为套用附件模式新增人物关系、情绪、武器、法术、泪水、光源、地点或时间变化
- 把普通摄影机运动直接当作转场，或把多个正式SHOT伪装成一个短镜头
- 牺牲Required Coverage、表演可读性、轴线、焦段连续性或稳定终点

冲突时：Coverage返回Sequence / STATE-06；Camera原子返回对应Camera Knowledge；边界返回Transition；FX和Performance返回其事实拥有者。

---

## Lighting Knowledge Contract

Module Type：STATE-04、STATE-06至STATE-08辅助Knowledge。

触发：时间、天气、环境实用光源、人物受光、明暗关系、光线变化、反射或参与介质影响镜头可见结果。

输入拥有者：Visual Direction、Environment / Character / Prop / FX Asset、Shot Purpose、空间与边界连续性。

输出拥有者：STATE-04由Project Bible对应字段拥有；STATE-06由Shot Design Template拥有；STATE-08由Selected Model对应的唯一Template拥有。

下游消费者：Detailed Shot Design、Clip Production、Video Generation、Review。

不变量：

- 内部模式ID只能为LGT-01至LGT-20，最终Prompt不得输出模式ID
- 每个适用光影设计必须有已确认或可由环境成立的光源/介质依据
- 连续镜头保持光源空间锚点、方向、光质、综合色温关系与动态状态连续
- 光影语义必须映射到现有Template字段，不创建Lighting最终字段

禁止：

- 把浅景深、运镜、构图、调色、FX或情绪表演重复定义为灯光原子
- 用“电影感、高级感、压迫感”等抽象标签代替光源、方向与可见结果
- 为套用模式新增灯具、火焰、雾、雨、水、车辆、招牌或剧情反应
- 静默修改时间、天气、环境结构、资产状态或镜头目的

冲突时：项目级光线体系返回STATE-04；环境/实用光源/介质资产返回其事实拥有者；逐镜执行与动作容量返回STATE-06。

---

## Camera Composition Knowledge Contract

Module Type：STATE-06至STATE-08辅助Knowledge。

触发：镜头需要构图、视点、空间层次、人物关系、动作路线或氛围组织。

输入拥有者：Shot Purpose、Scene、已确认资产、Visual Development、Performance、FX与空间连续性。

输出拥有者：STATE-06由对应Shot Design Template拥有；STATE-08由Selected Model对应的唯一Template拥有。

下游消费者：Detailed Shot Design、Clip Production、Video Generation、Review。

禁止：

- 把图片“适配情节”当成剧情事实
- 用构图模式新增枪火、爆炸、人物关系或环境事件
- 与Camera Angle、Movement、Perspective、Lens、FX或Performance建立重复原子定义
- 创建新的最终Prompt字段

不变量：

- **交付画幅**（横屏 / 竖屏）由`knowledge/camera_language/composition_language/vertical_framing.md`拥有；相机成像画幅（全画幅等效倾向）由 Lens 目录拥有，两者不得互相推断
- 竖屏双人布局一次只用一种（过肩前后错位 / 上下错位 / 纵深分离），不横向挤三人以上
- 不得用裁切在横竖画幅之间转换；同一项目内不同Clip不混用交付画幅，切换画幅属交付规格变更需用户确认
- 平台安全区不得虚构数值；平台未确认时只写避开顶部与底部安全边带
- 资产图比例由`rules/02_asset_rules.md`的`Asset Canvas Ratio Default｜资产图画幅默认`拥有，本目录不重复定义

---

## Quality Knowledge Contract

Module Type：STATE-06至STATE-09辅助Knowledge。

输入拥有者：已确认资产、Detailed Shot Design、Clip Production Plan、Prompt、生成结果与边界合同。

输出拥有者：正式Review由templates/16_review_report.md拥有；内部QA可进入Execution Ledger。

必须执行Shot QA、相邻镜QA、Execution Risk和适用的Prompt Scorecard。禁止用分数覆盖Hard Gate、把QA字段写入STATE-08 Prompt或用审美偏好改写剧情事实。

审美判据与判定纪律的唯一owner是`knowledge/quality/aesthetic_judgement.md`：它只覆盖"取舍是否可见"这一半，系统只输出观察证据，**审美结论必须由用户给出**，且"判据全过"不得当作"好看"的证明。`prompt_scorecard.md`（STATE-08，对象为Prompt文本）与`workflows/13_review_workflow.md`（STATE-09，对象为成片）只引用它，两处都不得复制其判据正文，也不得合并两处。

---

## Medium Profile Knowledge Contract

Module Type：STATE-00登记、STATE-01的`Production Setup Gate`确认、STATE-01与STATE-04消费的跨媒介Knowledge；不创建新STATE、不新增Template字段。

Owner：`knowledge/medium_profiles.md`。STATE-00只登记用户已明确输入的值；确认与写入发生在STATE-01的`Production Setup Gate`，结果写入`project_bible.md`的`Project Information → 媒介形式`字段；本文件拥有该字段的值域与三档分化规则。

触发：项目`媒介形式`为`live_action` / `3d_animation` / `2d_anime`时，在STATE-01（编剧承载）与STATE-04（美学与摄影方向）读取；为`Pending`时记录`Medium Profile: PENDING`并把决定返回STATE-01的`Production Setup Gate`，不加载分化表，且`Pending`不得穿过STATE-02 / STATE-03的媒介相关资产生产。

不触发：不因Genre、题材、平台或画风标签加载；Storyboard、Poster、Sequence、MUSIC、AUDIO等辅助模块不因本Knowledge改变各自既有边界。

不变量：

- 三档ID固定为`live_action`、`3d_animation`、`2d_anime`，不得新增第四档或改名
- 媒介与Genre正交，两者不得互相覆盖
- `2d_anime`不得指定焦段毫米数、光比比值、器材或真实景深；`3d_animation`不得沿用实拍光比捕捉语言
- 媒介分化只改变既有Template字段的表达方式，不新增任何字段
- 一个媒介的资产不得静默用于另一个媒介

禁止：把媒介当成Genre子类；从平台或题材推定媒介；用本Knowledge改写剧情事实、资产身份或STATE-08 Schema。

冲突时：媒介决定本身缺失、为`Pending`或冲突时返回STATE-01的`Production Setup Gate`；资产身份返回资产拥有者；逐镜镜头语言返回STATE-06；项目级美学方向返回STATE-04。

---

## Genre Profile Knowledge Contract

Module Type：STATE-00登记、STATE-04消费、STATE-05 / 06 / 08按需回读的跨类型Knowledge；不创建新STATE、不新增Template字段。

Owner：`knowledge/genre/index.md`是登记表、共享Genre File Schema、加载规则、正交声明、反公式边界与共享不变量的唯一owner；`knowledge/genre/01_mystery_thriller.md`至`knowledge/genre/06_crime.md`是它登记的类型文件。类型由STATE-00在`templates/00_project_start_template.md`的`## Genre`登记；本模块拥有登记表的Profile ID与每个类型的**呈现层倾向**。

触发：项目`类型`已登记时，在STATE-04建立或修订`Visual Grammar Baseline`时读取命中的类型文件；STATE-05 / 06 / 08消费已锁定的基线，只在当前Scene / Shot的类型兑现出现真实分歧时定点回读对应类型文件的对应小节。

不触发：`类型`为`PENDING`时不加载，且不得从媒介、平台、题材标签、画风或参考片推定类型；Poster的类型倾向由`knowledge/poster_design/genre_tendencies.md`拥有，本模块不替代它；Storyboard、Sequence、MUSIC、AUDIO等辅助模块不因本Knowledge改变各自既有边界。

不变量：

- Profile ID固定为`mystery_thriller` / `action` / `romance` / `comedy` / `horror` / `crime`，不得改名或新增同义ID；登记表与`knowledge/genre/`下的文件一一对应
- 每个类型文件必须齐备九节共享Schema，其中`## When Not To Apply｜反公式边界与失败信号`为必答项
- 类型知识只提供带条件的候选手段，不得写成固定节拍模型、冲突公式或跨项目原则
- 类型与媒介正交、与导演风格正交，任何一条不得覆盖另一条
- 不改变STATE-08 Schema、不新增Template字段、不改写Production-Locked Script / Writer Intent / Director Intent / Canonical资产 / 已确认Blocking
- 视频Prompt永久禁止非剧情内配乐，类型不构成例外

禁止：用类型替代Writer / Director判断；把单项目做法升级为通用规则；用类型知识解释或改写剧情事实；以"类型需要"为由绕过Completion Gate、资产锁、Reference Budget或任何硬停点。

冲突时：类型登记缺失或冲突返回STATE-00的项目登记；类型承诺与已锁定剧本冲突返回Writer Owner（`knowledge/screenplay_development.md`）；项目级呈现取舍冲突返回STATE-04；逐镜呈现冲突返回STATE-06；媒介相关表达在非实拍档不成立返回`knowledge/medium_profiles.md`。

---

## Drawn-Medium Language Knowledge Contract

Module Type：`2d_anime`档的镜头语言等效与画风一致性Knowledge；STATE-04与STATE-06消费；不创建新STATE、不新增Template字段。

Owner：`knowledge/anime_language/index.md`是登记表、共享Atom Schema、加载规则、共享不变量与可校验不变量的唯一owner；`knowledge/anime_language/01_layout_and_space.md`至`knowledge/anime_language/04_style_and_consistency.md`是它登记的原子。本域是`knowledge/camera_language/index.md`（Camera Language Module唯一owner）在绘制媒介下的**分化**，不是第二套镜头语言路由。

触发：`媒介形式`确认为`2d_anime`时，在STATE-04（美学与摄影方向）与STATE-06（逐镜设计）按命中原子的对应小节读取；STATE-07的Clip连续性与STATE-08的Prompt编译消费已确认结果，不重新选择。角色资产形态改按`templates/04_character_asset_prompt.md`的`#### 2D Character Asset Sheet Prompt｜设定集与画风锚`。

不触发：`live_action`与`3d_animation`不加载（`3d_animation`的虚拟光学按既有实拍知识执行，不得借用绘制媒介词汇）；媒介为`Pending`时不加载，也不得从类型、平台、题材标签或画风推定媒介。

不变量：

- 不得写入焦段毫米数、光比比值、光圈、真实景深、轨道/摇臂/稳定器、云台、胶片型号等实拍专有量
- 轴线、银幕方向、视线匹配、人物拓扑与 Relational Screen Geometry 继续由既有owner拥有，本域不重建
- 一次运镜只允许一个方向与一个触发；透视不随版面平移旋转
- 冲击手段（smear / impact frame / 集中线）同一次冲击只用一种，同Clip不超过一次
- 线宽、上色法、网点/笔触在STATE-04一次锁定，跨镜只继承不重选
- 不新增STATE-08字段、不改变主Pipeline、不改变任何Model Adapter能力数值
- 视频Prompt永久禁止非剧情内配乐
- 2D角色资产形态由`templates/04_character_asset_prompt.md`拥有，本域只引用

禁止：用本域替代镜头必要性与运动触发判断；把实拍词表换成"感觉相近"的形容词继续写入；以"这是2D"为由放宽Completion Gate、资产双确认或Reference Budget。

冲突时：媒介缺失 / `Pending` / 冲突返回STATE-01的`Production Setup Gate`；模块路由、镜头必要性与人物拓扑返回`knowledge/camera_language/index.md`；轴线与空间关系返回`knowledge/spatial_blocking_layer.md`；项目级美学与画风基线返回STATE-04；角色资产结构返回`templates/04_character_asset_prompt.md`；逐镜冲突返回STATE-06。

---

## Period And Place Knowledge Contract

Module Type：时代与地域的可见约束与一致性Knowledge；STATE-02至STATE-08按阶段消费；不创建新STATE、不新增Template字段。

Owner：`knowledge/period_and_place/index.md`是登记表、共享Atom Schema、加载规则、考据纪律与可校验不变量的唯一owner；`knowledge/period_and_place/01_era_visibility.md`至`03_period_consistency.md`是它登记的原子。时代与地域作为**项目事实**由用户与已确认项目材料拥有，记录在`templates/01_project_bible_template.md`的`# 2. World Building`。

触发：`## Time Period`或`## Location System`已登记时，在STATE-02 / STATE-03（资产形制与不可变项）、STATE-04（时代基线与光线、声音方向）、STATE-06与STATE-08（逐镜与Prompt投影）按命中原子的对应小节读取。

不触发：两者均未登记时记`Period And Place: PENDING`，不加载，也不得从媒介、类型、平台、导演风格名、参考片或资产外观推定；现代题材同样需要确认。

不变量：

- 任何结论必须落在已确认来源 / 合理推断（须显式标注）/ 不可确认三类之一；不得把常识当史实
- 真实历史人物、真实机构、真实事件与真实品牌是一等禁项，与`rules/automation_mode.md`的Hard Stop同一口径
- 时代技术边界是硬事实：不得为可看性引入该时代不存在的技术类别；风格化只改变呈现方式，不改变技术类别
- 时代与地域冲突时以时代优先并记录让位
- 与媒介、类型、导演风格正交，任一轴不得覆盖另一轴；风格层的"不得擅自添加时代符号"与本域不互相替代
- 反刻板：地域不得靠符号清单表达，优先空间关系、称谓、身体距离与日常器物
- 时代基线与地域基线一次锁定（STATE-04与World Building），跨镜只继承；改变基线属项目事实变更
- 不新增STATE-08字段、不改变主Pipeline、不改变任何Model Adapter能力数值
- 视频Prompt永久禁止非剧情内配乐

禁止：用本域改写剧情事实或世界设定本身；把推断写成史实；用"风格化"豁免事实错误；以"时代需要"为由绕过Hard Stop、资产双确认或Reference Budget。

冲突时：登记缺失 / 冲突返回STATE-00与`templates/01`的World Building字段；剧情与世界设定返回Writer Owner；美学方向返回STATE-04；资产形制最终仲裁返回对应资产owner与`references/asset_lock_contract.md`；媒介表达返回`knowledge/medium_profiles.md`。

---

## Branded Content Knowledge Contract

Module Type：品牌诉求的呈现转译与商业事实边界Knowledge；STATE-01、STATE-04、STATE-06与STATE-08按阶段消费；不创建新STATE、不新增Template字段、不新建节拍模型。

Owner：`knowledge/branded_content/index.md`是登记表、共享Atom Schema、加载规则、商业事实纪律与可校验不变量的唯一owner；`knowledge/branded_content/01_brand_requirement_translation.md`至`03_form_and_delivery.md`是它登记的原子。品牌诉求作为**项目事实**由用户与已确认项目材料拥有，登记于`templates/00_project_start_template.md`的`# Input Material`。

触发：项目存在**已确认**品牌诉求或商业目标时，在STATE-01（诉求与目标形式）、STATE-04（品牌调性进入`Visual Grammar Baseline`）、STATE-06与STATE-08（产品可读性与呈现落点）按命中原子的对应小节读取。

不触发：普通叙事项目不加载，也不得从项目时长、平台、题材或道具品牌推定其为商业片；品牌诉求未确认时不加载，也不得自行补写品牌目标。

不变量：

- 真实价格、SKU与组合、可读品牌/Logo文字、功效与资质表述、受监管承诺、免责声明、授权人物与声音是**一等禁项**，不得由制作推断或生成，与`rules/automation_mode.md`的Hard Stop同一口径
- 资产侧三类归类由`workflows/03_asset_discovery_workflow.md`的`## Commercial Fact Triage`唯一拥有，本域只引用
- 不新建节拍模型：短剧 / 竖屏剧情 / 1—3分钟的节奏适配仍由`knowledge/adaptation/short_form_drama_adapter.md`拥有
- 时长由用户或已确认交付规格给定；不得按固定秒数分配段落
- 商业目标不拥有剧情事实：不得为露出改写Production-Locked Script、Canonical资产或已确认Blocking
- 与媒介、类型、时代地域三条轴正交，任一轴不得覆盖另一轴
- 不新增STATE-08字段、不改变主Pipeline、不改变任何Model Adapter能力数值
- 视频Prompt永久禁止非剧情内配乐
- 商业片不豁免资产双确认、Completion Gate、Reference Budget与任何Hard Stop

禁止：用画面替代缺失的商业事实；以“客户要快”为由绕过任何Gate；把普通叙事项目改造成商业片。

冲突时：商业事实缺失或冲突返回`workflows/03_asset_discovery_workflow.md`的`## Commercial Fact Triage`与Pending Decision；品牌诉求未确认返回STATE-00的`# Input Material`与STATE-01的Creation Brief；目标形式节奏返回短剧适配器；交付画幅返回`knowledge/camera_language/composition_language/vertical_framing.md`；美学方向返回STATE-04；剧情事实返回Writer Owner。

---

## Audience Profile Knowledge Contract

Module Type：受众定位引发的适宜性、理解难度与尺度分化Knowledge；STATE-01、STATE-04、STATE-05与STATE-06按阶段消费；不创建新STATE、不新增Template字段。

Owner：`knowledge/audience_profiles.md`拥有受众字段的值域与三档分化规则（`preschool` / `children_family` / `general`）、三张分层表与可校验不变量。

触发：受众定位由用户或已确认项目材料声明时，在STATE-01（信息承载与冲突形式）、STATE-04（项目级尺度）、STATE-05与STATE-06（逐场逐镜的内容适宜性与表演载体）读取对应小节。

不触发：未声明时记`Audience Profile: PENDING`，不加载分化表、按既有通用行为继续，也不得登记为已确认的儿童向或家庭向；**不得从媒介、类型、平台、画风或时长推定受众**。

不变量：

- 三档ID固定，不得改名或新增同义档
- 不得推定受众；"动画片是给孩子看的"是明确禁止的推定
- 分级条文属外部事实，必须由用户提供来源，不得虚构或声称符合未确认的分级体系
- 可模仿性判据：受众越小，危险动作越必须在同段落内给出可理解的负面后果
- 儿童向不等于降智：不得以可理解性为由简化因果或删除冲突
- 与媒介、类型、时代地域三条轴正交，任一轴不得覆盖另一轴
- 不新增STATE-08字段、不改变主Pipeline、不改变任何Model Adapter能力数值
- 视频Prompt永久禁止非剧情内配乐，儿童向不构成例外

禁止：为适宜性静默改写Production-Locked Script或已确认剧情事实；用"儿童向"当作删除冲突的理由；把海报渠道差异当作受众分化（那是`knowledge/poster_design/index.md`的边界）。

冲突时：受众未声明或冲突返回用户与已确认项目材料；适宜性与剧情事实冲突返回Writer Owner；理解难度与媒介表达冲突返回`knowledge/medium_profiles.md`；美学方向返回STATE-04；逐镜尺度返回STATE-06。

---

## Documentary And Non-Fiction Knowledge Contract

Module Type：纪实 / 非虚构目标形式的适配Knowledge；由STATE-01的`Adaptation Target Detection`触发；不创建新STATE、不新增Template字段。

Owner：`knowledge/adaptation/documentary_adapter.md`拥有来源台账、重现边界、真实主体与权利门、旁白权限、时间线忠实与**生成影像不得冒充档案**六项判据及其Acceptance Checklist。

触发：`Adaptation Target Detection`确认目标为纪实 / 非虚构（纪录片、观察式、访谈式、档案重组、口述史）时读取；短剧目标仍走`knowledge/adaptation/short_form_drama_adapter.md`，品牌目标仍走`knowledge/branded_content/index.md`，三者互不套用。

不触发：其他目标形式一律Not Applicable；无目标证据时按`Adapter Load: Pending`记录，不猜平台规则也不强加纪实纪律。

不变量：

- 每条事实陈述必须能指向可核对来源；写不出来源的不得以陈述句呈现
- 重现段落必须可区分并标注依据来源；不得与档案素材混排到无法分辨
- 真实人物、机构、事件与品牌的授权必须由用户提供，与`rules/automation_mode.md`的Hard Stop同一口径
- 旁白与字幕只承担可核对陈述，不得替观众下结论或替人物读心；引述必须标明
- 时间线与事件顺序必须与来源一致；压缩不得制造虚构因果
- **AI生成画面不得被呈现为档案或真实影像**，不得配纪实性字幕、时间码或档案式包装
- 不新增用户可见字段、不改变STATE-08 Schema、不改变任何Model Adapter能力数值
- 视频Prompt永久禁止非剧情内配乐

禁止：用"看起来真实"填补缺失来源；为叙事顺畅调换事件顺序；生成真实人物的可信影像并作为记录呈现。

冲突时：来源或权利冲突返回`PENDING`与用户决定；目标形式判定返回STATE-01入口路由；时代与地域事实返回`knowledge/period_and_place/index.md`；生成影像冒充档案属阻断项，返回本适配器`## Generated-Image Provenance｜生成影像的来源标注`。

---
