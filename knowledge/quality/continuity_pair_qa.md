# Adjacent-Shot Continuity QA

## Activation

从STATE-06起，对每一对相邻SHOT执行，包括跨UNIT、场景断点、时间跳跃、空镜和末镜收束。

---

## Pair Contract

每个边界记录：

- Previous Shot / Next Shot
- Boundary Class
- Outgoing Anchor
- Cut Point
- Incoming Anchor
- Inherited State
- Authorized Change
- Forbidden Anticipation
- Sound Tail / Bridge
- Direct Cut Fallback
- Result

---

## Checks

1. Boundary Class先于转场技术选择。
2. Continuous Handoff继承人物、环境、道具、FX、动作、情绪、光色和持续声音。
3. Motivated Discontinuity只重建剧情授权变化，身份和未授权事实继续锁定。
4. Unresolved Handoff不猜测下一镜内容。
5. 上一镜不得提前执行下一镜动作或对白。
6. 左右、视线、运动方向、道具持有者和轴线兼容。
7. Outgoing与Incoming Anchor在景别、焦段、构图和表演可读性上可剪辑。
8. 声音桥只使用剧情内声源；音乐桥只在Editing/Post。
9. UNIT重试不修改已接受的前序Exit Anchor。
10. 战斗、双主体、对峙、对话、追逐或相向运动已经逐项锁定A/B左右、身体朝向、视线目标、关系轴与摄影机轴线侧，而不是只写“面对彼此”。
11. 视线、攻击、武器、追逐路线、水流、能量或抛射物形成来源—路径—目标一致的空间连线；不得与喷口/武器方向、屏幕方向或受击位置矛盾。
12. 双方同框且相互面对时没有同时完整正脸；侧面、背侧或OTS关系锚点清楚。
13. Continuous Handoff的Outgoing Tail Frame与Incoming First Frame保持同一镜头几何；Reference-Only或Not Inherited具有合法边界说明。

---

## Return Routing

- 剧情/Scene断点错误：返回STATE-01或STATE-05事实拥有者。
- 资产状态错误：返回STATE-03。
- 镜头边界设计错误：返回STATE-06。
- Shot或边界事实错误：返回STATE-06；Clip组织或跨Clip Handoff错误：返回STATE-07。
- 生成结果执行错误：返回STATE-08或Editing。
