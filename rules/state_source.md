# State Source Resolution

## Purpose

本规则拥有“如何选择当前项目状态来源”的运行行为。状态字段、Portable State完整结构与写回语义由`references/project_state_contract.md`拥有；项目目录发现与身份核验由`references/project_workspace.md`拥有。

## Selection Priority

每次Workflow开始、恢复、保存、推进或重载后，都必须重新按以下优先级选择State Source：

```text
可访问且Project ID一致的Active Project Root/project_status.md
>
有效的portable_project_status.md
>
当前可验证的Project Context（先规范化为Canonical Portable State）
>
无项目证据时初始化STATE-00 Project Setup
```

“可访问”必须以本次实际读取成功为准；文本中出现路径不构成可访问性证据。Project ID不一致时不得自动合并。

## Runtime Behavior

- Work/Codex：实际可读且Project ID一致的Active Project Root状态是State Source of Truth，也是本地持久化目标。
- 普通Chat：本机Root、Skill安装目录或Registry不可读时直接回退到Portable State；这不是错误，也不得因此报告`BLOCKED`。
- Skill Source与State Source不得混淆：Portable State或Project Context只证明项目事实来源，不证明本轮已读取Current Skill Definition；反之，Runtime Reload失败也不得清空仍可验证的项目上下文。
- 对话中提供的完整Portable文档或附件属于第二级；可验证但非完整的对话Project Context属于第三级，必须先按状态合同补齐Canonical结构，只迁移有证据的事实。
- 多个候选项目存在时，不按“最近项目”猜测。使用明确Project ID、项目名、已确认Artifact与用户当前指代核验；无法唯一确认时记录Pending Decision。
- 用户当前一句话、历史Skill描述、模糊阶段名或孤立路径不能单独证明Current State。
- Portable模式不授权虚构资产、剧本、确认或完成状态；当前Workflow确实缺少外部输入时，按状态合同记录Pending Decision或`BLOCKED`。

## Resolution Procedure

1. 解析当前Project ID与候选Active Project Root。
2. 实际读取并核对`project_manifest.json`、`project_status.md`或Portable State。
3. 校验状态Schema、Project ID、Revision、Checkpoint与Artifact证据。
4. 对旧标签或旧Schema调用`rules/compatibility_mapping.md`。
5. 选定唯一State Source，并记录`Selected State Source`与`Source Selection Reason`。
6. 根据Current State、Completion Gate与Pending Decision确定Active / Next Workflow。
7. 状态发生变化时按`references/project_state_contract.md`写回并同步。

## Non-Negotiable Invariants

- 固定主路由为`STATE-06 Detailed Shot Design → STATE-07 Clip Production → STATE-08 Clip-based Video Prompt / Video Generation`。
- Storyboard只能是用户显式请求的Optional/Auxiliary Artifact，绝不成为STATE或固定Next Workflow。
- 当前状态与用户目标不匹配时，按Pipeline补齐必需阶段，不以目标词直接跳阶段。
