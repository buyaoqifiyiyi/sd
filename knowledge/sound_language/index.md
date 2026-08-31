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

STATE-08还必须先执行Voice Reference Override Gate：固定字段`音色特征：`始终保留。用户已明确提供当前音色参考资产，或Active CHAR Version存在当前模型实际使用的Confirmed Voice Audio Reference / Audio Reference / Voice Reference时，该字段声明Reference锁定声音身份且不得文字重定义，并删除其他字段中的Voice characteristics、音高、声线、音域、共鸣、语速、音色质感等文字音色描述；只允许在准确台词旁保留“轻声说、无奈地说、短暂停顿后说”等轻量表演指令。没有适用Reference但已有Confirmed Voice Profile时使用该Profile作为文字回退；两者都不存在时声明未建立独立音色资产且本Clip不创建或推导声音身份，不得自动调用AUDIO模块；无对白时明确无对白。该Gate不影响上述默认无背景音乐规则。

`voice_generation.md`中的Seed Audio结构只属于显式调用的AUDIO模块，不是STATE-03默认输出，也不是STATE-08视频Prompt字段。唯一输出Schema为`templates/21_seed_audio_voice_asset.md`。竹雀Voice Bible只用于示例和项目内复用，不自动投影到其他项目。
