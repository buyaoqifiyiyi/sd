# Facial Action Language

## Purpose

把“开心、愤怒、悲伤、害怕”等抽象情绪翻译为演员和视频模型可观察的局部动作。该语言受FACS启发，但内部动作编号只用于分析；最终Prompt优先使用清楚自然语言，不输出编号堆叠。

## Baseline First

同一个局部动作在不同角色和情境中可能表示不同含义。设计表情前先锁定：

- 角色平时的眉眼、嘴角、头颈、呼吸与姿态基线；
- 当前视线目标、人物关系和公开/私密场合；
- 角色想表达什么、想隐藏什么以及身体正在做什么；
- 当前景别、机位、遮挡、光线与面部可见范围。

不得把角色资产的天生眼型、嘴型、面部不对称或年龄纹理误写成情绪动作。

## FACS-Inspired Action Regions

| 区域 | 可观察动作 | 可选内部AU参考 | Prompt表达原则 |
|---|---|---|---|
| 眉额 | 眉内侧抬起、眉外侧抬起、双眉下压靠拢、单侧挑眉 | AU1 / AU2 / AU4 | 说明对称或单侧、幅度、出现与回落，不写“眉毛表达悲伤” |
| 眼睑 | 上眼睑抬起、眼睑收紧、半垂、闭眼、一次眨眼或眨眼受抑 | AU5 / AU7 / AU43 / AU45 | 与视线目标、注意变化和光线可读性结合 |
| 眼周/面颊 | 眼轮匝肌收紧、面颊抬起 | AU6 | 区分真正参与的笑眼与只有嘴角的社交笑 |
| 鼻部 | 鼻翼轻张、鼻部皱缩 | AU9 | 只在强烈厌恶、呼吸负荷或已确认动作中使用，不机械搭配愤怒 |
| 上唇/嘴角 | 上唇抬起、嘴角双侧上提、单侧收紧、嘴角下压 | AU10 / AU12 / AU14 / AU15 | 指明单侧或双侧、是否与眼周一致 |
| 唇部 | 嘴唇拉伸、抿紧、压紧、微分、向内收 | AU20 / AU23 / AU24 / AU25 / AU28 | 对白、呼吸、吞咽、哭笑和咬牙不能同时互相冲突 |
| 下颌/口腔 | 下颌轻放、张口、深度张口 | AU26 / AU27 | 强度由动作与声音授权，不把“张嘴”当惊讶必然结果 |
| 下巴 | 下巴肌收紧或抬起 | AU17 | 常与压抑哭泣、坚持或唇部控制共同出现，需结合上下文 |

## Eye And Attention Language

## Temporal Action Shape

局部面部动作必须按时间过程设计，而不是把肌肉从第一帧直接写成峰值：

`Onset（开始）→ Apex（峰值）→ Offset（消退/保持）`

- **Onset**：由已确认刺激或台词触发词启动，写清先动哪一处、是否有延迟；
- **Apex**：只达到当前表演所需的可见强度，不默认拉满；
- **Offset**：写消退、停留或转入新的稳定状态，不能在切镜时凭空归零。

AU 编号只用于内部校准，最终仍写成可观察的自然语言；同一 AU 组合不能脱离目光、咬合、身体和情境直接命名情绪。

### Common Calibration Set｜常用辅助校准集

以下是对白与情绪转折中优先使用的辅助项，不是情绪公式：

- AU1：眉毛内侧抬起；
- AU4：眉毛下压；
- AU5：上眼睑抬起；
- AU7：眼睑收紧；
- AU15：嘴角下沉；
- AU17：下巴抬起并绷紧；
- AU23：嘴唇收紧；
- AU25 / AU26：嘴唇分开 / 下颚张开，可用于短促爆发。

使用时先写目光、咬合、身体、呼吸和情境，再用一个或少量 AU 校准；不要把整组编号直接堆进最终 Prompt。

## Research Reference: Prototypical And Compound Combinations

FACS 没有一份官方的“情绪 = 唯一 AU 组合”字典。下表是公开人工 FACS 研究中的原型参考：核心项在该研究类别中由多数被试使用，括号内为常见变体；它们用于内部起草和反查，不是硬性触发器，也不能替代角色、目光、身体、声音与情境。

| 类别 | 核心 AU | 常见变体 |
|---|---|---|
| Happy | AU12 + AU25 | AU6 |
| Sad | AU4 + AU15 | AU1 / AU6 / AU11 / AU17 |
| Fearful | AU1 + AU4 + AU20 + AU25 | AU2 / AU5 / AU26 |
| Angry | AU4 + AU7 + AU24 | AU10 / AU17 / AU23 |
| Surprised | AU1 + AU2 + AU25 + AU26 | AU5 |
| Disgusted | AU9 + AU10 + AU17 | AU4 / AU24 |
| Happily surprised | AU1 + AU2 + AU12 + AU25 | AU5 / AU26 |
| Happily disgusted | AU10 + AU12 + AU25 | AU4 / AU6 / AU9 |
| Sadly fearful | AU1 + AU4 + AU20 + AU25 | AU2 / AU5 / AU6 / AU15 |
| Sadly angry | AU4 + AU15 | AU6 / AU7 / AU11 / AU17 |
| Sadly surprised | AU1 + AU4 + AU25 + AU26 | AU2 / AU6 |
| Sadly disgusted | AU4 + AU10 | AU1 / AU6 / AU9 / AU11 / AU15 / AU17 / AU25 |
| Fearfully angry | AU4 + AU20 + AU25 | AU5 / AU7 / AU10 / AU11 |
| Fearfully surprised | AU1 + AU2 + AU5 + AU20 + AU25 | AU4 / AU10 / AU11 / AU26 |
| Fearfully disgusted | AU1 + AU4 + AU10 + AU20 + AU25 | AU2 / AU5 / AU6 / AU9 / AU15 |
| Angrily surprised | AU4 + AU25 + AU26 | AU5 / AU7 / AU10 |
| Angrily disgusted | AU4 + AU10 + AU17 | AU7 / AU9 / AU24 |
| Disgustedly surprised | AU1 + AU2 + AU5 + AU10 | AU4 / AU9 / AU17 / AU24 |
| Appalled | AU4 + AU10 | AU6 / AU9 / AU17 / AU24 |
| Hatred | AU4 + AU10 | AU7 / AU9 / AU17 / AU24 |
| Awed | AU1 + AU2 + AU5 + AU25 | AU4 / AU20 / AU26 |

研究中反复检验的高频同时出现组合包括：AU1+AU2、AU1+AU4、AU4+AU7、AU6+AU12、AU6+AU7。组合必须先通过口部容量、咬合、视线与身体状态检查；发生冲突时保留能证明当前剧情变化的最小组合，不把两个互斥动作同时拉到峰值。

来源：

- [Compound facial expressions of emotion](https://pmc.ncbi.nlm.nih.gov/articles/PMC3992629/)
- [Dynamic Facial Expression of Emotion and Observer Inference](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.00508/full)
- [Automated Facial Image Analysis](https://sites.pitt.edu/~jeffcohn/biblio/cohn%26kanade2007.pdf)

“眼神温柔、眼神冰冷、眼神坚定”仍是抽象词，至少拆成：

- **目标**：看谁、看哪个物体、看远处还是短暂失焦；
- **路径**：直接锁定、先扫视再停住、回避后复看、在两个对象间切换；
- **速度**：迟疑、迅速定向、缓慢移开；
- **保持**：短暂相遇、持续注视、注视被打断；
- **眼睑**：放松、收紧、抬起、半垂、眨眼或短暂停眼；
- **头眼关系**：眼先于头、头先转但眼仍滞留、头低而视线上抬。

瞳孔大小主要受光线、镜头与生理条件影响，普通生成模型也难以稳定控制。除非特写、光线稳定且剧情确有必要，不把“瞳孔放大/收缩/地震”作为核心表演指令；优先改写为上眼睑抬起、视线迅速定向、眨眼停止或目光失焦。

## Mouth, Breath And Voice Coordination

- 微笑、说话、吞咽、抽泣、喊叫和咬牙共享口部动作容量，必须排出先后。
- 真正开放的笑通常同时影响面颊、眼周、呼吸和躯干；不指定露出几颗牙。
- 哭泣先判断呼吸是否被打断、是否吞咽、能否说话，再决定泪水与嘴部动作。
- 怒吼必须由剧情和强度授权，并说明吸气、下颌释放、发声、结束后的呼吸状态。
- 无对白镜头也可用一次吸气、缓慢吐气、屏息、鼻息或喉部吞咽呈现内部变化。

## Conditional Physiology

脸红、耳红、泪水、出汗、鼻翼变化、颤抖和瞳孔变化不是每种情绪的固定结果。

- 只有剧情、体力、环境和角色状态支持时才使用；
- 与妆容、湿润度、天气、光线和跨镜连续性一致；
- 泪水采用“眼眶湿润 → 泪液聚集 → 一滴滑落/连续流泪”的可见过程；
- 颤抖说明发生在手指、下颌、肩部或呼吸，不写全身随机抖动；
- 脸红若不易稳定生成，可降级为视线回避、耳颈紧张、嘴角压住或自我触碰。

## Shot-Scale Visibility

| 景别 | 优先表演通道 | 避免 |
|---|---|---|
| Extreme / Close-Up | 眼睑、眉间、嘴角、吞咽、泪液、一次视线变化 | 同时叠加大幅手势和复杂走位 |
| Medium Close-Up / Medium | 面部 + 呼吸 + 肩颈 + 手部 + 轻微重心 | 依赖难以看清的极细眼部变化 |
| Full / Long Shot | 头颈、躯干、步幅、距离、手臂和行动选择 | 用“嘴角轻动”承担关键叙事证据 |

若当前景别、机位、遮挡或光影使关键表演不可读，应返回STATE-06 Detailed Shot Design调整其可读性，而不是在Clip Production或Storyboard中堆叠更多表情词。

## Prompt Serialization

最终自然语言优先按以下顺序：

`视线目标与变化 → 眉眼/嘴角的一项主要面部变化 → 呼吸/肩颈/手部的一项支持变化 → 行动选择 → 新的稳定状态`

单镜头不需要把所有面部区域写满。选择能证明当前剧情变化的最少动作组合。
