# Vendored Reference-Film Measurement Engine

> Skill维护层：只在修改本Skill时读取，不参与影视生产。

## Purpose

本目录是SD Film参考片拉片能力的**机器测量层**，来自第三方开源Skill包 **ReelBench** 的 `video-shots` 与 `video-sync` 两个Skill。它们在这里是**原样vendoring的上游实现**，不是SD Film自己的规则文件。

它回答一个问题：**切点、时长、每镜实测运动量由谁定。** 判据与方法正文归`knowledge/visual_styles/index.md`的`### Temporal Reference Decode｜参考片时间轴解码`；执行步骤归`workflows/22_reference_film_study_workflow.md`。本文件只记录来源、边界与升级方式。

## Why Vendored Instead Of Rewritten

上游是77 KB的确定性引擎与449项自测，重写它等于自己维护一套测量算法与15道质量门。因此本层**一字不改地保留上游代码**，SD Film自己的内容（测量法正文、词表对应、报告Schema、路由）全部落在上游目录之外。

代价与约束：**上游文件不得在本目录内编辑。** 要改行为，改SD Film自己的owner文件；要换算法，整块替换本目录；要修平台缺陷，写在本目录之外的包装层。

## Provenance

- Upstream：ReelBench skills package
- Source archive：`reelbench-skills-main.zip`，SHA-256 `79f30565236c4e438d840c759217b1dd0a4d4a06ec22a70cbdc15aae695cd708`
- Upstream license：Apache-2.0，全文见本目录`LICENSE`
- 收录范围：`video-shots`与`video-sync`两个Skill的可执行部分与技术参考（`scripts/`、`references/`、`examples/`），以及LICENSE
- **未收录**：上游两个Skill各自的`SKILL.md`、`README.md`、`README.en.md`与演示截图。理由见下方`## Non-Duplication`。

## Non-Duplication

上游的`SKILL.md`与README是**同一套七步流程的另一份完整正文**。它与SD Film的`workflows/22_reference_film_study_workflow.md`构成竞争副本，改动只同步一处即静默分叉——这正是可达性纪律禁止的重复定义。因此不收录：执行步骤的唯一owner是SD Film自己的Workflow。

需要上游的原始说明时，从上述Source archive重新解包，不要在本目录里重建副本。

## Integrity

收录文件的SHA-256前16位，用于确认本目录未被就地修改：

| Path | SHA-256 (first 16) |
|---|---|
| `scripts/reference-film/vendor/video-shots/scripts/video-shots.mjs` | `c49963d11b34bf56` |
| `scripts/reference-film/vendor/video-shots/scripts/report.js` | `94e888c99c0a08d6` |
| `scripts/reference-film/vendor/video-shots/scripts/report.css` | `41e278aa9dca66ec` |
| `scripts/reference-film/vendor/video-shots/scripts/selftest.mjs` | `b4fee91c8c26f52a` |
| `scripts/reference-film/vendor/video-shots/references/taxonomy.md` | `0ef5887632eead7e` |
| `scripts/reference-film/vendor/video-shots/references/schema.md` | `e25b42590d67942f` |
| `scripts/reference-film/vendor/video-shots/references/analysis-pass.md` | `a6f7dd291b61e02c` |
| `scripts/reference-film/vendor/video-shots/references/report-style.md` | `88ad9c8fef2ed145` |
| `scripts/reference-film/vendor/video-shots/examples/demo-shots.json` | `e727f659ff590e16` |
| `scripts/reference-film/vendor/video-shots/examples/demo-track.json` | `d7e011e4b9a4cdc2` |
| `scripts/reference-film/vendor/video-sync/scripts/video-sync.mjs` | `ad0386fbe90bdfbd` |
| `scripts/reference-film/vendor/video-sync/scripts/panel.css` | `e27dd1ad24d161c5` |
| `scripts/reference-film/vendor/video-sync/scripts/panel.html` | `9729bf9572e36506` |
| `scripts/reference-film/vendor/video-sync/scripts/selftest.mjs` | `b467c855f4340c10` |
| `scripts/reference-film/vendor/video-sync/references/layout.md` | `623c145a89048783` |
| `scripts/reference-film/vendor/video-sync/references/panel-style.md` | `10a6c13fc4c27da3` |

## Dependency Surface

- `node`（≥18）：**只用标准库**，无npm依赖、无网络调用、无API key
- `ffmpeg` / `ffprobe`：场景检测、运动测量、抽帧、联系表
- 无头浏览器（仅`video-sync`的`panels`需要）：Chrome / Chromium / Edge
- 两条上游自测，不碰ffmpeg、不调模型、不花额度：

```text
node scripts/reference-film/vendor/video-shots/scripts/selftest.mjs
node scripts/reference-film/vendor/video-sync/scripts/selftest.mjs
```

## Platform Notes

上游主要在POSIX环境开发。以下差异**在本机（Windows 11 / node v24 / ffmpeg 9.0.1 / Edge）实测**，并一律在本目录之外处理，不改上游代码。**每一条都写明是实测还是仅静态阅读**：

1. **`compose`在Windows上必然失败（实测）**。它把`motion.cmd`的绝对路径直接写进ffmpeg滤镜选项`sendcmd=f='<abs path>'`；Windows路径的`\`被滤镜解析器当成转义符，报`No option name near '\Users\…'`。**只把反斜杠转成正斜杠仍然失败**（`:`仍被当成选项分隔符）；实测只有写成`C\:/Users/…`（正斜杠 + 转义盘符冒号）才通过。修法在`scripts/reference-film/compose-win.mjs`：它用上游`plan`取几何、读上游`panels`写下的浏览器量测`layout.json`，只把这一处路径写法改对，再用`ffmpeg`执行自己拼出的滤镜图（滤镜图结构与上游`composeArgs`一致）。
2. **浏览器探测列表只有macOS / Linux路径（实测）**。`panels`不传`--chrome`时报"没找到无头浏览器"；传`--chrome "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"`后正常产出`static.png` / `list-dim.png` / `list-lit.png` / `layout.json` / `panel.html`。这是探测列表的射程问题，不是浏览器没装。
3. **`file://` + 原生Windows路径实测可用**。上游拼出的`file://C:\…\panel.html#static`在这台机器上被Edge正常渲染，`panels`全程无错，因此**不需要**为它做包装。不要凭静态阅读就把它记成已确认缺陷。
4. **`sheet`的concat列表用原生Windows路径实测可用**（`file 'C:\…\S01a.jpg'`配`-safe 0`），联系表正常产出。**唯一已知破绽是路径里含单引号`'`**——避免在拉片目录名里用它。
5. **`scripts/install.sh`是POSIX专用的安装脚本，不适用**，也不得在Windows上执行。本Skill不需要它：vendoring目录就是安装结果。

### 重定向必须写原始字节

`video-shots.mjs`的`seed` / `recut` / `render`把JSON或文档写**stdout**，且必须是无BOM的UTF-8。**Windows PowerShell 5.1的`>`与`Out-File -Encoding utf8`会把输出写成带BOM的UTF-8**（实测首三字节`EF BB BF`），下游解析直接报`Unexpected token ''`。实测`cmd /c "… > out.json"`写出`7B 0A 20`，可直接解析。执行步骤由`workflows/22_reference_film_study_workflow.md`拥有，本文件只记录这条平台事实。

### 在本机已验证的射程

| 步骤 | 状态 |
|---|---|
| `seed` / `frames` / `sheet` / `validate` / `render --md` / `render --html` | 实测通过（44镜与46镜两条片子各跑一遍） |
| 15道质量门全绿；失败即退出码1 | 实测：把`push-in`填到实测运动0.7的镜头上，门拦下并退出1 |
| `video-sync plan` / `panels` / 包装后的compose + 抽帧验收 | 实测通过（抽帧确认镜号与高亮行随切点跟踪） |
| 上游`compose`原名调用 | **实测失败**（见上第1条） |
| 上游两条selftest（449项 + 122项） | 实测全绿 |

## Upgrade Procedure

整块替换，不做逐行合并：

1. 从新的Source archive解包到Skill根目录之外的临时位置（**不得放在本Skill根目录内**，否则发现器会递归读到第二个入口）。
2. 用同样的收录范围替换`video-shots/`与`video-sync/`，保留`LICENSE`。
3. 重新计算并更新上方`## Integrity`表。
4. **把新的`composeArgs` / `motionPlan` / `ramp` / `commandFile`与`scripts/reference-film/compose-win.mjs`里的同名实现逐项对齐**——包装层复制了这四个函数，上游改结构时它必须跟着改。
5. 重跑两条上游自测，以及`scripts/validate_sd_film.py --skill-root <skill-root>`。
6. 只当本次替换改变了SD Film自己文件里写下的命令、参数默认值或产物字段时，才同步修改`knowledge/visual_styles/index.md`的`### Temporal Reference Decode｜参考片时间轴解码`、`workflows/22_reference_film_study_workflow.md`与`templates/26_reference_film_study_report.md`。

## Final Principle

上游代码在`vendor/`内属于第三方实现，SD Film只为"用哪条命令、读到什么数值、怎么映射成自己的语言"负责。
