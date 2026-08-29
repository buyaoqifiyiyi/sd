# Legacy Project File Pointer

本文件不再保存 Active Project 的真实 Project Bible。

原有项目已经迁移：

- 项目 ID：PROJECT-ZYH-OTTER-001
- Project Root：`C:\Users\Lenovo\Documents\Codex\SD Film Projects\PROJECT-ZYH-OTTER-001`
- 实际文件：`C:\Users\Lenovo\Documents\Codex\SD Film Projects\PROJECT-ZYH-OTTER-001\project_bible.md`

执行任何Workflow前，先按`可访问且Project ID一致的Active Project Root/project_status.md > portable_project_status.md > 初始化STATE-00`选择State Source。本地文件访问确实可用时先按`references/project_workspace.md`和`project_registry.json`解析Active Project；普通Chat本机路径不可访问时fallback到Portable，不得报错、`BLOCKED`、停止或要求用户重新提供路径。历史聊天文本不是状态源。

禁止把新的项目内容写入本兼容入口。
