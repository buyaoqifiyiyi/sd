# Movie Poster Design Knowledge

## Purpose

本模块把影片事实、已确认资产和Visual Direction转换为可执行的电影海报系统。

它解决的不是“剧照加片名”，而是：

- 海报向观众承诺什么类型与情绪体验
- 哪一个视觉母题最能压缩整部影片
- 人物、空间、物件和标题如何共同建立阅读顺序
- 如何把生成底图、准确文字、合成和交付拆成稳定层级
- 如何在使用参考图时保持原创差异与权利边界

## Activation Gate

仅在用户请求以下内容时加载：

- 电影海报、先导海报、正式海报、角色海报或概念海报
- Key Art、One-sheet、Poster Prompt、标题字设计或海报版式
- 由剧本、项目资产、剧照或参考图建立电影宣传主视觉

不适用于：

- 普通社交媒体封面、缩略图或信息长图
- STATE-08视频Prompt
- 未经请求把每个影视项目自动增加海报交付
- 原样复制现有海报或保留其可识别构图

## Required Reading

执行Poster Design Workflow时完整读取：

1. `knowledge/poster_design/foundations.md`
2. `knowledge/poster_design/composition_and_motif.md`
3. `knowledge/poster_design/typography_and_layers.md`
4. `knowledge/poster_design/reference_rights_and_qc.md`
5. `knowledge/poster_design/genre_tendencies.md`
6. `templates/15_poster_design_package.md`

## Authority Boundary

本模块是STATE-04条件性辅助Knowledge。

它可以：

- 选择海报类型、视觉母题、构图系统和信息层级
- 建立海报专用的色彩、质感、字图关系和分层制作计划
- 编译底图提示词、文字版式规范、合成规范与负面限制

它不得：

- 改写剧情、角色身份、环境结构、关键道具或已确认Visual Direction
- 把海报设计反向变成逐镜Shot Design
- 为海报虚构真实导演、演员、片商、奖项、电影节或发行事实
- 创建新的主Pipeline STATE
- 修改`templates/10_video_prompt.md`或STATE-08 Schema

## Core Principle

先判断影片，再判断宣传承诺；先确定一个一级视觉母题，再选择构图和字体；先建立准确的信息层级，再生成和合成。

