# Clip Production Foundations

## Definitions

- **Formal Shot / 正式镜头**：STATE-06 Confirmed Detailed Shot Design中的导演镜头设计单位，编号与内容保持不变。
- **Clip**：一次视频模型生成调用的执行单位，可包含一个Shot，或多个按原顺序排列、可连续执行且合计4—15秒的相邻Shot。
- **Intra-Clip Handoff**：同一 Clip 内前一分镜到后一分镜的连续执行关系。
- **Inter-Clip Handoff**：两个独立 Clip 之间通过尾帧与其他锚点建立的连接关系。

Clip不同于Sequence Plan中的UNIT：UNIT是上游Coverage、状态与重试隔离规划，可以在正式SHOT出现前建立；Clip只能在Detailed Shot Design确认后由STATE-07建立，直接对应一次G Prompt Package。一个UNIT可以产生一个或多个Clip，Clip不得反向改写UNIT的Required Coverage。每个Clip至少含1个正式Shot。

Clip执行模式只有三种：

1. **单Shot**：一个正式Shot，单一镜头连续生成。
2. **多Shot连续生成**：相邻Shot作为连续动作或连续运镜阶段；不中断、不硬切，仍受同一空间、轴线与摄影机路径约束。
3. **多Shot有动机剪辑**：同一次生成内允许导演确认的Match Cut、遮挡切换或世界切换；它不是随机跳帧许可，必须有叙事功能、明确切点与视觉媒介、切前结束状态、切后世界/角色/环境/道具/摄影机的稳定重建状态、保留与改变的连续性锚点，以及模型容量不足时返回STATE-07拆分Clip的安全降级。

硬切、跨时空、跨资产版本或重建摄影机默认应拆Clip；只有通过上述多Shot有动机剪辑合同且模型容量支持时才可留在同一Clip。任何一个分镜只要自身为4—15秒，都可独立成为单Shot Clip。

单分镜Clip不是失败兜底，而是合法生成单位；当相邻合并会超过15秒、提高动作/摄影机容量风险或破坏边界连续时，应优先保留单分镜Clip。

## Duration Window

每个 Clip 的确认目标时长必须满足：

`4 秒 ≤ Clip 目标时长 ≤ 15 秒`

时长来自已确认的 Detailed Shot Design目标时长。缺少时长时只允许生成 Planning 状态的 Clip 表；必须先补齐或确认时长，才能进入 STATE-08。

不得：

- 用按秒时间码拆解最终 Prompt
- 让单个 Clip 超过 15 秒
- 用无叙事作用的随机动作填充不足 4 秒的 Clip
- 为了满足时长删除 Required Coverage

## What May Be Combined

相邻分镜只有同时满足以下条件才可以进入同一 Clip：

1. 原始顺序连续，没有跳过中间正式分镜。
2. 总时长在 4—15 秒内。
3. 同一连续时间，或模型可在一次生成中稳定完成的已确认轻微时间推进。
4. 空间、角色、服装、妆发、道具、天气、光源、综合色彩和 FX 阶段兼容。
5. 人物动作可由上一分镜结束状态自然进入下一分镜起始状态。
6. 180 度轴线、行进方向、视线和摄影机侧别兼容。
7. 组合后的运镜、对焦、表演、对白、群体与 FX 密度不超过稳定执行能力。
8. 内部衔接可写成连续摄影机路径、动作匹配、视线接力、主体接力、遮挡揭示、构图/图形匹配、光区/焦点变化；若为有动机剪辑，必须另有完整切镜合同，而非把跳变写成连续运镜。

## Mandatory Split Conditions

出现以下任一情况必须新建 Clip：

- 合计时长超过 15 秒
- 地点、时间、现实/回忆层、角色身份或主要环境资产发生断点
- 服装、妆发、关键道具、天气、主光方向或 FX 阶段无法连续继承
- 需要越轴、反向行进或重建空间但没有已确认动机
- 多个互相冲突的主要摄影机路径、复杂对白口型、群体动作或高复杂度 FX 同时发生
- 只能依赖后期溶解、淡入淡出、分屏、图层合成或其他生成后剪辑才能成立
- 相邻镜头的 Start / End Boundary 互相矛盾
- 有动机剪辑缺少切点、视觉媒介、切前结束状态、切后稳定重建状态或连续性锚点
- 模型不支持当前多镜剪辑容量；返回STATE-07拆分Clip，不以无原因跳变冒充导演剪辑

## Minimum-Duration Recovery

候选 Clip 少于 4 秒时按以下顺序处理：

1. 尝试与下一相邻分镜合并。
2. 再尝试与上一 Clip 合并，并重新检查 15 秒上限与全部连续性门槛。
3. 如果故事允许，延长已经存在的动作过程、自然反应或稳定收尾；不得新增剧情动作。
4. 仍不能成立时返回 STATE-06 Detailed Shot Design 调整，并保持 Clip 为 Pending，不进入 STATE-08。

## Visual Reference Boundary

Clip Production只读取Detailed Shot Design生产语义与Canonical Assets。禁止读取或转发Storyboard图片、分镜板、漫画格、拼图、接触表、Scene Top-down Blocking Map及任何设计表截图；这些材料不得进入STATE-08【参考资产】。STATE-08稍后按Before-Single-Clip-Prompt Gate生成 / 接收并验证的单Clip `REF-SKETCH`不来自上述Planning材料，按独立Visual Blocking Authority合同处理。

每个候选Clip还必须按`knowledge/reference_budget.md`建立图片参考预算。默认保留原始独立资产，只有Projected Final Count出现接近或超过9张上限的风险时才整合同类非角色信息；核心角色独立三视图/角色锁定图不得合并或由动作图替代。预算失败不通过Clip确认。
