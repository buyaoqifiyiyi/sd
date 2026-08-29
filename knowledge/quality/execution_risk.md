# Shot Execution Risk

## Purpose

对单镜头的跨领域生成负载进行L1–L4分级。该等级不同于Camera Movement Combination的Class A–D，只用于内部设计、QA和重试路由。

---

## Risk Dimensions

每项按0–2计：

- Character / Group：单人、双人、多人交叉。
- Action：静态/简单、连续动作、快速碰撞或复杂调度。
- Performance / Dialogue：无对白、单人短对白、精确口型/重叠对白/哭笑等复合口部动作。
- Camera / Optics：固定或单路径、低复杂复合、换侧/变焦/高级路径。
- Composition / Visibility：无遮挡、可控遮挡、反射/曲面/群体/身份复制风险。
- Lighting / Color / FX：稳定环境、单一变化、多阶段FX或动态光色。
- Continuity：独立首镜、普通连续边界、跨UNIT/高风险状态继承。

---

## Levels

- L1：0–3，低风险，可直接执行。
- L2：4–6，中低风险，必须锁定主动作和单一摄影路径。
- L3：7–9，高风险，必须提供Stable Downgrade并减少至少一个非核心维度。
- L4：10以上或触发硬分镜条件，默认拆镜/拆UNIT，不允许直接进入STATE-08。

---

## Automatic L4 Triggers

- 多景别或多视点被伪装成一个SHOT。
- 快速群体动作 + 精确口型 + 复杂运镜。
- 角色身份反射/镜面复制 + 多人交叉 + FX。
- 动作、FX、摄影机同时反向或换阶段。
- 台词无法在内部确认时长中自然完成。
- 必要动作完成后没有稳定结束容量。

---

## Downgrade Order

删除装饰性运动 → 固定摄影平台 → 减少次要表演/群体变化 → 简化FX阶段 → 拆分Coverage → 拆分Generation Unit。

Required Coverage、剧情事实、资产身份和关键表演证据不得被降级删除。

