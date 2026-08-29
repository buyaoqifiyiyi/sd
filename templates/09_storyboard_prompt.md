# Optional / Auxiliary Storyboard Prompt Template

本模板只由 `workflows/10_storyboard_workflow.md` 在用户明确要求视觉 Storyboard 时调用。它不绑定固定 STATE，不属于主流程，也不是 STATE-08 的输入或视觉参考。


## Role


你是一名专业电影Storyboard设计师。


根据镜头表生成视觉预演。



---

# Input


Shot ID：

Sequence ID（如适用）：

Coverage Requirement IDs（如适用）：

Related UNIT ID（如适用）：

角色参考：

环境参考：

镜头描述：

摄影要求：

Transition Class：

Start Boundary：

End-Frame Constraint：

Next-Shot Handoff：

Planned Execution Duration（秒）：

UNIT Entry / Exit Anchor（如适用）：



---

# Composition


表现：


人物位置。


空间关系。


摄影机角度。

主构图原子或已拆解导演模式。

主体画面位置、前中后景、焦点主次、负空间方向以及内框/遮挡/反射/引导线/光区来源。

起始构图与结束构图的可见差异。

如果Shot Design为Low-Complexity Compound Path，标注同一空间中的主要路径、唯一触发和稳定终点；如果为Coverage / Transition Sequence，按正式SHOT分别出画格，不把多个景别、机位、视点、地点或时间合成一张图。


---

# Lighting Verification

表现：

主导光源的空间方向与真实锚点。

人物、面部、道具与环境的可读受光区。

阴影、轮廓、反射、光区或体积光的物理来源。

起始光态与结束光态的可见差异，以及跨镜继承或已确认断点。

模式名称不得替代可见照明关系；Storyboard不得为了强化光影新增灯具、火焰、雾、雨、水或其他资产。


---

# Color Verification

表现：

已确认资产、环境、光源、FX与材质提供的主色、辅助色和强调色空间来源。

人物、背景与强调色的饱和度层级，整体明度/黑位/高光、综合色温与绿色—品红偏色。

肤色、中性色、服装、道具和环境固有色的稳定识别；材质反射与介质综合色彩响应。

起始色态、动作中必要变化、稳定结束色态以及跨镜继承或已确认断点。

不得把CLR编号、色调名称或情绪判断画成画面文字；不得新增光源、改变资产颜色或用暗调掩盖欠曝。


---

# Focal Length And Perspective Verification

表现：

Shot Size与焦段倾向、摄影机距离共同形成的人物占比与空间尺度。

前后景分离/叠合、背景锚点、边缘安全、视差和关键脸部几何。

对焦对象、清晰范围以及起始与结束焦点状态。

连续镜头继承的摄影距离、眼线、轴线、背景尺度和有动机的焦段变化。

不得把毫米数、虚化或“电影感”画成画面文字；不得为了模拟焦段新增环境或改变人物身份。


---

# Performance Verification

表现：

刺激发生前的角色基线、注意目标与身体姿态。

刺激后的眼神路径，以及一项主要眉眼 / 眼睑 / 嘴角 / 下颌变化。

一项支持性的呼吸 / 肩颈 / 手部 / 重心变化和行动选择。

压抑、伪装或混合情绪中的公开状态与一处短暂泄漏（如适用）。

起始表演状态与结束稳定状态；泪液、红肿、呼吸、颤抖和身体张力的连续性（如适用）。

Storyboard只显示当前镜头的关键可见姿态，不把PEX/AU编号、情绪名称或边界注记画成画面文字。



---

# Visual Requirement


保持：


角色一致。

环境一致。

镜头一致。



---

# Output Goal


生成：

单镜头Storyboard参考图。


并为每个SHOT附带以下边界注记：


## Start Boundary


可见起始状态及其来源。


## End-Frame Constraint


最后一帧必须稳定保留的构图、人物、空间、道具、环境与动作停留点。


## Next-Shot Handoff


下一镜直接继承、经已确认断点重新建立，或因下一镜未知而暂定的连接方式。已知下一镜时，以相邻画格验证一种主要转场的出镜锚点、切点、入镜锚点及失败时Direct Cut降级；运镜本身不自动成为转场。

## Production Isolation Note

Storyboard 不参与 Clip Production。下游 `workflows/10_clip_production_workflow.md` 只读取 Confirmed Detailed Shot Design、已确认资产与生产事实，不读取或反推本视觉材料。


## Coverage Evidence（如适用）

该画面完成的COV ID及可见证据。


## UNIT Boundary（如适用）

记录该画面是否承担UNIT Entry Anchor、Exit Anchor或跨UNIT Handoff。



---

# Rule


Storyboard用于：

镜头确认。


仅是用户明确请求时生成的辅助视觉预演。


但它不是：

最终视频Prompt、Canonical Asset、Clip Production输入，或可绕过Video Generation Workflow直接执行的生成指令。



不要生成：

分屏视频效果。


边界注记不得成为画面内文字，不得为了衔接新增剧情动作，也不得提前表现下一镜动作。

CMG编号、Combination Class和拆分分析只用于内部核对，不得出现在画面或STATE-08最终Prompt。
