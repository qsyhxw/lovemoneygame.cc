import os

filepath = r"d:\Antigravity\lovemoneygame.cc\eun-mi.html"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Replace title and meta description
orig_head_part = """    <title>Eun-Mi Harvington - Harvey's Wife Wiki, Age & Lore (2026)</title>
    <meta name="description"
        content="Eun-Mi Harvington character guide: Harvey's 34-year-old Korean-American wife. Learn about her role in BLOODMONEY!, HEP game appearance, relationship with Harvey, and complete lore.">"""
new_head_part = """    <title>Eun-Mi Harvington: Harvey Harvington's Wife Wiki, Age & Lore</title>
    <meta name="description"
        content="Eun-Mi Harvington character guide: Harvey Harvington's Wife. Learn about this 34-year-old Korean-American's role in BLOODMONEY!, HEP game appearance, her relationship with Harvey, and complete lore.">"""

text = text.replace(orig_head_part, new_head_part)

# 2. Replace H1 and intro text
orig_hero = """                <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight">
                    Eun-Mi Harvington - Harvey's Wife Wiki & Character Guide
                </h1>
                <p class="mt-4 text-lg text-slate-700 dark:text-white/80 leading-relaxed">
                    Eun-Mi Harvington (also known as <strong>Joy</strong> or <strong>Choi Eun-Mi</strong>) is Harvey
                    Harvington's wife in the <strong>BLOODMONEY!</strong> universe. This guide covers her age,
                    background, role in the games, relationship with Harvey, and complete character lore.
                </p>"""

new_hero = """                <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight">
                    Eun-Mi Harvington: Harvey Harvington's Wife Wiki & Character Guide
                </h1>
                <p class="mt-4 text-lg text-slate-700 dark:text-white/80 leading-relaxed">
                    Eun-Mi Harvington (also known as <strong>Joy</strong> or <strong>Choi Eun-Mi</strong>) is <strong>Harvey Harvington's Wife</strong> in the <strong>BLOODMONEY!</strong> universe. This guide covers her age,
                    background, role in the games, their turbulent relationship, and complete character lore.
                </p>"""

text = text.replace(orig_hero, new_hero)

# 3. Replace first paragraph
orig_intro = """                <div class="space-y-4 text-slate-700 dark:text-white/80 leading-relaxed">
                    <p>
                        Eun-Mi Harvington is a central character in the <strong>BLOODMONEY!</strong> universe created by
                        SHROOMYCHRIST. While she doesn't appear directly in the original BLOODMONEY! game, she is
                        frequently referenced in the lore and plays a crucial role in understanding Harvey's backstory
                        and motivations.
                    </p>"""

new_intro = """                <div class="space-y-4 text-slate-700 dark:text-white/80 leading-relaxed">
                    <p>
                        As <strong>Harvey Harvington's Wife</strong>, Eun-Mi Harvington serves as a central and complex figure in the <strong>BLOODMONEY!</strong> universe created by SHROOMYCHRIST. While she doesn't appear directly in the original BLOODMONEY! game, she is frequently referenced in the lore and plays a crucial role in understanding her husband's tragic backstory and motivations.
                    </p>"""

text = text.replace(orig_intro, new_intro)


with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
