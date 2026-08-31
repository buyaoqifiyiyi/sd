# MUSIC / SEED-MUSIC Score Package

> 本Template只属于用户显式调用的独立Music / Score模块。它不得嵌入Seedance视频提示词，也不得由普通视频、Clip、Review或“继续”请求自动生成。

## Module Routing Record

- Route: `MUSIC / SEED-MUSIC Score`
- Explicit Trigger Evidence:
- Requested Scope:
- Requested Deliverable:
- Generation Mode: `INSTRUMENTAL` / `VOICE TEXTURE` / `LYRICS / SONG`
- Timeline Status: `CONFIRMED` / `PROVISIONAL`
- Source Artifacts / User Facts:

## Scope And Music Strategy

- Music Dramatic Role:
- Music Density Principle:
- Designed Silence Principle:
- Dialogue / Production Sound Priority:
- Genre / Cultural / Period Frame:
- Harmonic And Rhythmic World:
- Timbre Palette:
- Global Avoid List:

## Spotting Map

| Range / TC | Related Clip(s) / Scene | Decision | Narrative Reason | Entry Trigger | Exit Trigger | Dialogue / Action / Production Sound Relationship | Next Boundary |
|---|---|---|---|---|---|---|---|
|  |  | `MUSIC CUE` / `SILENCE / PRODUCTION SOUND ONLY` / `DIEGETIC MUSIC ONLY` / `MUSIC OUT` / `CARRY-OVER` / `PROVISIONAL` |  |  |  |  |  |

> 必须覆盖整个请求范围。留白行必须说明保留哪些同期声音以及为何音乐不进入；留白行不得创建SeedMusic Prompt。

## Music Bible / Motif Map

| Motif ID | Subject / Meaning | Contour / Rhythm Fingerprint | Harmony | Timbre Identity | Transformation Rule | Recall Rule |
|---|---|---|---|---|---|---|
| `MOTIF-01` / `None` |  |  |  |  |  |  |

## Cue Sheet

| Cue ID | Title | Related Clip(s) / Scene | Start / End | Target Duration | Narrative Function | Energy Arc | Motif / Harmony / Rhythm | Instrumentation | Dialogue / Action Relationship | Silence Before / After | Carry-over / Exit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `MUS-CUE-001` |  |  |  |  |  |  |  |  |  |  |  |

## SeedMusic Prompt Blocks

只为Cue Sheet中的实际`MUSIC CUE`输出。Clip存在时，标题和`Related Clip(s)`必须显示其归属；这些追踪信息不得进入代码块。

### MUS-CUE-001｜CLIP-XXX｜标题 SeedMusic纯音乐提示词

- Related Clip(s): `CLIP-XXX`
- Target Duration:
- Narrative Use:
- Entry / Exit:
- Generation Mode: `INSTRUMENTAL`

```text
style:
instrumental only; no vocals, no singing, no lyrics, no spoken word, no rap, no choir, no humming, no vocalise; music only, no dialogue, ambience, Foley or sound effects; <专业音乐描述>

structure:
[Verse]: 0s
[Chorus]: <递增秒点>s
[Bridge]: <递增秒点>s
[Outro]: <递增秒点>s
```

> 只保留实际需要的结构标签。第一个秒点必须为`0s`，后续严格递增。Clip标签、用途和说明均位于代码块外。

## Conditional Vocal / Lyrics Appendix

默认删除本节。只有当前用户明确要求`VOICE TEXTURE`或`LYRICS / SONG`时保留，并记录显式证据。

- Explicit Vocal / Lyrics Evidence:
- Mode:
- Language:
- Vocal Texture / Singer Direction:
- Lyrics And Section Mapping:
- SeedMusic Lyrics Input:

## Review

- [ ] 全请求范围已经完成Spotting，不只列出有音乐处
- [ ] 每个留白处都有专业理由和同期声音承载说明
- [ ] 没有全段默认铺音乐、每Clip必配或无理由转场音乐
- [ ] Cue ID唯一，Related Clip(s) / Scene可追踪
- [ ] 默认纯音乐没有歌词、人声、合唱、哼唱、吟唱、旁白、对白或说唱
- [ ] 每个执行块只有`style + structure`，结构从`0s`开始且秒点严格递增
- [ ] Clip归属和生产说明未混入SeedMusic执行块
- [ ] 任何配乐指令均未进入Seedance视频提示词
