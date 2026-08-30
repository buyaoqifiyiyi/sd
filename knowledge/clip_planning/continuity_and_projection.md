# Clip Continuity And Prompt Projection

## Clip-Level Continuity Ledger

每个 Clip 需要锁定：

- Entry State：人物、空间、道具、环境、FX、摄影机与声音起点
- Internal Shot Order：来源分镜原编号与顺序
- Camera / Composition Path：景别、机位、焦段、对焦、构图和运镜如何连续演进
- Performance / Action Arc：刺激、注意、反应、动作与稳定结果
- Lighting / Color Arc：真实光源、方向、强度/光比、色温/偏色、饱和度与资产固有色
- Sound Arc：对白、环境声、动作声、呼吸与Foley；STATE-08默认禁止生成背景音乐、配乐、BGM、主题音乐与氛围音乐，只有用户显式要求由Seedance为明确指定的Clip生成背景音乐时例外
- Exit State：稳定尾帧与下一 Clip 可用锚点
- Tail-Frame Use Mode：A【同镜头连续承接 / Direct】/ B【新镜头参考型 / Reference-Only】/ C【新镜头且无需尾帧 / Not Required】
- Tail-Frame Requirement：A/B标记`Tail Frame Required = YES`，C标记`NO`；不得由资产是否已存在反向决定
- Tail-Frame Purpose：A写“同镜头连续承接用途”；B写“空间/站位/景别参考用途”；C无`REF-TAIL`。只要出现`REF-TAIL`，用途不得省略
- Tail-Frame Availability：A/B统一登记`REF-TAIL-XX｜CLIP-XX尾帧参考`；尚未提供时仍列入参考资产声明并写“待用户提供/待上传、未确认”，占Projected位但不计入已提交图片，用户实际生成前补入；存在、可访问、已确认后才写真实引用。C不要求截图、不列尾帧
- Reference Budget Audit：按`knowledge/reference_budget.md`记录原始候选、连续性预留、去重/整合/裁剪、参考资产声明、已提交图片清单与总数；A/B无论是否已上传都进入Projected Final Count并在声明中列`REF-TAIL`及用途，只有实际存在、可访问且已确认时才计入已提交图片；C不列或预留尾帧

## Knowledge-To-Prompt Projection

Clip 表中的“知识投影摘要”不是知识名称清单，而是以下模块已经形成的可执行结果：

| Knowledge | STATE-08 Projection |
|---|---|
| Camera / Composition | 各`分镜X`的景别、镜头/机位、空间关系与画面描述 |
| Movement Combination | 同一 Clip 内分镜顺序、主摄影机路径、内部衔接与稳定终点 |
| Focal Length | 镜头/机位中的焦段倾向、摄影距离、对焦、背景尺度与连续风险 |
| Performance | 人物动作与情绪中的刺激、视线、微反应、身体支持动作、选择与结束状态 |
| Lighting | 主风格、环境一致性、起始状态、空间关系、画面变化与结尾状态 |
| Color | 主风格、环境一致性以及各分镜起始/变化/结束色态 |
| Transition | 同一 Clip 内“与下一镜衔接”及跨 Clip 尾帧、参考资产和起始状态 |
| Sound | `音色特征：`始终保留：有适用Voice/Audio Reference时写明Reference锁定声音身份且不得文字重定义，并只保留轻量台词表演指令；无适用Reference但已有Confirmed Voice Profile时由其投影；两者都不存在时声明未建立独立音色资产且本Clip不创建或推导声音身份，不得自动触发AUDIO模块；无对白时明确无对白。台词、音效和声音桥继续执行；默认不得出现背景音乐，只有用户显式要求由Seedance为明确指定的Clip生成背景音乐时例外 |
| FX | 画面描述、空间关系、道具/FX状态、声音与残留后果 |

最终 Prompt 不得输出内部知识编号、Projection Ledger或另建知识字段；必须把适用知识写进 `templates/10_video_prompt.md` 已有字段。

## Prompt Package Mapping

映射固定为：

`CLIP-001 → G01 Prompt Package`

`CLIP-002 → G02 Prompt Package`

每个 G Package：

- 包含 Clip 表列出的1个或多个`分镜X`；单镜Clip按独立镜头执行，多镜Clip写成同一次长镜头中的连续执行阶段
- `参考资产：`只列预算审计通过的当前Clip实际真实资产，以及A/B必需但尚待用户补充的`REF-TAIL`受控声明；Projected Final Count≤9，待补充尾帧不计入已提交图片数，核心角色各自保留独立三视图/角色锁定图，非角色整合仅在超限风险触发后执行
- 保持来源分镜编号、顺序与逐镜字段完整
- 使用`# CLIP-X｜标题 Seedance视频提示词`作为区块标题，在`时长：`写明4—15秒的平台生成时长；不得创建独立CLIP标题字段
- 在【主风格】之前输出一次【首帧参考】与【尾帧限制】，只在Package末尾输出一次【反向提示词】
- 最后一分镜与`尾帧限制：`定义本Clip新的稳定结束状态；实际生成、提取并确认后登记为`REF-TAIL-XX｜CLIP-XX尾帧参考`
- 下一 G Package先依据当前Clip Start Requirement判定A/B/C，再检查资产可用性：A/B均在`参考资产：`列统一`REF-TAIL`名称、对应用途和真实状态；A在`首帧参考：`写固定直接承接句，B明确另起新镜头重新构图且不得写该句；未上传时标记“待用户提供/待上传、未确认”，Prompt可交付但实际提交生成前补图。C不列`REF-TAIL`，可由Canonical资产、Spatial Blocking与文字End State建立新首帧

同一 Clip 内非末分镜的“与下一镜衔接”必须明确“同一 Clip 连续长镜头生成、不中断、不硬切”；Clip 末分镜必须说明与下一 Clip 的连接方式或最后一段收尾。
