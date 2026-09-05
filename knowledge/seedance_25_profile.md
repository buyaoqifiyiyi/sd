# Seedance 2.5 Model Profile

## Scope And Evidence Boundary

本Profile只在Model Execution Lock选择`Seedance 2.5`后由STATE-07/08消费。依据用户提供的火山方舟官方《Doubao Seedance 2.5 提示词指南》（41页）与《Doubao Seedance 2.5 教程》，它记录可核验的模型能力上限：单次生成最长30秒、最多50个参考素材（其中最多30张图/10段视频/10段音频）、可多轮Video Extension、Clay Render/白模、受控时间戳级定点编辑、绿幕、镜头视角与参考驱动编辑，以及更强多镜头叙事。它不声明未证实的API字段、上传格式、网关参数或所有第三方入口均可用；实际API/网关限制优先且取更严格值。

## Execution Modes

- `Standard Clip`：默认；沿用稳定4—15秒短Clip与既有Preflight、Reference Budget、A/B/C REF-TAIL和End-State合同。
- `Long-form Clip`：16—30秒；不是默认。只有镜头链、空间关系、表演连续性和动作/物理密度均通过更严格预检才启用；任一风险失败即拆回Standard Clip。
- `Video Extension`：以实际上一段已生成成片作为受控`REF-VIDEO`输入延展。它叠加于Canonical资产、首帧/尾帧、资产锁和End-State之上，绝不替代它们。
- `Targeted Edit`：仅用户明确要求修改既有视频时启用。仅此模式可在既有分镜正文的合适字段中写受控时间段语义；不新增时间轴字段、模型字段或逐秒分段。

## Reference And Authority

最多30图、10视频、10音频只是能力上限，Reference Selection / Routing仍采用最小充分原则，并受实际网关限制。不得因上限更高而填满额度。音频参考仍只在用户明确要求当前视频使用声音/音色控制时引用，且不改变Voice opt-in或视频Prompt永久禁止背景音乐、配乐、BGM。

经验证的无性别`REF-SKETCH`在2.5中可作为Clay Render/白模空间调度参考，但只拥有Position、Facing、Distance、Topology、Camera、Pose、Gaze和Action Path Authority。它不得覆盖Character外观/年龄/服装、Environment材质、灯光、色彩或最终画风；Character / Environment / Prop Canonical Authority与双确认继续优先。

多镜头叙事能力不放宽复杂多人交互、物理或动作风险。出现负荷过高、连续性不确定、状态重置或空间轴线风险时，执行既有拆分/降级并保留已确认上游事实。
