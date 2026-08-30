# STATE-08 Semantic Projection

## Module Contract

- Module Type：STATE-08 Knowledge Adapter。
- Trigger：所有 Video Prompt / Seedance Prompt 撰写任务。
- Inputs：已确认项目事实、Active CHAR Version中已经存在的Confirmed Voice Profile与Voice/Audio Reference状态（如有）、STATE-06 Detailed Shot Design、STATE-07 Confirmed Clip Production Plan、适用Knowledge、`knowledge/clip_planning/continuity_and_projection.md`与`knowledge/11_seedance_adapter.md`。
- Output Owner：`templates/10_video_prompt.md`；本文件不拥有、增加、删除或改名最终字段。
- Consumer：`workflows/11_video_generation_workflow.md`。
- Forbidden：新增剧情、重选资产、改变镜头目的、创建新主STATE、创建另一套最终Schema。

## Fixed-Template Projection Gate

投影粒度固定为Clip。每个Confirmed Clip分别投影为一个完整的`# CLIP-X｜标题 Seedance视频提示词`区块，完整重复Template规定的全局字段；每个`分镜X`完整重复Template规定的十个分镜字段。

禁止使用方头括号旧章节、独立CLIP标题字段、条件字段删除、“与下一镜衔接”或其他新增字段。下一镜承接与Boundary Class语义投影到“镜头结尾状态”；跨Clip首尾帧语义投影到“参考资产”“首帧参考”“尾帧限制”和首/末分镜的起止状态。

批量授权只改变本轮Clip数量，不改变逐Clip结构。不得压缩、合并、共享、删减或改名字段；内容过长时按完整Clip自动分批，批次边界不得拆开单个Clip。

Template Mapping后与交付前各执行一次字段完整性检查。标题、九个前置全局字段、一个或多个逐镜十字段组、末尾反向提示词必须完整、非空、无重复、无额外字段并严格按顺序。任一项失败不得输出。

## Core Rule

所有适用且已确认的上游知识必须在最终Prompt中留下可见、可执行、可连续检查的语义证据。知识模块名称、内部表格、模式ID、Ledger标题与分析栏目不得原样输出。

## Clip Preflight Projection Gate

每个Clip在Reference Budget与Template Mapping前必须读取并执行`knowledge/clip_preflight_check.md`最终版。内部顺序固定为：`Continuity Classification → World-State → Character Count → Spatial Composition → Prop State → Transition Five Elements（适用时）→ Reference Asset Check / Budget`。

- 连续性必须在`视觉连续 / 剧情连续 / 主动切场或切世界`中三选一。只有视觉连续的Direct / Reference-Only且实际尾帧图存在、可访问、已确认时，才把上一尾帧按`REF-TAIL-XX｜CLIP-XX尾帧参考`写入`参考资产`；没有实际尾帧图时不得虚构，必须把文字End State承接写入`首帧参考`和首镜`起始状态`。剧情连续或主动切场不得机械引用，必须写明重建依据。
- 每个分镜明确World-State；只投影当前阶段实际存在、实际出场且适用的角色、环境、道具与FX。完全位于转换后世界的Clip删除转换前资产；转换Clip按Pre/Post阶段投影两种状态及其转换过程。
- 每个分镜锁定角色精确数量。剧情唯一角色必须在`人物一致性`及适用的`画面描述 / 空间关系`中正向明确唯一一只/名、前中后景无第二个同类，并在`反向提示词`禁止复制、分身、镜像重复、背景第二个与相似替身。
- 追逐/战斗/多人空间锁投影到`镜头/机位`、`空间关系`、`画面描述`与`镜头结尾状态`。追逐默认后追前逃，禁止并排正对镜头、同景深海报式合影或群像站桩。
- 道具当前形态、尺寸、持有者/左右手、位置、方向、悬浮许可、转换完成状态与结束状态投影到`起始状态`、`道具状态`和`镜头结尾状态`；不同世界形态不得混用。
- 适用转场必须先具备起点状态、转换媒介、运动方向/过程、终点状态与转场后首个稳定构图，再分别投影到`首帧参考`、`起始状态`、`画面描述`、`空间关系`、`道具状态`和`镜头结尾状态`。不得新增“转场”字段。

任一Preflight项FAIL时停止投影并按Return Route修正；不得把失败设计交给反向提示词兜底。

## Reference Budget Projection Gate

每个Clip在Clip Preflight通过后才可建立`参考资产：`。读取并执行`knowledge/reference_budget.md`，以实际引用文件/帧重算图片位：先删除当前World-State不适用、当前Clip无关与重复项；只有视觉连续的Direct / Reference-Only且连续性帧实际存在、可访问、已确认时才加入，无图时只作文字承接且不得虚构；剧情连续或主动切场 / 切世界不得加入旧尾帧；得到Projected Final Count。≤7不整合；8张且无额外帧需求不整合；9张只有在没有未计入的合法连续性需求时允许直接使用；已有9张且仍需上一Clip尾帧/当前首帧时按10张处理并至少释放1位；>9必须整合同类非角色信息，仍超限则按规定优先级裁剪，最终≤9。

当前Clip每个核心角色的独立三视图/角色锁定图必须分别保留，动作/互动图不得替代外貌基准。整合仅限环境多视角、道具组、空间关系、动作/互动关系与使用示意等非角色信息。独立资产更清晰且总数未超限时继续独立使用；已有总图不构成强制替换理由。

最终`参考资产：`只能序列化真实存在且已确认的资产/帧，逐项写资产ID或名称、真实引用、用途与锁定约束。上一Clip实际可用尾帧统一命名为`REF-TAIL-XX｜CLIP-XX尾帧参考`；未生成、不可访问或未确认的尾帧不得以名称占位或文字End State冒充图片。不得输出未生成/未确认的总图、空间关系图或动作关系图。预算审计保留在STATE-07 Clip Plan与内部Projection Ledger，不新增最终字段。

每个Clip投影前必须通过四项硬门槛：

1. `参考资产：`显式列出实际使用资产及用途/锁定约束，并在空间/动作连续性判断后决定上一尾帧是否正式引用。
2. `首帧参考：`明确Direct、Reference-Only、视觉连续但无实际尾帧图的文字承接、跨场景不作正式参考资产仅作连续性核对或首段无上一尾帧，并与分镜1“起始状态”一致；使用实际尾帧时逐字包含`以 REF-TAIL-XX｜CLIP-XX尾帧参考 为直接承接依据起镜。`
3. “镜头结尾状态”与前置`尾帧限制：`形成稳定、清楚、可冻结、可继承的尾帧接口；当前Clip使用上一尾帧时，必须定义本Clip新的结束状态供下一Clip承接。
4. “镜头结尾状态”同时明确Continuous Handoff、Motivated Discontinuity或Unresolved Handoff，不另建字段。

Sound属于逐镜必投影模块。每个“音效”包含具体环境底声/空间底噪或有理由的有意静默、至少一个同步前景声层和声音尾部。禁止用“无”“静音”“有效内容”或背景音乐禁令替代正向制作声音。

声音身份先经过Voice Reference Override Gate，但`音色特征：`始终保留：

- 有适用Voice/Audio Reference时，在`参考资产：`标明声音专用Reference，`音色特征：`写明声音身份由该Reference锁定且不得文字重定义；其他字段不得出现Voice characteristics、音高、声线、音域、共鸣、语速或音色质感。
- 无适用Reference但已有Confirmed Voice Profile且有对白时，以该Profile填充`音色特征：`。
- 有对白但没有任何已确认声音资产时，`音色特征：`写`No Voice Asset`声明：未建立独立音色资产，本Clip不创建或推导声音身份；不得自动触发AUDIO模块。
- 全段无对白时，`音色特征：`明确无对白以及听觉叙事由环境声、动作声与呼吸声承担。

`时长：`的4—15秒平台生成时长只复制Confirmed Clip Production Plan的目标时长，不得重新估算；最终Prompt不写逐镜时长、时间码、按秒动作区间、帧率或帧数。

## Global Projection Matrix

| 来源知识 | 固定目标字段 | 必须保留的语义 |
|---|---|---|
| Project / Clip Plan | Markdown标题；时长 | 正式Clip编号、人类可读标题、4—15秒平台生成时长；不输出独立CLIP标题字段，不把SEQ/BEAT/COV/UNIT变成栏目 |
| Format / Visual Development / Color | 画幅；主风格 | 已确认画幅、媒介、色彩来源与层级、明度/对比、白平衡/偏色、肤色保护、光线体系、镜头稳定性与表演尺度 |
| Character / Environment / Prop / FX / Voice Assets | 参考资产 | 只列当前Clip实际使用、真实存在且经Reference Budget审计后最终≤9张的图片资产；逐项写资产ID/名称、真实引用、锁定用途与禁止修改特征；核心角色独立图不可合并；Voice/Audio Reference只锁定声音；合法尾帧按Direct/Reference-Only/Not Inherited判定 |
| Previous Clip / Opening State | 首帧参考 | 首帧来源；有实际尾帧时使用统一`REF-TAIL`名称和固定承接句；无实际尾帧时文字承接且不虚构资产；人物姿态/位置/朝向/距离、摄影机/构图、环境/天气、道具、动作、光线与情绪状态及唯一承接模式 |
| Clip End State / Next Clip | 尾帧限制 | 可冻结最终帧、人物/摄影机/道具/环境/声音最终状态、最后1秒限制与下一Clip用途 |
| Character Continuity / Performance | 人物一致性；主风格 | 外观与状态锁定、表演尺度、跨镜湿润/伤痕/体力/情绪连续性 |
| Environment / Spatial / Lighting / Color | 环境一致性 | 地点、天气、固定结构、光源方向、色彩来源与锚点、材质响应、运动方向、轴线和背景逻辑 |
| Sound / Dialogue / Voice Identity | 音色特征 | 始终非空；Reference Override、Voice Profile Fallback、No Voice Asset或无对白四分支之一 |
| Cross-shot Risk | 反向提示词 | 默认禁BGM首句及本Clip真实高风险项；只有用户显式指定的Clip可使用音乐例外 |

## Per-Shot Projection Matrix

| 来源知识 | 固定目标字段 | 必须保留的语义 |
|---|---|---|
| Shot Scale / Focal Length | 景别；镜头/机位；画面描述；空间关系；镜头结尾状态；反向提示词 | 景别与焦段分离；摄影机距离、尺度、边缘安全、对焦/景深、运动约束与结束连续性；不输出FLN编号 |
| Camera Movement / Combination | 镜头/机位；画面描述；空间关系；镜头结尾状态 | 起点、路径、速度、触发、终点、轴线与稳定落点；每镜一个主要路径；边界语义进入镜头结尾状态；不输出CMG编号 |
| Composition / Director Patterns | 镜头/机位；画面描述；空间关系；镜头结尾状态 | 主体位置、前中后景、负空间、内框/遮挡/反射/引导线来源、焦点主次、变化过程与最终几何 |
| Lighting / Color | 起始状态；画面描述；空间关系；道具状态；镜头结尾状态；主风格；环境一致性；反向提示词 | 光源、方向、光质、曝光、介质、颜色来源与层级、材质响应、起止光色状态及连续性；不新增光线或Color字段 |
| Character Action / Performance | 起始状态；画面描述；人物动作与情绪；台词；音效；镜头结尾状态；人物一致性 | 刺激、注意/视线、主要面部与身体动作、呼吸、公开状态与泄漏、行动选择、强度、Settled State与连续性 |
| Dialogue Performance | 人物动作与情绪；台词；音效；音色特征 | 准确台词、轻量表演、口型与空间声；声音身份只服从已经存在的Reference或Confirmed Voice Profile；两者都不存在时不得临时推导 |
| Character Count | 人物一致性；画面描述；空间关系；反向提示词 | 每镜实际角色精确数量；唯一角色的正向唯一性和前中后景无第二个同类；复制、分身、镜像重复、背景第二个与相似替身禁令 |
| Spatial / Blocking | 起始状态；空间关系；画面描述；镜头结尾状态；反向提示词 | A/B左右、前后景、朝向、视线、距离、路线、遮挡顺序、关系轴线、正脸/侧背许可、同景深许可及最终位置；追逐默认后追前逃并禁止并排合影 |
| Prop | 起始状态；画面描述；道具状态；镜头结尾状态 | 当前World-State、形态、尺寸、持有者、左右手、位置、方向、悬浮许可、转换完成状态、物理变化过程和最终状态 |
| Sound | 音效；台词；镜头结尾状态 | Persistent Ambience、同步Foley/动作声/呼吸/对白/剧情内声源、距离与Sound Bridge/Cut/Fade |
| FX | 画面描述；人物动作与情绪；空间关系；道具状态；音效；镜头结尾状态；反向提示词 | 来源、触发、阶段、方向、尺度、强度、物理交互、光影/声音影响、残留后果与专项风险 |
| Editing / Handoff / Transition | 参考资产；首帧参考；尾帧限制；起始状态；镜头结尾状态 | Boundary Source、Transition Class、Outgoing/Incoming Anchor、Cut Point、继承/断点/未决状态与禁止提前动作；不新增边界字段，不输出TRN编号 |
| Sequence / Coverage / Clip | 画面描述；镜头结尾状态；Markdown标题；时长 | Required Coverage完成证据、Clip内逐镜状态链与跨Clip状态；内部ID不成为栏目 |

## Serialization Rules

Color、Lighting、Focal Length、Composition、Camera Movement和Director Pattern必须拆成固定字段中的具体执行语义，不得只保留“电影感”“冷色调”“85mm”“压迫构图”“缓慢推进”等标签。

最终Prompt不得输出CLR编号、CMG编号、FLN编号或其他内部模式ID。未触发用户显式音乐例外时，`反向提示词：`首句固定为“禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。”。

连续性投影固定为：

`首帧参考 → 分镜1起始状态 → 可见动作过程 → 分镜1镜头结尾状态 → 下一分镜起始状态或下一Clip首帧参考 → 尾帧限制`

同一Clip内的连续分镜在前一分镜“镜头结尾状态”中写明Boundary Class、同一Clip连续生成、Outgoing Anchor与禁止提前动作；后一分镜“起始状态”逐项继承。跨场景时明确断点与重建依据，不伪造连续动作。

## Applicability Gate

逐镜内部判断：资产与状态、Coverage目的、主要动作与表演、Camera/Composition、焦段、Lighting、Color、Sound、FX、Prop、Dialogue、群体表演、转场、Sequence与模型稳定性是否Applicable。只有Applicable模块进入投影；每个Applicable模块至少在矩阵指定的一项固定字段中留下具体证据。

未触发模块不得为了形式完整而虚构事实。模板字段始终完整，但不适用内容应明确写出“不适用”及具体原因，不得留空或写“同上”。

## Internal Projection Ledger

Template Mapping前建立一次性内部核对，不得原样输出：

| Applicable Source | Confirmed Fact / Design | Target Existing Field(s) | Evidence Present | Conflict / Return Route |
|---|---|---|---|---|

Ledger只防止语义丢失，不拥有最终Schema。发现上游冲突时返回事实拥有者，不以Prompt文案掩盖冲突。

## Semantic And Structure Loss Check

最终格式化前后各检查一次：

- Applicable Knowledge是否留下具体执行证据，未触发模块是否没有被虚构。
- 是否丢失摄影机终点、人物最终状态、FX后果、声音尾部或下一镜锚点。
- 是否泄漏内部知识标题、模式ID、Ledger或SEQ/BEAT/COV/UNIT栏目。
- 是否严格按Confirmed Clip Production Plan分组，每个Clip、每个分镜和每个字段都完整、顺序不变。
- 是否因批量或篇幅压缩、共享、合并、删减、改名字段，或使用“同上/沿用前文/略”。
- 是否正确保留`音色特征：`并执行Reference Override、Voice Profile Fallback、No Voice Asset或无对白四分支内容规则。
- 是否没有方头括号旧章节、独立CLIP标题字段、“与下一镜衔接”或其他额外字段。
- `参考资产：`、`首帧参考：`、`尾帧限制：`是否无条件存在且非空。
- `参考资产：`是否通过Reference Budget Check：最终图片数≤9、无当前Clip无关项、无重复占位、无虚构资产、核心角色各自独立；是否仅在超限风险触发后整合同类非角色信息。
- 是否通过Clip Preflight：连续性三选一且尾帧引用正确；逐分镜World-State与资产一致；角色精确数量、追逐/多人空间构图、关键道具状态和适用转场五要素均有现有字段证据；失败设计没有被反向提示词兜底。
- 是否只有实际存在、可访问且已确认的尾帧图才以`REF-TAIL-XX｜CLIP-XX尾帧参考`进入`参考资产`；无图时是否只作文字承接；有图时固定首帧承接句与本Clip新尾帧限制是否完整。
- 每个分镜是否完整重复十个固定字段；下一镜语义是否已进入“镜头结尾状态”。
- 未触发背景音乐例外时，`反向提示词：`首句是否为固定禁BGM句；例外是否仅作用于用户明确指定的Clip。

## Priority On Conflict

格式冲突优先级固定为：

`templates/10_video_prompt.md固定输出契约 > 任何旧Template / Workflow / Adapter / Knowledge / Rules / Validator / 示例 / 历史格式`

内容事实仍服从已确认上游资产、剧情和生产决策；Template只拥有格式，不拥有改写事实的权限。

## Final Principle

知识架构的价值不在于Prompt中出现多少专业名词，而在于每项适用知识都被转换成模型可执行、可观察、可连续验证的固定字段内容，同时每个Clip严格保持完整统一模板。
