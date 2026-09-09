# MiniMax H3 Adapter

```yaml
model: MiniMax H3
duration: { min_seconds: 4, max_seconds: 15 }
aspect_ratio: { text_or_all_reference: ["21:9", "16:9", "4:3", "1:1", "3:4", "9:16"], start_end: input_image_ratio }
resolution: { modes: [768p, 1440p], recommended: 1440p, external_parameter_only: true }
frame_rate: { fps: 24, external_parameter_only: true }
timeline: { supported: basic_shot_structure, default: story_or_shot_segments, continuous_take: explicit_no_cut }
reference_assets: { all_reference: { images_max: 9, videos_max: 3, audio_max: 3, mixed_files_max: 12, video_or_audio_each_seconds: "2-15", total_video_or_audio_seconds: 15, audio_requires_image_or_video: true }, start_end: { images_max: 2, two_images: no_automatic_cut }, minimal_sufficient: true }
negative_prompt: { supported: true, concise_and_risk_specific: true }
audio_output: { native_stereo: true, explicit_reference_or_voice_control_only: true, non_diegetic_music: forbidden_by_skill }
dialogue_and_lipsync: { supported: true, explicit_only: true, multilingual: true, cross_shot_j_cut_l_cut: explicit_only }
prompt: { max_characters: 7000, preferred_structure: [reference_materials, core_idea, visual_process] }
execution_modes: [text_to_video, start_or_end_frame, start_end_frame, all_reference, video_edit]
unsupported_without_official_verification: [Seedance_Video_Extension, Seedance_timecoded_Targeted_Edit, long_duration_over_15_seconds]
```

在 Model Selection 后由 STATE-07 消费。Natural Unit 只有在 4—15 秒、动作和镜头复杂度通过预检时才保持单个 Execution Clip；超过 15 秒时按已确认的动作、空间、End-State 与 A/B/C 连续性合同 `ADAPT_SPLIT`。H3 具备基础分镜与较强切镜点遵从：多镜 Clip 可按故事线或 Shot 分段；要一镜到底时，明确单段连续动作且禁止切镜。两张首/尾帧图模式只补两帧间的动作、光影和声音，不能规划自动切镜。

MiniMax H3 的全能参考模式支持最多9张图、3段视频、3段音频，混合输入最多12个文件；视频或音频每段2—15秒、各类总时长最多15秒，音频必须与图片或视频一起输入。首/尾帧入口最多2张图。每个实际投喂素材在`参考资产：`中必须按上传顺序显式标注`@图片N / @视频N / @音频N`及唯一用途（人物/物体/场景/关键帧/风格/构图/动作/运镜/音色/音频复用/视频编辑）；不使用的素材不得列入，也不得伪造已上传状态。

负面提示词只收束当前高风险错误，并保留全局无 BGM 不变量；H3 编译时在末尾额外写`非叙事性音乐：N/A`。所有H3结果原生带双声道输出，但对白、口型、跨Shot J-cut/L-cut、音频复用或声音身份控制只有用户明确要求当前 H3 视频包含该控制时才投影到既有 `台词：`、`音效：` 和条件 `音色特征：`；不触发 AUDIO 模块，也不自动使用声音身份参考。

H3支持在已有视频基础上做人物、物体、场景、声音与细节编辑；仅在用户明确要求编辑且提供实际视频输入时，按`CHANGE`/`PRESERVE`最小变更执行，不写未获官方验证的逐秒时码。不得移植 Seedance 2.5 的 Video Extension、长时长、Clay Render或Seedance时码式Targeted Edit。现有 A/B/C `REF-TAIL` 可在H3首/尾帧或全能参考入口作为真实图片使用；缺图仍按C的Canonical + Spatial Blocking文字重建路径执行。
