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
14. 双人对话、反打、并排坐、追逐、对峙与相向运动均读取已建立的Interaction / Eyeline / Action Axis和camera safe side；切换机位后人物屏幕左右与相反眼线可以从Scene Spatial Snapshot和固定环境锚点复算。
15. 屏幕左右发生翻转时，不机械判定为错误，也不以“创意越轴”免责：必须存在沿轴线中性镜头、观众可见的摄影机跨轴移动、角色镜内明确换位，或插入隔离后以建立镜重建新轴线中的至少一种可感知过渡；新机位侧、固定地标与后续方向已稳定。
16. 同一连续场景内的人物位置变化满足`Start Position → Visible Movement Path → End Position`；下一镜无可见过程的换边、换位、前后层级交换或道具瞬移判定为失败。
17. Scene Spatial Snapshot只承担长期场景几何；Shot-State Memory、Accepted Canon State与REF-TAIL只承担各自局部/瞬时状态，任何一个临时来源都没有覆盖Environment Canonical的空间身份。
18. Pose按`Position → Torso → Shoulder → Head → Gaze`逐层继承，未授权上层没有被局部视线 / 头部Delta带动；Relationship Topology即使左右不变也未从Side-by-side漂成Face-to-face。存在Confirmed `REF-SKETCH`时，它与Blocking Signature一致、只承担Visual Blocking Authority，且普通Prompt Rewrite没有重复生成草图。

---

## Return Routing

- 剧情/Scene断点错误：返回STATE-01或STATE-05事实拥有者。
- 资产状态错误：返回STATE-03。
- 镜头边界设计错误：返回STATE-06。
- Shot或边界事实错误：返回STATE-06；Clip组织或跨Clip Handoff错误：返回STATE-07。
- 生成结果执行错误：返回STATE-08或Editing。
