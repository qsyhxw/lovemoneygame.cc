# LoveMoney 网站页面创建规范

## 核心原则

作为「事实校对员 + 内容创作者」，创建新页面时必须严格遵守：

1. **信息准确性第一**：排除引用任何自身网站的页面或内容，确保信息准确度
2. **SEO 优化**：标题和描述长度符合 Google SEO 要求（Title: 50-60字符，Description: 120-160字符）
3. **风格一致性**：所有新建页面必须与网站首页 `index.html` 保持一致的设计风格和结构

## 内容创作流程

### 第一步：事实核查与交叉验证

对文中所有【可核验陈述】（角色/武器名称、解锁条件、数值/机制、道具/羁绊、关卡/位置、掉落/触发、版本与日期等）：

**信息源优先级：**
1. 官方公告 / 补丁说明 / Steam 或 itch.io 商店页 / 开发者 Discord
2. 专业媒体与开发者访谈
3. 社区维基 / 视频 / Reddit

**验证规则：**
- 使用至少 2 个独立来源进行交叉验证
- 若来源互相矛盾，以最新补丁与官方渠道为准
- 必须标注证据的"新鲜度"（发布日期或补丁号）
- 无补丁且 >12 个月的证据需谨慎使用
- 严禁主观推断或杜撰；不清楚就写"未知/待确认"
- 专有名词保留英文原文（可在括号中附中文解释）

**输出格式：事实校对表**

| Claim | Verdict | Corrected | Evidence1 | Evidence2 | Notes | Confidence |
|-------|---------|-----------|-----------|-----------|-------|------------|
| 陈述内容 | ✅/❌/❓ | 修正内容 | 链接+出处+日期 | 链接+出处+日期 | 备注 | 0-1 |

### 第二步：内容撰写

基于已验证的信息，输出包含：
- SEO 友好的标题（Title）
- 1 段简介（可用作 Meta Description）
- 合理分层的 H2/H3 结构
- 正文内容与事实校对表保持一致
- 存疑信息使用稳妥、模糊但诚实的表述

### 第三步：风险评估与优化建议

**1. High-Risk 信息清单**
- 列出对玩家决策影响大、且证据不足或来源冲突的陈述
- 说明为何影响大

**2. 内容优化建议**
- 3-5 条可执行的改进建议
- 例如：增加官方引用、拆分章节、补充图示/表格、后续可更新的版本节点

**3. 版本差异提示**
- 总结关键差异（补丁号 + 变化点）
- 提示本文基于哪个版本撰写
- 标注未来可能需要更新的部分

## 页面风格要求

## 必需元素清单

### 1. HTML Head 结构
```html
- charset="utf-8"
- viewport meta tag
- SEO 优化的 title (包含年份 2026)
- meta description (120-160字符)
- meta keywords (相关关键词)
- canonical URL
- Google AdSense script
- Google Analytics (gtag.js)
- Favicon 完整集合
- Open Graph tags
- Twitter Card tags
- Theme color (light/dark)
- Tailwind CDN (3.4.10)
- FAQ Schema (如适用)
```

### 2. 设计系统

**颜色方案：**
- Primary: `bg-pink-500` / `hover:bg-pink-400`
- Background: `bg-white` / `dark:bg-[#0B0B12]`
- Text: `text-slate-900` / `dark:text-[#EAEAF0]`
- Borders: `border-black/10` / `dark:border-white/10`
- Cards: `bg-slate-50/80` / `dark:bg-white/5`

**组件样式：**
- 圆角: `rounded-xl` / `rounded-2xl`
- 按钮: `px-4 py-2` / `px-6 py-3`
- 间距: `py-12` sections, `mb-6` headings
- 过渡: `transition` on interactive elements
- Focus: `.focus-outline` class

### 3. 页面结构模板

```
1. Header (sticky, backdrop-blur)
   - Logo + 18+ badge
   - Desktop nav (About, Guides, Play, FAQ)
   - Mobile menu toggle
   - CTA button

2. Main Content
   - Breadcrumb navigation
   - Hero section with h1
   - Content warning (如适用)
   - Quick facts/stats
   - Main content sections
   - FAQ section
   - Related guides grid

3. Footer
   - Copyright with dynamic year
   - Links (Endings, itch.io)
```

### 4. Accessibility 要求

- Skip to content link
- ARIA labels on buttons
- Semantic HTML (nav, main, section, article)
- Focus visible states
- Reduced motion support
- Screen reader only text (`.sr-only`)

### 5. SEO 优化

**Title 格式：**
`[主题] (2026) — [副标题]`

**Description 格式：**
简洁描述 + 关键词自然融入 + CTA

**内部链接策略：**
- 每个页面至少 3-5 个内部链接
- 链接到相关指南
- 链接到首页 sections (#about, #guides, #play)
- 使用描述性锚文本

**关键词布局：**
- H1 包含主关键词
- H2/H3 包含相关关键词
- 首段包含主关键词
- 自然分布，避免堆砌

### 6. 响应式设计

- Mobile-first approach
- Breakpoints: `sm:`, `md:`, `lg:`
- Grid: `grid sm:grid-cols-2`
- Hidden elements: `hidden md:flex`
- Mobile menu with smooth transition

### 7. Dark Mode 支持

- 所有颜色必须有 dark: variant
- 使用 `dark:bg-[#0B0B12]` 作为主背景
- 使用 `dark:text-[#EAEAF0]` 作为主文本
- 边框使用 `dark:border-white/10`

### 8. 性能优化

- 使用 CDN (Tailwind, Google fonts)
- Async scripts (AdSense, Analytics)
- 优化图片 (如使用)
- 最小化 custom CSS

### 9. 内容规范

**18+ 内容警告：**
- 红色边框 `border-2 border-red-500`
- 背景 `bg-red-50/80 dark:bg-red-900/10`
- 🔞 emoji
- 明确的年龄确认文本

**卡片样式：**
- 渐变背景用于重要内容
- 悬停效果 `hover:border-pink-500`
- 一致的内边距 `p-4` / `p-6`

**按钮层级：**
- Primary: `bg-pink-500`
- Secondary: `bg-black/5 dark:bg-white/10`
- Text links: `hover:text-pink-500`

### 10. JavaScript 要求

**必需功能：**
```javascript
- 动态年份: document.getElementById('year').textContent = new Date().getFullYear()
- Mobile menu toggle
- Smooth scroll behavior (CSS: scroll-smooth)
```

## 创建新页面时的检查清单

- [ ] 所有 meta tags 完整
- [ ] SEO title 包含年份和关键词
- [ ] Breadcrumb 导航正确
- [ ] 18+ 警告（如需要）
- [ ] 至少 3 个内部链接
- [ ] Related guides section
- [ ] FAQ section with schema
- [ ] Footer 完整
- [ ] Mobile menu 功能正常
- [ ] Dark mode 所有元素都有样式
- [ ] Accessibility features 完整
- [ ] 响应式设计测试

## 文件路径规范

**Wiki 页面：** `/wiki/[page-name]/index.html`
**普通页面：** `/[page-name].html`

## 示例参考

参考文件：
- `index.html` - 首页设计系统
- `gameplay-scenes-guide.html` - 内容页面结构
- `wiki/lovemoney-soap-scene/index.html` - Wiki 页面结构
