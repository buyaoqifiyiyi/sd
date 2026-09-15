# Atom 4 — Style And Consistency｜画风锚与一致性

## Purpose And Owner

本原子拥有 `2d_anime` 档的**画风锚与跨镜一致性纪律**：线宽、上色法、网点/笔触与色指定如何在整片内保持可对照。

它与`knowledge/color/color_continuity.md`、`knowledge/lighting/lighting_continuity.md`互为**对等物**：那两者用实拍的光比与色温表达连续性，本原子用绘制量表达同一件事。

边界：不拥有角色形状与配色的**结构**（归`templates/04_character_asset_prompt.md`的2D设定集）；不拥有项目级美学方向（归 STATE-04 的`Aesthetic Decision Lock`与`knowledge/medium_profiles.md`的Aesthetic Layer）；不判断画得好不好看（归`knowledge/quality/aesthetic_judgement.md`）。

## Executable Vocabulary｜可执行词汇

| 实拍量（本档禁止写入） | 绘制媒介等效物 | 写进哪个既有字段 |
|---|---|---|
| 光比 / 光位 | **阴影形状与阴影层数**（cel 一层 / 二层 / 三层）及其边缘形状 | 光线 |
| 光源方向 | 阴影落在哪一侧、边缘是硬边还是渐层 | 光线 |
| 色温 | **色指定的冷暖倾向与暗部色**（不是色温数值） | 光线、视觉风格 |
| 胶片颗粒 / 镜头暗角 | **网点、笔触、留白**；暗角在本档不成立 | 视觉风格 |
| 皮肤次表面散射 / 材质渲染 | **上色法**（平涂、渐层、水彩边界）与**高光形状** | 视觉风格 |
| 景深虚化 | 分层简化度（见`knowledge/anime_language/01_layout_and_space.md`） | `构图` |
| 一致性锚 | **设定集**（形状与色指定）+ **画风锚**（线宽、上色法、网点） | Canonical Reference |

## Conditions And Anti-Use｜成立条件与反用

- **一次锁定，跨镜不逐镜改**：线宽、上色法、网点/笔触三项必须在 STATE-04 的`Visual Grammar Baseline`与`Aesthetic Decision Lock`一次性锁定，之后进入已确认资产与 Project Bible；STATE-06 / 07 / 08 只继承，不重新选择。
- **色指定用可命名色块**：以"主色 / 暗部色 / 强调色"加明度与饱和度关系表达。用户未提供色值时**不得虚构 Hex、RGB、LUT、胶片库或色域参数**（沿用`knowledge/color/foundations.md`的既有纪律）。
- **画风锚必须可执行**：写"线宽统一的一级线 + 二层 cel 阴影 + 暗部暖灰网点"是可复核的；写"日式赛璐璐风""高级感""低饱和"不是画风锚。
- **漂移是本档最典型失败**：相邻 Clip 之间，线宽、阴影层数、网点密度与色指定必须能被对照检查；任一项改变都算画风漂移，不是"风格变化"。
- **禁止**：把胶片颗粒、镜头暗角、次表面散射、镜头瑕疵、真实景深当作 2D 的美学载体。

## Prompt Translation｜Prompt 转译

只使用既有字段（`视觉风格`、`光线`、`构图`）。示例写法：

- `视觉风格：统一线宽的一级线稿、二层 cel 上色、暗部为暖灰网点（中等密度）；高光为硬边小块`
- `光线：主光来自左上方，阴影为二级（本体影 + 一层投影），边缘硬边`
- 不得出现"胶片感""电影感""低饱和胶片"等实拍词表；同一意图改写成上述可执行项。

## Failure Signals｜失败信号

- 相邻 Clip 的线宽、阴影层数或网点密度肉眼可辨地变化——画风漂移。
- 画面出现写实皮肤质感、镜头暗角、颗粒或真实景深——实拍词表漏进 Prompt。
- 阴影在暗部发灰失去色相，或色指定在相邻镜头间冷暖反转。
- 画风锚只写了形容词，QA 无法对照检查。
- 擅自出现用户未提供的色值（Hex / RGB / LUT）。
