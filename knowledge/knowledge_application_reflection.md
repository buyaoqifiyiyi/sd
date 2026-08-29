# Knowledge Application Reflection Layer

## Purpose

本层用于STATE-08撰写每个Clip Prompt之前的内部实现策略筛选：先读取该Clip已经确认的`Director Decision Notes`，再判断哪些已学Knowledge最适合实现该导演意图，选择1—3个最有价值且可执行的策略，并把策略转译为Seedance能够观察和执行的具体描述。

Knowledge不是必须填满的清单。只有能够明显增强当前Clip的叙事或情绪目标，并且不破坏剧情、资产、空间、动作、风格、连续性与Seedance稳定性的知识才可采用。禁止为了证明“使用了知识库”而堆砌专业术语、模式或技巧。如果增加运镜、色彩变化或其他技巧没有收益，应把“保持已确认设计，不增加复杂运镜或额外视觉事件”作为一条有明确价值的克制 / 稳定策略，而不是虚构装饰性知识点。

本层不创建新STATE，不重做Director Decision、STATE-06 Camera Language Decision或STATE-07 Clip Movement Plan，不拥有STATE-08最终字段。它不得重新决定“为什么这样拍、观众知道/感受/等待什么、人物关系如何表达或总体视听策略是什么”。最终Prompt Schema仍只由`templates/10_video_prompt.md`拥有。

## Module Contract

- **Module Name**：Knowledge Application Reflection Layer
- **Module Type**：STATE-08内部决策Knowledge；STATE-07可提供非约束性机会线索；STATE-09只执行轻量QA
- **Trigger**：每个Confirmed Clip在读取Clip Production结果及对应Director Decision Notes后、生成最终Prompt之前必须执行一次
- **Not Triggered As**：独立Workflow、额外主STATE、用户可见固定章节、另一套Prompt Schema或上游重设计步骤
- **Required Inputs / Owners**：当前Clip对应的Director Decision Notes、Confirmed Clip Production Plan、Detailed Shot Design、已确认资产与Visual Direction、Camera Language Decision、Clip Movement Plan、边界与连续性合同，以及当前任务实际适用并已读取的Knowledge；叙事目的、观众体验、人物关系与总体视听方向由Director Decision Layer拥有，本层只读
- **Output Owner**：本层只产生一次性内部Reflection Record；最终Prompt仍由`templates/10_video_prompt.md`拥有，正式Review仍由`templates/16_review_report.md`拥有
- **Read / Write Boundary**：允许读取当前项目已确认产物和适用Knowledge；不得向Skill根目录写项目数据。内部记录可留在执行上下文或既有Execution / Projection Ledger，不创建用户交付字段
- **Downstream Consumers**：STATE-08 Prompt Compilation、STATE-08 Final Validation、STATE-09 Knowledge Application QA
- **Protected Upstream Facts**：不得修改剧情、角色/环境/道具/FX身份、Visual Direction、SHOT/CLIP顺序、Shot Purpose、Director Decision Notes、Camera Language Decision、Clip Movement Plan、关系轴、边界或时长
- **Conflict Route**：事实冲突返回事实拥有者；逐镜设计冲突返回STATE-06；Clip编排或Movement Plan冲突返回STATE-07；只有转译、取舍或Seedance执行措辞问题留在STATE-08
- **Deterministic Invariants**：每Clip先读取Director Decision Notes再执行Opportunity Check；最终选择1—3项且有Clip级收益；每项均有具体Prompt证据或明确放弃理由；没有反向改写导演意图；无内部模式ID/知识标题泄漏；无新增最终字段；无知识堆砌；无连续性或稳定性冲突

## Responsibility Boundary

- **Director Decision Layer**回答：为什么这样拍、观众知道/感受/等待什么、人物关系与Blocking如何表达、镜头总体动或停、色光是否功能性变化、表演尺度、声音加强/留白以及高潮/余韵方向。
- **Knowledge Application Reflection**只回答：用哪些已读取Knowledge最有效、最稳定地实现上述方向；选择1—3项具体策略，或选择一项有明确收益的克制/稳定策略。

当Knowledge候选与Director Decision Notes冲突时，必须Reject候选；不得因为知识库中存在某种运镜、色调、构图、灯光、表演或声音技巧，就反向修改剧情方向、观众体验或人物关系。若Notes本身与上游事实冲突，返回STATE-06或事实拥有者，不在本层重新导演。

## Internal Reflection Flow

对每个Confirmed Clip依序完成，先决策、后写Prompt：

1. **读取并锁定目标**：从当前Clip对应的Director Decision Notes读取已经确认的主叙事目标、Audience Know / Feel / Wait、人物关系与总体视听方向；不得在本层重新发明或替换目标。
2. **扫描机会**：已有Knowledge中，哪些知识能明显增强这个目标？必须基于当前Clip事实和已读取资源，不凭记忆虚构模块能力。
3. **排除代价**：哪些候选会造成炫技、动作/口型/FX或摄影机负荷过高、信息重复、风格漂移、资产变化、轴线/边界破坏或连续性风险？
4. **选择策略**：只选择1—3个价值最高且彼此兼容的策略。没有合格的增强技巧时，选择“保持静止 / 少动 / 单一路径 / 不增加额外色彩变化”等有助于可读性、连续性或Seedance稳定性的克制策略；不得为了凑数采用没有收益的技巧。
5. **执行转译**：把每个策略转译为Seedance可执行、可观察、可验证的摄影、构图、光线、表演、声音、剪辑或限制语句，再映射到`templates/10_video_prompt.md`已有字段。

内部可使用以下一次性记录，不得原样进入最终Prompt：

| Clip Goal | Opportunity | Expected Gain | Cost / Conflict | Select / Reject | Concrete Prompt Evidence | Target Existing Field |
|---|---|---|---|---|---|---|

## Knowledge Opportunity Check

每个Clip至少扫描以下十类。`Applicable`不表示必须采用；只有通过Selection Gate的候选才进入最终Prompt。

| Domain | Opportunity Question | 合格的可执行证据方向 |
|---|---|---|
| Camera Language | 摄影机位置、路径、速度、触发与终点能否更清楚地表达关系、发现、压力、释放或节奏变化？ | 明确起点/侧位、唯一主路径、运动方向与幅度、人物动作触发、轴线限制、减速/停止点和结束景别；不得只写Side Tracking、Push In等名称 |
| Composition | 主体位置、前中后景、负空间、遮挡、反射、引导线或焦点变化能否提升信息与关系可读性？ | 明确真实空间来源、画面左右/层次、视觉焦点如何变化及稳定终点 |
| Color / Tone | 已确认资产、环境光源、材质与Visual Direction中的色相层级、饱和度、明度/对比或综合色温能否服务当前情绪与视觉重点？ | 明确颜色来源、主辅强调色的空间位置与面积关系、饱和度/明暗/偏色、肤色与中性色保护、材质响应及稳定结束色态；不得只写“低饱和”“冷暖对比” |
| Lighting | 已确认光源、介质、遮挡或材质响应能否增强人物可读性或情绪变化？ | 明确光源锚点、方向、光质、光比/曝光、受光结果与结束光态；不得凭空新增光源 |
| Performance | 注意、视线、呼吸、面部/身体动作、控制/泄漏或距离变化能否让情绪过程可见？ | 明确刺激→注意变化→最少可见反应→行动选择→稳定状态；不得只写“悲伤、克制、感动” |
| Sound | 环境底声、同步Foley/动作声/呼吸/对白或剧情内声源能否强化空间、动作和情绪节奏？ | 明确声源、距离、同步点与声音尾部；背景音乐不进入STATE-08正向声音设计 |
| Editing Rhythm | Clip内动作、停顿、视线或声音节拍，以及跨Clip边界，能否通过切点、出入镜锚点、同期Sound Bridge或Direct Cut更清楚？ | 明确节拍落点、Outgoing Anchor、Cut Point、Incoming Anchor、继承/重建方式与降级；不得把普通运镜当转场 |
| Director Style | 已确认的导演/影片/类型风格是否有可转译、且不依赖姓名标签的行为特征？ | 转译为具体构图、机位、光线、综合色彩、表演距离或节奏行为；最终Prompt不得只写导演名字或“某某风格” |
| Continuity | 哪些人物、资产、空间、动作、光态、色态、声音或尾帧状态需要显式继承/重建？ | 写出可核对的起始状态、结束状态、轴线/左右/道具/情绪锚点和下一镜关系 |
| Seedance Stability | 哪个知识策略在当前时长和负荷内可稳定执行？需要何种简化或降级？ | 保留一个主要摄影机路径、有限动作事件、清楚身份与空间、低动作稳定结尾；必要时删辅助、降速、缩短路径、固定机位或返回拆分 |

## Selection Gate

候选知识只有同时满足以下条件才可选择：

- 对主叙事/情绪目标有可说明的增益，而不只是增加“电影感”词汇。
- 与Director Decision Notes、Confirmed Assets、Visual Direction、Shot Purpose、Camera Language Decision、Clip Movement Plan及边界合同一致。
- 与其他已选策略分工清楚，不重复表达同一效果，也不会彼此产生相反指令。
- 能在当前Clip的4—15秒平台时长、动作密度、口型、FX和摄影机复杂度内稳定执行。
- 能被写成具体、可观察的Prompt语句，并映射到现有Template字段。

任一条件失败即Reject。优先级为：剧情/资产/连续性正确 > 叙事与情绪增益 > Seedance稳定性 > 风格丰富度。不得为了凑足1—3项而降低门槛；克制策略也必须说明它如何保护表演可读性、连续性或模型稳定性，不能成为空洞占位。

## Translation Rules

最终Prompt只保留选择后的执行语义，不输出Opportunity Check、候选列表、拒绝理由、知识文件名、内部模式ID、Reflection Record或“应用了哪些知识”的说明。

禁止只写：

- `使用Side Tracking与Push In。`
- `使用某导演风格。`
- `采用压迫构图、电影感光线、克制表演。`

必须改写为具体行为，例如：

> 摄影机位于两人关系轴同一侧的侧面中景，与两人的慢速步行平行跟随并保持距离；当其中一人停步并抬眼确认对方时，只进行一次短距离靠近，随后减速停住，不环绕、不换侧。两人始终分处画面左右，湿玻璃的反射留在前景边缘而不遮挡眼神。她先收紧呼吸、手指停在伞柄上，再抬眼维持短暂停顿；雨点击伞与鞋底踏水声延续到稳定尾帧。

这段示例展示转译粒度，不是固定模板，也不授权当前Clip新增雨、伞、玻璃、人物动作或任何剧情事实。

## Internal Visibility Rule

本层默认只作为内部决策，不要求向用户展示。用户明确要求查看时，只提供简洁的决策摘要：Clip目标、被选策略、放弃的高风险候选及其可执行转译；不得把内部记录变成后续Prompt固定栏目，也不需要暴露逐步隐式推理。

## Completion Check

进入Template Mapping前确认：

- 已完成十类Opportunity扫描，而不是直接套用默认Prompt模板。
- 已先读取并保持Director Decision Notes；Knowledge选择没有重新定义叙事目的、观众体验、人物关系或总体视听策略。
- 已选择1—3项最有价值策略，并且每项都有具体执行语句落点；其中可以包含有明确收益的克制 / 稳定策略。
- 可用知识没有因惯性模板而完全消失；不适用知识也没有被强行填充。
- 没有只写知识名、导演名、模式ID或抽象美学标签。
- 没有知识堆砌、相互冲突、动作/摄影机过载、剧情/资产/连续性破坏或Seedance难执行。
- 最终只输出`templates/10_video_prompt.md`拥有的内容。
