# FX Continuity

## Purpose

确保效果不会在镜头间无原因出现、消失、换向、重置或清除后果。

---

## FX State Ledger

每个FX在镜头边界记录：

- Active / Inactive
- Triggered / Not Triggered
- Intensity
- Direction
- Coverage Area
- Source Condition
- Residue
- Character Impact
- Environment Impact
- Prop Impact
- Lighting Impact
- Sound Tail

---

## Boundary Rules

### Continuous Handoff

下一镜继承上一镜最后一帧的效果强度、方向、覆盖范围、残留物和受影响资产状态。

### Motivated Discontinuity

只有已确认的时间跳跃、场景切换、蒙太奇或清理事件可以改变继承结果；必须建立新的时空锚点。

### Unresolved Handoff

下一镜未知时，保留可验证的安全结束状态，不猜测效果是否扩大、熄灭、消散或造成新破坏。

---

## Lifecycle Check

逐镜确认：

1. 效果是否已有触发原因。
2. 来源是否仍存在。
3. 运动方向是否与风、重力、冲击或发射源一致。
4. 强度变化是否有原因。
5. 被影响资产是否保留后果。
6. 最后一帧是否能成为下一镜可继承状态。
7. 声音尾部是否与视觉消散同步或形成已设计的Sound Bridge。

---

## Forbidden Resets

禁止：

- 雨中人物下一镜衣服自动干燥
- 碎裂物体下一镜自动复原
- 烟雾无风情况下突然换向
- 火焰消失但环境没有熄灭原因
- 自发光效果结束后反射仍无期限保留
- 爆炸结束后人物、道具和环境没有任何可见后果

