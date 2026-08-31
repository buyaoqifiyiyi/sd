# Music And Silence Compatibility Boundary

本文件保留旧路径兼容，但不再拥有后期Music / Score规划方法。

## Production-Sound Silence

STATE-04—09中的“静默”只指生产声音设计：保留或收缩空间底噪、呼吸、对白尾音、Foley、动作声或剧情内声源。它不是Music Cue，也不得把“无配乐”写进STATE-08正向音效字段。

## Music Routing

只有用户当前明确请求配乐规划、Music Spotting、Cue Sheet、主题动机、场景 / 转场音乐或SeedMusic提示词时，才读取`workflows/music_router.md`。Positive Route后由以下资源独占音乐方法与交付：

- `workflows/21_seed_music_score_workflow.md`
- `knowledge/music_score/`
- `templates/22_seed_music_score.md`

普通视频、Shot、Clip、Seedance、Review、Editing或“继续”请求不得因读取本兼容文件而触发Music模块。

STATE-08永久禁止背景音乐、配乐、BGM、主题音乐与氛围音乐，不存在用户指定Clip例外。
