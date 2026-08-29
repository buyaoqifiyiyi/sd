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

1. Audience Evidence：观众必须看清什么。
2. Shot Scale：所需信息决定景别，不用情绪标签直接决定。
3. Perspective / Angle：谁观察、权力与空间关系。
4. Camera Position：距离、高度、侧位、轴线。
5. Lens Tendency：与位置、景别、脸部几何、背景尺度和对焦共同决定。
6. Composition：一个主构图原子及真实空间来源。
7. Movement：固定或一个主要路径；只有必要时进入Movement Combination。
8. Lighting / Color Readability：保证关键证据可见。
9. Execution Risk：读取knowledge/quality/execution_risk.md。
10. Stable Downgrade：保留Required Coverage，删除装饰复杂度。

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
- 找不到充分动机时使用固定机位或单向Push/Pull/Track。

---

## Internal Decision Record

记录Purpose、Required Evidence、Selected Atomic Language、Rejected Alternatives、Risk Level和Stable Downgrade。

这些内部栏目不得进入STATE-08最终Prompt。

