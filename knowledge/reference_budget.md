# Reference Budget / 参考资产预算控制

## Contract

本规则是 STATE-07 Clip Production 与 STATE-08 Clip-based Video Prompt / Video Generation 共享的全局参考资产预算合同。单个视频 Clip 最终提交给模型的图片参考硬上限为 9 张。它必须在`knowledge/clip_preflight_check.md`完成Continuity Classification与World-State Check之后执行；预算不得反向决定连续性分类，也不得让不属于当前世界状态的资产因为“已有参考位”进入清单。

目标不是把参考图压到越少越好，而是在不超过 9 张的前提下，优先保留表达更清晰、更准确的原始独立资产。资产整合是参考位不足时的条件性补救，不是默认预处理。

预算只对已经通过`knowledge/clip_preflight_check.md` Visual Input Eligibility Test的视觉条目计数。预算不能把纯文字约束变成资产，也不能因为一个说明写得很重要就给它分配图片位。

## Count Scope

预算按单个 Clip 独立计算。候选视觉条目只能来自实际存在、可访问且已经确认可用于当前视频生成的资产或合法首尾帧，包括适用的 Canonical Character / Environment / Prop / FX References、经Before-Single-Clip-Prompt Gate确认并绑定当前Blocking Signature的`REF-SKETCH-XX`与 Direct / Reference-Only 所需的首尾帧；或来自已经明确确定必须由用户实际补入的具体视觉参考图占位。待补视觉条目必须记录具体图像对象、实际投喂用途与`待用户补充/待上传、未确认`，占1个Projected图片位但不计入已提交图片数。它不得代替应返回STATE-03完成双确认的正式Canonical资产；A/B `REF-TAIL`仍执行其更严格的专用命名和用途规则。Final Assessment=`REQUIRED`但草图尚未生成 / 验证时，不得把名称占位当成可继续Prompt的替代；该Clip必须先完成草图Gate。

`REF-SKETCH-MASTER`不属于当前Clip视频参考候选：即使真实文件已注册并在草图生成时作为Sketch Presentation输入，也不写入最终视频`参考资产：`、不占本9张预算。只有由它辅助生成、再通过Sketch Validation与Template Content Leakage Check的当前`REF-SKETCH-XX`按1张真实图片计位。母版未注册时也不得创建待补视频资产占位。

- 一个实际提交的图片文件或帧占 1 个参考位。
- Voice/Audio Reference 不属于图片时，不计入 9 张图片上限，但仍必须按声音规则登记；若目标平台把它转换或上传为图片输入，则按实际图片位计数。
- 未实际存在、未生成、未确认、Candidate 状态、路径/ID无法核验或仅在文字中设想的“总设定图”“空间关系图”“动作关系图”不得进入候选清单或最终`参考资产：`。受控待补视觉条目只声明一个已经确定需要用户实际投喂的具体缺失图，不得把想象中的合成总图、普通文字规则或未来可能有用的素材包装为占位；A/B `REF-TAIL`必须同时写专用用途与“待用户提供/待上传、未确认”，不得冒充现有图片。
- 站位说明、不可换边、人物距离、同坐一张板凳、道具数量、空间关系、行为限制、禁止项与镜头规则占0个图片位，并必须从`参考资产：`移到对应的`空间关系 / 起始状态 / 道具状态 / 首帧参考 / 尾帧限制 / 反向提示词 / Spatial Blocking Rules`。
- 非当前 Clip 出场角色、未使用环境、未使用道具、未使用动作图、当前分镜World-State不适用的资产及与当前生成无关的资产必须在计数前删除。完全位于转换后世界的Clip不得保留转换前世界的环境或道具形态；只有当前Clip正在执行已确认状态转换时，转换前后资产才可按各自阶段同时作为候选。
- 上一Clip尾帧是否必需由Preflight的A/B/C决定，不由图片当前是否存在决定。A【同镜头连续承接】与B【新镜头参考型】均为`Tail Frame Required = YES`并预留1个Projected连续性图片位；【参考资产】必须直接列出`REF-TAIL-XX｜CLIP-XX尾帧参考`、对应用途类型与真实状态。未提供时写“待用户提供/待上传、未确认”，不得写假路径、不得冒充已上传/已确认图片，也不得计入已提交图片数；实际存在、可访问并已确认后才进入已提交图片清单。C【新镜头且无需尾帧】为`NO`，不得加入或预留上一尾帧。
- Storyboard、多格分镜板、拼图、接触表、Scene Top-down Blocking Map与设计表截图继续服从既有禁用规则，不因预算紧张而获得引用资格。唯一例外是按`knowledge/clip_preflight_check.md`为单一Clip生成 / 接收、通过Sketch Validation与Template Content Leakage Check、已注册Confirmed且只承担Clip Blocking / Visual Blocking Authority的`REF-SKETCH-XX`；它不是Storyboard、Planning Map或Canonical Asset，并按实际图片数计位。`REF-SKETCH-MASTER`不属于这个例外的最终视频输入层。

## Conditional Trigger Thresholds

先按World-State删除不适用资产，再统计当前真实候选数；加入已经由A/B确定的上一Clip尾帧预留位，以及其他合法连续性图片需求，得到`Projected Final Count`。Projected预留不等于真实资产已存在。【参考资产】可以包含A/B的待补充`REF-TAIL`声明，但“已提交图片清单”仍只计已上传、可访问且确认可用的图片：

- `Projected Final Count ≤ 7`：不整合，直接保留原始独立资产。
- `Projected Final Count = 8`：原则上不整合；必须检查是否还需为首帧、上一 Clip 尾帧或临时关键资产预留位置。没有额外需求时直接使用 8 张。
- `Projected Final Count = 9`：允许直接使用，但必须确认没有尚未计入的连续性参考需求。若当前已有 9 张且还必须加入上一 Clip 尾帧或当前首帧，则真实需求为 10 张，立即进入整合/释放流程并至少释放 1 个位置。
- `Projected Final Count > 9`：必须依序执行删除无关资产、去重、同类非角色资产整合、再计数；仍超限时按优先级裁剪，最终必须 `≤ 9`。

不得为了“预防可能超限”而在 7 张或以下提前整合；8 张且已确认没有额外帧需求时也不得默认整合。

## Core Character Independence Hard Gate

当前 Clip 中每个核心角色必须各自保留独立的三视图或角色锁定图。多个核心角色不得为了节省参考位合并成一张角色总表，也不得互相共享同一个角色外貌参考位。

角色动作图、姿势图、表情图或互动图只负责动作、姿态、表情或关系信息；它们不得替代、覆盖或重新定义独立角色图的脸型、五官、年龄感、发型、服装、体型、物种与身体结构。预算裁剪时，核心角色独立外貌基准不可被动作图替代。

## Integration Scope

只有触发超限风险后，才允许优先整合能由高信息密度单图清楚覆盖的非角色信息：

- 同一环境的多视角与关键区域
- 同一道具组或同一使用链中的道具
- 已确认的空间关系
- 已确认的动作/互动关系
- 已确认的使用示意或状态对照

整合资产必须真实存在并完成对应资产确认闭环。已有并已确认的总设定图可在超限时替代它完整覆盖的零散图；若需要新建总图，必须返回相应资产 Workflow 完成 Prompt确认、图像生成、图像确认与 Registry 登记，不能在 STATE-07/08 仅凭名称虚构。

如果独立资产表达更清晰、更准确且最终总数未超限，继续使用独立资产。不得因为 Registry 中已经存在总设定图，就强制把所有对应单图替换掉。某个单独道具、局部细节或动作是当前 Clip 的高精度关键对象且参考位充足时，应继续使用其独立图。

## Reference Budget Check

每个 Clip 在 STATE-07 建立计划时执行一次，在 STATE-08 最终编译前按实际文件/帧再执行一次：

1. 读取当前Clip Preflight的逐分镜World-State、实际角色数量、Prop State与连续性主分类；缺失或FAIL时停止，不得开始预算审计。
2. 列出当前 Clip 候选资产，逐项记录实际资产 ID/名称、Active/Confirmed状态、真实引用文件或受控ID、适用World-State / 转换阶段、用途与图片位数；待补视觉图则记录具体图像对象、实际投喂用途和待补状态。
3. 逐项回答`这是不是一张实际会被投喂/引用的视觉资产？`。答案为否的纯文字规则立即移出候选并记录迁移字段；不得继续参与去重、优先级或计数。如果对象已有真实视觉资产，改用正式ID与真实文件/受控ID。
4. 删除非当前 Clip 出场角色、未使用环境、未使用道具、未使用动作图、当前世界状态不适用的资产及其他无关项。
5. 去除同一文件重复引用与不增加信息的重复资产；不得把语义不同的核心角色图误判为重复。
6. 读取Preflight中的Visual Anchor State、A/B/C与`Tail Frame Required = YES / NO`。Final=`REQUIRED`且当前Confirmed `REF-SKETCH-XX`通过Signature与Template Content Leakage比较时，将实际草图计入当前Clip图片位并锁定其用途 / Authority；`REF-SKETCH-MASTER`始终为0个视频图片位。Final=`NONE`不预留草图位；普通Prompt Rewrite复用既有草图，不重复计数或生成；REPLACE / RETIRE / CREATE后以当前Active Anchor重新计算。A/B为上一Clip尾帧预留1个Projected位，并在【参考资产】直接列出统一`REF-TAIL`名称：A标“同镜头连续承接用途”，B标“空间/站位/景别参考用途”。实际存在、可访问且已确认时记录真实引用并计入已提交图片；未提供时写“待用户提供/待上传、未确认”，主动提示用户截取并添加，不计入已提交图片数但仍计入Projected Final Count。C不得加入或预留旧尾帧。统计`Projected Final Count`。
7. 若最终需求 `≤ 9`，直接使用独立资产，不执行整合；仅 8/9 张时完成预留与连续性复核。
8. 若最终需求 `> 9`，只对同类非角色信息执行整合。优先选择已经存在且已确认、能完整覆盖对应零散图的总图；新总图必须先完成资产确认闭环。
9. 再次计数；仍超限时按优先级从低到高裁剪，记录删除项、理由与由何种文字/已保留资产承接信息。
10. 最终核对每个核心角色仍有独立外貌基准；所有真实条目均属于当前World-State或合法转换阶段；所有待补视觉条目都能说明具体图像与实际投喂用途；没有文字伪资产或重复占位；Projected Final Count与实际提交图片数均`≤ 9`。待补视觉条目不冒充已提交图片；若是应成为Canonical的正式资产则按Return Route处理。其他失败不得确认 Clip Plan或输出STATE-08 Prompt。

## Retention Priority

发生超限且去重/整合后仍需裁剪时，按以下从高到低的保留优先级执行：

1. 当前 Clip 出场核心角色的独立三视图/角色锁定图
2. 当前主要环境
3. 当前关键道具
4. 当前Final Assessment=`REQUIRED`的Confirmed Visual Blocking Anchor与当前关键动作/互动关系
5. 上一 Clip 尾帧/当前首帧连续性参考
6. 特殊一次性道具/次要角色

该排序用于裁剪，不取消已经判定为 Direct / Reference-Only 的连续性硬需求。若连续性图片是当前边界的必需输入，必须先通过非角色整合或裁剪更低优先项为其释放位置；不得把必需尾帧静默删除后仍声称连续继承。

同理，Final Assessment=`REQUIRED`的Confirmed Visual Blocking Anchor不得为通过预算而静默删除；应先删除无关项、去重、整合或裁剪更低优先项。若与其他硬输入仍无法同时满足≤9，当前Clip不得输出Prompt，返回STATE-07调整执行合同或STATE-06降低Blocking / 动作复杂度。

## Required Audit Record

STATE-07 在`templates/20_clip_plan.md`现有 Clip Detail Card 内记录预算审计；STATE-08 不新增最终字段，只把最终清单写入既有`参考资产：`并在内部 Projection Ledger 复核。审计至少包含：

- 原始候选数
- Visual Input Eligibility结果、移出的纯文字伪资产及其语义迁移字段
- Continuity Classification与逐分镜World-State过滤结果
- Visual Anchor State / Blocking Signature、Final Assessment、当前Active `REF-SKETCH` Revision、KEEP / REPLACE / RETIRE / CREATE结果及其图片位；NONE时明确0位
- 删除无关项与去重结果
- `Tail Frame Required = YES / NO`及其判定证据；待用户提供/待上传、已加入的连续性图片位分别记录
- A/B/C尾帧使用方式；只要出现`REF-TAIL`，是否明确标注“同镜头连续承接用途”或“空间/站位/景别参考用途”
- 是否触发整合及触发原因
- 总图替代的零散图及总图真实资产证据
- 裁剪项与理由
- 最终参考图清单和总数
- 待补充`REF-TAIL`声明与已提交图片清单分开计数；不得把“待用户提供/待上传、未确认”写成已上传或已确认
- 每个核心角色独立图检查
- `PASS ≤ 9` 或 Return Route

## Acceptance Scenarios

| 场景 | 预期结果 |
|---|---|
| A. 候选7张，无额外需求 | 不整合，最终7张 |
| B. 候选8张，已确认无额外帧需求 | 不整合，最终8张 |
| C. 候选9张，另需上一Clip尾帧 | 真实需求10张，主动去重/整合/裁剪并至少释放1位，最终≤9 |
| D. 候选12张 | 自动删除无关项、去重、整合同类非角色信息，仍超限则按优先级裁剪，最终≤9 |
| E. 多核心角色场景 | 每个核心角色仍保留各自独立三视图/角色锁定图，不合并角色总表 |
| F. A同镜头连续承接但无实际尾帧图 | Projected Final Count预留1位；【参考资产】直接列`REF-TAIL`、同镜头连续承接用途与“待用户提供/待上传、未确认”；不计入已提交图片；Prompt可交付，实际提交生成前补图 |
| G. B新镜头参考型但无实际尾帧图 | Projected Final Count预留1位；【参考资产】直接列`REF-TAIL`、空间/站位/景别参考用途与“待用户提供/待上传、未确认”；不计入已提交图片；不得误写Direct |
| H. C新镜头且无需尾帧 | 不加入或预留上一尾帧图片位，不要求用户截图；依靠Canonical基础资产、Spatial Blocking与文字空间规则建立新首帧 |
| I. `板凳参考说明｜用途：锁定两人共坐同一张板凳` | 答案不是实际投喂/引用的视觉资产；占0个图片位，从参考清单删除并迁移到`空间关系`或`道具状态`。若已有真实双人钢琴凳图片，则以正式`PROP-BENCH-01`及其真实引用重新进入候选 |
| J. CLIP-04 Final=`REQUIRED`且`REF-SKETCH-04`已验证 | 当前草图作为1张真实视觉输入计位并写明Clip Blocking / Visual Blocking Authority；`REF-SKETCH-MASTER`保持0个视频图片位且不列入最终参考资产；普通Prompt重写继续复用同一图片位，不重复生成或重复计数；Blocking重构后按KEEP / REPLACE / RETIRE / CREATE更新Active Anchor与预算 |
