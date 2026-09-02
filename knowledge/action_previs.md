# Action PREVIS Knowledge

## Purpose

本模块把走位、道具交互、追逐、摔倒、舞蹈、特技与武打等动作，从抽象结果词编译为可见的物理因果、空间路径和可继承结束状态。它服务 `STATE-06 Detailed Shot Design` 的内部动作设计，不创建新 STATE，不要求固定 15 秒结构，也不拥有任何用户可见 Template 字段。

`knowledge/camera_language/director_patterns/action_composition.md`继续只拥有动作构图模式；本模块唯一拥有 Action Execution Level 与通用 Kinetic Chain。具体武术、舞蹈、驾驶或特技专业事实必须来自用户、已确认剧本、适用专业来源或项目资产，不能由本模块猜测。

## Module Contract

- **Module Name / Type**：Action PREVIS Knowledge；STATE-06 条件执行、STATE-07/08 消费、STATE-09 审核的内部动作编译 Knowledge。
- **Trigger**：Scene / Shot Mode Routing 判定为 `Action-dominant` 或 `Mixed`；`Performance-dominant` 镜头只有存在需要展开的物理动作时才按对应等级调用。
- **Not Triggered As**：独立 Workflow、新主 STATE、固定 15 秒打戏模板、武术招式库、视觉风格档位、最终 Prompt Schema 或动作资产生成器。
- **Position**：`STATE-06 Spatial Blocking Decision → Shot Purpose Gate / Scene-Shot Mode Routing → Action PREVIS → Professional Detailed Shot Script`。
- **Required Inputs / Owners**：剧情目标与动作结果来自 Production-Locked Script / Scene；人物、环境、道具与 FX 身份来自 Active Canonical Assets；起点、路径、终点、轴线与障碍来自 Confirmed Spatial Blocking Result；镜头目的与边界来自 STATE-06；Accepted Take / Accepted Canon State 存在时，由其拥有已接受的瞬时动作与站位事实。
- **Output Owner**：本模块只产生内部 Action PREVIS Record；STATE-06 用户可见动作语义仍映射到 `templates/08_shot_design_prompt.md` 的既有字段，STATE-08 最终 Schema 仍唯一属于 `templates/10_video_prompt.md`。
- **Read / Write Boundary**：只读已确认项目事实；内部 Record 可保留在当前 STATE-06 上下文、Spatial Blocking工件或既有 Execution Ledger，不创建新 ID、Registry、Template 字段或 Skill 根目录项目数据。
- **Downstream Consumers**：STATE-06 Detailed Shot Design、STATE-07 Shot-State Memory / Clip End-State Record、STATE-08 Prompt Compilation、STATE-09 Review。
- **Protected Facts**：不得改变剧情胜负、伤害结果、人物能力、动作顺序、资产身份、空间结构、关系轴、Shot / Clip 顺序、Accepted Canon State 或用户安全边界。
- **Conflict Route**：剧情或动作结果冲突返回 STATE-01 / STATE-05 事实拥有者；资产/道具/FX 冲突返回 STATE-03；路径、轴线、容量或动作 Coverage 冲突留在 STATE-06；Clip 组织与 carryover 冲突返回 STATE-07；只有 Prompt 转译或生成执行偏差留在 STATE-08。
- **Validator Invariants**：A1/A2/A3 均存在且复杂度递增；复杂度与视觉风格强度分离；A1 不强制完整动力链；A3 启用完整 PREVIS；Record 有稳定 End State / Next-action Carryover；不含固定 15 秒、默认高燃、强制硬撞、机枪式对招或高潮定格；不新增主 STATE 和最终字段。

## Action Execution Level

先按物理执行复杂度选择最小充分等级。等级只决定动作展开深度，不决定写实、商业化、夸张或奇幻风格。

### A1 Simple Physical Action

适用于走、坐、站起、拿起、放下、转头、开门等单主体或低交互动作。

只需锁定：`Start State → Visible Path / Change → End State`。道具动作再补持有手、接触点和结束位置。禁止为 A1 机械加入蹬地、腰胯、受力、FX、复杂运镜或完整动力链。

### A2 Coordinated Action

适用于追逐、拉扯、摔倒、接住、多人协调、复杂道具交互或穿越障碍。

在 A1 基础上补充：参与者先后、重心与支撑变化、空间路径、接触 / 近接触、受力或反作用、障碍与道具状态、恢复动作和可继承结束状态。只展开当前动作可见且必要的链节。

### A3 Choreographed Action

适用于武打、追车、舞蹈、复杂特技、连续攻防或多阶段高风险动作。

启用完整 Action PREVIS：先拆清动作 Beat、动力链、Coverage、轴线、接触与反应、恢复、稳定降级和下一动作继承。完整 PREVIS 是导演内部设计深度，不等于最终 Prompt 必须逐项打印全部链节。

## Style Intensity Is A Separate Axis

动作复杂度与视觉风格强度必须分开决定：

- **Realistic**：真实速度、支撑、惯性、接触与后果。
- **Commercial**：在物理可读前提下强化节奏、构图或重点反馈。
- **Stylized / Fantasy**：只有上游事实授权时增加非写实尺度、能力或 FX；仍需保留来源、路径、作用点、反馈与残留。

任何 A1/A2/A3 都不能自动推导某一风格；A3 也不默认高燃、玄幻、快速切镜或强 FX。

## Kinetic Chain Compiler

复杂动作按需从下列链节中选择；关键动作至少要让观众看懂“为什么发生、如何发生、最后留下什么”。不是每个动作都机械填写十一项。

1. **Intent / Trigger**：谁因何事件开始动作，目标或目的是什么。
2. **Preparation / Wind-up**：可见的准备姿态、蓄势、抓握或防守变化。
3. **Weight Shift**：重心如何在双脚、单脚、身体前后或高低之间转移。
4. **Ground / Foot Drive**：支撑点、蹬地、制动、轮胎抓地、支点或其他力源。
5. **Hip / Torso Transfer**：力量如何经髋、躯干、肩带或整个身体传递。
6. **Limb / Prop Trajectory**：肢体、车辆或道具的可见路线、方向、幅度与避障关系。
7. **Contact / Near-contact Point**：接触、擦过、抓住、落点或明确未命中的最近点。
8. **Force Response**：对方、道具、衣物、地面或环境如何产生可见反作用与位移。
9. **Follow-through / Inertia**：动作完成后的余势、制动、回摆或方向延续。
10. **Recovery / End State**：稳定支撑、姿态、位置、持有状态、体力与摄影机可读终点。
11. **Next-action Carryover**：哪些惯性、失衡、抓握、朝向或未完成动作必须由下一 Shot / Clip 继承。

对于过渡动作，只保留能改变可见结果的链节；对于 A3 关键 Beat，若省略某一链节会造成瞬移、无来源发力、接触不清或状态重置，必须补齐。

## Action PREVIS Record

内部记录最小结构：

```text
Shot / Beat:
Mode: Action-dominant / Mixed
Action Execution Level: A1 / A2 / A3
Style Intensity: Realistic / Commercial / Stylized-Fantasy
Start State And Trigger:
Selected Kinetic Chain:
Spatial / Axis Constraints:
Contact And Force Response:
Recovery / End State:
Next-action Carryover:
Coverage / Visibility:
Stable Downgrade:
```

## State And Continuity Compatibility

- Confirmed Spatial Blocking Result 提供长期几何、路径、障碍和 camera safe side；Action PREVIS 不重新摆位或越轴。
- STATE-07 Shot-State Memory记录每个动作 Beat 的当前局部状态；复杂动作跨 Clip 时，上一 End State 必须成为下一 Start State 或获得明确断点授权。
- 已接受 Take 的 Observed State 写入 Accepted Canon State 后，在同一瞬时维度上覆盖原 Planned State；不得无过程“纠回”计划动作。
- `REF-TAIL`只在 A Direct / B Reference-Only 需要时承接瞬时姿态、站位、朝向、动作阶段与构图，不拥有人物身份、环境结构或道具造型。
- A2 / A3存在高漂移的起点、路径、接触 / 近接触、受力方向、终点或Next-action Carryover时，只向`knowledge/clip_preflight_check.md`提供Visual Blocking Risk与A-SKETCH / Combined候选；是否生成、验证、持久化及进入参考资产仍由Before-Single-Clip-Prompt Gate唯一决定。A3不等于强制草图或Formal Keyframe。
- Reference Selection / Routing 只选择解决当前身份、空间结构、道具造型或瞬时状态风险的最小充分来源；不得把 PREVIS Record、Blocking Map 或文字动力链伪装成视觉参考资产。

## Prompt Pollution Boundary

本模块主要服务上游导演设计。STATE-08继续执行 `Source Carries State, Prompt Carries Delta`：

- 不输出 `A1/A2/A3`、Kinetic Chain 标题、内部 Record、QA 或路由标签。
- 不要求每个镜头写满十一环；只序列化当前 Clip 真正需要且未被 Source 锁定的动作因果、路径、接触、反馈与状态变化。
- A1 保持简洁；A2/A3 也只保留能改变可见结果、连续性或稳定性的链节。
- 不把其他 Shot 的动作阶段、历史失败、未来动作或重复资产描述带入当前 Clip。
- 若动作、群体、FX、摄影机和口型同时过载，先保护剧情结果、主体身份、空间与动作因果，再减少辅助动作、切镜、FX或摄影机复杂度；必要时返回 STATE-06 / 07 拆分。

## Final Principle

动作设计先证明起因、路径、力的传递、结果与可继承终点，再决定速度、构图、风格和效果强度。
