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

H01 / S01 实跑后新增：
- Core / Supporting / Consequence 分层；
- 社会题先定义实验边界；
- 高不确定系统使用分支推演。

### wm-research-agent — v0.1
证据层 Skill。

只有两种模式：
- **Pass A｜Premise Check**：创意承诺前，纠正前提、术语、日期和范围；
- **Pass B｜Evidence Pack**：Blueprint 形成后，建立 claim ledger、source ledger、Do Not Strengthen 与生产证据。

它不写最终文章、脚本或故事。

## 下一批

1. wm-creative-director
2. wm-story-builder
3. wm-expression-router
4. wm-reviewer

原则：
- 每个 Skill 有明确输入输出；
- 关键 Gate 不隐式通过；
- Skill 可替换，schema 和 Golden Cases 尽量稳定；
- 先让方法变好，再让流程变快。
