# FX Knowledge Index

## Purpose

本目录提供影视物理效果、环境效果、破坏与变化效果的设计知识。

FX Knowledge服务于：

- STATE-02 识别效果资产需求
- STATE-03 建立并确认FX Asset
- STATE-04 建立项目级效果美学
- STATE-06 设计逐镜头效果行为
- STATE-07 预演效果构图与遮挡
- STATE-08 转换为可执行的视频行为

它不新增主STATE，也不定义STATE-08最终Prompt Schema。

---

## Routing

### physical_effects.md

用于设计：

- 火、烟、雾、水、雨、雪、风、灰尘、碎屑
- 能量、发光、变形、破坏、坍塌
- 效果与角色、环境、道具、光线的物理交互

### fx_continuity.md

用于管理：

- 效果的起始、发展、结束和残留状态
- 跨镜头强度、方向、覆盖范围与环境后果
- 效果触发条件和镜头边界继承

---

## Loading Rule

只加载当前任务所需文件。

创建或修改FX Asset时，同时执行：

workflows/15_fx_asset_workflow.md

并使用：

templates/13_fx_asset_prompt.md

作为资产记录结构。

最终视频Prompt仍只能使用：

templates/10_video_prompt.md

