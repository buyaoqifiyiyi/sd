# Legacy Compatibility — Shot Execution Plan

- Active Route：false
- New Project Use：Forbidden
- Duration Notice：本文件中的4—15秒正式Shot窗口仅为旧项目兼容；新项目服从STATE-06可短于4秒，并在STATE-07按Model Execution Lock的模型窗口组织Clip：2.0为4—15秒；2.5为4—30秒，16—30秒须严格预检PASS，实际秒数由用户选择。

本模板不再绑定STATE-07，也不参与新项目主流程。仅用于读取或迁移旧项目；新项目使用`templates/08_shot_design_prompt.md`直接进入`templates/20_clip_plan.md`。

- Project ID：
- Status：Planning / Confirmed
- Source Shot Design Revision：
- Total Formal Shots：
- Formal Shot Duration Window：4—15秒
- Output Mode：Text Only
- Visual Storyboard Asset：None / Forbidden

## Production Safety Declaration

- 本文件是文字分镜执行计划，不是 Storyboard 图片或视频参考图。
- 禁止生成或引用Storyboard图片，包括线稿、分镜板、漫画格、接触表、拼图与多画面材料。
- 不生成线稿、草图、漫画格、分镜板、接触表、拼图或多画面参考。
- STATE-08不得把本文件截图、渲染图或任何 Storyboard材料写入【参考资产】；只允许引用已确认的单一角色/环境/道具/FX资产、合法首尾帧与上一Clip尾帧。

## Shot Order Table

| Shot ID | Scene / Sequence | Coverage / UNIT | 镜头目的 | 目标时长 | Start Boundary | End-Frame Constraint | Next-Shot Handoff |
|---|---|---|---|---:|---|---|---|
| SHOT-001 |  |  |  | 8秒（4—15秒） |  |  |  |

## Shot Execution Cards

### SHOT-001

- Scene / Sequence：
- Coverage / UNIT（如适用）：
- 镜头目的：
- Planned Execution Duration：8秒（必须4—15秒）
- Start Boundary：
- 起始人物/环境/道具/FX状态：
- 景别与机位：
- 焦段/摄影距离/对焦：
- 构图与空间关系：
- 镜头/运镜路径：
- 画面与动作过程：
- 人物表演与微表情：
- 光影与色彩执行：
- 台词与口型（如有）：
- 声音：仅对白、环境声、动作声、呼吸、Foley或剧情内声源；禁止背景音乐
- End-Frame Constraint：
- Next-Shot Handoff：
- 资产与连续性锁定：
- 风险与稳定降级：
- Applicable Knowledge Evidence：写可执行语义，不输出内部模式ID

按 SHOT ID 继续建立 Shot Execution Card。

## Adjacent-Shot Continuity Ledger

| From | To | Boundary Class | Outgoing Anchor | Cut Point | Incoming Anchor | State Inheritance / Rebuild | Direct-Cut Downgrade |
|---|---|---|---|---|---|---|---|
| SHOT-001 | SHOT-002 | Continuous Handoff / Motivated Discontinuity |  |  |  |  |  |

## Coverage And Validation

- 所有正式SHOT是否按原顺序出现且只出现一次：
- 每镜是否具有4—15秒目标时长、起止边界与稳定尾帧：
- 超过15秒的镜头是否已按自然执行边界拆分；少于4秒的镜头是否已安全延展或返回Shot Design重构：
- 人物/环境/道具/FX/轴线/动作/光影/色彩/声音是否连续：
- Applicable Knowledge是否已形成具体执行证据：
- 是否完全没有生成或引用Storyboard图片、线稿、拼图或多画面材料：
- 是否可作为只读兼容输入交给STATE-07 Clip Production，且无需读取任何Storyboard视觉资产：
- Pending / Return Route：
