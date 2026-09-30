# Architecture v0.1

## 1. 总原则
> **理解层独立于表达层，表达层独立于生产工具。**

不能让“今天哪个模型最强”“某种画风正火”反向决定我们思考什么、怎么理解、讲什么。

## 2. 核心不是直线，而是双入口回路

### Route A — Question-first
真实困惑 → Mechanism Explorer → Creative Exploration

### Route B — Spark-first
有生命力的母题 → Creative Exploration → Mechanism Explorer

两条路线都必须经过：
**Mechanism ↔ Creative Exploration → Editorial Gate → Creative Blueprint**

为什么这样设计：
- 好问题需要创意把机制变成可感受的世界；
- 好母题也需要机制探索避免沦为漂亮空壳；
- 不把“母题先于机制”和“理解世界是核心”做成二选一。

## 3. 六层架构

### Layer A — Capture
输入可能是：
- 真实问题；
- 观察；
- 新闻；
- 历史细节；
- 知识点；
- 一个突然出现的世界规则或关系母题。

产物：`Question Seed` 或 `Creative Seed`。

### Layer B — Mechanism
拆 actors、forces、constraints、incentives、flows、feedback loops、thresholds、time scale、information asymmetry、path dependence。

产物：`Mechanism Map`。

### Layer C — Creative Exploration
发散母题、反事实和人物行为，检查同一规则是否能持续产生状态变化。

产物：`Creative Candidates`。

### Layer D — Editorial + Blueprint
总编辑负责淘汰与保真；Creative Blueprint 把问题、机制、规则、人物任务、知识载荷与 Must Preserve 锁为跨媒介接口。

产物：`Creative Blueprint`。

### Layer E — Research + Content Master
查事实、原始资料、历史脉络与争议边界，把 Fact / Interpretation / Hypothesis / Fictional Rule 分开，再形成媒介无关的故事或内容母版。

产物：`Evidence Pack` + `Content Master`。

### Layer F — Renderer / Production
编译为 story-film、minimal-line、whiteboard、archive、evidence+MG、article、comic、talk 或 hybrid。

产物：`Production Package`。

## 4. 人工 Gate
1. **Question / Mechanism Gate**：这真是我想弄明白的问题吗？这轮探索让我多理解了一层吗？
2. **Creative Gate**：去掉寓意和知识点，这个母题本身还值得看吗？
3. **Blueprint Gate**：核心问题、机制、世界规则、人物任务、知识载荷与 Must Preserve 是否已人工确认？
4. **Release Gate**：最终作品是否忠于 Blueprint，没有被生产便利性带偏？

生产层可以高度自动化，Gate 不默认自动通过。

## 5. Notion 与 GitHub

### GitHub：系统真源
保存稳定、可版本化、可测试的能力：
- engine
- schemas
- skills
- renderer contracts
- golden cases
- regression checks
- architecture decisions

### Notion：创作者驾驶舱
保存活的、尚在形成中的内容：
- 问题火花
- 阅读与观察
- 选题池
- 项目状态
- 临时研究材料
- Blueprint 工作稿
- 作品链接
- 个人复盘

原则：**Notion 不复制全部规则；GitHub 不吞掉人的思考轨迹。**

## 6. 核心中间语言
Creative Blueprint 是跨媒介稳定接口。

只要 Blueprint 仍成立，Renderer 可以随技术变化替换。
