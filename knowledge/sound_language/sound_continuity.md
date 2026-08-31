# Sound Continuity

## Sound State Ledger

镜头边界记录：

- Persistent Ambience
- Local Source Position
- Dialogue Speaker And Line State
- Foley Tail
- FX Sound Tail
- Intended Silence
- Bridge / Cut / Fade Logic

---

## Connection Types

### Continuous Handoff

同一时空的底噪、持续声源、对白状态和声音距离必须继承。

### Sound Bridge

声音可先于画面进入或越过切点延续，但必须说明声源归属和叙事目的。

### Motivated Audio Discontinuity

场景、时间或主观听觉发生变化时，可以硬切、衰减或重建声场；必须有明确断点。

### Unresolved Handoff

下一镜未知时，只记录当前可验证的声音尾部，不假设新的音乐、对白或环境声。

STATE-08中的声音尾部和Sound Bridge只允许对白、环境声、动作声、呼吸、Foley、FX声或剧情内真实声源。后期音乐连续性只由显式调用的独立MUSIC / SEED-MUSIC模块维护。

---

## Checks

- 声源位置是否与画面空间一致
- 摄影机/人物距离变化是否反映在响度和空间感中
- 切镜是否让持续声无原因消失
- 对白是否在说话动作结束后继续
- FX结束后声音尾部是否符合物理衰减
