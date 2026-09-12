# SD Film Project Workspace

# Read Scope

本文件被多个阶段复用，**不得整文件通读**：按当前事项只读对应小节。

| 当前事项 | 只读 |
|---|---|
| 解析项目候选 | `## Project Root Contract`、`## Active Project Resolution` |
| 新项目 | `## New Project Rule` |
| 既有项目 | `## Existing Project Rule` |
| 与 State Source 衔接 | `## State Source Integration` |
| 路径别名 | `## Path Alias Rule` |
| 校验命令 | `## Validation Commands` |
| 不必在运行时读取 | `## Purpose`、`## Runtime Skill Source`、`## Final Principle` |

---

## Runtime Skill Source

Runtime Reload是否触发、如何解析当前可访问Skill resources及如何报告只服从`rules/runtime_reload.md`，并在解析项目前执行。普通Chat先使用当前runtime实际可访问的installed / exposed Skill resources，不因Windows本机路径不可读默认切Work。Portable State只携带项目状态，不是Skill Definition。旧对话中的Skill描述不是权威Skill Source。Skill Definition解析完成后，再按`rules/state_source.md`为Project Context选择唯一来源。

## Purpose

本文件定义 SD Film 的多项目隔离与项目文件解析规则。

项目状态字段、转换、Review退回与Checkpoint语义统一服从：

`references/project_state_contract.md`

Skill 安装目录保存通用的 `SKILL.md`、Rules、Workflows、Knowledge、Templates、References 和 Scripts，以及普通 Chat 兼容所需的最小状态镜像 `portable_project_status.md`。

以下完整项目数据必须保存在独立的 Project Root 中：

- `project_manifest.json`
- `project_status.md`
- `project_bible.md`
- `asset_registry.md`
- 后续场景、Detailed Shot Design、Clip Production Plan、Prompt、Review 与生成结果

禁止把新项目的可变数据直接写回 Skill 安装根目录。

`portable_project_status.md`是唯一例外：它只保存恢复与路由所需的最小状态镜像，不保存完整项目资产或阶段交付物。它是否被选作State Source只服从`rules/state_source.md`；本文件仅定义其工作区位置与本地项目文件的关系。

---

## Project Root Contract

每个独立项目必须拥有唯一 Project Root：

```text
<project-root>/
├── project_manifest.json
├── project_status.md
├── project_bible.md
├── asset_registry.md
├── execution_ledger.md
├── artifact_registry.md
├── source/
├── assets/
├── scenes/
├── sequences/
├── shots/
├── shot-plans/
├── prompts/
├── reviews/
└── outputs/
```

没有实际内容的子目录不必提前创建。前三个 Markdown 项目文件和 Manifest 为必需文件。

生产交付包（已确认生产物的分类打包与zip）不放在Project Root内，其位置、命名、构成与**执行环境前提**由`references/asset_package.md`唯一拥有：它位于Project Root之外的交付目录，只复制真实已确认文件，不改写Project Root、不改名已确认资产图片、不改动`asset_registry.md`，也不被当作运行时Required Resource。只有在能读写本机目录的Work / Codex本地模式才产包与zip；普通Chat的Portable模式不产zip，只交付清单、命名映射与目录骨架文本。`.git`、`tmp`不属于Project Root Contract，也不得进入包内。

`project_manifest.json` 至少包含：

```json
{
  "schema_version": 1,
  "project_id": "PROJECT-...",
  "project_name": "...",
  "project_type": "...",
  "created_at": "YYYY-MM-DD",
  "source_material": "..."
}
```

---

## Active Project Resolution

运行环境确实提供本地文件访问时，按以下顺序解析Active Project候选并提供Project ID、路径与可访问性证据；是否采用其`project_status.md`只由`rules/state_source.md`决定：

1. 用户在当前任务中明确指定的 Project Root 或 Project ID。
2. 当前工作目录或其父目录中可确认的 `project_manifest.json`，且当前会话已明确指向该项目。
3. 恢复或继续既有项目时，按`rules/state_source.md`的Intent Scope Gate使用项目路径、项目`project_status.md`或Portable State。
4. 如果输入明确属于新项目，进入 STATE-00并建立会话内最小状态；只有用户明确要求保存或归档时，才在独立目录初始化新的 Project Root。

本Skill不维护项目登记表：不得建立、读取或更新任何项目索引、清单或注册文件，也不得为了找出既有项目而扫描磁盘。找回项目只使用用户给出的路径/Project ID、当前可访问的项目目录或Portable State。

如果存在多个合理候选且当前信息无法唯一判断，不得自动选择最近项目；必须先确认用户要继续的项目。

Active Project 只对当前任务上下文生效；Skill不保存任何全局“当前项目”指针，防止不同任务互相切换状态。

---

## State Source Integration

本文件输出经过身份核验的Active Project Root候选、Manifest与Registry证据；随后由`rules/state_source.md`选择唯一State Source。Portable候选的字段合法性和写回由`references/project_state_contract.md`验证。本文件不得维护State Source优先级、fallback或Chat运行差异的竞争副本。

如果存在多个合理Root候选且无法唯一确认，本文件返回候选与身份冲突，不选择“最近项目”、不合并Project ID，也不覆盖任何项目。路径或Registry实际不可读时只报告不可用性，由State Source Rule决定下一来源。

---

## Path Alias Rule

Work/Codex 本地模式中，现有 Workflow 未限定路径的项目文件名统一解释为：

```text
project_status.md  = <active-project-root>/project_status.md
project_bible.md   = <active-project-root>/project_bible.md
asset_registry.md  = <active-project-root>/asset_registry.md
```

它们不得解释为 Skill 安装根目录中的同名兼容入口。

Skill 根目录中的同名文件只用于兼容说明；不得在其中继续写入真实项目状态。

普通 Chat Portable 模式中：

```text
project_status.md = 当前任务最新可用的 portable_project_status.md
```

`project_bible.md`、`asset_registry.md`与阶段交付物优先使用当前对话已经确认的内容或已附加的项目文件。仅因本机路径不可访问不得停止；真正缺少当前Workflow必需事实时，按Workflow的Pending Decision处理。

---

## New Project Rule

STATE-00必须先确定会话Project ID。默认不创建Project Root、也不展示项目初始化页；它在当前响应内完成最小启动事实后进入下一个可交付阶段。用户明确要求保存或归档时，才确定Project Root并初始化项目文件。

新 Project Root 必须满足：

- 不与现有项目共用三个核心状态文件。
- Project ID 与Project Manifest、Status、Bible和Asset Registry中的写法一致。
- 初始化不得覆盖已有非空项目目录。
- project_status.md符合references/project_state_contract.md。
- execution_ledger.md与artifact_registry.md已经建立最小入口。
- 用户没有确认的信息保持待分析，不通过初始化脚本虚构。

本Skill不登记项目：新项目只在自己的Project Root内建立最小文件，不写入任何Skill根目录下的索引、清单或注册文件。Skill安装目录只保存通用定义，不是项目仓库。

---

## Existing Project Rule

当`rules/state_source.md`选中Active Project Root时，继续项目必须读取其中的Manifest和三个核心项目文件；选中Portable或规范化Project Context时，按`rules/chat_compatibility.md`读取当前可用资料，不要求用户仅为路径访问问题重复上传。

如果 Manifest 与任一项目文件中的 Project ID 不一致：

- 停止状态推进。
- 不自动合并两个项目的数据。
- 运行项目校验并定位冲突文件。

Work/Codex项目级更新只能写入 Active Project Root。完成阶段后，不得同时更新其他项目；随后按`references/project_state_contract.md`同步Portable State。

---

## Validation Commands

Skill自身由`scripts/validate_sd_film.py`确定性校验（唯一入口为skill root）：

```text
validate_sd_film.py --skill-root <skill-root> [--report]
```

本次交付的视频Prompt由`scripts/validate_prompt_package.py`校验：

```text
validate_prompt_package.py <prompt-file> [--clip-plan <confirmed-clip-plan.md>]
```

生产交付包由`scripts/build_asset_package.py`构建并顺带核验命名与对应性（可选加固，规范真源仍是`references/asset_package.md`）：

```text
build_asset_package.py --project-root <project-root> [--check-prompt <compiled-prompt.md>]
```

项目根内的`project_status.md` / `asset_registry.md` / `artifact_registry.md` / `execution_ledger.md`当前**没有**独立的确定性CLI校验器：它们由各Workflow的Required Read、`# Completion Gate`与`references/project_state_contract.md`的写回要求人工判定。本节不发布不存在的子命令。

校验器只报告结构和确定性协议问题，不替代剧情、表演、摄影或审美判断。

---

## Final Principle

Skill 是生产工具，Project Root 是Work/Codex中单个项目的完整可变状态；Portable State是普通Chat可继续执行的最小状态镜像。Skill只保存通用定义，不保存任何项目索引或注册表。

Runtime Reload只替换Skill Definition，不清空Project Context。已确认Script、资产、Checkpoint、已接受交付物与用户约束仍属于当前项目，只按最新Pipeline重新映射路由。

必须保持：

```text
通用能力与规则留在 Skill
项目状态与交付物留在独立 Project Root
每次任务先解析 Active Project
所有项目写入只作用于当前 Project Root
普通Chat无法访问Project Root时使用Portable State而不中断
Work/Codex更新真实状态后同步Portable State
```
