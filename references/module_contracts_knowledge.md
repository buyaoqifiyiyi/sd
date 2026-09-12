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

---

## Quality Knowledge Contract

Module Type：STATE-06至STATE-09辅助Knowledge。

输入拥有者：已确认资产、Detailed Shot Design、Clip Production Plan、Prompt、生成结果与边界合同。

输出拥有者：正式Review由templates/16_review_report.md拥有；内部QA可进入Execution Ledger。

必须执行Shot QA、相邻镜QA、Execution Risk和适用的Prompt Scorecard。禁止用分数覆盖Hard Gate、把QA字段写入STATE-08 Prompt或用审美偏好改写剧情事实。

审美判据与判定纪律的唯一owner是`knowledge/quality/aesthetic_judgement.md`：它只覆盖"取舍是否可见"这一半，系统只输出观察证据，**审美结论必须由用户给出**，且"判据全过"不得当作"好看"的证明。`prompt_scorecard.md`（STATE-08，对象为Prompt文本）与`workflows/13_review_workflow.md`（STATE-09，对象为成片）只引用它，两处都不得复制其判据正文，也不得合并两处。

---

## Medium Profile Knowledge Contract

Module Type：STATE-00确认、STATE-01与STATE-04消费的跨媒介Knowledge；不创建新STATE、不新增Template字段。

Owner：`knowledge/medium_profiles.md`。STATE-00负责把确认结果写入`project_bible.md`的`Project Information → 媒介形式`字段；本文件拥有该字段的值域与三档分化规则。

触发：项目`媒介形式`为`live_action` / `3d_animation` / `2d_anime`时，在STATE-01（编剧承载）与STATE-04（美学与摄影方向）读取；为`Pending`时记录`Medium Profile: PENDING`并把决定返回STATE-00，不加载分化表。

不触发：不因Genre、题材、平台或画风标签加载；Storyboard、Poster、Sequence、MUSIC、AUDIO等辅助模块不因本Knowledge改变各自既有边界。

不变量：

- 三档ID固定为`live_action`、`3d_animation`、`2d_anime`，不得新增第四档或改名
- 媒介与Genre正交，两者不得互相覆盖
- `2d_anime`不得指定焦段毫米数、光比比值、器材或真实景深；`3d_animation`不得沿用实拍光比捕捉语言
- 媒介分化只改变既有Template字段的表达方式，不新增任何字段
- 一个媒介的资产不得静默用于另一个媒介

禁止：把媒介当成Genre子类；从平台或题材推定媒介；用本Knowledge改写剧情事实、资产身份或STATE-08 Schema。

冲突时：媒介决定本身返回STATE-00；资产身份返回资产拥有者；逐镜镜头语言返回STATE-06；项目级美学方向返回STATE-04。

---
