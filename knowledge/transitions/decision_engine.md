# Transition Decision Engine

## Decision Order

### Gate 0｜Is The Next Shot Known?

若下一镜未知、资料冲突或只生成当前单镜：选择 **Unresolved Handoff**。当前镜形成低动作安全结尾，不猜测转场、不生成未来动作；下一镜确定后成对复核。

### Gate 1｜Classify The Boundary

- 同一时空、动作、视线或因果连续：Continuous Handoff。
- 已确认地点/时间/主观层次变化：Motivated Discontinuity。
- 不能确定：Unresolved Handoff。

### Gate 2｜Find A Real Anchor

按优先级检查：

1. 同一动作阶段；
2. 视线与被看对象；
3. 反应与刺激；
4. 构图、形状、方向或尺度；
5. 同期声源或持续环境声；
6. 完整前景遮挡；
7. 已确认光态、介质或 FX。

没有锚点时回退 Direct Cut。

### Gate 3｜Choose One Primary Technique

#### Continuous Handoff

- 默认：Direct Cut。
- 共享动作且动作阶段可精确交接：Match on Action。
- A 的视线指向 B/物体，下一镜揭示目标：Eyeline Match。
- 下一镜承担刺激后的结果：Reaction Cut。
- 共享清晰的形状、方向、画面位置或尺度：Graphic / Direction / Scale Match。
- 同一剧情内声源可跨切点持续：Sound Bridge，作为 Direct Cut 或匹配切的辅助。
- 有完整、自然、已确认的遮挡：Occlusion Cut。

#### Motivated Discontinuity

- 默认：Direct Cut，并明确新时空锚点。
- 强烈节奏或反差：Smash Cut，仅在叙事明确需要时。
- 时间流逝、回忆、梦境或主题性叠化：Dissolve，仅在断点已确认且不会伪造连续动作时。
- 章节结束、长时间断裂或明确黑场/白场：Fade Out / Fade In。
- 已确认的共同图形、动作、颜色、光态或同期声：Motivated Match Cut。

#### Unresolved Handoff

不选具体转场。输出安全结尾、已知锚点与待确认项。

### Gate 4｜Physical Feasibility

若选择遮挡或光效转场，必须回答：

- 什么对象覆盖画面？
- 何时达到近乎完整覆盖？
- 下一镜从什么兼容状态开始？
- 它是否已存在于上游资产/场景/FX？
- 失败时如何降级为 Direct Cut？

无法回答时降级。

### Gate 5｜Sound Policy

只允许剧情内声音建立 J-cut、L-cut 或持续声桥，例如雨声、脚步、列车、门声、对白尾音、呼吸或机器声。不得使用背景音乐、配乐、歌曲或节拍作为 STATE-08 转场机制。

## Output Projection

内部先确定 `Outgoing Anchor → Cut Point → Incoming Anchor`，再进行以下字段投影：

- **上一G段前置【尾帧限制】**：定义可复用出镜状态；实际生成、提取并确认后保存为`REF-TAIL-XX｜CLIP-XX尾帧参考`。下一Clip先按Start Requirement判定A/B/C，再检查资产实际可用性；A/B的待补充声明不等于图片已存在。
- **下一G段【参考资产】**：先判定A/B/C。A/B均第一顺位列上一段`REF-TAIL-XX｜CLIP-XX尾帧参考`并分别标明“同镜头连续承接用途”或“空间/站位/景别参考用途”；未提供时写“待用户提供/待上传、未确认”，Prompt可交付但实际提交生成前补图。A使用固定直接承接句；B说明另起新镜头重新构图且不使用该句。C不要求截图、不列`REF-TAIL`，可由Canonical资产、Spatial Blocking与文字End State承接或重建。
- **镜头结尾状态**：写出出镜锚点、动作阶段、遮挡/焦点/光态、同期声尾部和稳定窗口。
- **与下一镜衔接**：写出边界类型、主要转场技术、切点、匹配锚点、继承/重建状态与禁止提前动作。
- **下一镜起始状态**：从入镜锚点开始，不重复已完成动作。
- **音效**：只写同期声音桥及空间状态。
- **反向提示词**：只写相关高风险错误；首个非空内容行无例外逐字写“禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。”。

该投影发生在两个独立Prompt Package之间，不得为了获得“无缝”而把相邻分镜合并进同一生成段。

内部分析可使用 `TRN-01` 等模式 ID；最终 Prompt 不得输出任何 TRN ID、Gate 名称或分析表格。
