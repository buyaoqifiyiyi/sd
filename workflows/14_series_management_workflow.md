# SD Film Series Management Workflow

# AI影视系列项目管理流程


## Workflow Purpose

执行前读取references/project_state_contract.md、references/asset_lock_contract.md与references/artifact_revision_contract.md。系列层只聚合各项目Selected State Source，不建立全局当前项目指针；普通Chat本机Root不可读时使用各当前任务的Portable State。


本Workflow负责：

管理连续剧、短剧、多章节AI影视项目。


目标：

保持：

角色连续性。

世界观连续性。

资产复用。

剧情连续。



---

# Workflow Position


适用阶段：


Series Project


多集项目启动后执行。



---

# Core Principle


系列影视不是多个独立视频。


而是：

同一个影视世界中的连续生产。



必须维护：


角色资产库。

环境资产库。

道具资产库。

剧情状态。



---

# Series Initialization


创建系列项目时：

建立：



## Series Bible


系列总设定。



包含：


世界观。


时代背景。


视觉风格。


叙事规则。



---

## Character Database


角色数据库。



包含：


角色ID。

姓名。

年龄。

外貌。

服装。

性格。

关系。



---

## Environment Database


环境数据库。



包含：


地点ID。

名称。

结构。

时间变化。

可复用状态。



---

## Prop Database


道具数据库。



包含：


道具ID。

来源。

功能。

状态变化。



---

# Episode Management


每一集必须建立：

Episode记录。



格式：


EP001


EP002


EP003



---

# Episode Structure


每集包含：


## Episode Bible


本集剧情目标。



---

## Episode Assets


本集新增资产。



---

## Episode Shots


本集镜头列表。



---

# Asset Reuse Rules


已有资产优先复用。


优先级：


已有资产

＞

修改已有资产

＞

创建新资产



---

# Character Continuity


跨集必须保持：


脸。

年龄。

发型。

服装逻辑。

人物关系。



---

# Costume Management


服装变化必须记录。



格式：


CHAR-001


Costume:

COST-001



状态：

当前使用。



---

# Environment Continuity


场景变化必须记录。


例如：


ENV-001


状态：

Episode 01:

完整。


Episode 05:

损毁。



---

# Prop Continuity


重要道具必须追踪。


例如：


PROP-001


状态：

Episode 01:

出现。


Episode 08:

损坏。



---

# Episode Workflow


每集执行：


STATE-00 Project Setup

↓

STATE-01 Script Analysis

↓

STATE-02 Asset Discovery

↓

STATE-03 Asset Development

↓

STATE-04 Visual Development

↓

STATE-05 Scene Breakdown

↓

STATE-06 Detailed Shot Design

↓

STATE-07 Clip Production

↓

STATE-08 Clip-based Video Prompt / Video Generation

↓

STATE-09 Review



---

# New Asset Gate


新增资产前必须检查：


是否已有类似资产。



禁止：

重复创建。



---

# Version Management


资产支持版本：



CHAR-001_V1.0


CHAR-001_V2.0



修改原因必须记录。



---

# Project Memory


系列项目必须维护：


按State Source优先级选定的project_status.md或portable_project_status.md


asset_registry.md


Series Bible

每次集状态推进后，Work/Codex同步Portable State；普通Chat输出更新后的完整Portable State；两者都执行references/project_state_contract.md的`Portable Required Field Writeback`。



---

# Quality Check


每集完成检查：



## Character


□ 是否保持一致



## World


□ 是否符合世界观



## Timeline


□ 时间是否连续



## Asset


□ 是否正确复用



---

# Failure Handling


发现连续性错误：



角色错误：

返回Character Asset。


场景错误：

返回Environment Asset。


剧情错误：

返回Script Analysis。



---

# Output Format

最终Series Status必须使用：

templates/19_series_status.md

Workflow负责跨集状态、资产复用和连续性判断；Template独占最终字段、顺序与排版。



---

# Final Principle


系列短剧制作：

不是重复生成视频。


而是持续维护一个可扩展影视世界。
