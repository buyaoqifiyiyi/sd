# Seedance 2.5 Adapter

```yaml
model: Seedance 2.5
prompt_output_template: templates/12_seedance_25_video_prompt.md
duration: { min_seconds: 4, max_seconds: 30 }
timeline: { supported: timestamp_text_control, default: omit, use_when: multi_beat_or_montage_or_complex_continuous_take, placement: existing_shot_body_only }
reference_assets: { minimal_sufficient: true, default_capacity_limit: { combined: 50, images: 30, videos: 10, audio: 10, video_total_seconds: 30, audio_total_seconds: 30 }, actual_submission_limit: verified_gateway_or_surface_limit }
audio: { explicit_only: true, pure_audio_driver: supported, requires: confirmed_audio_source_and_explicit_motion_or_lipsync_scope }
reference_audit: { every_submitted_input_requires: unique_primary_role, no_role: exclude_from_submission }
visual_blocking_sketch: { supported: true, submission: actual_image_at_picture_n, authority: [position, facing, distance, topology, axis, camera, pose, gaze, action_path] }
continuous_take: { supported: true, requires: long_duration_preflight_for_16_to_30_seconds }
capability_valid_as_of: 2026-09-11
```

在 Model Selection 后由 STATE-07 消费。23 秒 Natural Unit 经长时长预检 PASS 后保持单 Execution Clip；不因旧 15 秒规则拆分。34 秒 Natural Unit 才按连续性合同适配拆分。

本Adapter的`duration`、`default_capacity_limit`（30图 / 10视频 / 10音频 / 合计50）等能力数值属于`O｜Operational Parameter`，不是跨项目原则。`capability_valid_as_of`到期、模型版本更新或平台能力变更时，必须先重新取证再引用；未复测前不得作为当前依据，也不得把旧数值当成该模型的不变属性。

Timeline 是能力而非固定字段：单动作、简单一镜到底默认省略；多段动作、蒙太奇或连续长镜头内多个节奏节点，可在既有分镜正文中使用与Clip时长一致、严格递进的`0—3秒 / 第3秒`时间戳语义。它不新增最终字段、表格或逐帧技术参数。每个时间段必须说明可见事件、摄影机、动作/对白/音效与结束状态；时间戳不精确承诺模型必然逐帧命中。

Seedance 2.5默认以能力上限规划参考容量：30图、10视频、10音频，合计不超过50；视频和音频各自总时长不超过30秒。最小充分原则只决定实际提交多少，不再把2.5人为回退为9图上限；实际入口/网关更低时才按已验证限制收缩。每项实际输入均须有唯一Primary Role。纯音频驱动只在用户明确要求用该音频控制当前Clip的动作、口型或节奏、且音源可用时启用；它不改变Voice opt-in和视频Prompt永久无BGM规则。

Targeted Edit 与 Video Extension 仍须有用户明确请求和有效输入。Dreamina Web专有的30—180秒一键长视频、标注编辑、绿幕、双视频无缝转场和多格分镜，只有用户明确指定Dreamina网页端且该入口可用时才可作为外部提交方案；不得将它们写成方舟/API能力或默认进入常规Clip。

当Final Assessment=`REQUIRED`时，Confirmed `REF-SKETCH`必须以真实可访问图像作为`@图片N`提交，计入图片与合计预算；它不是只在文本中提及的Clay Render标签。输入不可实际提交、Signature不匹配或当前入口没有剩余图像位即FAIL / Return Route。它仅控制Position / Facing / Distance / Topology / Axis / Camera / Pose / Gaze / Action Path，不能覆盖Canonical角色、环境、道具、材质、光色或最终画风。

## Dreamina Web Surface（显式入口限定）

这不是第四个模型，也不改变STATE-06后的`Selected Model = Seedance 2.5`；它只在用户明确说“Dreamina网页端 / Dreamina Web”时写入内部`Delivery Surface = DREAMINA_WEB`。没有该明确选择时，忽略本节并继续通用4—30秒路线。

- **Long Video**：可准备30—180秒的一次性网页提交包。沿用已确认剧本、资产、Shot和Director Intent；长提示用“参考素材职责 → 一句话总述 → 递进时间线/剧情 → 全局约束”。这不修改常规API的4—30秒能力或Clip Plan。
- **Smart Edit / Marked Edit**：必须有原始视频；标注编辑还必须有用户提供的标注帧/区域/锚点和对应时间点。提交包只写`CHANGE`、`PRESERVE`、适用时间段与区域，未标注区域默认保持，不能猜测标记位置。
- **Green Screen / Viewpoint Edit**：必须有原始视频和明确目标（透明/纯绿背景，或新的相机视角）；保留哪些主体、动作、构图和声音须逐项写明。没有实际入口或输入时，只交付Prompt方案，不宣称完成编辑。
- **Seamless Transition**：必须有两段用户提供视频；分别锁定两端内容不改，并描述衔接媒介、方向、连接点和连续性锚点。它不是常规Clip自动合并理由。
- **Multi-grid Storyboard**：必须有用户上传的多格分镜图；每格只作为剧情、构图、场景、动作和机位参考，仍用Prompt补足每镜可执行语义，不能把多格图误登记为Canonical资产或普通Clip视觉输入。
