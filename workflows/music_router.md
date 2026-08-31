# MUSIC / SEED-MUSIC Explicit Router

## Decision

本Router只判断：当前用户请求是否显式要求规划、设计、生成、修改或输出后期配乐 / SeedMusic交付物。

输出只允许：

- `ROUTE: MUSIC / SEED-MUSIC Score`
- `ROUTE: ORIGINAL WORKFLOW`

## Positive Route

当且仅当用户当前请求明确要求创建、规划、设计、生成、修改、更新或输出以下任一交付物时，返回`ROUTE: MUSIC / SEED-MUSIC Score`：

- 配乐规划、音乐设计、Score Plan、Music Spotting、Cue Sheet
- 哪里使用配乐、哪里留白、音乐进入 / 退出 / 延续规划
- 主题动机、角色主题、场景音乐、转场音乐或音乐连续性
- SeedMusic / Seed-Music配乐提示词、纯音乐提示词、歌曲或歌词版音乐提示词
- 已有音乐Cue的改写、延长、风格迁移或续写

显式意图必须同时包含音乐交付物与“规划、设计、生成、修改、更新、给我、输出、开始配乐”等请求语义。项目资料、剧本、镜头或参考作品中仅出现“音乐、BGM、配乐”等词，不构成触发。

## Negative Route

以下情况返回`ROUTE: ORIGINAL WORKFLOW`：

- 普通视频制作、Detailed Shot Design、Clip Production、Seedance视频Prompt、Storyboard或Review
- 用户只要求继续、下一步、下一个Clip、输出视频提示词或生成视频
- 剧情、情绪、导演风格或场景天然适合配乐，但用户没有发出当前配乐指令
- 只请求对白、环境声、Foley、动作音效、音色、配音或Voice Asset
- 用户说“视频不要配乐”“Seedance严禁BGM”或同义否定约束；只记录边界，不启动完整音乐模块
- STATE-08或Review发现没有配乐计划

Negative Route不得加载`workflows/21_seed_music_score_workflow.md`、`knowledge/music_score/`或`templates/22_seed_music_score.md`，不得自动创建Music Bible、Spotting Map、Cue Sheet或SeedMusic Prompt。

## Default Mode And Mixed Requests

- Positive Route默认进入`INSTRUMENTAL`：纯音乐，无歌词、演唱、说唱、对白、旁白、合唱、哼唱、吟唱或Vocalise。
- 只有用户当前请求另行明确要求歌词、歌曲、人声纹理、合唱、哼唱、吟唱或Vocalise，才切换到对应显式模式。
- 同一请求同时明确要求视频Prompt与配乐交付时必须拆分路由和输出：视频仍由原Workflow生成且永久禁配乐；配乐由本模块独立规划和输出，两个Template不得混合。
- 用户只指定“给某个Clip配乐”时，范围可以是单Clip；用户要求全片或整段配乐时，系统必须专业审阅整个请求范围，逐段决定`MUSIC CUE`或`SILENCE / PRODUCTION SOUND ONLY`，不能把“全段”解释为“每一段都铺音乐”。

## Fallback

- 语义模糊时返回`ROUTE: ORIGINAL WORKFLOW`，不推定配乐授权。
- Positive Route但缺少可判断的画面范围、时间线或叙事事实时，仍进入Music Workflow，由该Workflow请求最小必要输入或输出明确标记为`PROVISIONAL`的Spotting；不得假装完成精确计时。

## Canonical Self-Check Cases

| Input | Expected Route |
|---|---|
| 开始为整条片子规划配乐和留白 | MUSIC / SEED-MUSIC Score |
| 给CLIP-006输出SeedMusic纯音乐提示词 | MUSIC / SEED-MUSIC Score |
| 这一段需要歌词版主题歌 | MUSIC / SEED-MUSIC Score |
| 输出CLIP-006的Seedance视频提示词 | ORIGINAL WORKFLOW |
| 视频提示词里严禁BGM | ORIGINAL WORKFLOW |
| 继续制作视频 | ORIGINAL WORKFLOW |
