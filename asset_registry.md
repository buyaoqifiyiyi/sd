# Legacy Project File Pointer

本文件不再保存 Active Project 的真实 Asset Registry。

公开技能包不绑定任何具体项目、Project ID或本机绝对路径。真实Asset Registry仅保存在运行时解析出的Active Project Root中。

执行任何Workflow前，先按`可访问且Project ID一致的Active Project Root/project_status.md > portable_project_status.md > 初始化STATE-00`选择State Source。本地文件访问确实可用时先按`references/project_workspace.md`和`project_registry.json`解析Active Project；普通Chat本机路径不可访问时fallback到Portable，不得报错、`BLOCKED`、停止或要求用户重新提供路径。历史聊天文本不是状态源。

禁止把新的资产状态写入本兼容入口。

## Visual Production Status Schema

Active Project Root中的每条正式CHAR、ENV、PROP、FX视觉资产记录必须同时保留资产版本`Status`与独立的`Visual Production Status`：

| Visual Production Status | 含义 | 允许的视觉引用 |
|---|---|---|
| Prompt Draft | 完整Image Prompt已输出，等待用户确认 | 无新图；不得生成 |
| Prompt Confirmed | 用户已确认当前Prompt Revision，可以生成图片 | 无新Canonical Reference |
| Image Generated | 图片已生成或已回传，等待用户确认 | 仅Candidate References |
| Asset Confirmed | 用户已确认图片，视觉资产闭环完成 | 可登记Canonical References并切换Active Version |

固定顺序：`Prompt Draft → Prompt Confirmed → Image Generated → Asset Confirmed`。Prompt确认与图片确认必须分别记录；不得把`Image Generated`或资产版本`Approved`自动解释为`Asset Confirmed`。

## Two-Tier Asset Registry Fields

Active Project Root中的每条CHAR、ENV、PROP记录还必须明确：

```text
Asset Tier: Core | Support
Board ID: Not Applicable | BOARD-CHAR-001 | BOARD-ENV-001 | BOARD-PROP-001
Item ID: Not Applicable | A-01 | A-02 | ...
Prompt Status: Not Started | Draft | Confirmed
Image Status: Not Generated | Candidate | Confirmed
Confirmed Status: No | Yes
```

- Core记录的Board ID与Item ID固定为`Not Applicable`。
- Support记录必须有Board ID与板内稳定Item ID，并记录Board Name、Included Asset IDs、Item ID Mapping及Canonical Board Reference的区域/标签对应关系。
- Board建议包含4—9个同类型对象；角色、环境与道具不得跨类型混板。Item ID确认后不得重排或复用，后续引用使用`<Board Name> / <Board ID> / <Item ID>`。
- 正式FX Asset本次保持原有Formal FX规则，`Asset Tier`、`Board ID`与`Item ID`可写`Not Applicable`。

状态投影必须与`Visual Production Status`一致：

| Visual Production Status | Prompt Status | Image Status | Confirmed Status |
|---|---|---|---|
| Prompt Draft | Draft | Not Generated | No |
| Prompt Confirmed | Confirmed | Not Generated | No |
| Image Generated | Confirmed | Candidate | No |
| Asset Confirmed | Confirmed | Confirmed | Yes |

任何Core Asset、Support Board或Support Item在图片未获用户明确确认前，`Confirmed Status`必须为`No`，不得标记confirmed、Active或Canonical。
