# Technical Visual Blocking Sketch Generation Template

本模板只服务STATE-08 Before-Single-Clip-Prompt Gate中Final=`REQUIRED`的`REF-SKETCH-XX`生成。它拥有图像生成输入包与候选草图证据记录的结构，不拥有Assessment算法、STATE-08最终视频Prompt Schema或Storyboard输出。

## Route Lock

- Route：`TECHNICAL_VISUAL_BLOCKING_SKETCH`。
- Output：单张`Technical Director Blocking Sheet / Spatial Blocking Diagram`。
- Forbidden Route：`STORYBOARD`、`ARTISTIC_STORYBOARD`、`CINEMATIC_PENCIL_SCENE`、`KEY_ART`、`CONCEPT_ART`。
- 禁止读取或调用`templates/09_storyboard_prompt.md`；Storyboard与本模板互不复用默认生图指令。

## Generator Call Contract

先读取`references/ref_sketch_master.md`并从当前Skill根解析`Persistent Asset Path`。

- 母版状态为`REGISTERED`、PNG真实可读且登记尺寸/SHA-256均通过Integrity Check：图像生成调用必须把解析后的绝对路径放入真实图像参考参数，例如支持`referenced_image_paths`的工具必须传`referenced_image_paths: [<absolute master path>]`。记录`Master Input Mode = VISUAL_REFERENCE`与实际路径；不得只在文字Prompt中提到母版。
- 母版状态为`UNAVAILABLE`、文件不可读、发生`Integrity Mismatch`或工具不支持图像参考：记录`Master Input Mode = TEXT_CONTRACT_FALLBACK`和具体失败来源；Integrity Mismatch必须逐项记录尺寸或SHA-256差异。不得声称使用了视觉母版，也不得仅更新登记信息来掩盖不一致。
- 使用本地文件路径时不得同时用会话最近图片参数替代或混入未知图片。

## Current Clip Input Package

只从当前已确认语义权威填入：

- Clip ID / Sketch Type：`S-SKETCH / P-SKETCH / A-SKETCH / Combined`。
- Blocking Signature：Characters、Position、Topology、Shared Facing、Seat / Spatial Relation、Allowed Delta、Camera Logic、Axis、Movement Path、Clip Start / End Blocking。
- Role Mapping与Character Labels；只传递角色名 / ID、技术标注颜色和位置标签，不传递或模仿Character Asset外观。
- Main Blocking：位置、身体朝向、距离、共享结构、当前环境锚点。
- Direction Annotation：Facing、Gaze、Head Delta、Movement / Action Path与适用接触 / 受力方向。
- Spatial Proof：Top-down或当前动作所需的空间 / 路径证明、Interaction / Eyeline / Action Axis、Camera Safe Side。
- Camera Information：最小充分的Shot Size、Angle、Lens tendency、Camera Side。
- Blocking / Movement Permission：LOCK / LIMITED / CHANGE与当前动作要点。
- Usage / Reference Authority：只锁Position / Facing / Distance / Topology / Axis / Camera / Pose / Gaze / Action Path；最终Clip参考资产说明只需写`草图人物为无性别调度人偶，仅用于空间 / 姿态 / 机位关系，不作为人物外观参考。`人物外观服从正式Character Asset；环境 / 道具造型、材质、灯光、色彩或最终画风也不由草图控制。

## High-Priority Image Instruction

生成一张多区域工程版式的`Technical Director Blocking Sheet`，不是单幅叙事插画。最大区域必须是Main Blocking Panel；另有清楚分隔的Spatial / Top-down或Action Path Diagram、Camera Information、Blocking / Movement Permission与Usage / Reference Authority区域。人物绘制层严格执行`references/ref_sketch_master.md`的`Neutral Mannequin Representation Rule`：所有人物使用同一套无性别技术调度人偶 / 中性关节pose dummy，无真实五官、发型、具体服装、明显性别化胸腰臀 / 体态、年龄 / 美貌 / 气质身份；不根据Character Asset重画外观。只用角色名 / ID、少量技术颜色、左右 / 位置标签、姿态与方向 / 视线 / 动作箭头证明Current Clip的空间和动作关系。A-SKETCH只有物理约束所必需的比例可以表达，仍不得恢复角色视觉身份。

最终电影风格、导演名、青春 / 阴雨 / 唯美气氛、cinematic illustration、海报感、概念艺术、高燃光效不得成为本次草图的正向风格目标。母版中的人物、钢琴、琴凳、窗户、乐谱、雨景或文字只有在Current Clip事实明确要求时才可出现。

## Candidate Evidence Record

候选图生成后，必须由实际视觉检查填写JSON证据并运行：

```text
python scripts/validate_sd_film.py sketch <evidence.json> --skill-root <current-skill-root>
```

证据字段：

```json
{
  "schema_version": 1,
  "clip_id": "CLIP-XXX",
  "assessment": "REQUIRED",
  "route": "TECHNICAL_VISUAL_BLOCKING_SKETCH",
  "generator_template": "templates/23_visual_blocking_sketch_prompt.md",
  "sketch_type": "S+P",
  "master_input_mode": "VISUAL_REFERENCE",
  "master_asset_path": "assets/ref_sketch_master.png",
  "image_path": "<actual candidate PNG path>",
  "blocking_signature": "<non-empty current signature>",
  "spatial_top_down_required": true,
  "layout": {
    "main_blocking_panel": true,
    "character_role_labels": true,
    "direction_gaze_movement_annotation": true,
    "spatial_top_down_diagram": true,
    "camera_information": true,
    "blocking_movement_notes_or_permission": true,
    "usage_authority_note": true
  },
  "artistic_storyboard_drift": false,
  "template_content_leakage": false,
  "neutral_mannequin_representation": true,
  "character_appearance_leakage": false,
  "blocking_match": true,
  "registration_status": "CONFIRMED"
}
```

`assessment=NONE`时使用`route=NONE`、`registration_status=NONE`且不生成图片。任何`REQUIRED`候选只有命令返回PASS才可注册；单幅叙事插画固定返回`FAIL = Artistic Storyboard Drift`；人物出现真实五官、具体发型 / 服装、明显性别化体态、角色外貌重绘或其他身份污染时固定返回`FAIL = Character Appearance Leakage / Identity Contamination`；其他FAIL也保持`FAILED / REVISE`，不得进入最终Clip【参考资产】。
