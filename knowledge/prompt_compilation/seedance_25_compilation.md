# Seedance 2.5 Native Compiler

## Scope And Boundary

仅当`Target Video Model = Seedance 2.5`且Model Execution Lock已锁定时使用，并同时读取`knowledge/seedance_25_profile.md`。本文件是内部 Model Compilation Template：把已确认的Clip翻译为2.5可验证的参考与任务语义；它不声明API字段、上传格式或网关能力，也不拥有最终Prompt字段、顺序或排版。

## Internal Resource Mapping

在共享Preflight、Reference Budget和Projection之前，为每项实际投喂素材建立内部映射：`来源ID / 上传顺序（如实际入口需要）/ 类型 / 当前Clip用途 / Authority / 可用状态`。仅保留最小充分集合。

- 图像可承担主体、动作、Clay Render/白模空间调度、风格、分镜格或关键帧等已确认用途；`REF-SKETCH`仍仅有Blocking / Pose / Axis / Camera / Action Path Authority，绝不覆盖Canonical人物身份、服装、年龄、材质、光色或最终画风。
- 实际上一段成片仅在`Video Extension`时登记为受控`REF-VIDEO`；它叠加而不替代首帧、尾帧、Canonical资产、A/B/C `REF-TAIL`和End-State。
- 音频仅在用户明确要求当前视频的声音或音色控制时才可映射；它不能解除Voice opt-in，也不能引入背景音乐、配乐或BGM。

映射账本仅供网关适配和语义投影，绝不原样写入最终Prompt。

## Task Semantics

从已确认的Execution Mode选择一项内部任务语义：常规参考生成、首/尾帧约束、Video Extension或Targeted Edit。实际网关没有明确支持时，退回共享稳定路径或请求合法输入；不得猜测2.5的角色、字段或编码。

- 首/尾帧只绑定已确认的首帧与End-State语义；如网关暴露角色机制，由网关适配层在已验证时处理，最终Prompt仍只使用既有`首帧参考`和`尾帧限制`。
- `Targeted Edit`必须由用户明确请求修改既有视频；只在已有分镜正文的合适字段表达已确认的受控时间段与“修改什么 / 保持什么”，不新增时间轴字段。其余模式禁止时间码、逐秒区间、帧率和帧数。
- 16—30秒只在共享Long-duration Preflight=`PASS`时进入编译；用户选择的时长不因未知网关状态预先回退，实际平台拒绝时才返回STATE-07拆回4—15秒Clip。

## Handoff

把已验证的2.5语义归并到`state08_projection.md`现有字段。不得输出`Target Model`、任务类型、内部参考角色、上传顺序、API字段、Long-form或预检字段；最终格式继续唯一由`templates/10_video_prompt.md`拥有。
