# Seedance 2.0 Adapter

```yaml
model: Seedance 2.0
prompt_output_template: templates/10_video_prompt.md
duration: { min_seconds: 4, max_seconds: 15 }
timeline: { supported: false, default: omit }
reference_assets: { minimal_sufficient: true, visual_budget: 9, actual_image_input: named_real_file_or_controlled_id }
visual_blocking_sketch: { supported: true, submission: actual_image_input_in_existing_reference_assets, authority: [position, facing, distance, topology, axis, camera, pose, gaze, action_path] }
continuous_take: { supported: stable_short_clip }
capability_valid_as_of: 2026-09-11
```

在项目视频模型偏好通过STATE-06按Clip能力复核后运行。Natural Clip 在4—15秒内则KEEP；超过上限时才按已确认的动作、空间和End-State进行`ADAPT_SPLIT`。当Final Assessment=`REQUIRED`时，Confirmed `REF-SKETCH`必须以真实可访问文件或受控ID占用这9张视觉参考中的一个输入位，并在既有`参考资产：`逐项标明实际提交；仅文字列名不算提交。输入不可实际提交、Signature不匹配或预算不足即FAIL / Return Route。不得臆造2.5的Video Extension、Targeted Edit、Clay Render、参考角色或时间控制能力。

本Adapter的`duration`、`visual_budget`等能力数值属于`O｜Operational Parameter`，不是跨项目原则。`capability_valid_as_of`到期、模型版本更新或平台能力变更时，必须先重新取证再引用；未复测前不得作为当前依据，也不得把旧数值当成该模型的不变属性。
