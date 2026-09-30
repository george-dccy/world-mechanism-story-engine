# 世界机制故事引擎 · World Mechanism Story Engine

> 借助模型加深人的思考与对世界的理解，再把这种理解编译成孩子和朋友愿意看、愿意读、愿意继续想的作品。

这个项目不是“一句话生成视频”的流水线，也不是一个固定的科普 Skill。它把人的问题意识、判断、好奇心和设计放在最上层，把模型作为研究、推演、创作与生产的放大器。

## 核心链路

```text
Question
  ↓
Mechanism Explorer
  ↓
Research / Evidence
  ↓
Creative Hypothesis
  ↓
Creative Blueprint
  ↓
Story / Essay / Explanation
  ↓
Expression Router
  ↓
Video / Article / Comic / Talk / Other
  ↓
Production + QA
  ↓
Retrospective
  ↺ 回到问题与机制
```

**先理解，再表达；先设计，再生产。**

## 两个核心资产

### Mechanism Explorer
不急着回答“这个题怎么做成内容”，而是持续追问表面现象背后的机制、力量、约束、反馈和反事实。

### Creative Blueprint
所有表达形式共享的“源代码”。一个成熟 Blueprint 应能被编译成视频、公众号文章、漫画、演讲、亲子讨论或其他作品，而不被某个媒介反向绑架。

## 仓库分工
- `docs/`：项目哲学、架构、边界和人机协作方式
- `engine/`：机制探索、Creative Blueprint、故事、研究、质量评审
- `schemas/`：核心中间产物的机器可读结构
- `renderers/`：表达编译器，而非内容核心
- `skills/`：未来可执行 Agent / Skill
- `tests/golden-cases/`：保护创作味道与核心原则的黄金案例
- `references/`：外部工程参考及吸收边界

## v0.1 边界
1. 科学是重要来源域，但不是项目边界。
2. 技术、历史、文化、社会机制和有长期解释价值的当代现象都可以进入。
3. 热点只是入口，机制才是主角。
4. 固定爆款模板不是默认叙事结构。
5. Renderer 不能反向决定题材与思想。
6. AI 可以提出候选、证据和推演，但关键取舍必须保留人的判断。
7. 事实表达必须区分：已核验事实 / 解释 / 假设 / 寓言规则。

详见 [PROJECT.md](PROJECT.md) 与 [docs/architecture.md](docs/architecture.md)。
