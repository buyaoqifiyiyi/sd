# Sequence Continuity

## Purpose

在Scene、Coverage Requirement和Generation Unit之间保存可继承状态，防止每次生成重新初始化人物和世界。

---

## State Ledger Dimensions

每个边界按需记录：

- Character：身份、位置、朝向、视线、服装、身体状态
- Performance：情绪、呼吸、注意力、反应阶段
- Environment：地点、时间、天气、光线、空间结构
- Prop：持有者、位置、方向、状态
- FX：触发、强度、方向、覆盖、残留后果
- Sound：持续环境声、对白状态、音乐、声音尾部
- Camera Context：轴线一侧、观察方向、已建立的空间关系
- Story Knowledge：当前人物和观众已经知道的信息

---

## Boundary Types

### Continuous

同一连续时空，下一UNIT继承所有仍有效状态。

### Motivated Break

已确认场景切换、时间跳跃、蒙太奇、闪回或其他断点，只重建被剧情授权改变的状态。

### Unresolved

下一段未知或资料矛盾时保留安全结束锚点，不猜测新动作、新资产状态或新剧情结果。

---

## Sequence State Ledger

每个UNIT至少记录：

- Entry State
- Authorized Change
- Exit State
- Persistent State
- Next-unit Handoff
- Unresolved Items

只有Authorized Change可以改变Entry State中的事实。

---

## Conflict Routing

- 剧情事实冲突：返回Script Analysis或Scene Breakdown
- 资产身份冲突：返回对应Asset Workflow
- Coverage缺失：返回Sequence Planning
- 正式镜头无法实现：返回Shot Design
- 生成执行偏差：返回Video Generation或Editing

