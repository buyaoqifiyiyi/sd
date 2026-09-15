# Documentary And Non-Fiction Adapter

## Purpose And Trigger

本Knowledge是`knowledge/script_adaptation.md`的条件性**纪实 / 非虚构**适配器。只有STATE-01 `Adaptation Target Detection`确认目标属于以下任一类型时才加载：

- 纪实 / 纪录片
- 观察式记录 / 访谈式
- 档案重组 / 口述史

其他目标（短剧、品牌广告、儿童动画、电影短片、长篇剧情）一律Not Applicable；短剧目标仍走`knowledge/adaptation/short_form_drama_adapter.md`，品牌目标仍走`knowledge/branded_content/index.md`。

## Machine-executable Decision Contract

```text
Target Evidence
→ Source Reality Inventory
→ Claim-to-Source Ledger
→ Reconstruction Boundary Declaration
→ Real-Subject And Rights Check
→ Narration Authority Audit
→ Timeline Fidelity Check
→ Generated-Image Provenance Label
→ PASS / REVISE / PENDING
```

任一硬门缺失返回`REVISE`；需要用户决定的权利或来源冲突返回`PENDING`。**不得用"看起来真实"填补缺失的来源。**

## Hard Gates

### 1. Source Reality Gate

每一条被当作事实陈述的内容，必须能指向一个可核对的来源（用户提供的材料、已确认档案、可追溯的公开记录）。写不出来源的，不得以陈述句呈现；需要保留时改成明确标注的假设或删除。

### 2. Reconstruction Boundary Gate

重现（reconstruction）与档案素材必须**可区分**：

- 重现段落必须显式标注为重现，并在内部记录其依据来源；无依据的重现降级为示意。
- 重现不得与档案素材在交付中混排到无法分辨。
- 重现只补足**可核实的事实间隙**（环境形态、动作顺序、器物使用），不得补足人物内心、未记录的对话与未发生的动机。

### 3. Real Subject And Rights Gate

真实人物、真实机构、真实事件与真实品牌沿用一等禁项，与`rules/automation_mode.md`的Hard Stop同一口径。出现真实主体的影像、声音、姓名与经历时，授权与使用范围必须由用户提供；未提供时保持Pending Decision，不用近似物替代后当作真实主体使用。

### 4. Narration Authority Gate

旁白与字幕只承担**来源可核对的陈述**：时间、地点、数量、已记录的行动与已确认的引述。禁止用旁白替观众下结论、替人物读心、或把推断说成事实。引述必须标明是引述。

## Claim-to-Source Ledger

内部维护一张最小台账：每条事实主张 → 来源 → 来源类型（用户材料 / 档案 / 公开记录 / 假设）→ 置信等级。台账是内部生产证据，不新增用户可见字段；它保证"这句话从哪来"随时可答。答不出即该主张不成立。

## Generated-Image Provenance｜生成影像的来源标注

**本适配器最重要的一条**：AI生成的画面**不得被呈现为档案或真实影像**。

- 任何由模型生成的画面，在交付与内部记录中都必须可被识别为生成影像，不得配上纪实性字幕、时间码或档案式包装使其看似史料。
- 需要"史料感"时，只能用于**已确认存在**的档案位置并明确标注，或在重现标注下使用。
- 不得生成真实人物的可信影像并作为记录呈现；涉及真实主体时按`### 3. Real Subject And Rights Gate`处理。

## Timeline And Causality Fidelity

时间线、因果与顺序属于来源事实：不得为叙事顺畅而调换事件顺序、合并不同时间的事件或制造未记录的前因后果。为可看性压缩与并置是允许的，但**压缩后的顺序必须与来源一致**，且被省略的部分不得被暗示为未发生。

## Sound And Image Authenticity Boundaries

- 声音设计可以服务观看，但不得制造未记录的现场声（把推断的环境声当作同期声证据）——需要时按重现处理。
- 访谈与口述段落，其画面覆盖（B-roll）不得暗示未被陈述的内容。
- **视频Prompt永久禁止非剧情内配乐**：纪录片不构成例外，情绪不靠配乐推。

## Acceptance Checklist

```text
[ ] Target Evidence明确属于纪实 / 非虚构目标
[ ] Claim-to-Source Ledger覆盖全部事实陈述，无来源项已改写或删除
[ ] 重现段落全部带标注与依据来源
[ ] 真实主体的授权与使用范围由用户提供
[ ] 旁白与字幕只陈述可核对内容，引述已标明
[ ] 时间线与事件顺序与来源一致，压缩未制造虚构因果
[ ] 全部生成画面可被识别为生成影像，未冒充档案
[ ] 未新增用户可见字段、未改变STATE-08 Schema
[ ] 未使用非剧情内配乐
```

全部通过才返回`PASS`并交给通用Adaptation Fidelity Check；否则返回`REVISE`或`PENDING`及最小修正范围。
