# SD Film Regression Scenarios — Director Module / Camera Language

> Skill维护层：只在修改本Skill时读取，不参与影视生产。

本文件是回归集的一部分；完整范围与其余文件见 `references/regression_scenarios.md` 的 Regression File Index。覆盖 Director Module 与 Camera Language 端到端（R23），可按编号直接定位，不整集通读。

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

### R23-O Camera Language — Emotion Drives The Move, Not The Label

输入：一个“平静→压迫→确认”的单人等待Shot；草案只写“人物很压抑，镜头缓缓推进带电影感”，并同时要求变焦压缩、轻微横摇、浅景深、前景遮挡与手持呼吸，用来“增加情绪”。

PASS：STATE-06先写出三段式情绪变化`起始状态 → 变化触发与过程 → 结束落点 / 观众残留感受`，并指出触发来自哪个可见刺激或表演Beat；再指定唯一主要承担变量（例如随确认发生的距离变化），其余变量保持或明确让位并说明理由；主运镜写出`Trigger → Path（含Mid-path Change）→ Stop → End Composition`与运镜理由，或给出有理由的Static / Locked-Off所保护的表演与信息。抽象词已改写为可执行的连续视觉动作与构图变化，STATE-08仍只使用既有字段，不输出内部标签。

FAIL：只标注“压抑 / 震撼 / 氛围感”并据此推进；九个画面关系变量同时改变而没有主承担者与让位理由；主运镜只写“缓缓推进 / 轻微横移 / 环绕”而不给Trigger、Path、Stop、落点与运镜理由；或为凑情绪叠加无理由的快环绕、频繁推拉、炫技转场与持续运动。

### R23-P Shot Necessity — The Default Replacement Must Cost Something

输入：一个“她坐在咖啡馆等一个不会来的人”的Shot草案：内容、表演与光线都正确，但设计文档只能写出“中景、固定机位、轻微推进”；被问“换成平视中景固定机位并保持相同台词与动作会失去什么”时，回答是“会少点电影感”。

PASS：STATE-06执行Default-Replacement Loss后先指出可指认的信息或感受损失（例如观众必须看见门口反射里一直没有出现的人，或她收回手又放回桌面外沿的重复动作），再据此确定唯一主要承担变量与观察权，并写出`Trigger / Path（含Mid-path Change）/ Stop / End Composition`与运镜理由；若确实找不到可指认损失，则与相邻兼容SHOT合并或删除。有叙事理由的Static / Locked-Off同样通过，但必须写出它保护了什么。

FAIL：以“更有电影感 / 更高级 / 更有氛围”为由保留或升级镜头；把答不出损失的镜头因为“好看”而留在Shot列表；或反过来把所有Static默认判为平庸。

### R23-Q Camera Language — Motif Nodes, Movement Phase And Novelty Budget

输入：一个Clip已有确认的视觉母题轨迹（门口 → 距离变化 → 门框吞没人物）与一个已确认的视觉高潮Shot；草案让四镜都使用环绕，其中两镜不在母题节点上，且没有说明观众是先知、同时知还是后知。

PASS：STATE-06只在已确认的母题节点上复用该视觉动作，并写出本次改变哪一个变量（距离 / 侧位 / 遮挡 / 焦点）与哪些保持不变，非节点镜头写`Not Applicable`并使用不同观察层次；每镜显式选择Movement Phase（抢先 / 同步 / 滞后 / 拒绝跟随）；整个Clip最多1次运动新奇度破例并绑定视觉高潮，其余镜头靠距离、遮挡、焦点与时相制造差异。STATE-08只写既有字段语义，不输出内部标签。

FAIL：未到母题节点就重复同一构图或运镜，或用“呼应”当理由复用；同一Clip出现两次及以上运动破例，或破例未绑定视觉高潮；缺少Movement Phase而无法说明观众先于 / 同时于 / 晚于人物获得信息；把Generation Budget与运动新奇度预算混为一谈。

---
