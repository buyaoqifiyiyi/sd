# Transition Continuity

## Transition Ledger

内部为每个相邻镜头维护：

| 项目 | 记录内容 |
|---|---|
| Boundary Class | Continuous / Motivated / Unresolved |
| Primary Technique | 一种主要转场或待确认 |
| Outgoing Anchor | 人物位置、动作阶段、视线、构图、遮挡、焦点、光态或同期声尾部 |
| Cut Point | 动作峰值、遮挡完成、视线落点、反应起点、声源进入或稳定停顿 |
| Incoming Anchor | 下一镜可直接读取的首个可见/可听状态 |
| Inherited State | 身份、站位、方向、情绪、道具、环境、天气、光色、摄影机和持续声音 |
| Rebuilt State | 仅 Motivated Discontinuity 中由已确认剧情重建的项目 |
| Prohibition | 不得提前的下一镜动作、不得改变的连续性事实 |
| Fallback | 通常为 Direct Cut；未知则 Unresolved Handoff |

## Match On Action

动作匹配必须拆成：动作开始、主要运动、切点阶段、下一镜继续阶段、动作完成。上一镜不能越过切点，下一镜不能重新开始已完成阶段。方向、速度、受力和接触对象必须兼容。

## Eyeline And Reaction

视线匹配需锁定人物朝向、视线方向、目标空间位置和轴线。反应切需保留刺激发生的因果顺序，不得让反应先于刺激。

## Graphic And Light Match

图形、颜色或光态匹配必须由两镜真实可见的共同锚点支持。只写“冷色变暖色”“光芒铺满画面”不足以建立转场；必须说明来源、画面位置、覆盖程度、切点和下一镜对应锚点。

## Occlusion Continuity

遮挡切需记录遮挡物身份、运动方向、距镜头关系、覆盖比例趋势、完整覆盖点与下一镜兼容的揭开方向。未达到足够覆盖时只能作为前景动作，不能依赖它隐藏场景跳变。

## Sound Continuity

声音桥记录声源、空间位置、距离、混响、进入/离开方向和跨切点持续状态。只使用对白、环境声、动作声、呼吸、Foley 或剧情内播放源；背景音乐和配乐不得进入 STATE-08。

## Stable Handle

后期转场需要可剪辑把手。每镜结尾在主要动作完成后进入可读的低动作稳定状态；若使用 Match on Action，则在动作切点前后保留清楚、可验证的动作阶段。不得以精确秒数、帧数或百分比写入最终 Prompt。

## STATE-08 Projection

相邻正式SHOT先由Confirmed Clip Production Plan判定边界：同一Clip内使用逐镜End→Start状态链连续生成；跨Clip先按当前Clip是否需要严格视觉承接标记`Tail Frame Required = YES / NO`，再检查最终交付帧。`YES`且实际生成、可访问、已确认时，使用统一命名`REF-TAIL-XX｜CLIP-XX尾帧参考`传给下一段；未提供时主动请求用户从上一Clip最终成片手动截取最终有效尾帧并上传，草案标记“待用户提供/待上传”且暂停最终可执行版。`NO`不要求截图，可文字承接或重建；断点边界使用明确的不继承声明。不得跨Clip塞入Shot来回避跨段连续性。

### 镜头结尾状态

写出：最终位置/姿态、动作切点、视线、道具、摄影机、构图、遮挡/光态/焦点、同期声尾部、稳定窗口和不得提前动作。

### 与下一镜衔接

写出：边界类型；主要转场技术；切点；视觉/动作/声音锚点；继承或重建状态；下一镜入镜条件；禁止改变项；必要的 Direct Cut 降级方案。

### 下一镜起始状态

直接读取入镜锚点。Continuous Handoff 中不得重新初始化人物、道具或动作；Motivated Discontinuity 中只重建已确认的断点状态；Unresolved Handoff 中不得生成。

Continuous Handoff若当前Clip需要严格视觉承接，标记`Tail Frame Required = YES`；实际尾帧图可用时，必须在【参考资产】写入上一段`REF-TAIL-XX｜CLIP-XX尾帧参考`，在【首帧参考】逐字写`以 REF-TAIL-XX｜CLIP-XX尾帧参考 为直接承接依据起镜。`，且“起始状态”与该帧一致；未提供时不列入【参考资产】，主动请求用户截图，草案标记“待用户提供/待上传”且不形成最终可执行版。Motivated Discontinuity或非严格承接标记`Tail Frame Required = NO`，不要求截图，写明文字承接/重建原因和仍保留的状态锚点。
