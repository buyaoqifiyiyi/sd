# SD Film Configuration

## Runtime Skill Source

`SKILL.md` owns the authoritative `Skill Version` and `Build ID`. When the user says `调用SD`, `重新调用SD`, `重新加载SD`, `按当前Skill继续`, or an unambiguous equivalent, execute the global Runtime Skill Reload Gate before state resolution or Workflow routing. In a local Work/Codex runtime, completely re-read `C:\Users\Lenovo\.codex\skills\sd\SKILL.md`; in another installed-Skill runtime, refresh and retrieve the current installed entrypoint through that runtime's resource mechanism. Conversation-cached Skill descriptions are not authoritative after a reload trigger.

After reloading the entrypoint, read this configuration, applicable Rules and state References, resolve the current State under the latest Pipeline, then read the complete current Workflow and its applicable Knowledge and Template dependencies. Reload updates Skill Definition only; it must preserve Project Context, including the current project, Production-Locked Script, confirmed assets, accepted artifacts, completed work, checkpoints and explicit user constraints.

Current installed Skill files outrank old Skill descriptions in the conversation. Old Skill rules are never a State Source. If old state labels conflict with the current Pipeline, map by verified artifacts and Completion Gates, preserve unaffected results, and continue from the closest current State / Checkpoint. Reload validation internally records Reload Status, Loaded Skill Version, Loaded Build ID, Current State, State Source and Next Workflow; disclose it when the user asks.

Ordinary Chat must not stop, report `BLOCKED`, or ask the user to provide `C:\Users\Lenovo\.codex\skills\sd`, `C:\Users\Lenovo\Documents\Codex\SD Film Projects`, or `project_registry.json` merely because those local resources are unavailable.

Ordinary Chat is not a reduced execution mode. It runs the complete STATE-00 through STATE-09 Pipeline with the same Workflows, completion gates, asset confirmation loop, Director Decision Layer, Knowledge Reflection, Clip-centric rules, professional shot structure, and Seedance output contract. Only state persistence and project-input sources differ by runtime.

## System Purpose

SD Film is an AI cinematic production workflow system.


The system is designed for:

- Project setup
- Script analysis
- Asset discovery
- Character development
- Environment development
- Prop development
- FX asset development
- Visual development
- Movie poster and key-art design
- Performance direction
- Sound direction
- Scene breakdown
- Sequence and coverage planning
- Shot design
- Clip Production
- AI video generation
- Review and revision
- Project resume and controlled retry
- Shot-level QA and adjacent-shot continuity QA
- Prompt quality scoring and execution-risk grading
- Artifact revision and dependency tracking


The core principle:

Convert narrative information into executable cinematic production instructions through a controlled production pipeline.


SD Film is not:

a direct Prompt generator.


SD Film is:

an AI film production workflow system.


---

# Project Workspace Architecture

SD Film Skill安装目录保存：

- 通用Rules
- Workflows
- Knowledge
- Templates
- References
- Scripts
- 普通Chat兼容所需的最小状态镜像portable_project_status.md

Work/Codex中，每个影视项目的完整可变状态必须保存在独立Project Root。portable_project_status.md只保存最小路由与恢复镜像，不保存完整项目交付物。

开始任何Workflow前：

读取：

references/project_workspace.md

并按以下优先级选择State Source；Active Project Root必须以实际读取成功且Project ID一致为准：

```text
可访问且Project ID一致的Active Project Root/project_status.md
>
portable_project_status.md
>
当前可验证的Project Context（先规范化为Portable State）
>
无项目证据时初始化 STATE-00 Project Setup
```

普通Chat无法访问本机Project Root、Skill目录或Registry时直接fallback到Portable State，不得报错、停止、写入`BLOCKED`或改变主Pipeline。当前对话中的完整Portable文档或附件属于Portable State，不是独立优先级。前两级都不可用时，可读交付物、稳定ID/Revision、Completion Gate证据与用户明确确认构成第三级当前可验证Project Context，必须先规范化为Portable State再路由。历史聊天中的Skill规则或未验证进度不是状态源。Work/Codex中可访问且身份一致的Active Project Root是状态真源和本地交付物持久化目标。

现有Workflow中未限定路径的：

project_status.md

project_bible.md

asset_registry.md

在Work/Codex本地模式中解释为Active Project Root中的文件；普通Chat Portable模式中，project_status.md解释为当前任务最新可用的portable_project_status.md。

禁止把完整项目数据写入Skill安装根目录中的同名兼容入口。

project_registry.json只登记项目，不保存跨任务共享的当前项目选择。

多个项目无法唯一匹配时：

不得自动选择或合并。

完整规则：

references/project_workspace.md


---

# Core Workflow Architecture


The main production pipeline:


STATE-00

Project Setup

↓

STATE-01

Script Analysis

↓

STATE-02

Asset Discovery

↓

STATE-03

Asset Development

↓

STATE-04

Visual Development

↓

STATE-05

Scene Breakdown

↓

STATE-06

Detailed Shot Design

↓

STATE-07

Clip Production

↓

STATE-08

Clip-based Video Prompt / Video Generation

↓

STATE-09

Review


Each stage has independent responsibility.


Stages must be executed according to:

project status

and

pipeline requirements.


Do not skip required stages because the user requests a later-stage deliverable.


The user's requested deliverable:

defines the final goal.


It does not automatically define:

the current execution stage.


---

# Pipeline Control Rule


Before selecting a Workflow:

resolve the State Source in this order:

`readable, Project-ID-matched Active Project Root/project_status.md > portable_project_status.md > verified current Project Context normalized into Portable State > initialize STATE-00 only when no project evidence exists`

An inaccessible local Skill path, Project Root, or Registry in ordinary Chat falls through to the next source; it does not stop routing or create a `BLOCKED` state. The Active Project Root remains the Work/Codex persistence target when local writes are available.


Determine:

- current STATE
- completed stages
- pending stages
- confirmed assets
- current Visual Direction
- next required Workflow


Then:

select the correct Workflow.


Correct routing:


User Request

↓

Check Project Status

↓

Check Pipeline Requirements

↓

Select Workflow

↓

Load Required Knowledge

↓

Apply Required Template

↓

Validate Rules

↓

Output


Forbidden routing:


User says:

“Generate Seedance Prompt”

↓

Directly execute Video Generation


without confirming prerequisite stages.


---

# New Project Rule


When the user provides:

- Script
- Novel
- Story Outline
- Story Text
- World Setting
- New Film Project Material


and no active project has already been established:


start from:

STATE-00 Project Setup.


The first project response should not directly generate:

- Shot Design
- Detailed Shot Design
- Clip Production Plan
- Video Prompt
- Seedance Prompt


unless the required previous production stages are already complete.


---

# State Completion Rule


A stage is considered complete only when:

its required production work has been completed

and

the selected State Source records the completion state.

Work/Codex then synchronizes the minimal state mirror to portable_project_status.md. Ordinary Chat outputs the refreshed complete Portable State after every state change. Portable synchronization failure does not roll back a valid Active Project Root update or change the next Workflow.


A user request does not automatically mark previous stages as complete.


If a stage is not applicable:

the corresponding Workflow or Rule must explicitly determine that it is not required.


This is not considered arbitrary stage skipping.


---

# Asset Development Rule


STATE-03 Asset Development may include:

- Character Asset Workflow
- Environment Asset Workflow
- Prop Asset Workflow
- FX Asset Workflow


Every required visual asset follows:

Asset Design

→ Image Prompt Generation

→ User Prompt Confirmation

→ Image Generation

→ User Image Confirmation

→ Asset Registry


The Prompt and Image confirmations are separate hard gates. A complete executable Image Prompt must be delivered before image generation; image generation is forbidden until the current Prompt Revision is confirmed. Generated images remain Candidate References until the user confirms them. Only then may the record use `Visual Production Status: Asset Confirmed`, Active Version and Canonical References.


If image generation is unavailable, preserve the complete Prompt and confirmation checkpoint and keep STATE-03 IN_PROGRESS; a text-only appearance description is not a completed visual asset.


The project does not need to create every possible asset type.


Only assets actually required by:

Script Analysis

and

Asset Discovery


need to be developed.


STATE-03 is complete when:

all required core assets are confirmed

or

a specific asset category has been explicitly determined unnecessary.


For a visual asset, “confirmed” means `Visual Production Status: Asset Confirmed` and `Status: Active`; `Prompt Draft`, `Prompt Confirmed` and `Image Generated` do not satisfy the completion gate.


FX Asset Workflow is auxiliary within STATE-03.


It does not create a new main STATE.


---

# Sequence Planning Rule


16_sequence_planning_workflow.md is a conditional auxiliary Workflow within STATE-05.


Use it for:

- long or multi-scene sequences
- dense narrative coverage
- montage, chase, battle, group or complex dialogue sequences
- multiple generation units
- continuation and retry boundaries


Simple scenes may mark Sequence Planning as Not Applicable with a reason.


Sequence Planning owns:

- SEQ IDs
- BEAT IDs
- COV IDs
- UNIT IDs


It does not own SHOT IDs, Detailed Shot Design fields, Clip Production fields or STATE-08 final fields.


STATE-06 maps formal SHOTs back to COV requirements.


Full interface contract:

references/module_contracts.md


---

# Poster Design Rule


17_poster_design_workflow.md is a conditional auxiliary Workflow within STATE-04.


Use it only when the user requests:

- movie poster
- key art
- one-sheet
- teaser / theatrical / character poster
- poster prompt or title treatment


It owns a separate poster design package through:

templates/15_poster_design_package.md


It does not create a main STATE, does not run for every project, and does not modify the STATE-08 Seedance Schema.


Poster ratios follow delivery channels; 9:16 is one option, not a universal default. Exact titles and legal copy use controlled editable typography layers rather than relying on image-generation text.


---

# Project Resume And Retry Rule

18_project_resume_workflow.md is an auxiliary Workflow for interrupted projects, Review return routes and controlled generation retries.

It reads references/project_state_contract.md and references/artifact_revision_contract.md, resumes only from a validated checkpoint, preserves accepted unaffected artifacts and never creates a new main STATE.

The second repeated failure requires Stable Downgrade. The third repeated failure returns to the fact or design owner instead of blind retry.

---

# Editing Workflow Rule


12_editing_workflow.md is not a fixed STATE in the main pipeline.


It is an auxiliary Workflow.


Use it when:

- user requests revision of an existing video result
- Review identifies a local execution problem
- motion needs adjustment
- camera needs adjustment
- visual details need adjustment
- local continuity needs correction


After Editing:

the result must return to:

STATE-09 Review.


Editing must not create:

STATE-10.


---

# Series Management Rule


14_series_management_workflow.md is an auxiliary management Workflow.


It does not replace:

the main production pipeline.


Each episode or production unit still follows:

STATE-00

↓

STATE-01

↓

STATE-02

↓

STATE-03

↓

STATE-04

↓

STATE-05

↓

STATE-06

↓

STATE-07

↓

STATE-08

↓

STATE-09


Series Management is responsible for:

cross-episode continuity

and

project-level organization.


---

# Module Responsibility


SD Film uses separate responsibility layers.


## Rules


rules/


Responsible for:

- production constraints
- pipeline boundaries
- consistency rules
- output restrictions
- forbidden behavior


Rules define:

what is allowed.


---

## Workflows


workflows/


Responsible for:

- stage execution
- production transformation
- state progression
- production decisions


Workflows define:

how work is performed.


---

## Knowledge


knowledge/


Responsible for:

- cinematic knowledge
- directing knowledge
- camera language
- visual style knowledge
- model adaptation
- continuity knowledge
- quality control


Knowledge improves:

production quality.


Knowledge does not define:

pipeline state.


Knowledge does not define:

final output Schema.


---

## Templates


templates/


Responsible for:

final stage output structure.


Templates define:

- field names
- field order
- numbering
- final layout


If a stage has a corresponding Template:

the final stage output should use that Template.


Templates must not:

bypass Workflow execution.


---

# Final Schema Ownership


Final output format belongs to:

the corresponding Template.


Rules:

define constraints.


Workflows:

prepare content.


Knowledge:

provides professional information.


Templates:

define final presentation structure.


For STATE-08 Clip-based Video Prompt / Video Generation:


the final Seedance output Schema is defined only by:

templates/10_video_prompt.md


Other modules must not create:

a competing Seedance final Schema.


---

# Knowledge System


SD Film uses external knowledge modules to enhance production quality.


Knowledge modules include:


## Director Knowledge


Purpose:

Convert directing concepts into executable film language.


Includes:

- directing principles
- visual storytelling
- performance direction
- cinematic rhythm


Relevant knowledge:

knowledge/01_director_principles.md


---

## Visual Asset Knowledge


Purpose:

Improve visual asset design.


Includes:

- visual identity
- asset clarity
- production usability
- visual consistency


Relevant knowledge:

knowledge/02_visual_asset_design.md


---

## Character Consistency Knowledge


Purpose:

Maintain character identity across production stages.


Includes:

- appearance consistency
- costume consistency
- facial identity
- character state
- visual continuity


Relevant knowledge:

knowledge/03_character_consistency.md


---

## Scene Design Knowledge


Purpose:

Improve environment and scene construction.


Includes:

- location design
- architecture
- atmosphere
- spatial relationships
- visual hierarchy


Relevant knowledge:

knowledge/04_scene_design_rules.md


---

## Camera Language Knowledge


Purpose:

Convert narrative purpose into camera execution.


Includes:

- shot size
- focal tendency
- camera movement
- camera position
- spatial relationship
- visual emphasis


Canonical Camera Knowledge Router:

knowledge/camera_language/index.md

Legacy overview `knowledge/05_camera_language.md` is only a compatibility pointer.


Extended Camera Language Library:

knowledge/camera_language/


Current structure includes:

knowledge/camera_language/index.md

knowledge/camera_language/camera_movement/

knowledge/camera_language/camera_angle/

knowledge/camera_language/composition_language/

knowledge/camera_language/perspective_language/

knowledge/camera_language/lens_language/

knowledge/camera_language/temporal_language/

knowledge/camera_language/editing_language/

knowledge/camera_language/lighting_camera/

knowledge/camera_language/advanced_camera_movement/

knowledge/camera_language/source_coverage.md


Camera Language should be selected according to:

story function

character emotion

spatial relationship

shot purpose.


Do not use complex camera movement only to make a shot feel cinematic.


---

## Clip Production Knowledge


Purpose:

Organize Confirmed Detailed Shot Design into 4—15 second CLIP execution units while preserving shot order, start/end state, continuous action, camera/spatial relationships, prop continuity and model feasibility.


Relevant knowledge:

knowledge/clip_planning/


---

## Prompt Engineering Knowledge


Purpose:

Improve AI-generation instruction clarity.


Relevant knowledge:

knowledge/07_prompt_engineering.md


Prompt Engineering is:

an execution layer.


It does not replace:

the production pipeline.


---

## Model Adapter Knowledge


Purpose:

adapt cinematic information for AI generation models.


Relevant knowledge:

knowledge/08_model_adapter.md


---

## Continuity Knowledge


Purpose:

maintain continuity across shots.


Includes:

- character continuity
- environment continuity
- prop continuity
- spatial continuity
- motion continuity
- emotional continuity


Relevant knowledge:

knowledge/09_continuity_management.md


---

## Quality Control Knowledge


Purpose:

support final production review.


Canonical quality routing:

knowledge/quality/index.md

Legacy overview `knowledge/10_quality_control.md` is only a compatibility pointer.


---

## Seedance Adapter Knowledge


Purpose:

convert cinematic execution information into a form that Seedance can understand reliably.


Relevant knowledge:

knowledge/11_seedance_adapter.md


Its internal dimensions may include:

- Scene
- Character
- Action
- Composition
- Camera
- Lighting
- Sound
- Editing


These are:

internal analysis dimensions.


They are not:

final output field names.


STATE-08 final output structure must still follow:

templates/10_video_prompt.md


---

# Sequence And Coverage Knowledge

Purpose:

Organize long scenes and connected story segments into narrative beats, coverage requirements, generation units and cross-unit state contracts.

Relevant knowledge:

knowledge/sequence/

Formal planning uses:

workflows/16_sequence_planning_workflow.md

templates/14_sequence_plan.md


Sequence knowledge supports STATE-05 through STATE-09.


It cannot create formal SHOT IDs or define STATE-08 final fields.


---

# Legacy Clip Planning Compatibility

Purpose:

Legacy project migration only. New projects perform this responsibility inside STATE-07 Clip Production.

Relevant knowledge:

knowledge/clip_planning/

Formal planning uses:

workflows/10_clip_production_workflow.md

templates/20_clip_plan.md

CLIP IDs define generation batches, not new story or shot facts. STATE-08 final fields remain owned by templates/10_video_prompt.md.

---

# FX Knowledge

Purpose:

Design executable physical, atmospheric, destructive and transformational effects while preserving their consequences across shots.

Relevant knowledge:

knowledge/fx/

Formal FX assets use:

workflows/15_fx_asset_workflow.md

templates/13_fx_asset_prompt.md


---

# Performance Knowledge

Purpose:

Translate emotion and dialogue intention into observable acting beats, micro-expression, listening behavior and multi-character reactions.

Relevant knowledge:

knowledge/performance/

Primarily used by STATE-04, STATE-06, STATE-07 and STATE-08.


---

# Sound Language Knowledge

Purpose:

Design dialogue, ambience, Foley, silence and sound continuity for production; keep music planning isolated to Editing/Post.

Relevant knowledge:

knowledge/sound_language/

Dialogue, ambience, Foley and continuity are used by STATE-04, STATE-06, STATE-07 and STATE-08. Music knowledge is used by STATE-09 Editing/Post and must not enter STATE-08 audio fields.


---

# Transition Knowledge

Purpose:

Classify shot boundaries, select one primary transition, and design outgoing/cut/incoming anchors without changing story or assets.

Relevant knowledge:

knowledge/transitions/

Used by STATE-06, STATE-07, STATE-08 and STATE-09. It projects into existing boundary fields and never creates a new STATE-08 schema field.


FX, Performance and Sound knowledge are internal production resources.

They do not define the final STATE-08 Prompt Schema.


---

# Visual Style Knowledge


Purpose:

Extend cinematic visual style capabilities.


Visual Style Knowledge handles:

- Director visual aesthetics
- Film style references
- Cinematography style
- Lighting systems
- Color systems
- Composition tendencies
- Emotional visual language


Location:

knowledge/visual_styles/


Current structure:


```text
knowledge/visual_styles/

├── index.md
│
└── directors/
    ├── 01_wong_kar_wai.md
    ├── 02_iwai_shunji.md
    ├── 03_denis_villeneuve.md
    ├── 04_christopher_nolan.md
    ├── 05_akira_kurosawa.md
    ├── 06_steven_spielberg.md
    ├── 07_david_fincher.md
    ├── 08_stanley_kubrick.md
    ├── 09_zhang_yimou.md
    └── 10_bong_joon_ho.md
```


Visual Style Knowledge is expandable.


New style files may be added when needed.


Do not reference:

directories or knowledge modules that do not currently exist.


---

# Visual Style Loading Rules


Visual Style Knowledge should be activated when the user requests:

- Director style reference
- Film style reference
- Cinematic feeling
- Specific photography style
- Genre visual direction
- Specific visual atmosphere


Examples:

“Create a Wong Kar Wai style urban night scene.”

“Use Iwai Shunji-like youth-film atmosphere.”

“Use Kurosawa-inspired historical spatial composition.”


The system should retrieve:

only the relevant visual style knowledge.


Do not load every director style file without reason.


---

# Visual Development Ownership


Formal Visual Style decisions belong primarily to:

STATE-04 Visual Development.


STATE-04 establishes:

Visual Direction.


Later stages:

STATE-05 Scene Breakdown

STATE-06 Detailed Shot Design

STATE-07 Clip Production

STATE-08 Clip-based Video Prompt / Video Generation


should inherit:

the confirmed Visual Direction.


Do not randomly select a new visual style in each later stage.


---

# Visual Style Translation Rules


Director names and film references are:

retrieval labels.


They should not be the only final visual instruction.


The system must translate style references into executable cinematic language.


Translation dimensions:


## Camera Language


Including:

- Lens tendency
- Camera movement
- Camera distance
- Shooting method
- Camera stability
- Depth of field tendency


---

## Lighting Language


Including:

- Light source
- Light direction
- Contrast
- Shadow
- Color temperature
- Environmental reflection
- Atmosphere


---

## Color Language


Including:

- Main color direction
- Supporting color direction
- Saturation
- Contrast
- Warm / cool relationship
- Grading tendency


---

## Composition Language


Including:

- Framing
- Spatial relationship
- Character placement
- Foreground
- Background
- Visual focus
- Negative space


---

## Emotional Language


Including:

- Mood
- Rhythm
- Performance scale
- Camera observation distance
- Audience feeling


Final production language should describe:

executable filmmaking characteristics.


Do not rely only on:

style names.


---

# Knowledge Priority


Knowledge priority applies only within:

the current valid production stage.


It does not override:

Rules

or

Pipeline.


Within the current stage:

information priority is:


Explicit User Requirements

>

Confirmed Project Information

>

Confirmed Assets

>

Confirmed Visual Direction

>

Relevant Specific Knowledge

>

General Cinematic Knowledge


Important:


User Requirements may define:

creative intent.


They may not automatically override:

pipeline order

confirmed asset identity

continuity rules

or

stage boundaries.


---

# Confirmed Asset Priority


When visual assets are already confirmed:


Character Asset

Environment Asset

Prop Asset


have priority over:

temporary text descriptions.


Knowledge modules may:

help interpret those assets.


Knowledge modules may not:

silently redesign them.


---

# Style Combination Rules


Multiple visual references can be combined when:

the user explicitly requests a hybrid visual direction.


Example:


Urban emotional photography

+

poetic youth-film emotional atmosphere


should become:

a unified visual system.


The system should translate the references into:

camera language

+

lighting

+

color

+

composition

+

performance

+

rhythm


Do not simply concatenate:

style names.


---

# Style Conflict Rule


When multiple visual references conflict:


prioritize:

current story function

↓

confirmed environment

↓

confirmed character assets

↓

confirmed project Visual Direction


Then:

create one coherent visual system.


Do not preserve contradictory style traits merely because they were present in different references.


---

# Unknown Style Handling


When the user provides an unknown visual reference:


analyze only the information that can actually be supported.


Possible dimensions:

- Visual characteristics
- Cinematography
- Lighting
- Color
- Composition
- Emotional direction


Do not:

invent unsupported details.


Do not:

pretend that an unavailable knowledge file exists.


---

# Output Language Rules


Default output language:

Chinese.


Professional filmmaking terminology may remain in English where useful.


Examples:

Close-Up

Dolly In

Tracking Shot

Rack Focus

Long Take


All generated cinematic instructions should prioritize:

- clear visual description
- professional filmmaking logic
- spatial clarity
- temporal clarity
- asset consistency
- AI video generation compatibility


---

# Prompt Principle


Prompt generation is:

a downstream production action.


Prompt is not:

the starting point of SD Film.


Character Prompt:

belongs to Character Asset Development.


Environment Prompt:

belongs to Environment Asset Development.


Detailed Shot Design:

belongs to STATE-06 and feeds STATE-07 Clip Production directly.

Storyboard:

is an Optional/Auxiliary Workflow invoked only when explicitly requested; it owns no STATE and is never a STATE-08 reference asset.

Clip Production:

belongs to STATE-07 and produces the Confirmed Clip Production Plan. Shot is the directing unit; Clip is the AI generation unit; STATE-08 compiles one continuous Prompt per Clip.


Video Prompt:

belongs to Video Generation.


Seedance Prompt:

belongs to STATE-08.


The user mentioning the name of a Prompt:

does not automatically authorize execution of that later stage.


## STATE-08 No-Timeline Output


The final Seedance prompt uses shot numbers only.


Do not include timecodes, timestamps, total duration, per-shot duration, second-by-second action ranges, frame ranges, or frame-rate constraints in the prompt body.


Timing information from upstream production remains internal for action-density and executability checks.


If the generation surface requires duration, frame count, or frame rate, treat it as a platform parameter outside the prompt.


---

# Continuity Principle


Every production stage must preserve:

Character Continuity

Environment Continuity

Prop Continuity

Spatial Continuity

Motion Continuity

Emotional Continuity

Visual Style Continuity


Later stages may:

add execution detail.


They may not:

silently replace confirmed upstream information.


From STATE-06 onward, every shot-level deliverable must preserve three boundary semantics:

- the source of the shot's start state
- a stable and verifiable end-frame constraint
- the handoff to the next shot, or the reason direct inheritance is not possible


The current stage Template owns the final field names and order.


Boundary behavior and transition classification are defined by:

rules/04_consistency_rules.md


Continuous shots inherit valid prior state.


Confirmed scene changes, time jumps, hard cuts, montage, flashbacks, and intentional jump cuts must be represented as motivated discontinuities rather than fabricated transition actions.


Automatic handoff logic may not change story facts, asset identity, character blocking, prop state, or execute the next shot's action early.


---

# Revision Principle


When the user requests a correction:

use the minimum necessary revision.


Example:


If the problem is:

characters are facing the camera instead of each other.


Modify:

spatial relationship

camera placement

body orientation

eyeline


Do not automatically:

redesign the character

rewrite the scene

rebuild the whole project.


---

# Expansion Principle


SD Film supports continuous expansion.


Before adding or changing a module:

read and follow:

references/module_contracts.md


Every module must declare its trigger, position, input owner, output owner, allowed writes, downstream consumers, forbidden authority and deterministic invariants.


New knowledge modules should extend:

existing capabilities.


Prefer:

knowledge expansion

over

unnecessary structural modification.


Do not modify:

- Pipeline structure
- Existing Rules
- Workflow responsibilities
- Prompt Templates


unless:

a verified structural conflict or production problem requires the change.


New knowledge should:

fit the current system architecture.


It should not:

create duplicate authority.


---

# Configuration Final Principle


SD Film configuration establishes:

system-wide production behavior.


The main pipeline is:

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


The user's final request:

does not override the production pipeline.


Before workflow routing:

select State Source using `readable, Project-ID-matched Active Project Root/project_status.md > portable_project_status.md > verified current Project Context normalized into Portable State > initialize STATE-00 only when no project evidence exists`.


Rules define constraints.

Workflows define execution.

Knowledge provides professional support.

Templates define final output Schema.


For STATE-08 Seedance output:

templates/10_video_prompt.md

is the single final Schema source.
