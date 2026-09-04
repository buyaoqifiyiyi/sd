# REF-SKETCH-MASTER｜Visual Blocking Sketch Master Template

## Registration Record

- Reference ID：`REF-SKETCH-MASTER`。
- Authority Type：`Sketch Presentation Authority`。
- Presentation Intent Status：`CONFIRMED`；用户已确认以技术型导演Blocking Sheet作为默认草图表达参考。
- Asset Status：`REGISTERED`。
- Persistent Asset Path：`assets/ref_sketch_master.png`。
- Verified Dimensions：`1308 × 1202`。
- SHA-256：`4d086fcd7b58a43cd3e920277375bd8232ce43f81c9d370fff43c331f6ef97ac`。
- Recovered Session Source：引用会话附件`已生成图像 1.png`；2026-09-04已对上述持久文件重新验证PNG签名、尺寸与SHA-256。视觉检查确认其仍符合Technical Director Blocking Sheet、无性别技术人偶及Sketch Presentation Authority合同，因此保留为REF-SKETCH-MASTER。

运行时必须先从当前Skill根解析上述相对路径并验证文件可读、PNG签名、登记尺寸与SHA-256；验证通过后，草图生成调用必须把该绝对路径作为真实视觉参考输入传递。尺寸或SHA-256不一致固定判定为`Integrity Mismatch`：不得声称已使用注册母版，也不得仅为通过校验覆盖登记信息；先记录具体不一致原因，再且仅再可进入`TEXT_CONTRACT_FALLBACK`。只在实际工具不支持图像参考、文件读取失败、Integrity Mismatch或调用失败时才允许明确降级为`Text Contract Fallback`，并记录失败来源；不得把“已读取本Markdown”误报为“已使用母版图像”。

## Authority Boundary

`REF-SKETCH-MASTER`只控制草图如何表达，不控制当前Clip表达什么。

它控制 / 继承：

- `Technical Director Blocking Sheet`的整体技术图表达语言；
- 主Blocking图 + 辅助信息区的版式逻辑与信息层级；
- 由下述`Neutral Mannequin Representation Rule`统一控制的中性技术人偶抽象程度；
- Character Label、Facing / Gaze / Action Arrow与必要技术颜色标记；
- Spatial / Top-down Diagram的存在、Relationship Topology、Shared Facing、Interaction / Eyeline Axis与Camera Safe Side表达；
- Camera Information、Blocking / Action Notes、Reference Authority / Usage Notes区；
- 工程化可读性、空间错误检查友好性与最小充分信息密度。

它绝对不控制 / 不继承：

- 当前角色身份、人物数量、五官、发型、服装或身体视觉身份；
- 当前场景身份、具体环境结构、道具身份或示例中的固定物件；
- 当前人物位置、Blocking、Camera、Lens、Action、Pose、Gaze或Movement Path；
- 当前色彩、灯光、材质、天气、气氛或最终视频美术风格；
- 示例中的林夏、许栀、两女、钢琴、长琴凳、窗户、乐谱、雨景、教室文字或任何其他剧情内容。

正式原则：

`Master Template carries sketch language; Current Clip data carries blocking content.`

## Neutral Mannequin Representation Rule

本规则统一拥有S-SKETCH / P-SKETCH / A-SKETCH / Combined的人物绘制层；它是`Sketch Presentation Authority`的一部分，不新增Character Authority或平行草图标准。

- 默认把每名人物画成同一套`gender-neutral technical blocking mannequin / neutral pose dummy`：简化关节与中性人体块面、无真实五官、无发型、无具体服装或身份装饰、无胸部 / 腰臀等明显性别化体态，也不通过身材曲线、年龄感、美貌或角色气质表达视觉身份。
- 不读取或模仿正式Character Asset中的性别、脸、发型、服装、年龄感、体型或身份特征来重画草图人物。正式Character Asset仍是这些维度的唯一视觉权威；草图人偶只是`blocking proxy`，不拥有任何`Character Identity Authority`。
- 所有角色优先使用相同的人偶语言；人物识别只通过`角色名 / 角色ID + 技术标注颜色 + 左右 / 前后 / 位置标签`完成，不通过长发 / 短发、裙装 / 裤装、脸、身体曲线或其他外观差异完成。
- S-SKETCH、P-SKETCH与A-SKETCH均适用。A-SKETCH只有在身体比例本身构成动作路径、接触点、受力方向或可达性的必要物理约束时，才表达最小必要比例；即使如此也保持无性别、无身份化，不恢复角色外观。
- Position、Facing、Gaze Arrow、`Head LIMITED / LOCK`等Pose Permission、Relationship Topology、Camera / Axis与Action Path继续通过人偶姿态、标签、箭头、接触点和技术颜色表达。
- 本规则覆盖母版示例中的人物绘制内容：`REF-SKETCH-MASTER`只控制Layout / Diagram Language / Annotation / Information Hierarchy；即使母版示例出现发型、服装、性别或体型特征，当前草图也不得继承。

## Runtime Use Gate

S-SKETCH / P-SKETCH / A-SKETCH / Combined只有在`knowledge/clip_preflight_check.md`的Final Visual Blocking Anchor Assessment=`REQUIRED`时才进入生成；母版存在本身不改变Assessment，也不强制任何Clip出图。

生成当前草图时：

1. 先从Current Clip的Scene Spatial Snapshot、Shot-State Memory、Visual Anchor State / Blocking Signature、Pose Hierarchy、Relationship Topology、Camera / Axis与Action Path取得内容语义权威。
2. 若本记录为`REGISTERED`且`Persistent Asset Path`真实可读并通过尺寸/SHA-256完整性核验，将母版作为草图生成的视觉参考输入，只继承技术图表达语言与信息组织。
3. 若本记录为`UNAVAILABLE`、路径缺失、文件不可读或发生`Integrity Mismatch`，明确使用`Text Contract Fallback`并记录具体原因，不得声称参考了母版图片；仍按本文件的Authority Boundary与默认版式生成Technical Director Blocking Sheet，而不是艺术型Storyboard Illustration。
4. Current Clip事实与母版示例冲突时，始终以Current Clip语义权威为准；不得修改正式Blocking来迁就母版图。

实际生图输入、参数传递和候选图证据记录唯一使用`templates/23_visual_blocking_sketch_prompt.md`；不得调用`templates/09_storyboard_prompt.md`。

草图生成核心不得以“铅笔感、电影感、青春感、岩井俊二、阴雨氛围、唯美、概念艺术、高燃”等最终视觉风格词驱动。必要的线稿 / 铅笔介质只能作为低权重技术标注载体；首要目标是`Technical Director Blocking Sheet / Spatial Blocking Diagram`，不是`Artistic Storyboard Illustration`。

## Adaptive Layout Contract

默认信息组织至少包含：

1. **Main Blocking Diagram**：最大区域；能直接读出角色标签、位置、身体朝向、共享座位 / 桌面 / 车辆等Relationship Topology、环境锚点和Camera Direction。
2. **Spatial / Top-down Diagram**：证明左右 / 前后、Shared Facing、Interaction / Eyeline / Action Axis、Camera Safe Side和适用Movement Path。
3. **Camera Information**：只保留当前真正有控制价值的Shot Size、Camera Angle、Lens tendency与Camera Side，不堆砌器材参数。
4. **Blocking / Movement Permission**：按风险选择性标注`Position LOCK / Torso LOCK / Head LIMITED / Gaze CHANGE`等Permission；不要求每次机械列全。
5. **Usage / Reference Authority**：明确当前草图只锁空间、姿态、机位、视线或动作路径；草图人物是无性别调度人偶，不作为人物外观参考；人物外观服从正式Character Asset，环境 / 道具造型、材质、灯光与最终画风也不由草图控制。

布局继承信息层级与技术表达语言，不要求像素级复刻。三人围桌、追逐、武打、车辆内、狭窄空间或复杂道具场景可以重新分配区域、改变标注数量或合并信息区，只要Main Blocking、空间证明、Camera、Permission与Authority仍清楚可检验。

## Two-Level Reference Routing

- `REF-SKETCH-MASTER` → `Sketch Presentation Authority`：只告诉草图生成器“草图应该如何表达”；不绑定任何Clip，不进入Visual Anchor State，不控制Blocking Signature。
- `REF-SKETCH-XX` → `Clip Blocking Authority`：通过Sketch Validation并绑定当前Clip / Blocking Signature后，才控制Position / Facing / Distance / Relationship Topology / Axis / Camera / Pose / Gaze / Action Path。

两者都不得覆盖Active Character / Environment / Prop Canonical References的身份、结构或造型Authority。

`REF-SKETCH-MASTER`主要服务于生成当前`REF-SKETCH-XX`，默认不得进入最终视频Prompt的`参考资产：`、不得计入视频模型9张图片预算，也不得作为最终视频美术参考。只有当前草图生成执行环境明确支持并需要模板图输入时，才把真实已注册母版投喂给草图生成器；真正进入视频模型参考资产的是经验证的当前`REF-SKETCH-XX`。

## Template Content Leakage Check

每张候选`REF-SKETCH-XX`在注册Confirmed前必须执行Template Content Leakage Check：

- Current Clip人物数量、角色标签、空间结构、道具、Camera与动作是否完全来自当前语义权威；
- 是否无依据继承母版示例中的两女、人物发型 / 服装、钢琴、长琴凳、窗户、乐谱、雨景、黑板 / 文学文字或其他装饰内容；
- 是否把技术颜色标记误继承成最终场景色彩、灯光或服装设计；
- 是否把母版固定版式机械套用到三人围桌、武打、追逐或车辆内场景，导致当前Topology / Action Path不可读。

任一项命中即`FAILED / REVISE`，必须以Current Clip数据重做；不得删除或改写当前Clip事实来让结果贴近母版示例。

Template Content Leakage之外还必须执行`Character Appearance Leakage Check`：候选人物若出现明显真实五官、具体发型、具体服装设计、明显性别化胸腰臀 / 体态、年龄 / 美貌 / 气质身份表达，或依据正式Character Asset重画角色外貌，固定判`FAIL = Character Appearance Leakage / Identity Contamination`并重做；不得注册为Confirmed `REF-SKETCH-XX`。
