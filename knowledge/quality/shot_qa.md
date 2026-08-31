# Shot-Level QA

## Activation

从STATE-06起，每个正式SHOT都必须执行；空镜也不能跳过环境、声音与边界检查。

---

## Hard Gates

任一失败则该SHOT不得进入下一阶段：

1. Story / Coverage：镜头目的来自已确认Scene或COV，没有新增剧情。
2. Asset Lock：所有出现资产绑定存在的Active Version。
3. Start / End：起始来源、稳定结束状态和下一镜衔接完整。
4. Space：人物左右、方向、视线、距离、轴线与行动路线可读。
5. Action：有起因、过程、结果，容量足够且无瞬移。
6. Camera：一个主要路径；复杂组合已分类并有降级。
7. Evidence：关键剧情、表演、道具或FX结果在选定景别和遮挡条件下可见。
8. Seedance Boundary：最终Prompt遵守Template、无时间轴、无背景音乐生成要求。

---

## Conditional Checks

### Character / Performance

- 身份、版本、服装和当前身体状态正确。
- 刺激、注意、反应、行动选择、Settled State可见。
- 嘴部动作、呼吸、哭笑、遮脸和台词不存在容量冲突。

### Dialogue / Lip-sync

- Exact Line和Speaker已确认。
- 内部时长能够容纳自然语速与停顿。
- 说话者嘴部可见时才把精确口型设为高优先级。
- 非说话者明确倾听状态，禁止误口型。
- 超出容量时返回STATE-06拆分、缩短台词或改变说话方式；不得在STATE-08异常加速。

### Camera / Lens / Composition

- 景别、摄影机距离、焦段、透视和景深因果正确。
- 主体、前中后景、负空间、遮挡和反射来源明确。
- 结束构图稳定且不越轴、不换侧、不随机变焦。

### Lighting / Color

- 光源、方向、强度、综合色温和材质响应有环境依据。
- 资产固有色、肤色、中性色和综合色彩连续。

### Sound / FX

- 声音绑定真实声源、动作或空间。
- FX来源、阶段、交互、残留和声音尾部完整。
- STATE-08不含配乐/BGM；音乐只有用户显式调用独立MUSIC / SEED-MUSIC模块后才另行交付。

---

## Result

每镜只允许：PASS / REVISE / REBUILD。

必须记录Affected ID、问题、Fact Owner、最小修复、Return Route和Recheck Scope。
