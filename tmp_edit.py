import os

filepath = r"d:\Antigravity\lovemoneygame.cc\harvey-character-analysis.html"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Edit "Who Is Harvey Harvington?" to add Infobox
orig_who = '<h2 class="text-2xl sm:text-3xl font-bold mb-6">Who Is Harvey Harvington?</h2>'
new_who = '''<h2 class="text-2xl sm:text-3xl font-bold mb-6">Who Is Harvey Harvington?</h2>

        <!-- Character Infobox -->
        <div class="float-none md:float-right w-full md:w-80 ms-0 md:ms-8 mb-6 bg-slate-50 border border-black/10 dark:bg-white/5 dark:border-white/10 rounded-2xl overflow-hidden shadow-sm">
          <div class="bg-pink-100 dark:bg-pink-900/30 p-4 border-b border-pink-200 dark:border-pink-800 text-center">
            <h3 class="font-bold text-lg text-pink-900 dark:text-pink-100">Harvey Harman Harvington</h3>
          </div>
          <div class="p-4 space-y-3 text-sm">
            <div class="flex justify-between border-b border-black/5 dark:border-white/5 pb-2">
              <span class="font-semibold text-slate-500 dark:text-white/50">Age</span>
              <span class="text-right text-slate-800 dark:text-white">Late 30s</span>
            </div>
            <div class="flex justify-between border-b border-black/5 dark:border-white/5 pb-2">
              <span class="font-semibold text-slate-500 dark:text-white/50">Spouse</span>
              <span class="text-right"><a href="/eun-mi/" class="text-pink-600 dark:text-pink-400 hover:underline font-semibold">Joy Eun-Mi</a></span>
            </div>
            <div class="flex justify-between border-b border-black/5 dark:border-white/5 pb-2">
              <span class="font-semibold text-slate-500 dark:text-white/50">Children</span>
              <span class="text-right text-slate-800 dark:text-white">Toby Harvington</span>
            </div>
            <div class="flex justify-between border-b border-black/5 dark:border-white/5 pb-2">
              <span class="font-semibold text-slate-500 dark:text-white/50">Role</span>
              <span class="text-right text-slate-800 dark:text-white">Protagonist / Victim</span>
            </div>
            <div class="flex justify-between pb-1">
              <span class="font-semibold text-slate-500 dark:text-white/50">Games</span>
              <span class="text-right text-slate-800 dark:text-white">LoveMoney, BloodMoney</span>
            </div>
          </div>
        </div>'''
text = text.replace(orig_who, new_who)

# 2. Add H2 for Age, Appearance, Personality
orig_appearance = '<h2 class="text-2xl sm:text-3xl font-bold mb-6">Physical Appearance & Design</h2>'
new_appearance = '''<h2 class="text-2xl sm:text-3xl font-bold mb-6">Harvey Harvington Age, Appearance, and Personality</h2>
        <p class="text-slate-700 dark:text-white/80 leading-relaxed mb-6">
          While players frequently search for <strong>Harvey Harvington's age</strong>, it isn't explicitly codified as a single number. However, his context as a father to Toby and his marriage places him in his late 30s. His physical appearance naturally extends to the core of his personality—both meticulously crafted to hide an underlying desperation.
        </p>'''
text = text.replace(orig_appearance, new_appearance)

# 3. Modify "Personality & Psychological Profile" from H2 to H3
orig_personality = '''    <!-- PERSONALITY & PSYCHOLOGY -->
    <section class="py-12 border-b border-black/10 dark:border-white/10">
      <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
        <h2 class="text-2xl sm:text-3xl font-bold mb-6">Personality & Psychological Profile</h2>'''
new_personality = '''    <!-- PERSONALITY & PSYCHOLOGY -->
    <section class="py-12 border-b border-black/10 dark:border-white/10">
      <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
        <h3 class="text-xl sm:text-2xl font-bold mb-6 mt-4 text-pink-600 dark:text-pink-400">Psychological Profile & Traits</h3>'''
text = text.replace(orig_personality, new_personality)

# 4. Internal linking 1:
orig_link1 = 'purchase increasingly harmful tools'
new_link1 = '<a href="/lovemoney-items-guide/" class="font-semibold text-pink-600 dark:text-pink-400 hover:underline">purchase increasingly harmful tools</a>'
text = text.replace(orig_link1, new_link1)

# 5. Internal linking 2:
orig_link2 = '<h2 class="text-2xl sm:text-3xl font-bold mb-6">Character Evolution Across Endings</h2>'
new_link2 = '<h2 class="text-2xl sm:text-3xl font-bold mb-6"><a href="/all-endings/" class="hover:underline hover:text-pink-600 dark:hover:text-pink-400">Character Evolution Across Endings</a></h2>'
text = text.replace(orig_link2, new_link2)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
