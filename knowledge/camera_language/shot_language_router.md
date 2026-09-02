# Shot Language Router

## Purpose

把Shot Purpose转换为景别、角度、视点、焦段倾向、构图、摄影机运动和稳定降级的统一路由。

本文件只负责选择顺序，不重复定义Camera原子，不定义STATE-08字段。

---

## Required Inputs

- Shot Purpose / Required Coverage
- Character Blocking And Performance Evidence
- Space / Axis / Screen Direction
- Active Asset Versions
- Visual Direction
- Internal Duration / Dialogue Capacity
- FX And Sound Requirements
- Previous / Next Boundary

---

## Routing Order

每个正式SHOT固定按以下Director-to-Camera顺序完成，不得先选焦段、机位或运镜再倒推理由：

1. **Shot Purpose**：确定本镜带来的Narrative / Emotional / Relationship / Spatial-Action / Information / Atmosphere-Rhythm变化。
2. **Audience Attention**：观众第一眼、第二眼分别需要看到什么；若删镜，观众具体损失什么。
3. **POV / Audience Position**：观众跟谁知道、从哪里看、先于/同时/晚于人物获得信息。
4. **Relationship & Blocking**：读取Spatial Blocking、Pose Hierarchy、Relationship Topology、Axis与Screen Direction；不重新摆位。
5. **Composition Strategy**：决定距离、压迫、权力、疏离、亲密、窥视、对立、共享空间、留白、框中框、前景遮挡或Reveal中哪项承担主要功能。
6. **Shot Size**：由Required Evidence和表演载体决定；面部情绪不自动等于特写，身体/关系证据可能要求中景或全景。
7. **Lens**：与摄影机距离、景别、脸部几何、背景尺度、景深与对焦共同决定。
8. **Camera Position**：确定距离、高度、角度、侧位、安全轴线侧和观察权。
9. **Camera Movement**：选择Static或一个主要路径；写清Camera Movement Trigger、Path、Stop和End Composition，必要时才进入Movement Combination。
10. **Duration / Hold**：为动作、反应、信息延迟或Post-action Residue保留可见时间；不能用无理由移动填满停顿。
11. **Cut Motivation**：说明为何此刻继续Hold、切到反应、揭示、确认、对照或进入下一边界。
12. **Lighting / Color Readability**：保证上述关键证据可见，不以色光效果覆盖信息层级。
13. **Execution Risk**：读取knowledge/quality/execution_risk.md。
14. **Stable Downgrade**：保留Required Coverage与导演功能，删除装饰复杂度。

---

## Purpose Map

| Shot Purpose | Scale / View Priority | Camera Tendency | Composition Priority | Default Stability |
|---|---|---|---|---|
| 建立空间 | Wide / Establishing | Fixed、Pan或简单Crane | 地理、路线、锚点 | 高 |
| 人物进入/寻找 | Medium / Shoulder / Side | Shoulder Follow或Tracking | 路线、遮挡、目标 | 中高 |
| 信息发现 | Medium→Close Coverage | Fixed、短Push或Pan Reveal | 刺激与视线 | 高 |
| 精细反应/口型 | Close / Clean Eyeline | Fixed或极轻Push | 面部与倾听者证据 | 最高 |
| 双人关系 | Two-shot / OTS Coverage | Fixed、Side Track或克制Dolly | 左右、距离、轴线 | 高 |
| 动作结果 | Medium/Wide + Detail Coverage | Single Track或固定机位 | 因果与物理结果 | 高 |
| 群像调度 | Wide / Layered | Fixed或单向移动 | 前中后景、阵型、方向 | 高 |
| FX揭示 | Scale Evidence | Fixed、Pull或单向Reveal | 来源、尺度、交互 | 高 |
| 情绪余韵 | Close/Medium/Wide按关系 | Static Hold、Pull或停止跟随 | 稳定结束与留白 | 高 |

---

## Conflict Rules

- 精确口型、微表情、快速动作、群体、复杂FX任一为主时，摄影复杂度降一级。
- 多景别、多视点、新刺激—反应或换侧必须拆成Coverage。
- 导演模式只能影响选择偏好，不能覆盖资产、空间、证据和稳定性。
- 找不到充分动机时优先固定机位；只有存在明确Trigger、Stop与独特功能时才使用单向Push/Pull/Track。

---

## Internal Decision Record

记录Purpose、Audience Attention Hierarchy、Audience Position、Blocking Source、Composition Function、Shot Size、Lens / Distance、Camera Position、Movement Trigger / Stop、Duration / Hold、Cut Motivation、Selected Atomic Language、Rejected Alternatives、Risk Level和Stable Downgrade。

这些内部栏目不得进入STATE-08最终Prompt。
