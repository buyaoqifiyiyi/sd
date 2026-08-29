# AUDIO / SEED-AUDIO Explicit Router

## Decision

本Router只回答一个问题：当前用户请求是否显式要求制作角色声音身份资产。

输出只允许：

- `ROUTE: AUDIO / SEED-AUDIO Voice Asset`
- `ROUTE: ORIGINAL WORKFLOW`

## Positive Route

当且仅当用户当前请求明确要求创建、设计、生成、修改或更新以下任一交付物时，返回`ROUTE: AUDIO / SEED-AUDIO Voice Asset`：

- 音色提示词
- 音色制作
- 角色声音
- Seed Audio / SeedAudio
- 配音音色
- 声音资产 / Voice Asset
- Voice Profile
- 角色音色样本Prompt
- 角色Voice/Audio Reference的制作、筛选或登记

显式意图必须同时包含“声音身份/音色交付物”与“制作、生成、修改、更新、给我、输出”等请求语义。仅在项目资料中出现这些词，不构成当前请求的显式触发。

## Negative Route

以下情况返回`ROUTE: ORIGINAL WORKFLOW`：

- 角色有对白、旁白、画外音、口播、通话或呼喊，但用户没有要求制作音色资产
- 普通视频制作、角色分析、Character Asset、分镜、Storyboard、Clip Production、视频Prompt或Seedance Prompt
- “继续视频制作”“输出Clip B视频提示词”“下一个Clip”“下一步”“继续”“下一个”
- 只请求台词、口型、环境声、Foley、音效、配乐、歌曲、正式整段配音或多人声场
- STATE-08发现Voice Profile / Voice Reference不存在

Negative Route不得加载`knowledge/sound_language/voice_generation.md`或`templates/21_seed_audio_voice_asset.md`，不得生成或登记Voice Profile、Seed Audio Prompt、Voice Audio Reference或Not Applicable记录。

## Priority And Mixed Requests

显式音色请求只对声音资产子任务具有最高优先级。同一请求还显式要求视频/Clip交付时，分别路由：声音资产子任务进入AUDIO Workflow，视频子任务进入原Workflow；两种Template不得混合。

没有显式音色请求时，本Router不得覆盖State Source、主Pipeline、Storyboard、Poster、Editing或其他辅助Workflow路由。

## Fallback

- 语义模糊但更像对白、同期声或音效处理：返回原Workflow，不推定音色制作授权。
- 用户明确说不要制作音色、只继续视频或只要Clip Prompt：返回原Workflow。
- 用户显式请求音色资产但必要角色事实不足：仍进入AUDIO Workflow，由该Workflow请求最小必要输入；不得改走普通自然语言Prompt。

## Canonical Self-Check Cases

| Input | Expected Route |
|---|---|
| 给我钟馗的音色提示词 | AUDIO / SEED-AUDIO Voice Asset |
| 输出Clip B视频提示词 | ORIGINAL WORKFLOW |
| 继续制作视频 | ORIGINAL WORKFLOW |

