# Seedance 2.5 Adapter

```yaml
model: Seedance 2.5
duration: { min_seconds: 4, max_seconds: 30 }
timeline: { supported: true, default: omit, use_when: multi_beat_or_montage_or_complex_continuous_take }
reference_assets: { minimal_sufficient: true, visual_budget: 9, capability_upper_bound: { images: 30, videos: 10, audio: 10 } }
continuous_take: { supported: true, requires: long_duration_preflight_for_16_to_30_seconds }
```

在 Model Selection 后由 STATE-07 消费。23 秒 Natural Unit 经长时长预检 PASS 后保持单 Execution Clip；不因旧 15 秒规则拆分。34 秒 Natural Unit 才按连续性合同适配拆分。Timeline 是能力而非固定字段：单动作、简单一镜到底默认省略；多段动作、蒙太奇或连续长镜头内多个节奏节点才使用其必要语义。Targeted Edit 与 Video Extension 仍须有用户明确请求和有效输入。
