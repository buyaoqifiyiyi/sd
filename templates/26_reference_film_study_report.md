# Reference Film Study Report

本模板只由`workflows/22_reference_film_study_workflow.md`在用户要求拉片、拆镜头或分析参考片时调用。它不绑定固定STATE，不属于主流程，不是项目交付物，也不是STATE-08的输入。

它拥有本报告的**用户可见字段、顺序与必填性**。测量词表、判据与质量门不在本模板重复定义。

---

# Study Identity

- Source Video：
- Study Title：
- Study Scope：Full Film / Segment（Segment 写明起止时间码）
- Study Purpose：Style Reference / Editing Rhythm / Material Inventory / Other
- Reference Film Study Dir：
- 交付日期：

# Execution Condition｜执行条件

- Measurement Path：Measured（node + ffmpeg 实测）/ Manual（人工回看，无实测数值）
- 测量参数：`sceneThreshold` / `minShotSeconds` / `trackHz`
- 检测切点数 / 合并后镜头数：
- 补刀数 / 并刀数：
- 未实测项与原因（Manual 路径必填）：

**不得在 Manual 路径下填写任何实测数值。** 未实测的时长与运动量一律留空或标注为估计，不得写成读数。

# Result Summary｜实际观看结果

- 片长：
- 镜头数：
- 平均镜长 / 中位镜长：
- 每分钟切次：
- 最短镜头 / 最长镜头（镜号 + 时长 + 位置）：
- 景别分布：
- 类别分布：
- 运镜分布（含固定机位占比）：
- 转场分布：
- 节奏形态（做节奏分析时必填：开篇钩子位置、转折位置、收口方式）：

# Output Artifacts｜本次落地的文件

| Artifact | Path | 状态 |
|---|---|---|
| 拉片主数据（shots.json） | | |
| 运动曲线（track.json） | | |
| 时间码镜头表（shots.md） | | |
| 单页交互式报告（shots-report.html） | | |
| 关键帧目录（frames/） | | |
| 联系表目录（sheets/） | | |
| 对照合成视频（如已请求） | | Not Requested / Produced / Failed |

报告打开方式与播放器指向：

# Camera Grammar Control｜机器字段与模型字段

本报告的机器字段与模型字段必须可区分，**不得手改机器字段**：

| 字段类别 | 字段 | 来源 |
|---|---|---|
| 机器 | `meta`、`seedCuts`、`manualCuts`、`start`、`end`、`seconds`、`motion`、`id` | 测量引擎与`recut` |
| 模型 | `size`、`category`、`camera`、`transitionIn`、`subjects`、`frame`、`onscreenText`、`audio`、`rhythm`、`rhythmNote`、`note`、`cast` | 本轮判断 |

# Quality Gate Result｜质量门

- 结论：通过 / 有违规已修 / 未通过（未通过不得交付）
- 失败门与处理：
- **跳过的门**及其原因（跳过不等于通过，必须列出）：
- **提示（不拦）**清单与需要人回看的镜号：

# Shot Table｜逐镜表

**景别**：`extreme-wide` 大远景 / `wide` 全景 / `medium-wide` 中远景 / `medium` 中景 / `medium-close` 中近景 / `close` 近景 / `extreme-close` 大特写 / `none` 不适用

**类别**：`establishing` 定场 / `subject` 主体 / `dialogue` 对话 / `reaction` 反应 / `insert` 插入特写 / `pov` 主观 / `empty` 空镜 / `product` 产品展示 / `text-card` 字卡 / `transition` 转场镜头 / `archive` 引用素材

**运镜**：`static` 固定 / `push-in` 推 / `pull-out` 拉 / `zoom-in`·`zoom-out` 变焦 / `pan-left`·`pan-right` 摇 / `tilt-up`·`tilt-down` 俯仰 / `truck-left`·`truck-right` 横移 / `pedestal-up`·`pedestal-down` 升降 / `tracking` 跟拍 / `arc` 环绕 / `whip-pan` 甩镜 / `handheld` 手持 / `shake` 剧烈晃动 / `rack-focus` 变焦点 / `micro-push` 微推 / `roll` 旋转 / `drone` 航拍

**转场**：`cut` 硬切 / `dissolve` 叠化 / `fade-in` 淡入 / `fade-out` 淡出 / `whip` 甩切 / `match-cut` 匹配剪辑 / `wipe` 划像 / `morph` 特效转场

**节奏**：`hook` 钩子 / `setup` 铺垫 / `build` 递进 / `beat` 重音 / `turn` 转折 / `payoff` 兑现 / `breath` 换气 / `close` 收口

| Shot | In | Out | Sec | 实测运动 | 景别 | 类别 | 运镜 | 转场 | 画面 | 节奏 |
|---|---|---|---|---|---|---|---|---|---|---|
| S01 | | | | | | | | | | |
| S02 | | | | | | | | | | |

# Cast｜出场人物

| ID | 人物 | 说明 | 镜头数 |
|---|---|---|---|
| P1 | | | |

# Three-Layer Conclusion｜结论分层

## Observable Evidence｜可见证据

可直接从画面读出的机位、景别、运动、切点与信息顺序，以及本轮实际测得的时长与运动量。每条写明镜号或时间码。

- 

## Inference｜推断

对该运动触发与意图的解释。**每条必须显式标注为推断**，不得与可见证据混排。

- 

## Unknown / Not Confirmable｜不可确认

器材、轨道与稳定器、拍摄顺序、幕后流程、参数与后期。这一类不得因"成片看起来如此"而当作已确认事实。

- 

# Cross-Shot Camera Progression｜跨镜头机位递进

- 景别递进：
- 机位与视轴变化：
- 运动触发方式：
- 剪辑停点与信息顺序：

# Style Decompilation｜风格反编译（进入项目时才填）

**只在用户明确要求"把这种方法用于当前项目"时填写本区。** 未触发时整区写`Not Applicable`。

本区只做`### Reference-To-System Evidence Gate`的三类划分，**不建立Visual Grammar、不写Project Bible字段**——那些由STATE-04按该阶段既有规则完成。

- Observable Reference Evidence：
- Project Proposal：
- Unknown / Not Transferable（具名作品、器材型号、模型参数与能力数值、他人工作流步骤）：
- 入口：经`workflows/workflow_map.md`路由至STATE-04 Visual Development

# Boundaries｜本次不做的事

- 没有语音转写：台词只来自画面上烧录的字幕；没有字幕的片子`audio`大面积留空是正常的
- 不做人脸识别与人物自动归并：`cast`是人工编号
- 不评价片子好坏：报告只给事实与统计
- 不剪辑、不导出片段、不做镜头内物体检测
- 实测运动量不区分机位动还是主体动

# Status

Status：Draft / Confirmed / Not Applicable

Not Applicable Reason：

# Final Principle

参考片是研究材料，不是本项目事实：本报告产出证据与判定，不产出资产、交付物或项目状态。
