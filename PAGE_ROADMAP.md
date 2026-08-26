# PAGE_ROADMAP

这是站点级页面施工路线图，不是玩家页面，也不代表所有页面都已获准创建。

## Roadmap Metadata

- Site: LoveMoney Game
- Domain: lovemoneygame.cc
- Source Research: `D:\Codex\GSC数据\lovemoneygame.cc\26.8.25-SEO 页面级决策与修改规格.md`
- Homepage: `index.html`
- Last Updated: 2026-08-26
- Roadmap Status: ACTIVE
- Current Recommended Queue Order: P2-04

## Status Values

只能使用：`PLANNED_NOT_CREATED`、`READY_FOR_PAGE_PROMPT`、`RESEARCHING`、`CREATED_NEEDS_REVIEW`、`PUBLISHED`、`DELAYED`、`MERGED`、`ARCHIVED`。

## Page Roadmap

| Queue | Priority | Status | Page | URL | Primary Keyword | Player Task | Traffic Role | Independent Value | Required Verification | Current Evidence | Hands-on Required | Publishable Without Hands-on | Creation Trigger | Navigation Level | Homepage Placement | Natural Next Page | Related Existing Pages | Last Checked |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | P1 | CREATED_NEEDS_REVIEW | 首页品牌意图恢复 | `/` | `lovemoney`, `lovemoney game` | 了解 LoveMoney，并选择浏览器试玩或进入 Buwu 的 itch.io 桌面下载页 | LANDING | 根 URL 直接回答品牌、游戏类型、试玩、桌面下载与指南分工 | 核对 Title、Meta、H1、首段、canonical、浏览器入口与桌面平台事实；观察 7 天及 28 final 日指标 | 2026-08-26 已核验 Buwu itch.io 页面列出 Windows/macOS；公开首页存在浏览器播放入口；未把 Android 作为官方平台 | NO | YES | 已批准 P1-01；本次已完成静态施工，待发布环境复核 | GLOBAL_NAV | Root URL 首屏、Start Your Journey、Popular Guides | P1-03：Endings 主页面集中与陈旧声明清理 | `/download-guide`, `/how-to-play`, `/games-like-lovemoney`, `/all-endings/`, `/lovemoney-mobile/`, `/uncensored-version` | 2026-08-26 |
| 1 | P1 | CREATED_NEEDS_REVIEW | Endings 主页面集中与陈旧声明清理 | `/all-endings/` | `all endings`, `ending routes`, `secret ending overview` | 查看路线总览、Soap 决策、版本边界与证据等级 | SUPPORT | 将一般结局总览与 Wiki 重复意图集中到根级页面 | 核验主页面 Title、Meta、H1、canonical、路线证据边界与 true-ending self-canonical；线上核验 Wiki all-endings 301；观察 7/28/56 天 | 2026-08-26 已核验 Buwu 官方 listing：Windows/macOS、OLD/UPDATE 区分、UPDATE 含 secret content；官方未发布固定结局数量；主页面已完成本地静态施工；`_redirects` 已加入 Wiki all-endings → `/all-endings/` 301 规则，待线上 HTTP 验证 | NO | YES | P1-03 页面与迁移规则已完成本地施工；待发布环境复核与 301 验证 | HUB_OR_FEATURED | Start Your Journey 的 endings 入口 | P1-02：Uncensored 归属集中与 CTR 恢复 | `/index.html`, `/how-to-play.html`, `/harvey-character-analysis.html`, `/wiki/lovemoney-true-ending/`, `/wiki/lovemoney-all-endings/` | 2026-08-26 |
| 2 | P1 | CREATED_NEEDS_REVIEW | Uncensored 归属集中与 CTR 恢复 | `/uncensored-version` | `uncensored`, `no blur`, `NSFW version status` | 核对当前版本状态、来源与 patch 边界 | SUPPORT | 由专页承接版本状态，首页只提供导航 | 核验主页面 Title、Meta、H1、canonical、证据等级；线上核验 Wiki uncensored 301 与内链；观察 28/56/90 天 | 2026-08-26 已核验 Buwu 官方 listing：成人内容警告、Windows/macOS、OLD/UPDATE 区分；官方未说明独立 uncensored/no-blur 版本或 patch；主页面已完成本地静态施工，Wiki FAQ 301 规则已加入，待线上 HTTP 验证 | NO | YES | P1-02 已批准并按用户指令跳过观察窗口完成本地施工；待发布环境复核与 301 验证 | CONTEXTUAL_ONLY | 首页 focused guide 入口 | P2-04：Mobile / Android / APK | `/itch-io-download.html`, `/where-to-play.html`, `/lovemoney-18-plus-guide.html`, `/wiki/lovemoney-uncensored/` | 2026-08-26 |

## Queue Rules

- `READY_FOR_PAGE_PROMPT` 才能直接交给 `03A-分页快速创建提示词.md`。
- `CREATED_NEEDS_REVIEW` 表示本地静态施工已完成，但仍需发布环境或人工复核。
- 新页面不得进入冻结的 `/wiki/` 命名空间；任何合并、301 或批量 canonical 变更另开技术任务。
- 每次页面施工、研究报告更新、版本变化或流量数据出现新信号后，重新排序 Queue。

## Next Action

- Next Page: P2-04：Mobile / Android / APK
- Prompt: `03A`
- Required Before Start: 完成 P1-02 主页面与 Wiki uncensored 301 线上复核；确认移动页面合并范围与官方来源边界
- Action: WAIT
- Reason: P1-02 已完成本地施工但仍需发布环境复核；P2-04 是上游已批准的下一项合并任务，必须继续单独核对移动/APK 的事实与迁移边界。
