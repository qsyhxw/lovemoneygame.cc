# 执行摘要 (Executive Summary)
1. **Significant Intent Mismatch Detected**: High-impression queries for specific game elements (e.g., "lovemoney items", "games like lovemoney") are currently landing on generalized pages like the homepage or ending guides, diluting relevance and CTR.
2. **Untapped Character Lore Potential**: Queries surrounding "harvey harvington" and his wife suffer from poor average positions (40+) and low CTR, indicating existing character analysis pages lack authoritativeness and fail to capture long-tail subtopics (age, appearance).
3. **High-Value Technical Queries Underperforming**: Terms like "lovemoney apk download" and "lovemoney android" drive commercial intent but suffer from suboptimal CTR on existing mobile pages, requiring targeted SERP snippet optimization.
4. **Actionable Roadmap**: The strategy prioritizes the creation of 3 new intent-aligned pages (Items hub, Alternatives guide, Gameplay overview) and the optimization of 4 existing pages (Harvey profile, Eun Mi profile, Mobile hub, All Endings) to capture low-hanging traffic.

---

# 事实校对表 (Fact-Checking Table)
| Claim | Verdict | Corrected | Evidence1 | Evidence2 | Notes | Confidence |
|-------|---------|-----------|-----------|-----------|-------|------------|
| 游戏包含角色 Harvey Harvington 和 Eun Mi (Harvey's wife) | ✅正确 | - | GSC Data (query: harvey harvington wife) | Landing Page: /eun-mi | 数据集内确凿 | 1.0 |
| 玩家搜索 "lovemoney items" 与 "all items" | ✅正确 | - | GSC Data (query: lovemoney items) | GSC Data (query: lovemoney all items) | 数据集内确凿 | 1.0 |
| 玩家搜索关于 "games like lovemoney" 与 "gameplay" | ✅正确 | - | GSC Data (query: games like lovemoney) | GSC Data (query: lovemoney gameplay) | 数据集内确凿 | 1.0 |

*(注：本分析基于您提供的 2026年3月 GSC 数据集。所有事实陈述及关键词建议均溯源自该数据。)*

---

# 机会图谱 (Opportunity Map by Topic Cluster)

### 1. Characters / Lore (角色与故事)
* **Top queries**: `harvey harvington` (Imp: 89, Pos: 45.3), `harvey harvington wife` (Imp: 59, Pos: 21.8).
* **Metrics / 诊断**: 高曝光但排名极差（>20），且 CTR 低下（<0.02）。
* **结论 (Underperforming coverage)**: 弱覆盖。现有页面 `/harvey-character-analysis` 无法有效满足具体查询意图（如年龄、全貌、妻子），整体缺乏信息深度与结构化呈现。

### 2. Weapons / Items / Gear (物品与道具)
* **Top queries**: `lovemoney items` (Imp: 14, Pos: 7.5), `lovemoney all items`.
* **Metrics / 诊断**: 作为强信息调研意图，目前无任何专门页面承接，统一降级/重定向至 `/all-endings/`。
* **结论 (Missing-page)**: 缺页。用户需要查询具体道具的使用与解锁位置，直接指向结局页导致严重的意图错配。

### 3. Builds / Meta / Similar Games (类似替代游戏)
* **Top queries**: `games like lovemoney` (Imp: 46, Pos: ~38).
* **Metrics / 诊断**: 具备高商业调研意图（Commercial Investigation），但完全缺失内容，直接降阶至 `https://lovemoneygame.cc/` 首页。
* **结论 (Missing-page)**: 缺页。需要一篇高质量的 “Alternative games” 引流转化文章，捕获品类泛搜索词。

### 4. Gameplay / Features (实机与机制)
* **Top queries**: `lovemoney gameplay` (Imp: 198, Pos: 6.6), `lovemoney full gameplay` (Imp: 17, Pos: 10.2).
* **Metrics / 诊断**: 这类基础认知词整体展现量高，但都粗暴地指向首页，缺乏深度。
* **结论 (Missing-page / Low CTR)**: 缺页且弱覆盖。需要专门的玩法介绍或图库页，以此吸收转化初期漏斗的用户。

### 5. Transactional / Mobile (移动端下载)
* **Top queries**: `lovemoney android` (Imp: 99, Pos: 9.6, CTR: ~10%), `lovemoney app download` (Imp: 17).
* **Metrics / 诊断**: 准确指向 `/lovemoney-mobile/`。CTR较好但排名尚在第二页边缘。
* **结论 (Mismatch / Low-CTR)**: Mismatch / 弱覆盖。虽然有对应页面，但在 Title/Meta 中有可能缺乏 “APK” 或 “Android Download” 的抢眼促排标识，转化未达上限。

---

# 优先优化而非新建 (Optimize Instead of New)

| Existing page | Issue type | Target queries | Recommended actions |
|:---|:---|:---|:---|
| `/harvey-character-analysis` | 弱覆盖 | harvey harvington, harvey harvington age | 1. H2 添加 “Age, Appearance, Personality” 以击生长尾词。<br>2. 注入人物 Infobox 表格。<br>3. 强化内部锚文本链接。 |
| `/eun-mi` | 错配 / 低CTR | harvey harvington wife | 1. 标题(Title)和摘要(Meta)中强制包含 “Harvey Harvington's Wife”。<br>2. 在正文第一段开门见山点出两者关系。 |
| `/lovemoney-mobile/` | 低CTR | lovemoney android, lovemoney apk | 1. 更新 TDK 增加 "Android APK & iOS"。<br>2. 补充一栏 FAQ 回答有关 "Download" 的常见安装故障。 |
| `/all-endings/` | 流量泛滥与错配 | lovemoney items, lovemoney walkthrough | 1. 剥离并移除所有 "Items" 主题，加上对新建 Items 页的跳转。<br>2. 补充目录 (TOC) 使结局导航更清晰。 |

---

# 新建页面蓝图 (New Pages Backlog)

| Page title | Page type | Primary keyword | Intent | Keyword cluster (short) | Suggested URL | Priority | Notes |
|:---|:---|:---|:---|:---|:---|:---|:---|
| LoveMoney All Items & Unlock Guide | Item page | lovemoney items | Informational | lovemoney items [GSC], lovemoney all items [GSC], item locations [Derived] | `lovemoney-items-guide` | P1 | 弥补 items 词条错放进 ending 带来的流量流失。 |
| Best Games Like LoveMoney | Listicles / FAQ | games like lovemoney | Commercial Inv. | games like lovemoney [GSC], alternative games [Derived], similar games [Derived] | `games-like-lovemoney` | P2 | 商业调研高意图，建立品类权威以低成本获取精准用户。 |
| LoveMoney Gameplay Overview | Gameplay guide | lovemoney gameplay | Informational | lovemoney gameplay [GSC], lovemoney full gameplay [GSC], free play [GSC] | `lovemoney-gameplay` | P1 | 极高的搜索印象数(>190)。拦截从首页分流的好奇心玩家。 |

## 各新建页面详情蓝图 (New Page Action Plans)

### 1. LoveMoney All Items & Unlock Guide
* **Page Type**: Item page
* **Primary keyword**: `lovemoney items` (来自 GSC)
* **Keyword cluster**: `lovemoney items` [GSC], `lovemoney all items` [GSC], `love money items` [Derived], `item unlocks` [Derived], `find items lovemoney` [Derived]. *(受限于数据量，扩展词严格遵循要求)*
* **Search intent**: 玩家处于游戏中后期，希望快速查阅物品效果及如何获取。
* **Suggested URL slug**: `lovemoney-items-guide`
* **Recommended page template**: **推荐表格字段** (Icon, Item Name, Type, Effects/Stats, How to Unlock/Locations).
* **Outline (H1–H3)**:
  - H1: Complete LoveMoney Items Guide: Locations & Unlocks
  - H2: Introduction to the Item System
  - H2: Key Progression Items (Story Critical)
  - H2: Consumables & Hidden Items
  - H2: FAQ: How Items Affect Endings
* **Internal linking plan**:
  - In-links: 从 `/all-endings/` 与 首页导航直接链入。
  - Out-links: 根据物品触发的结局链向对应的 `/all-endings/#ending-name`。
* **Priority + Reason**: **P1**。大量有价值的长尾流量由于意图完全不匹配被重定向至结局页而浪费。

### 2. Top Games Like LoveMoney
* **Page Type**: FAQ hub / Listicle
* **Primary keyword**: `games like lovemoney` (来自 GSC)
* **Keyword cluster**: `games like lovemoney` [GSC], `similar games to lovemoney` [Derived], `lovemoney alternatives` [Derived], `games like bloodmoney` [Derived].
* **Search intent**: 玩家已经通关或对游戏类型感兴趣，正寻找竞品和同类游戏（高转化商业意图）。
* **Suggested URL slug**: `games-like-lovemoney`
* **Recommended page template**: 图文混排的锚点列表 (Listicle Schema) + 内嵌相关视频。
* **Outline (H1–H3)**:
  - H1: 5 Best Visual Novel Games Like LoveMoney
  - H2: Why LoveMoney Defines This Thriller Genre
  - H2: Top Recommendations
    - H3: [Game 1 Name & Overview]
    - H3: [Game 2 Name & Overview]
    - H3: Bloodmoney (官方竞品/外传引导)
  - H2: Are there other mobile alternatives?
* **Internal linking plan**:
  - In-links: 站底部 (Footer) 或 `/about` 页面。
  - Out-links: 指向姊妹篇 `/bloodmoney-18-plus-guide` 和 `/lovemoney-vs-bloodmoney` 实现流量内循环。
* **Priority + Reason**: **P2**。能拦截竞争对手与品类的搜索热度，虽不提升游戏本身留存，但极度增加整站的会话量。

### 3. LoveMoney Gameplay Overview
* **Page Type**: FAQ hub / Mechanics overview
* **Primary keyword**: `lovemoney gameplay` (来自 GSC)
* **Keyword cluster**: `lovemoney gameplay` [GSC], `lovemoney full gameplay` [GSC], `playing lovemoney` [GSC], `lovemoney game play` [GSC], `love money gameplay` [GSC], `lovemoney mechanics` [Derived], `how to play` [Derived].
* **Search intent**: 潜在玩家希望在下载试玩前快速了解画面、系统和交互模式。
* **Suggested URL slug**: `lovemoney-gameplay-overview`
* **Recommended page template**: Video & Image Gallery 组件，配合 FAQ Schema Markup。
* **Outline (H1–H3)**:
  - H1: LoveMoney Gameplay Overview: What You Need to Know
  - H2: Basic Gameplay Loop
  - H2: Key Game Mechanics
    - H3: Branching Dialogues & Moral Choices
    - H3: Resource & Item Management
  - H2: Gameplay Gallery (实机截图)
  - H2: Censored vs Uncensored Mode Differences
* **Internal linking plan**:
  - In-links: 核心导航和首页上方链入。
  - Out-links: 指向 `/moral-choices-guide` 以深入探索，以及引流至 `/uncensored-version`。
* **Priority + Reason**: **P1**。由于该簇曝光数极高 (>200+ Impressions) 但点击极差，缺乏专门承接的页面严重损害了此商业词的吸储能力。

---

# 需要的补充输入与免责声明 (Assumptions & Needed Inputs)

1. 能否提供游戏所有内部有效物品（Items）的确切名称和图片清单？以用于新建首个 Item 数据库页面。
2. 对于“Games like LoveMoney”，是否有官方开发者之前推崇过的游戏灵感原型？以确保我们推荐的游戏高度契合 Wiki 基调。
3. *No additional inputs needed for existing page optimizations.*

*(本分析报告由 SEO Growth Consultant 依据提供的 GSC 表格数据执行信息架构分析并生成。)*
