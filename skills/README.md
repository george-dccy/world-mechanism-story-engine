# Skills Roadmap

## 已实现

### wm-mechanism-explorer — v0.2
认知层入口 Skill。

负责：
- operationalize 模糊问题；
- 建 Question Ladder；
- 生成 competing mechanism candidates；
- 区分 F / I / H / R；
- 建 Mechanism Map；
- 用 consequence ladder 或 branching scenarios 做反事实；
- 在生产前停止，把关键判断交还给作者。

### wm-research-agent — v0.1
证据层 Skill。

两种模式：
- **Pass A｜Premise Check**：创意承诺前纠正前提、术语、日期和范围；
- **Pass B｜Evidence Pack**：Blueprint 形成后建立 claim ledger、source ledger、Do Not Strengthen 与生产证据。

### wm-creative-director — v0.1
创意方向 Skill。

H01 / S01 人工反馈后新增，专门解决：
- 正确但普通；
- 美国案例默认化；
- 历史题自动历史剧化；
- 所有题都被强迫故事化。

核心方法：
- China-first, World-second；
- First Association Test；
- Truth Surprise；
- Audience Distance；
- Form Fit；
- Author Fit；
- KEEP / HOLD / REJECT。

## 下一批

1. wm-story-builder
2. wm-expression-router
3. wm-reviewer

原则：
- 每个 Skill 有明确输入输出；
- 关键 Gate 不隐式通过；
- Skill 可替换，schema 和 Golden Cases 尽量稳定；
- 先让方法变好，再让流程变快。
