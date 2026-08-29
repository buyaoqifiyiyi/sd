# Legacy Project File Pointer

本文件不保存任何项目的真实状态，也不固定指向某个最近项目。

执行任何Workflow前，按以下优先级选择State Source：

```text
可访问且Project ID一致的Active Project Root/project_status.md
>
portable_project_status.md
>
初始化 STATE-00 Project Setup
```

- 当前对话中明确提供的完整Portable文档或附件属于`portable_project_status.md`这一层；历史聊天文本、摘要与目标描述不得作为状态源。
- 普通Chat：Active Project Root不可访问时读取当前任务最新的`portable_project_status.md`；本机Skill目录、Project Root或Registry不可访问时直接fallback，不得报错、写入`BLOCKED`、停止或要求用户重新提供路径。
- Work/Codex：先按`references/project_workspace.md`与`project_registry.json`解析当前任务的唯一Active Project Root；实际可读且Project ID一致时使用其中的`project_status.md`，否则fallback到Portable State。
- 以上来源都不可用：在Portable State初始化STATE-00，不退回旧Pipeline。

禁止把真实项目状态写入本兼容入口；Portable最小镜像写入`portable_project_status.md`。
