# Movement Combination Continuity And Projection

## Combination Ledger

每个适用镜头或Coverage段内部记录：

| 项目 | 要求 |
|---|---|
| Class | A / B / C / D |
| Purpose / COV | 必须完成的可见信息 |
| Start Camera State | 侧位、高度、距离、角度、焦段倾向、焦点、稳定方式 |
| Primary Path | 方向、速度、主体同步关系 |
| Optional Continuation | 仅Class B；触发、同向路径和必要性 |
| End Camera State | 终点、景别、焦点、构图和稳定窗口 |
| Geometry | 轴线、左右、屏幕方向、背景锚点、遮挡顺序 |
| Split / Cut | Class C/D的拆镜点和真实锚点 |
| Downgrade | 删除次级运动、拆镜或固定机位方案 |

## Continuity Rules

### Axis And Screen Direction

连续动作保持相同关系轴线和屏幕运动方向。短弧线或侧移不能在镜头中途偷偷换侧；需要换侧时建立中性镜头、明确轴线重建或另行切镜。

### Lens And Distance

复合路径默认保持同一焦段倾向。摄影机靠近/远离产生真实视差，Optical Zoom只改变视角；二者不得无意叠加。长焦跟拍需降低速度和手持幅度，广角近距离需保护脸形与边缘。

### Focus

Rack Focus可以作为一次支持性光学变化，但不能与快速复合运镜、复杂动作和多主体换位同时发生。焦点必须在结束前落稳。

### Performance Readability

对话、微表情、泪液形成、手部细节和动作命中都需要可见窗口。摄影机若导致关键证据短于可读窗口，应固定、减速或拆镜。

### Transition Handoff

Class C/D按每个边界记录Outgoing Anchor、Cut Point、Incoming Anchor。镜头运动只提供可剪辑把手；实际技术由Transition模块选择。没有下一镜时保持低动作稳定结尾，不猜测未来转场。

## STATE-06 Projection

写入现有Shot Design内容：

- `Camera Movement`：主要路径、可选延续、触发与降级；
- `Camera Position` / `Lens Feeling`：起止机位、距离、焦段与焦点；
- `Composition Intent`：路径中的构图变化与稳定终点；
- `Coverage Mapping`：该SHOT完成的Required信息；
- `End-Frame Constraint` / `Next-Shot Handoff`：落点与跨镜把手。

可以新增内部“Combination Class”分析，但不得把它变成STATE-08字段。

## Clip Production Projection

STATE-07在Clip Production Plan中记录每个Clip的关键起始姿态、连续摄影机路径、内部Shot阶段、稳定结束姿态与风险降级。Class C/D保持正式SHOT边界，不得为合并Clip而把互斥景别、地点或时间压入同一生成单元。

## STATE-08 Projection

不新增字段，按以下方式序列化：

- `镜头/机位`：起始侧位、高度、距离、焦段倾向、一个主要路径；Class B再写一次有动机的同向延续、触发、速度和终点。
- `画面描述`：人物动作与摄影机路径同时发生时的可见过程，不复述模式名。
- `空间关系`：轴线、人物左右、屏幕方向、背景锚点、前景/遮挡和视差。
- `镜头结尾状态`：最终景别、机位、焦点、构图和稳定窗口。
- `与下一镜衔接`：Class C/D的主要转场、切点和入镜锚点；Class A/B只写真实把手。
- `【反向提示词】`：只在适用时限制无理由反向、换侧、越轴、随机叠加运镜、焦点游移、景别抽动或运动终点漂移。

内部CMG编号、Class/Gate/Ledger名称不得进入最终Prompt。

## Prompt Compiler Example

不合格：

`跟随逃离运镜，中景奔跑→跟拍→偏移带出追兵，电影感。`

合格：

`镜头/机位：摄影机位于跑者右后侧腰部高度，以中景同速向前跟拍；跑者越过门框后，摄影机沿原方向轻微向右横移一次，将后方追兵纳入画面左后景，随后停止横移并保持跟拍距离。空间关系：跑者始终位于画面右前景，追兵位于左后景，双方屏幕运动均由左向右，摄影机不换侧、不越轴。镜头结尾状态：两人位置与距离清楚，摄影机落在稳定中景并保留短暂可剪辑窗口。`

## Final Principle

最终Prompt只呈现模型需要执行的路径、空间和落点，不呈现内部组合学名。
