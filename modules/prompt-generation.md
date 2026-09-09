# Prompt Generation Module

入口：`workflows/11_video_generation_workflow.md`；语义投影 owner：`knowledge/prompt_compilation/state08_projection.md`；最终格式由Selected Model唯一路由：Seedance 2.0使用`templates/10_video_prompt.md`，Seedance 2.5使用`templates/12_seedance_25_video_prompt.md`，MiniMax H3使用`templates/13_minimax_h3_video_prompt.md`。任何未来模型必须先建立独立最终Prompt Template，才能接入Model Selection。

只读取确认的 Script、Director Intent、Storyboard（仅用户选择的辅助参考，非 Canonical）、Spatial Blocking、Natural Clip / Adapter result、Assets、首尾帧与当前 Model Adapter，编译最终模型提示词。

不得改写剧情、人物关系、导演意图、Shot 目的、确认空间关系或 Canonical Asset。参考上一 Clip 尾帧时，必须明确其是镜头连续、人物站位连续、环境连续或空间关系延续用途。视频 Prompt 永久不含配乐；音色控制仍为显式 opt-in。
