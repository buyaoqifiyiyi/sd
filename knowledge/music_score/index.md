# Music / Score Knowledge Index

## Purpose

本目录是SD Film独立的Explicit-Only Music / Score专业知识模块，只在`workflows/music_router.md`返回Positive Route后读取。它拥有配乐Spotting、留白、主题动机、Cue架构与SeedMusic提示词编译方法，不拥有主STATE、视频Prompt Schema或最终交付格式。

## Routing

- `spotting_and_silence.md`：判断哪里进音乐、哪里退音乐、哪里只保留同期声音；建立进入 / 退出 / Carry-over和跨Clip留白逻辑。
- `music_bible_and_cues.md`：建立项目音乐语言、主题动机、节奏 / 和声 / 音色策略、场景音乐、转场Cue与跨Cue连续性。
- `seedmusic_prompting.md`：把已批准的Cue设计编译为SeedMusic `style + structure`执行块；默认纯音乐，歌词 / 人声显式才可用。

## Isolation

- 普通视频、Shot、Clip、Seedance、Review、Editing或“继续”请求不得加载本目录。
- 本目录的任何内容不得投影到`templates/10_video_prompt.md`。STATE-08永久禁止背景音乐、配乐、BGM、主题音乐和氛围音乐。
- Clip ID只用于Cue追踪；SeedMusic执行正文中不得包含“为CLIP-XXX配乐”等生产元数据。
- `knowledge/sound_language/`继续负责对白、环境声、Foley、剧情内声源和同期声音连续性，不再负责后期配乐设计。
