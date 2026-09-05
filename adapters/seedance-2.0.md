# Seedance 2.0 Adapter

```yaml
model: Seedance 2.0
duration: { min_seconds: 4, max_seconds: 15 }
timeline: { supported: false, default: omit }
reference_assets: { minimal_sufficient: true, visual_budget: 9 }
continuous_take: { supported: stable_short_clip }
```

在 Model Selection 后运行。Natural Clip 在 4—15 秒内则 KEEP；超过上限时才按已确认的动作、空间和 End-State 进行 `ADAPT_SPLIT`。不臆造 2.5 的 Video Extension、Targeted Edit、Clay Render、参考角色或时间控制能力。
