# REF-SKETCH-MASTER｜Visual Blocking Sketch Master Template

## Registration Record

- Reference ID：`REF-SKETCH-MASTER`。
- Authority Type：`Sketch Presentation Authority`。
- Presentation Intent Status：`CONFIRMED`；用户已确认以技术型导演Blocking Sheet作为默认草图表达参考。
- Asset Status：`REGISTERED`。
- Persistent Asset Path：`assets/ref_sketch_master.png`。
- Verified Dimensions：`1914 × 822`。
- SHA-256：`fadbcf14cff479361453ab6fda280c9d4b4818a834ac204d67852495ec601286`。
- Recovered Session Source：引用会话附件`已生成图像 1.png`；2026-09-02已从可访问的会话附件缓存复制到上述持久位置，并验证PNG签名、尺寸与SHA-256。

运行时必须先从当前Skill根解析上述相对路径并验证文件可读；验证通过后，草图生成调用必须把该绝对路径作为真实视觉参考输入传递。只在实际工具不支持图像参考、文件读取失败或调用失败时才允许明确降级为`Text Contract Fallback`，并记录失败来源；不得把“已读取本Markdown”误报为“已使用母版图像”。

## Authority Boundary

`REF-SKETCH-MASTER`只控制草图如何表达，不控制当前Clip表达什么。

它控制 / 继承：

- `Technical Director Blocking Sheet`的整体技术图表达语言；
- 主Blocking图 + 辅助信息区的版式逻辑与信息层级；
- 简化人体的抽象程度，不追求人物美术完成度；
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

## Runtime Use Gate

S-SKETCH / P-SKETCH / A-SKETCH / Combined只有在`knowledge/clip_preflight_check.md`的Final Visual Blocking Anchor Assessment=`REQUIRED`时才进入生成；母版存在本身不改变Assessment，也不强制任何Clip出图。

生成当前草图时：

1. 先从Current Clip的Scene Spatial Snapshot、Shot-State Memory、Visual Anchor State / Blocking Signature、Pose Hierarchy、Relationship Topology、Camera / Axis与Action Path取得内容语义权威。
2. 若本记录为`REGISTERED`且`Persistent Asset Path`真实可读，将母版作为草图生成的视觉参考输入，只继承技术图表达语言与信息组织。
3. 若本记录为`UNAVAILABLE`、路径缺失或文件不可读，明确使用`Text Contract Fallback`，不得声称参考了母版图片；仍按本文件的Authority Boundary与默认版式生成Technical Director Blocking Sheet，而不是艺术型Storyboard Illustration。
4. Current Clip事实与母版示例冲突时，始终以Current Clip语义权威为准；不得修改正式Blocking来迁就母版图。

实际生图输入、参数传递和候选图证据记录唯一使用`templates/23_visual_blocking_sketch_prompt.md`；不得调用`templates/09_storyboard_prompt.md`。

草图生成核心不得以“铅笔感、电影感、青春感、岩井俊二、阴雨氛围、唯美、概念艺术、高燃”等最终视觉风格词驱动。必要的线稿 / 铅笔介质只能作为低权重技术标注载体；首要目标是`Technical Director Blocking Sheet / Spatial Blocking Diagram`，不是`Artistic Storyboard Illustration`。

## Adaptive Layout Contract

默认信息组织至少包含：

1. **Main Blocking Diagram**：最大区域；能直接读出角色标签、位置、身体朝向、共享座位 / 桌面 / 车辆等Relationship Topology、环境锚点和Camera Direction。
2. **Spatial / Top-down Diagram**：证明左右 / 前后、Shared Facing、Interaction / Eyeline / Action Axis、Camera Safe Side和适用Movement Path。
3. **Camera Information**：只保留当前真正有控制价值的Shot Size、Camera Angle、Lens tendency与Camera Side，不堆砌器材参数。
4. **Blocking / Movement Permission**：按风险选择性标注`Position LOCK / Torso LOCK / Head LIMITED / Gaze CHANGE`等Permission；不要求每次机械列全。
5. **Usage / Reference Authority**：明确当前草图只锁空间、姿态、机位、视线或动作路径，不锁人物外观、环境 / 道具造型、材质、灯光与最终画风。

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
