# Sound Language Index

## Purpose

本目录建立可执行的对白、环境声、动作声、同期静默与跨镜生产声音连续性。后期Music / Score由独立`knowledge/music_score/`拥有，本目录不规划配乐。

适用于：

- STATE-04 建立项目级声音原则
- STATE-06 定义逐镜声音目的和连接
- STATE-07 标注关键声音触发
- STATE-08 建立同期声音执行逻辑；不得生成背景音乐
- STATE-09复核生产声音与声画连续性

Sound Knowledge不定义最终Prompt Schema。最终字段仍由templates/10_video_prompt.md决定。

---

## Routing

- voice_generation.md：显式调用的`AUDIO / SEED-AUDIO Voice Asset`模块用于Voice Profile、Seed Audio角色音色样本Prompt、试听文本与Audio Reference交接；只有用户当前请求明确要求音色提示词、音色制作、角色声音、Seed Audio、配音音色、声音资产或同义声音身份制作时读取。角色有对白、普通Character Asset、视频/Clip/Seedance请求、“继续视频制作”或“下一个Clip”均不得触发
- dialogue_and_lipsync.md：对白、音色、口型与声像
- ambience_and_foley.md：空间底噪、动作声、材质声
- music_and_silence.md：旧路径兼容边界，只说明生产声音留白与新Music模块路由；不再拥有配乐方法
- sound_continuity.md：Sound Bridge、声场继承与断点

STATE-08默认只加载对白、环境声、动作声、呼吸、Foley、剧情内声源与同期声连续性；“音效”不得写背景音乐、配乐、BGM、主题音乐、氛围音乐、歌曲或“无配乐”，【反向提示词】首个非空内容行必须逐字写“禁止生成背景音乐、配乐、BGM、主题音乐、氛围音乐，只保留台词、环境声、动作音效和必要的自然声音。”。该规则永久生效，不存在用户指定Clip、批量Clip或模型级例外。任何配乐请求都必须分流至显式调用的独立MUSIC / SEED-MUSIC模块。

STATE-08默认执行Voice Identity Omission Gate：不检查或投影Voice Profile / Voice Audio Reference，不输出`音色特征：`或声音资产存在/缺失状态；默认外部已有可用角色音色资源。即使已有Confirmed Voice Profile或Reference，也由Source携带身份，常规视频Prompt不重复描述。只有用户明确要求把声音控制写进当前视频模型Prompt时，才按Template条件输出最小Delta。准确台词旁可保留“轻声说、无奈地说、短暂停顿后说”等Dialogue Performance，但不得借此重定义稳定Voice Identity。该Gate不影响上述默认无背景音乐规则。

`voice_generation.md`中的Seed Audio结构只属于显式调用的AUDIO模块，不是STATE-03默认输出，也不是STATE-08视频Prompt字段。唯一输出Schema为`templates/21_seed_audio_voice_asset.md`。竹雀Voice Bible只用于示例和项目内复用，不自动投影到其他项目。
