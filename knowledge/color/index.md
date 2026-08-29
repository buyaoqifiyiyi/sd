# Color Knowledge Index

## Module Contract

- Module Type：STATE-04、STATE-06至STATE-09辅助Knowledge。
- Trigger：项目或镜头需要综合色彩体系、调色倾向、综合色温关系、饱和度/明度/对比、肤色保护、色彩变化或跨镜色彩连续性。
- Inputs：已确认Character / Environment / Prop / FX Asset、Visual Direction、Lighting、Shot Purpose、时间/天气、材质与边界状态。
- Output Owner：STATE-04由Project Bible拥有；STATE-06由Shot Design Template拥有；STATE-08仍由`templates/10_video_prompt.md`拥有。
- Consumer：Detailed Shot Design、Clip Production、Video Generation、Review。
- Forbidden：新增光源、改变资产固有色、用色调替代表演、创建新主STATE或新的最终Prompt字段。

## Library

- [Color Foundations](foundations.md)：色相、饱和度、明度、对比度、白平衡/偏色、肤色、中性色、光源和材质的职责边界。
- [Tone Patterns](tone_patterns.md)：CLR-01至CLR-09九类附件色调的专业改写、适用条件和稳定降级。
- [Color Continuity](color_continuity.md)：跨镜综合色彩、肤色、中性色、资产固有色和动态变化连续性。
- [Image Source Coverage](image_source_coverage.md)：三张“AI电影色调”附件的逐图覆盖、纠错与去重结果。

## Shared Rule

色调不是情绪按钮，也不是光源、曝光或资产颜色的替代物。必须先确认真实光源与资产，再用色相关系、饱和度、明度/对比、白平衡/偏色、肤色/中性色保护和材质响应组织画面。最终Prompt不输出CLR编号，不新增“Color/色调”字段。
