# Emotion Dynamics And Subtext

## Emotion Is A Process

表情不是情绪名称的静态插图。逐镜建立：

`Baseline → Stimulus → Attention Shift → Appraisal → Impulse → Control / Leakage → Action Choice → Settled State`

- **Baseline**：上一镜继承的视线、呼吸、面部张力、姿态和互动距离。
- **Stimulus**：人物实际听见、看见、触碰或想起的已确认事件。
- **Attention Shift**：眼睛、头部或动作先转向何处。
- **Appraisal**：人物确认、误解、怀疑或拒绝信息的短暂处理。
- **Impulse**：靠近、退避、攻击、保护、隐藏、求助、冻结或继续任务的倾向。
- **Control / Leakage**：人物是否压住反应；被压住的反应从哪个通道短暂泄漏。
- **Action Choice**：人物最终做出的可见选择。
- **Settled State**：镜头结尾可继承的面部、呼吸、姿态、距离与注意目标。

内部分析可使用“喜悦、愤怒、悲伤、恐惧”等标签帮助理解，但最终Prompt必须写过程证据。

## Performance Arc Map

单镜表演链不能替代跨镜情绪弧。对每个实际参与情绪、关系或对白变化的角色，在Scene / Shot Group进入正式逐镜设计前建立内部`Performance Arc Map`：

| Character | Inherited Baseline | Confirmed Trigger | Pre-action State | In-action Change | Post-action Residue | Arc Endpoint | Relative Amplitude / Visual Priority | Next-shot Carryover |
|---|---|---|---|---|---|---|---|---|

- **Inherited Baseline**必须来自上一有效镜头、Scene初始事实或Motivated Discontinuity，不能按镜头重新归零。
- **Pre-action State**记录人物在动作或台词发生前的预期、迟疑、压制、警觉、误判或主动保持；它可以极轻，但不能只写一个情绪名称。
- **In-action Change**记录刺激到来后最先改变的注意、呼吸、局部面部、姿态或距离，以及人物如何继续、停止或改变动作。
- **Post-action Residue**记录动作、台词或信息结束后仍留下的呼吸、视线、肌肉张力、恢复、余惊、得意、失望或控制结果；不得在结果发生后立即恢复默认脸。
- **Arc Endpoint**必须是可被下一镜继承的状态，而不是“情绪结束”。

一个短SHOT只需承载整条弧中当前可见的一段，不得为了“情绪完整”把所有阶段挤进同一镜。跨SHOT连接必须满足`Previous Settled State = Current Inherited Baseline`，任何升级、回落、反转或恢复都要有新刺激、时间经过或主动控制作为依据。

如果剧情要求人物克制、冷淡、观察或暂时没有外显变化，可以使用`Intentional Hold / 主动保持`，但必须说明人物正在注意什么、压住什么、反应延迟多久或通过哪个低幅通道保持活性。没有注意目标、呼吸/姿态变化、延迟反应或行动选择的“面无表情 / 一直平静”属于静态标签，不是有效表演设计。

`Performance Arc Map`是内部设计与检查记录，不创建Template字段，不授权新增剧情、台词、动作、镜头或情绪转折。需要新增未写刺激或改变剧情才能成立时，返回事实拥有者；仅缺少可执行表演证据时，修正Affected SHOT及其相邻Handoff。

## Channel Budget

短镜头优先使用：

- 一个主要面部通道；
- 一个身体或呼吸支持通道；
- 一个注意/视线变化；
- 一个行动结果与稳定结束状态。

强度更高不等于通道更多。高强度表演应由刺激、动作、发声和持续后果共同成立，不把瞪眼、张嘴、握拳、后退、落泪同时堆在每个角色身上。

## Mixed Emotion And Subtext

复杂人物常同时存在“公开表情”和“内部反应”。设计时选择主导动机与一处不一致证据：

- 嘴角维持礼貌弧度，但眼周不参与且呼吸变浅；
- 视线保持镇定，拇指却反复压住指节；
- 先出现短暂欣喜，确认信息后嘴角收回并移开视线；
- 想靠近却把重心留在后脚，手抬到一半停住；
- 愤怒冲动出现，下颌收紧后选择压低声音而不是爆发。

不得同时写两个完整互斥表情。混合情绪通过不同通道或先后变化表达。

## Suppression And Leakage

“故作镇定、隐忍不哭、憋屈忍怒、假笑”至少说明：

1. 人物试图维持的公开状态；
2. 哪个局部动作泄漏真实反应；
3. 人物如何重新控制或控制失败；
4. 结尾留下的呼吸、视线或肌肉张力。

微表情是短暂泄漏，不应被持续整镜保持。最终Prompt不写精确秒数，只写“短暂出现后被压回”“一闪而过，随后恢复”等可执行时间关系。

## State Versus Emotion

疲惫、困倦、醉意、疼痛、缺氧、寒冷、发热和体力透支属于身体状态，会改变表演基线，不等同情绪。它们可以与悲伤、警惕、愤怒等叠加，但必须分别说明来源与可见结果。

## Interaction Boundaries

- **Character Asset**：拥有脸型、五官、年龄、疤痕、妆容和个体不对称；Performance不得改脸。
- **Action / Blocking**：拥有人物位置、路线、接触和道具动作；表情只说明动作中的心理可见性。
- **Dialogue / Sound**：拥有准确台词、声线和声音空间；Performance决定说话前后行为、发声强度与倾听反应。
- **Camera / Composition**：拥有景别、机位和视觉重点；必须保证关键表演可见，不用特写自动制造情绪。
- **Lighting**：拥有光源和受光可读性；冷暖、明暗不能替代表演，也不随表情任意变化。
- **FX / Makeup**：拥有泪液、汗、水、血、污渍等正式效果与物理连续性；Performance只规定触发和人物反应。

## Performance Continuity Ledger

内部逐镜记录，不作为最终Prompt栏目：

| Character | Attention Target | Face / Mouth | Breath / Voice | Posture / Hands | Intensity | Control / Leakage | End State |
|---|---|---|---|---|---|---|---|

Continuous Handoff必须继承尚未恢复的泪液、红肿、呼吸、颤抖、肌肉张力、视线目标和动作阶段。Motivated Discontinuity可以重建状态，但不得借断点改变角色身份或未获授权的身体后果。

## Stable Downgrade

当表演过密或模型不稳定时依次降级：

1. 删除装饰性面部动作；
2. 只保留一个眼神变化和一个呼吸/身体反应；
3. 把复杂混合情绪改为“公开状态 + 一处泄漏”；
4. 减少同步对白或手部动作；
5. 保留刺激、行动选择和稳定结尾，不改变剧情结果。
