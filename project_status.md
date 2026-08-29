# Legacy Project File Pointer

本文件不保存任何项目的真实状态，也不固定指向某个最近项目。

本文件不是State Source规则拥有者。执行任何Workflow前，由`references/project_workspace.md`解析项目候选，并只按`rules/state_source.md`选择状态来源；字段与同步行为服从`references/project_state_contract.md`。

禁止把真实项目状态写入本兼容入口；Portable最小镜像写入`portable_project_status.md`。
