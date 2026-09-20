# screenwriting-skills 工程学习笔记

> Skill维护层：只在修改本Skill时读取，不参与影视生产。
>
> **本文件是面向人的外部项目学习笔记，属于非运行时文件。** 它未被任何 Workflow 列为 Required Resource，不参与运行时读取，也不是规则、恢复、路由、Schema 或知识判据的来源；不得被当作影视生产依据，也不得据此改写任何 STATE、Template、字段或 Gate。运行时权威是 `SKILL.md`、`rules/`、`workflows/`、`knowledge/`、`references/` 与 `templates/`。
>
> 笔记中所有 `plugins/…`、`tools/…` 路径都属于**外部仓库** `jtydhr88/screenwriting-skills`，不是本 Skill 的文件，不得从本 Skill 根解析。

## 学习对象

| 项 | 事实 |
|---|---|
| 仓库 | `jtydhr88/screenwriting-skills` —— 47 本编剧／剧作理论书 + 23 卷出版剧本与曲谱，提炼为 26 个 agent skill，覆盖电影长片、电视剧集、舞台剧与戏曲 |
| 结构 | 单一插件 `plugins/screenwriting/skills/` 下 26 个 kebab-case 目录，每个含 `SKILL.md`（原理／清单／工作流程）+ `reference.md`（表格／引文／逐集分析），少数再分多册；另带 `.claude-plugin` 与 `.codex-plugin` 两份 manifest 共用同一份 skills |
| 约定 | 正文中文；`name` 与文件夹同名；`description` 英文长句以 `Use when …` 收尾并附中文关键词；`SKILL.md` 控制在约 40 KB 以内，范例与引文外移到 `reference.md` |
| 自检 | `tools/check-skills.py`（纯标准库）：frontmatter 齐备、`name` 与目录同名、`description` ≤ 1024 code points（>1000 告警）、含 `Use when` 子句、`SKILL.md` 与 `reference*.md` 中每个相对链接都能解析 |
| 本地副本 | `tmp/screenwriting-skills-study/repo`（浅克隆，`tmp/` 不入库） |

**它与本 Skill 的关系**：这是**上游编剧方法论**的同业者，不是下游生产系统。它做"剧本怎么写"，本 Skill 做"剧本怎么变成可投喂的镜头与 Prompt"。**它的组织方式**本 Skill 已有更细的对应机制（见下文各节实测），无需迁移；但**它在编剧工艺轴上的领域内容本 Skill 并未覆盖**——2026-09-20 复核推翻了本文档初版"领域内容已有更细的 owner"的结论，理由与证据见`## 八、工艺轴复核`。

初版结论的错误性质是**样本不足导致的推断越界**：本文档的`## 证据与自我限制`已自认只读了组织方式相关的少数文件，却把结论外推到了领域内容。七条判定在组织方式轴上成立，在工艺轴上不成立。

---

## 一、四层结构：媒介层用"替换"接入，通用层一字不改

它把 26 个 skill 分成四层（README 明列）：

```text
1. 通用剧作层   前提 · 结构 · 人物 · 对白 · 场景 · 格式 · 类型解剖 · 项目调度
2. 媒介层       剧集（单集与季结构 · 引擎与 bible · 编剧室 · 半小时喜剧）
                舞台（戏曲：板腔体与曲牌体两套方法，各带全本语料库）
3. 传统与行业层 美国 · 日本 · 韩法 · 中国大陆 · 行业生意
4. 大师语料层   契诃夫 · 小津 · 继承之战 · 剧集案例库
```

关键不是分层，而是**新增媒介时的接入纪律**（README"新媒介怎么加进来而不污染通用层"）：

> 一个新 skill；skill 里一张媒介边界表，说明通用层哪几层能用；`sw-workflow` 入口路径加一行。**通用 skill 不改。** 剧集层（13 → 20）就是这么加的，`sw-story-structure` 一字未动；戏曲也是这么加的，`sw-dialogue` 反而变短了。

媒介边界表本身是一张**带判定的三列表**（`| 组 | 通用层的哪一条 | 判定（依据）|`），判定词是一套**分级回答**而不是是／否：**能／不能／不够／反向／不必／有下界／有上界／部分／半能／不适用**，每条都带来源页码。例：`BS2 十五节拍、40 卡、页码表 → 不能；戏曲是流动的分场结构`；`悬念靠隐瞒 → 反向；不向观众保守秘密，秘密对台上人保守`。

**与本 Skill 对照（结论：已被覆盖，且本 Skill 更细）**：`knowledge/medium_profiles.md` 就是同一机制，且是三档（`live_action` / `3d_animation` / `2d_anime`）× 四层（Screenwriter / Director / Aesthetic / Shared Invariants）的逐维分化表，判定词同样分级（**不适用／降级为版面位移／成立（虚拟光学）／禁用**），并明确写出"本文件不创建STATE、不新增Template字段、不改变任何Model Adapter能力"。本 Skill 还多两件它没有的：**未确认媒介记为 `Pending` 且不得推定**、`## Cross-Medium Asset Rule`（一个媒介的资产不得静默用于另一个媒介）。**无需迁移。**

---

## 二、术语锚定表：唯一一项本 Skill 没有的机制

`sw-workflow/terms.md` 是这套 skill 的**跨语言基础设施**，也是它最完整的一件发明。它的立论值得完整记住：

> 这一行的术语绝大多数**原本就是英文的**——log line、act out、beat sheet、showrunner 都是英文原词，中文书里的"计程绳""出幕""节拍表""剧目管理人"才是译文，而且不同译者给的不一样。所以把中文说法映射回英文原词，不是翻译，是**还原**。

表格形态是四列：`英文原词 | 本库中文用法 | 其他常见中译 | 出处`，并对**没有英文对应物**的词单列两节，规则是"任何语言下保留原词＋一句释义"，例如 `戏眼 (xìyǎn — the one-line core attraction of an episode)`、`ト書き (tosho — the action line of a Japanese script)`。

它同时承载三条输出纪律（`sw-workflow` 六之二）：

1. **输出语言＝提问语言**，skill 正文是中文不影响输出语言；
2. **术语回锚到原词**，不自创译名（"进展纠葛"的原词是 progressive complications，不是 progressive entanglement）；
3. **剧本正文的语言另算**——用英语讨论一个中文剧本是常态，谈话换语言，稿子不换。

配套的是一条**翻译否决记录**（README"多语言支持"）：曾有一个把 20 个 skill 全部译成英文的平行插件，做完合并后又撤掉，理由是——

> 只要另出过一份译本，就再没有原则性的理由拒绝第二份。

（五种语言＝230 个文件各改各的，哪一份过时没人说得清。）

**实测：本 Skill 的对应状况**

| 检查 | 实测结果 |
|---|---|
| 是否已有术语锚定表 | **没有**。全库唯一的 `terms` 类文件是这份外部笔记本身 |
| 是否已在用英文行业术语 | **在大量使用**：176 个文件、988 处、19 个不同术语（`Blocking` 621、`Coverage` 172、`Camera Movement` 84、`Eyeline` 23、`Shot Size` 15、`Match Cut` 8、`Over-the-Shoulder`、`OTS`、`Dutch Angle`…） |
| 中文工作术语的体量 | `镜头` 1854、`机位` 496、`运镜` 418、`景别` 410、`分镜` 348、`轴线` 331、`对白` 261、`转场` 179、`成片` 120、`留白` 110、`越轴` 64、`反打` 55、`拉片` 49、`过肩` 10、`走位` 20 |
| 这些术语的英文rendering是否漂移 | **实测未发现漂移**。按"中文术语＋括号英文"的模式逐行提取 176 个文件，没有出现同一中文术语被给成多个互斥英文名的情况 |
| 易混词是否已被刻意区分 | **是**。`分镜` 兼指 shot 与 storyboard，但本 Skill 已把两者分写：`分镜板`／`Storyboard` 专指被禁止进入 STATE-08 的那类规划材料，逐镜则用 `镜头`／`每镜`／`SHOT` |
| 输出语言纪律 | 无成文条款；`SKILL.md` 的 `description` 以中文关键词触发（210 code points，远低于 1024） |

**判断：不迁移，但记一条待观察。** 它做这张表是因为它的**来源是多种互相冲突的中译本**，必须"还原"；本 Skill 的来源本来就是英文行业标准做法，术语直接以英文原名充当锚点（`Motivated Discontinuity`、`REF-TAIL`、`Shot Purpose`、`Face Economy`），中文侧是**已统一的自家工作语言**。**没有观察到的问题不值得为它建表**——那会是一张根据"应该有用"而编的 40 行映射，没有消费者。

真正可考虑的只有一件事，且不属于"术语表"：**用户用英语提问时，本 Skill 的输出语言是什么**。这是产品决策（本 Skill 的用户面是中文短剧生产），不是知识缺口，因此留给你判断，本次不动。

---

## 三、入口路径表：把"接活"做成一张可查的路由表

`sw-workflow` 的调度核心是两张表：

- **阶段图**：`| # | 阶段 | 调用的 skill | 交付物（写入 bible 的节） | 建议通过标准 |` —— 七个阶段，每格都指明调谁、交什么、什么算过。
- **入口路径**：按"用户是什么情况"分流，而不是按"现在在哪个阶段"。同一张表里并列了**长片、剧集、戏曲板腔体（X0–X6）、戏曲曲牌体（Q0–Q6）四条互不相同的阶段链**，每行还写"特别处理"。

三条值得单独记的判据：

1. **阶段可以回退，且回退要给归因**："阶段 5 发现对白写不动，通常是阶段 3 的人物或阶段 1 的前提有洞，回去补，然后在决策日志记一笔。"
2. **通过标准怎么用**：标准是**建议门槛，不是硬阻断**；用户要跳步就跳，但要标记"（跳过阶段 3 人物表）"并在进入下一阶段前提醒一次。同时规定"通过标准里凡是能量化的都量化（页数、卡片数、人物数、问号数）"。
3. **甲方格式优先于任何 skill 体例**：用户或委托方给了页数、字数、栏目、模板，就按他们的；skill 体例是**默认值**，只用来填对方没规定的空白；冲突时压缩体例、不要超格式，展开版另存自用。**不要为了交齐 skill 要求的字段而交出一份不合甲方规格的文件。**

**与本 Skill 对照**：`core/pipeline.md` 与 `rules/progression_rules.md` 已有 STATE 链与合法推进；第 1、2 条与 `rules/completion_gate.md` 的"路径存在、文字说明不等于 Gate 通过"同源但方向相反——本 Skill 的 Gate 是硬门，它的标准是软的。**这是两种合理取舍**：它面向人写稿（用户想跳就跳），本 Skill 面向可投喂产物（规格错了就白生成）。第 3 条与本 Skill 的"Template 是唯一输出 owner"不冲突但也不同源，属它的行业现实。**无需迁移。**

---

## 四、每阶段的最小动作：把"别通读"写成要求

`sw-workflow` 四之开头一句：

> 不必把对应 skill 全文读一遍。每阶段先读该 skill 的"工作流程"和"诊断清单"两节，需要具体方法再读对应章节，需要范例再读 reference.md。

`sw-chinese-opera-banqiang` 把这个做成了一张**带"跳过"列的路由表**：

```text
| 任务 | 读 | 跳过 |
| 写一段唱词 | 六、七、【之三】 | 一、十一、十二、十四 |
| 定板式与决定标不标 | 九、十、§8a | 二、三、十一 |
| 改老戏／整理传统题材 | 十一、五、【之三】 | 十二、十三 |
```

**与本 Skill 对照**：`# Read Scope` 已在约 20 个文件里落地（`rules/resource_loading.md` 第 36 行规定"文件顶部有 `# Read Scope` 区块时，按它分配给当前事项的章节读"），`references/context_budget.md` 的 Size Index 还要求 `INTEGRAL` 文件写明"按章节读"的入口。**本 Skill 已有的机制等价且更系统**（含 Size Index 与 Validator 校验）。它多出来的只有"**跳过**"这一列——明确列出**不读什么**。这条在本 Skill 的按需读取纪律下是隐含的（不命中就不读），不构成缺口。**无需迁移。**

---

## 五、仓库治理：两条可对照的写法

1. **显式"不做什么"**（README"舞台门类"）：它写明**不做什么**——"竖屏短剧与 AI 漫剧，它们靠投放，谈不上剧作学。按题材拆、按导演拆、按剧种拆的 skill [不做]"，并给出一条**判断规则**："一个门类会不会让模型写出结构、格式、语言规则都不同的东西？会，就单开 skill；只是题材或风格不同，就放进现有 skill 当案例。"还给了反例边界：粤剧归属未定就先不单开，等材料到了再试。
2. **来源分歧并列保留**："来源之间有分歧时并列保留，并注明什么情况用哪个"（例：道格拉斯的四幕格子对奥贝格的"幕断只是香肠的尺寸"，主题预设派对主题涌现派）；"行业事实一律带来源年份（费率、平台格局、幕数这些变得快）"。
3. **frontmatter 约定**：`name` 与目录同名；`description` 以 `Use when …` 收尾、附中文关键词。

**实测：本 Skill 的对应状况**

| 检查 | 实测结果 |
|---|---|
| 有无"不做什么"声明 | **有，且更细**：`knowledge/poster_design/index.md` 有 `不适用于：` 清单；`knowledge/sound_language/voice_generation.md` 有 `## Official Capability Boundary`；8 个文件各有 ≥3 条"不改变任何主STATE／不新增Template字段／既有owner不变"式层隔离声明 |
| 外部事实是否带来源与日期 | **有**：`knowledge/platform_profiles.md` 明定平台事实属**外部事实**、必须由用户提供或引用可核对来源；`adapters/` 的能力数值归 `O｜Operational Parameter` 并标复核日期 |
| `description` 是否符合 agentskills.io 约定 | 210 code points（限 1024，余量充足）；无 `Use when` 子句——沿用中文关键词触发写法，对中文用户是更有效的触发面 |
| 相对链接是否有死链 | **0 处**（全库 `.md` 逐条解析，与它的 `check-skills.py` 同一项检查） |

**结论：三条都不构成缺口。** 第 1 条本 Skill 做得更细；第 2 条已有 owner；第 3 条实测合规。

---

## 六、它"有意不做"的两件事，对本 Skill 有参照价值

1. **不维护平行译本**（理由见第二节引文）。本 Skill 同理：`SKILL.md`、`rules/`、`knowledge/` 只此一份中文，不为任何语言或平台分叉。这条纪律本 Skill 已在 `SKILL.md` 的 Self-Maintenance 与 `references/context_budget.md` 的单一 owner 纪律里表达过，它的价值是**给出了拒绝第二份的原则性理由**：一旦有第二份，就没有理由拒绝第三份。
2. **不按题材／导演拆 skill**："题材（谍战、古装、家庭）和导演风格不算；除非像小津那样有完整剧本集，否则当案例收，不单开方法。" 对应到本 Skill：`knowledge/genre/` 与 `knowledge/visual_styles/directors/` 都是**案例层**而不是新 STATE，与它的判断一致。

---

## 七、实测汇总与结论

| # | 学到的机制 | 本 Skill 现状（实测） | 判定 |
|---|---|---|---|
| 1 | 四层结构 + 媒介边界表（分级判定 + 来源页码） | `knowledge/medium_profiles.md` 三档 × 四层逐维分化表，判定同样分级，另有 Pending 纪律与 Cross-Medium Asset Rule | **已覆盖，本 Skill 更细** |
| 2 | 术语锚定表（还原原词、保留无对应词） | 无此表；但英文行业术语已在 176 个文件中直接充当锚点，**实测未发现 rendering 漂移** | **不迁移**（无问题可解）；仅"输出语言"一条留作产品决策 |
| 3 | 入口路径表 + 可回退的阶段链 | `core/pipeline.md` + `rules/progression_rules.md` + `rules/completion_gate.md` 已有，且 Gate 更硬 | **无需迁移** |
| 4 | "每阶段最小动作" + **跳过列** | `# Read Scope`（约 20 文件）+ `references/context_budget.md` 的 Size Index 与读取入口校验 | **已覆盖**；"跳过列"不构成缺口 |
| 5 | 显式"不做什么" + 门类拆分规则 | `poster_design` 的 `不适用于：`、`voice_generation` 的 `## Official Capability Boundary`、8 个文件的层隔离声明 | **已覆盖，本 Skill 更细** |
| 6 | 来源分歧并列 + 行业事实带年份 | `platform_profiles` 的外部事实纪律；`adapters/` 的 `O｜Operational Parameter` + 复核日期 | **已覆盖** |
| 7 | frontmatter 约定 + 相对链接自检 | description 210 code points；**全库相对链接死链 0 处** | **实测合规** |

**本次对 SD Film 的改动：无**（初版结论，仅对组织方式轴成立；工艺轴的复核与处置见`## 八、工艺轴复核`）。

这是刻意的结论，不是遗漏。两次外部学习（Jellyfish、screenwriting-skills）到现在只落地了一处真实缺口（`scripts/validate_prompt_package.py` 的"已确认资产名逐字保留"断言）。一个成熟 Skill 学到的东西多半是"确认自己已经做对了"——把外部项目当镜子用，比当模板用更值钱。凡本笔记判定"已覆盖"的条目，**回读对应 owner 才是权威**，本文件不得被引用为规则来源。

---

## 八、工艺轴复核（2026-09-20）

上文七条判定全部属于**组织方式／约定轴**，在该轴上成立。本节是对**领域内容（编剧工艺）轴**的重新核对，推翻了初版的"无需迁移"。

### 复核方法

对 26 个外部 skill 的 `SKILL.md` 逐概念提取，再对本 Skill 的 Writer 层文件（`knowledge/writer/screenplay_development.md`、`screenwriting_optimization.md`、`script_adaptation.md`、`directorial_interpretation.md`、`workflows/02_script_analysis_workflow.md`、`templates/02_script_analysis_prompt.md`）做全串检索，判定"有 owner／无 owner"。

### 实际读过的文件

`sw-workflow`、`sw-story-structure`、`sw-scene-craft`、`sw-dialogue`、`sw-character-conflict`、`sw-premise-theme`、`sw-genre-anatomy`、`sw-format-adaptation`、`sw-industry-business` 的 `SKILL.md`。**初版一个都没有打开**——这正是初版结论失效的原因。

### 结论

| 概念 | 外部有 | 本 Skill 初版状态 |
|---|---|---|
| 结构操作（激励事件、进展纠葛、中点、危机/高潮/结局、段落） | `sw-story-structure` | **无 owner**，且`genre/index.md`的禁令把公式与工艺一并禁掉 |
| 人物构建法（pressure 定义人物、want vs misbelief、起源场景、对手筹码、反照人物） | `sw-character-conflict`、`sw-premise-theme` | **只有字段名，无构建方法** |
| 场景技法（晚进早出、转折点只能由动作或揭示创造、价值对翻转、直接相对、重复节拍） | `sw-scene-craft` | **无 owner** |
| 对白技法（行动测试、遮名测试、互换测试、潜文本、第三件事、细节具体化、道具链） | `sw-dialogue` | **只有一条链**`Dialogue → Surface Meaning → Subtext → Hidden Objective` |
| logline／pitch／treatment | `sw-premise-theme`、`sw-industry-business` | 无 owner（本次不引入：本 Skill 不做剧本出售） |
| coverage／WGA／期权／系列引擎／页数经济 | `sw-industry-business`、`sw-series-*` | 无 owner（本次不引入：各有适配边界或与现有形态冲突） |

### 已执行的处置

1. 在唯一 Writer owner `knowledge/writer/screenplay_development.md` 内新增`## Craft Manual｜工艺手册`，采用与该库`SKILL.md`同源的**带条件手段**写法：每个条目必备`成立条件`／`反用场景`／`失效信号`。**用自己的 schema 重写，不复制外部文件。**
2. 新增`## Directable Screenplay Gate｜可失败判定`五项——该层此前只有"存在性"判据，没有可失败的判据。
3. `knowledge/genre/index.md` 新增`## Craft And Formula｜工艺与公式`分界节，把禁令的对象限定为 Formula 形态，使 Craft 不再被一并禁止。
4. `scripts/validate_sd_film.py` 新增`check_screenplay_craft`，使该层成为可机械守卫的知识域（此前是唯一没有守卫的域）。
5. 本次未引入的条目（logline／coverage／系列引擎／页数经济）**记录为已知缺口**，不在本文档外另行声明为已覆盖。

### 法务边界（实测原文）

MIT（`LICENSE:1`，"Copyright (c) 2026 Terry Jia"）覆盖 `NOTICE:5-10` 所列原创部分，含"编号原则、检查表与工作流"，可改写吸收、商用亦可；`NOTICE:14-33` 明确**不覆盖**`reference.md` 的书目引文、中译本与结构统计表。因此本次只吸收方法论并重写，不搬运任何 `reference.md` 内容。

---

## 证据与自我限制

- 结论来自直接阅读：`README_ZH.md`（全文）、`sw-workflow/SKILL.md`（全文）、`sw-workflow/terms.md`（全文）、`sw-chinese-opera-banqiang/SKILL.md`（前 89 行，含媒介边界表全表）、`tools/check-skills.py`（全文）、`.claude-plugin/marketplace.json`，以及抽样的三份 `SKILL.md` frontmatter。
- **工艺轴复核（`## 八`）另读**：`sw-story-structure`、`sw-scene-craft`、`sw-dialogue`、`sw-character-conflict`、`sw-premise-theme`、`sw-genre-anatomy`、`sw-format-adaptation`、`sw-industry-business` 的 `SKILL.md`，以及 `LICENSE` 与 `NOTICE` 全文。
- 对本 Skill 的全部"实测"数字均由脚本在本地全库现算：英文术语出现次数与文件数、中文术语频次、中文术语＋括号英文的逐行提取、相对链接解析、`SKILL.md` description 长度。
- **未验证**：它的 26 个 skill 的实际运行效果（未安装、未调用）；`reference.md` 各册的领域内容正确性（本次只读组织方式，未逐本核对剧作学结论）。
- **方法限制一处**：术语漂移检查用的是"中文术语＋紧邻括号英文"模式，能覆盖本库这类写法；若漂移以其他形式存在（例如同一概念在两个文件里分别写成两个英文词而都不带括号），本次的检测手段会漏掉。因此第二节的"未发现漂移"**射程只到该模式**，不等于已普查。
- **初版结论越界的教训**：本文档初版把"组织方式轴上的七条判定"外推为"领域内容已有更细的 owner"，而支撑它的实测只覆盖了组织方式。**凡结论涉及某个轴时，证据必须落在同一个轴上**；跨轴外推需重新取证，不能沿用。`## 八`是该规则的一次实际执行。
