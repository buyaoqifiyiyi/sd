# Poster Design Workflow

## Module Position

Module Type：STATE-04 Visual Development条件性辅助Workflow。

它不创建新的主STATE，也不替代`workflows/07_visual_development_workflow.md`。

## Trigger Gate

触发：

- 用户明确请求电影海报、Key Art、One-sheet、先导海报、正式海报、角色海报、概念海报、标题字或海报提示词
- 项目在STATE-04或之后，且已存在足够的影片判断、已确认资产和Visual Direction

不触发：

- 普通视频Prompt、Storyboard、分镜或镜头设计
- 用户未请求海报时的常规影视项目
- 普通社交媒体封面、缩略图或非电影宣传图

如果用户目标是海报但前置事实或核心资产尚未完成：

返回对应事实拥有者，不用海报文案补造剧情或资产。

## Required Resources

- references/artifact_revision_contract.md

执行前完整读取：

1. `references/project_workspace.md`
2. 按优先级选定的`<active-project-root>/project_status.md`或`portable_project_status.md`
3. 可访问的`<active-project-root>/project_bible.md`或当前对话已确认的Project Bible内容
4. 可访问的`<active-project-root>/asset_registry.md`或当前对话已确认的资产记录
5. `knowledge/poster_design/index.md`
6. `knowledge/poster_design/foundations.md`
7. `knowledge/poster_design/composition_and_motif.md`
8. `knowledge/poster_design/typography_and_layers.md`
9. `knowledge/poster_design/reference_rights_and_qc.md`
10. `knowledge/poster_design/genre_tendencies.md`
11. `templates/15_poster_design_package.md`

## Input Ownership

- 剧情、类型、人物关系与核心冲突：STATE-01 Script Analysis
- 角色、环境、道具与FX身份：Asset Registry及STATE-03资产输出
- 光影、综合色彩、摄影气质与整体观看体验：STATE-04 Visual Direction
- 海报用途、投放渠道、准确片名、宣传语、日期、credits与logo：用户或已确认项目资料
- 参考图：仅作为已分类的设计参考；直接编辑必须有用户授权

## Output Ownership

最终结构只由`templates/15_poster_design_package.md`拥有。

项目输出目录：

`<active-project-root>/poster_design/`

建议产物：

- `poster_design_package.md`
- `base/`
- `type/`
- `composite/`
- `delivery/`
- `layout-spec/`

## Processing Pipeline

### Step 1: Readiness Check

确认：

- 类型、亚类型与核心冲突可追溯
- 核心角色、环境和关键道具已确认或明确不适用
- Visual Direction已确认
- 海报用途、宣传阶段和目标渠道可判断

缺少准确文案时，使用`待确认`，不得虚构貌似真实的主创、日期、片商、奖项或电影节信息。

### Step 2: Poster Brief

建立：

- Poster Type与宣传阶段
- 目标观众和渠道
- Aspect Ratio / Delivery Format
- Exact Copy Ledger
- 必须使用的授权资产与不可改变元素
- 参考图角色及其授权状态

### Step 3: Narrative Promise

从已确认影片事实提炼：

- 一句话宣传承诺
- 情绪温度
- 关系模型
- 三个以内意象候选
- 一个一级视觉母题

母题必须是可见关系，不得只写“高级、震撼、电影感”。

### Step 4: Composition Selection

只选择一个Primary Composition Model，最多一个Supporting Model。

必须明确：

- 主体尺度与重心
- 前、中、背景职责
- 眼路与第一注意点
- 标题承载表面和安全区
- 关键资产不可遮挡区
- 多比例派生的重排策略

### Step 5: Reference And Rights Check

每张参考只分配一个主要角色：Composition、Palette、Lighting、Typography、Texture或Narrative Device。

记录：

- 可提取的抽象设计原则
- 必须重新设计的维度
- 是否允许直接编辑或裁切
- 字体、图片、纹理、logo与credits授权状态

任何未授权素材不得直接进入最终海报。

### Step 6: Visual System

继承而不改写项目Visual Direction，建立海报专用：

- 主色、辅助色、强调色与层级
- 明度、对比、综合色温、肤色和关键资产颜色保护
- 光线与标题表面的可读关系
- 胶片、纸张、印刷、玻璃、反射、数字监控或绘画质感
- 与影片类型一致的媒体完成度

### Step 7: Typography And Copy

建立Exact Copy Ledger并逐项标注确认状态。

定义：

- 主片名字体方向、字重、字距、排向、尺度与位置
- 宣传语、英文副题、日期、credits和法务信息层级
- 字图关系：压、穿、嵌、隔、退、反射或遮断
- 可编辑文字层、字体授权与替代字体策略

准确文字默认由可控排版工具制作。生成式字形只能作为草案，必须核字并重建。

### Step 8: Layered Production Plan

分别编译：

1. Base-image Prompt
2. Typography / Layout Specification
3. Composite / Delivery Specification
4. Negative Constraints

Base-image Prompt必须禁止最终文字、logo、桂冠、奖项、随机小字和未确认身份信息，并为标题保留结构性安全区。

### Step 9: Quality Gate

执行：

- Narrative Gate
- Thumbnail / Mid-distance / Close-read Gate
- Exact Text Gate
- Asset Consistency Gate
- Reference Originality Gate
- Rights Gate
- Delivery Gate

评分低于80，或Exact Text、Rights、Asset Consistency任一硬门槛失败时，不得标记完成。

### Step 10: Record Result

Work/Codex将设计包写入Active Project Root；普通Chat本机Root不可读时在当前对话交付设计包，不伪造本机落盘。

在Selected State Source当前STATE的Completed Tasks中记录Poster Design完成；若不适用，记录`Poster Design Not Applicable`及理由。

不得因为Poster Design完成而改变主Pipeline当前STATE。

## Conflict Routing

- 剧情、类型或关系冲突：返回STATE-01
- 资产身份、外观、空间或道具冲突：返回STATE-03对应资产Workflow
- 项目光影、综合色彩或视觉体系冲突：返回STATE-04 Visual Development
- 文案、日期、credits、logo或授权不确定：保持待确认，不擅自生成
- 海报要求实际改变某张参考图：按图像编辑流程处理，并确认用户有权使用

## Completion Invariants

完成或Not Applicable后按references/project_state_contract.md登记Poster Artifact、Checkpoint与Revision ID并同步或输出完整Portable State，执行其`Portable Required Field Writeback`；不改变STATE-04主状态推进权。

- 只有一个一级视觉母题
- 只有一个Primary Composition Model，Supporting Model不超过一个
- 画幅来自渠道要求，不硬编码9:16
- Exact Copy Ledger存在且最终文字可逐字核验
- base、type、composite、delivery与layout-spec职责明确
- 不出现未经确认的真实身份、标识、奖项或发行事实
- 不复制参考图可识别构图
- 不修改STATE-08 Schema或任何上游资产事实
