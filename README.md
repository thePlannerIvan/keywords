# Keywords：领域杠杆词图谱与工具清单

将未知或复杂专业领域的概念体系，沉淀为一份**直观、可溯源、开箱即取的领域杠杆词图谱（Leverage Words Atlas）与可调度工具清单**。

作者：阿祖不看 TVC  ·  小红书同名账号  ·  [demyth.info](https://demyth.info)  ·  `Lawyif@163.com`

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue.svg)](LICENSE)

---

## 为什么需要 Keywords？底层理论与认知痛点

### 1. 语言的边界即认知的边界
在用 AI 探索或创作某个未知领域时，新手与高手的差距并不在于打字速度或 Prompt 的长短，而在于**领域核心概念的贫瘠与丰饶**：
* **新手**只能用漫无边际的日常大白话勉强描述：“做一个酷炫的网页，有很多圆角小方块，黑色边框粗一点，黄色背景...”；
* **专家**只需给出一个精准的概念术语：“`Neobrutalism`” 或 “`Bento Grid`”。

> *"Die Grenzen meiner Sprache bedeuten die Grenzen meiner Welt"*  
> —— 我的语言的界限意味着我的世界的界限（维特根斯坦，Ludwig Wittgenstein）

人类无法清晰思考自己未曾命名的概念，更无法要求 AI 精确生成自己说不出来的东西。

### 2. 大模型潜在空间的流形采样机制
大语言模型（LLM）不是死板的字面打字机，而是高维潜在空间的流形采样器：
* **漫散射与均值坍缩（Regression to the Mean）**：用模糊日常口语描述需求时，注意力向量在潜在空间中过度弥散，最终退化为全网统计概率的平庸均值（俗称 "AI Slop"）。
* **杠杆词的强引导向量（Steering Vectors & Anchor Tokens）**：行业权威术语是大模型潜在空间中的高密度致密锚点。一个精准的杠杆词，能让多层自注意力机制瞬间收敛到该领域专家语料的优质几何流形上。

### 3. 什么是「杠杆词（Leverage Word）」？
普通词汇只是描述标签，**杠杆词是高密度的控制手柄**。
只有当一个词能切实改变人类的观察分辨能力、决策动作、或促使 AI 生成完全不同的结果时，它才被称为杠杆词。

**黄金调度公式**：
$$\text{专业调度指令} = \text{核心杠杆词 (Anchor)} + \text{2~3 个不可妥协的属性槽位 (Canonical Constraints)}$$

---

## 双重前置工具与证据地基（严禁空想造词）

本 Skill 严禁跳步臆造。构建任何领域的图谱前，强制顺序执行双前置探索：

1. **迷雾导航 (`/wayfinder`)**：
   探明领域骨架、梳理认知边界、辨析主要流派与核心决策分歧，将开放式的学科迷雾收敛为 **3~5 个互斥且支撑决策的主分支（Branches）**。
2. **一手调研 (`/research`)**：
   深入行业奠基著作（如设计学派 Nancy Duarte、Edward Tufte；排版学派 Robin Williams 等）、业界标杆工程与权威规范。每一个名词必须外部锚定，中英名成对出自权威一手来源，杜绝凭空造词。

> **前置依赖与出处**：`wayfinder` 与 `research` 是外部 Skill，**不随本仓库分发**。二者来自 [Matt Pocock 的开源 Skill 集](https://github.com/mattpocock/skills)（MIT，Copyright (c) 2026 Matt Pocock）；本仓库只调用它们，不包含其任何内容。环境里没有这两个 Skill 时，用等价的领域建图与一手取证流程完成同样两步再进入图谱构建——**可以换实现，不许跳过**。

---

## 可视化呈现哲学：360px 基准视口与比例自适应

**核心契约：以 360px 宽度作为微视口设计基准（Base Viewport），容器 100% 弹性填充，高度自然自洽撑开。**

1. **告别蚂蚁字**：大模型若无尺度基准，极易画出 1200px+ 复合大海报，塞进侧栏抽屉后文字被等比压缩成 3px 无法阅读。锚定 360px 宽度基准可确保字阶在移动端与抽屉中始终处于舒适阅读区间（标题 `12~14px`，正文 `10~12px`）。
2. **单节点聚焦（Single Concept Micro-Card）**：每个可视化必须是专门为当前单一概念设计的独立微型卡片，禁止跨概念拼接多合一大海报。
3. **比例驱动自适应**：
   * 横向对比 / 视频动效 / 双向对照：**16:9**（`viewBox="0 0 360 200"`）
   * 架构拓扑 / 网格系统 / 卡片组件：**1:1** 或 **4:3**（`viewBox="0 0 360 360"` / `viewBox="0 0 360 270"`）
   * 移动端界面 / 垂直动线 / 状态流：**9:16** 或纵向自适应卡片

---

## 标准工作流

```text
1. 迷雾导航 (Wayfinder 强制) 
   -> 2. 一手调研 (Research 强制) 
   -> 3. 提炼杠杆词与槽位 
   -> 4. 装配 360px 单体微卡片 
   -> 5. 编译交付双视图
```

---

## 交付产物与目录契约

生成的领域图谱目录结构：
```text
<atlas-folder>/
├── index.md              # 纯文本结构化索引，供人浏览或被 Agent grep 快速检索
├── media/                # 单节点独立可视化微卡片库（SVG / 动效）
│   ├── cue-concept-a.svg # 概念 A 单体演示 (如 16:9 360x200)
│   └── cue-concept-b.svg # 概念 B 单体演示 (如 9:16 360x380)
├── atlas.json            # 结构化数据源契约（branches, nodes, cues, distinctions, prompt, examples）
└── viewer.html           # 编译生成的单文件交互式思维导图（带 Inspector 属性抽屉）
```

---

## 内置 CLI 工具箱

无需从头手写前端，本 Skill 内置完整的确定性工程工具：

1. **轻量数据契约校验**：
   ```bash
   python3 scripts/validate_atlas.py <path/to/atlas.json>
   ```
   *检查 JSON 结构完整性、ID 唯一性、必要字段与依赖关系。*

2. **一键编译交互式思维导图**：
   ```bash
   python3 scripts/build_viewer.py <path/to/atlas.json> --output <path/to/viewer.html>
   ```
   *将数据注入单文件 Web 视图，集成可视化思维导图、全键盘快捷键导航与一键 Prompt 复制。*

---

## 安装与使用

### 安装至各 Agent Runtime

推荐用 skills CLI 安装：

```bash
npx skills add https://github.com/thePlannerIvan/keywords --skill keywords
```

也可以克隆到支持 Skill 的 Agent 目录（以下为 Claude Code）：

```bash
git clone https://github.com/thePlannerIvan/keywords.git ~/.claude/skills/keywords
```

两个脚本只用 `python3` 标准库，无需安装依赖。`build_viewer.py` 会把 DSH 设计令牌内联进页面（模板里有 267 处 `var(--dsw-*)` 引用，缺了整页会走形），所以令牌表随本仓库发了一份字节级镜像 `assets/dsh-tokens.css` —— **单独克隆就能出图，不需要额外安装 `planners-review-core`**。

镜像的上游是 `planners-review-core/assets/dsh-tokens.css`（抽自 DSH 发行版 0.2.0-rc.2，MIT，许可见 [assets/dsh-tokens.LICENSE.txt](assets/dsh-tokens.LICENSE.txt)）。构建时会打印实际用的是哪一份；两份同时存在且内容不一致时，会直接告警提醒同步：

```bash
# 在 monorepo 内重新同步镜像（上游重跑 vendor_dsh_tokens.py 之后也要跑一次）
cp 00-system/planners-review-core/assets/dsh-tokens.{css,LICENSE.txt} \
   06-agent-productivity/keywords/assets/
```

`validate_atlas.py` 不依赖令牌表，可完全独立运行。

### 典型调用指令

```text
我想系统了解一下「网页动效设计与微交互（Micro-interactions）」。
请用 /keywords 为我构建一份包含核心流派、经典术语与控制手柄的杠杆词图谱。
```

---

## 仓库结构

```text
keywords/
├── SKILL.md                # 核心执行规范与工作流契约
├── GOTCHAS.md              # 踩坑记录与反模式候选池
├── README.md               # 本说明文档
├── LICENSE                 # AGPL-3.0 许可文本
├── NOTICE                  # 作者与来源归属
├── TRADEMARK.md            # 名称使用边界
├── COMMERCIAL.md           # 合作与授权入口
├── THIRD_PARTY_NOTICES.md  # 第三方组件与许可（DSH 设计令牌，MIT）
├── .gitignore              # 缓存、环境与产物忽略规则
├── agents/
│   └── openai.yaml         # Agent 界面元数据声明
├── assets/
│   ├── keywords-viewer.html # 离线单文件思维导图骨架模板
│   ├── dsh-tokens.css      # DSH 设计令牌镜像（勿手改，来自 planners-review-core）
│   └── dsh-tokens.LICENSE.txt # 上述令牌的 MIT 许可全文
├── evals/
│   ├── evals.json          # 评测用例集
│   └── fixtures/           # 样例数据（如 Bento Grid 图谱）
├── references/             # 领域知识体系与架构文档
│   ├── architecture.md     # 模块所有权与系统接缝
│   ├── leverage-words.md   # 杠杆词提炼与晋升准则
│   ├── knowledge-graph.md  # 知识图谱结构规范
│   ├── presentation.md     # 360px 视口与可视化规范
│   └── maintenance-history.md # 维护历史记录
└── scripts/                # 确定性工具箱
    ├── validate_atlas.py   # 数据契约校验器
    └── build_viewer.py     # 单文件交互页面编译器
```

---

## 开源与归属

许可文本见 [LICENSE](LICENSE)（AGPL-3.0，允许商业使用；修改版与网络服务需公开对应源码）。作者和来源见 [NOTICE](NOTICE)，名称使用边界见 [TRADEMARK.md](TRADEMARK.md)，合作与授权入口见 [COMMERCIAL.md](COMMERCIAL.md)，随仓库分发的第三方内容（DSH 设计令牌，MIT / DeepSeek）见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

署名用于仓库文档与工作过程页面；生成的图谱、`viewer.html` 等交付物默认不带项目品牌信息，除非使用者明确要求。
