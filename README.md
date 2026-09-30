# 世界机制故事引擎 · World Mechanism Story Engine

> 借助模型加深人的思考与对世界的理解，再把这种理解编译成孩子和朋友愿意看、愿意读、愿意继续想的作品。

这个项目不是“一句话生成视频”的流水线，也不是一个固定的科普 Skill。它把人的问题意识、判断、好奇心和设计放在最上层，把模型作为研究、推演、创作与生产的放大器。

## 两种入口，一条主线

系统允许两种合法起点：

### Question-first
真实困惑 → Mechanism Explorer → 创意发散

### Spark-first
有生命力的母题 → 创意发散 → Mechanism Explorer

两条路会汇合到：

Mechanism ↔ Creative Exploration  
→ Editorial Gate  
→ Creative Blueprint  
→ Research Pass B / Evidence Pack  
→ Story / Essay / Explanation  
→ Expression Router  
→ Video / Article / Comic / Talk / Other  
→ Production + QA  
→ Retrospective

事实依赖题在 Mechanism Explorer 前后可触发 **Research Pass A｜Premise Check**。

**先理解，再表达；先设计，再生产。**

## 为什么允许双入口

不是所有好内容都从“研究问题”开始。有时先出现的是一个本身就有生命的怪事、人物关系或世界规则。

因此：
- 不能让机制分析扼杀第一闪念；
- 也不能让一个漂亮母题绕过理解世界这一层。

Mechanism Explorer 与 Creative Exploration 是一个可往返的核心回路，而不是僵硬的单向流水线。

## 当前两个核心 Skill

### wm-mechanism-explorer
把“我觉得这里有点奇怪”推进成 Mechanism Map。它负责 operationalize、 competing mechanisms、F/I/H/R、反事实与 Creator Gate。

### wm-research-agent
把研究拆成两次：
- Pass A：创意前纠错；
- Pass B：Blueprint 后建证据包。

研究的目的不是给稿子贴引用，而是**修正现实模型并限制我们能说多强**。

## Creative Blueprint

所有表达形式共享的“源代码”。一个成熟 Blueprint 应能被编译成视频、公众号文章、漫画、演讲、亲子讨论或其他作品，而不被某个媒介反向绑架。

## 仓库分工
- docs/：项目哲学、架构、边界、人机协作与实跑复盘
- engine/：机制探索、Creative Blueprint、故事、研究、质量评审
- schemas/：Blueprint / Evidence Pack 等机器可读接口
- examples/：真实 Blueprint 与 Evidence Pack 样例
- runs/：具体案例的真实运行记录
- renderers/：表达编译器，而非内容核心
- skills/：可执行的人机协作单元
- tests/golden-cases/：保护创作味道与核心原则
- references/：外部工程参考及吸收边界

## v0.1 三案例基线
- A08：科学 / 寓言 / 关系型
- H01：历史 / 技术 / 制度型
- S01：当代社会 / 多方激励 / 非故事型

H01 和 S01 当前仍是 Golden Candidate，只有在真实作品完成并经过人工复盘后才升级。

## 不变边界
1. 科学是重要来源域，但不是项目边界。
2. 热点只是入口，机制才是主角。
3. 固定爆款模板不是默认叙事结构。
4. Renderer 不能反向决定题材与思想。
5. AI 可以提出候选、证据和推演，但关键取舍保留人的判断。
6. 事实表达必须区分 F / I / H / R。
7. CI 只能证明结构没坏，不能证明创意已被批准。

详见 PROJECT.md、docs/architecture.md 与 docs/workflow.md。
