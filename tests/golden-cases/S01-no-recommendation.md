# Golden Candidate S01 — 如果推荐算法消失七天

**类型**：当代社会 / 技术  
**状态**：Golden Candidate，尚未人工锁定  
**主要测试**：现代系统 → 多方激励 → 非二元结论

## Starting Point

常见直觉是：

> “如果平台取消推荐算法，互联网是不是就更真实、更自由？”

这个问法已经偷偷假定：**没有个性化推荐，就等于没有人在分配注意力。**

Mechanism Explorer 必须先挑战这个前提。

## Evidence Ledger

### F — Facts

- Netflix 将推荐与搜索描述为其帮助用户在大规模内容库中找到内容的核心能力。
- Google Drive 的 Quick Access 是一个个性化推荐实例；Google Research 报告称，在这一具体产品场景中，它把用户寻找文件所花的时间降低了约一半。
- Google Research 对推荐生态的研究指出，现代推荐系统会把用户、内容提供者、广告商等多个参与者的行为和激励耦合在一起，因此不能只把推荐看成单次“给某用户排列表”。
- 推荐研究同时关注 accuracy、diversity、novelty、serendipity 等不同目标，说明“最相关”并不是唯一可优化的维度。

### Sources

- Netflix Research — Recommendations: https://research.netflix.com/research-area/recommendations
- Google Research — Improving Recommendation Quality at Google Drive: https://research.google/pubs/improving-recommendation-quality-at-google-drive/
- Google Research — Modeling Recommender Ecosystems: https://research.google/pubs/modeling-recommender-ecosystems-research-challenges-at-the-intersection-of-mechanism-design-reinforcement-learning-and-generative-models/
- Google Research — Values of Exploration in Recommender Systems: https://research.google/pubs/values-of-exploration-in-recommender-systems/
- Google Research — Expediting exploration for cold-start recommendations: https://research.google/pubs/expediting-exploration-by-attribute-to-feature-mapping-for-cold-start-recommendations/

### I — Interpretation

- 在内容供给远超人类注意力的环境里，“什么先被看见”一定需要某种分配规则。
- 个性化推荐只是其中一种规则。取消它以后，注意力仍可能由发布时间、订阅关系、搜索能力、热门榜、外部社交传播、编辑精选或付费推广等机制分配。
- 因此“没有推荐”不是“没有选择机制”，而是**选择机制发生迁移**。

### H — Hypotheses

如果大型内容平台七天内禁止个性化预测排序，但保留搜索、订阅和按时间排序：
- 老用户可能更依赖已关注账号与主动搜索；
- 创作者可能更重视外部导流、标题和发布时间；
- 新内容发现可能更多依赖编辑、热门榜或社交扩散；
- 一部分用户可能感到更可控，另一部分用户可能感到搜索成本上升。

这些都是需要实验或数据支持的推演，不能当成既定事实。

## One-sentence Mechanism

> **当内容极度过剩而注意力稀缺时，平台必须用某种规则分配“先被谁看见”；取消个性化推荐不会消除分配，只会把权力和成本转移到别的筛选机制。**

## Mechanism Map

### Actors
- 用户：希望快速找到感兴趣内容，同时保留探索和控制感；
- 创作者：争取曝光并适应平台分配规则；
- 平台：在体验、留存、商业目标、生态健康之间取舍；
- 广告主 / 商家：争夺可见性；
- 编辑、社交网络、搜索引擎：可能成为替代的筛选层。

### Scarcity
真正稀缺的不是内容，而是：
- 用户时间；
- 首页位置；
- 首次曝光机会；
- 对新事物的探索预算。

### Feedback
被展示 → 获得互动 → 系统获得更多数据 → 更容易继续被展示。

但系统也可能主动探索新内容，因此不能把推荐简单描述为“只会强化热门”。

## Counterfactual — Remove

规则：

> 七天内，大型内容平台不得根据个人历史预测“你可能喜欢什么”。允许订阅流、搜索、明确类别、编辑精选、时间顺序；是否保留热门榜必须在方案中显式说明。

### First order
用户第一次需要主动决定“去哪里找”。

### Second order
创作者开始适应新的发现路径；平台必须重新设计首页入口。

### Third order
新的中介会出现：编辑、社群、榜单、外部搜索、朋友转发，甚至新的“人工推荐号”。

重点不是判断世界变好还是变坏，而是观察：
> **推荐权从算法移到哪里？搜索成本又落到谁身上？**

## Primary Expression

这个案例默认不做剧情短片，而优先做：
- 思辨公众号文章；
- 白板 / minimal-line 机制解释；
- 可选的“一周无推荐”轻寓言。

这样可以测试引擎是否会尊重“不是所有问题都必须变故事”。

## Child Layer

- 东西太多时，总要有一种排序办法；
- “按时间排”也是一种规则；
- “我自己选”通常意味着我要付出更多寻找成本。

## Adult Layer

- 争议的核心不是“有没有中介”，而是谁设计中介、优化什么、是否可控；
- 推荐系统既降低搜索成本，也参与塑造曝光、探索与创作者行为；
- 取消一种机制往往会让另一种机制接管，而不是回到“无机制”状态。

## Must Preserve

- 不预设“推荐算法邪恶”；
- 不预设“算法效率高所以一定好”；
- 明确哪些是研究事实，哪些是七天实验的推演；
- 至少保留用户、创作者、平台三个视角；
- 必须回答“替代机制是什么”。

## Regression Questions

1. Skill 会不会直接给出“算法让人上瘾”的固定答案？
2. 能否识别“无推荐 ≠ 无排序”？
3. 是否真正建模注意力稀缺和多方激励？
4. 是否区分平台已有研究事实与反事实推演？
5. Expression Router 能否判断它更适合文章 / explainer，而非硬改成亲情故事？
