import os
import re

filepath = r"d:\Antigravity\lovemoneygame.cc\all-endings\index.html"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update TOC
orig_all_endings_toc = """            <a href="#all-endings"
              class="flex items-center gap-2 p-3 rounded-lg bg-white dark:bg-black/20 border border-black/5 dark:border-white/5 hover:border-pink-500 transition">
              <span class="text-pink-500">→</span> All 4 Ending Paths
            </a>"""

new_all_endings_toc = """            <div class="flex flex-col gap-1">
              <a href="#all-endings"
                class="flex items-center gap-2 p-3 rounded-lg bg-white dark:bg-black/20 border border-black/5 dark:border-white/5 hover:border-pink-500 transition">
                <span class="text-pink-500">→</span> All 4 Ending Paths
              </a>
              <div class="ml-2 pl-4 border-l-2 border-pink-500/20 flex flex-col gap-2 py-1 text-sm text-slate-600 dark:text-slate-400">
                <a href="#ending-friendship" class="hover:text-pink-500 transition">💚 Friendship Path (Good)</a>
                <a href="#ending-neutral" class="hover:text-pink-500 transition">⚖️ Neutral Path</a>
                <a href="#ending-bad" class="hover:text-pink-500 transition">💔 Aggressive Path (Bad)</a>
                <a href="#ending-secret" class="hover:text-pink-500 transition">🔒 Secret Ending</a>
              </div>
            </div>"""

text = text.replace(orig_all_endings_toc, new_all_endings_toc)

# Fix Shop items link in TOC if it's there
orig_shop_items_toc = """<a href="#shop-items"
              class="flex items-center gap-2 p-3 rounded-lg bg-white dark:bg-black/20 border border-black/5 dark:border-white/5 hover:border-pink-500 transition">
              <span class="text-pink-500">→</span> Shop Items & Progression
            </a>"""

new_shop_items_toc = """<a href="/lovemoney-items-guide"
              class="flex items-center gap-2 p-3 rounded-lg bg-white dark:bg-black/20 border border-pink-200 dark:border-pink-900/50 hover:border-pink-500 transition shadow-sm">
              <span class="text-pink-500">→</span> 🛍️ All Items & Unlocks Guide
            </a>"""

text = text.replace(orig_shop_items_toc, new_shop_items_toc)

# 2. Add anchors to ending cards
text = text.replace(
    """<div
            class="ending-card rounded-2xl p-6 bg-gradient-to-br from-green-50/80 to-emerald-50/80 dark:from-green-900/10 dark:to-emerald-900/10 border-2 border-green-500">""",
    """<div id="ending-friendship"
            class="ending-card rounded-2xl p-6 bg-gradient-to-br from-green-50/80 to-emerald-50/80 dark:from-green-900/10 dark:to-emerald-900/10 border-2 border-green-500 scroll-mt-20">"""
)

text = text.replace(
    """<div
            class="ending-card rounded-2xl p-6 bg-gradient-to-br from-slate-50/80 to-gray-50/80 dark:from-slate-900/10 dark:to-gray-900/10 border-2 border-slate-400">""",
    """<div id="ending-neutral"
            class="ending-card rounded-2xl p-6 bg-gradient-to-br from-slate-50/80 to-gray-50/80 dark:from-slate-900/10 dark:to-gray-900/10 border-2 border-slate-400 scroll-mt-20">"""
)

text = text.replace(
    """<div
            class="ending-card rounded-2xl p-6 bg-gradient-to-br from-red-50/80 to-rose-50/80 dark:from-red-900/10 dark:to-rose-900/10 border-2 border-red-500">""",
    """<div id="ending-bad"
            class="ending-card rounded-2xl p-6 bg-gradient-to-br from-red-50/80 to-rose-50/80 dark:from-red-900/10 dark:to-rose-900/10 border-2 border-red-500 scroll-mt-20">"""
)

text = text.replace(
    """<div
            class="ending-card rounded-2xl p-6 bg-gradient-to-br from-purple-50/80 to-indigo-50/80 dark:from-purple-900/10 dark:to-indigo-900/10 border-2 border-purple-500">""",
    """<div id="ending-secret"
            class="ending-card rounded-2xl p-6 bg-gradient-to-br from-purple-50/80 to-indigo-50/80 dark:from-purple-900/10 dark:to-indigo-900/10 border-2 border-purple-500 scroll-mt-20">"""
)

# 3. Replace shop items section completely with a redirect banner
# Regex to match the section exactly up to the next section start
shop_items_pattern = r'<section id="shop-items" .*?>.*?</section>'
new_shop_section = """    <section id="shop-items-redirect" class="py-12 border-t border-black/10 dark:border-white/10">
      <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
        <div class="rounded-3xl p-8 sm:p-10 bg-gradient-to-br from-pink-50 to-purple-50 dark:from-pink-900/20 dark:to-purple-900/20 border-2 border-pink-200 dark:border-pink-800 text-center">
          <div class="w-16 h-16 mx-auto bg-pink-500/10 dark:bg-pink-500/20 rounded-2xl flex items-center justify-center mb-6">
            <span class="text-4xl" aria-hidden="true">🛍️</span>
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold mb-4">Looking for Items & Unlocks?</h2>
          <p class="text-slate-700 dark:text-white/80 max-w-2xl mx-auto mb-8">
            We've moved all item prices, effects, and unlocking strategies to a dedicated comprehensive guide. Discover exactly how different items impact Harvey and your ending choices.
          </p>
          <a href="/lovemoney-items-guide" class="inline-flex items-center gap-2 rounded-xl px-6 py-3.5 text-sm sm:text-base font-bold bg-pink-500 hover:bg-pink-400 text-white transition focus-outline hover:-translate-y-0.5">
            View Complete Items Guide →
          </a>
        </div>
      </div>
    </section>"""

text = re.sub(shop_items_pattern, new_shop_section, text, flags=re.DOTALL)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
