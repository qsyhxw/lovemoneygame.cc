import os

filepath = r"d:\Antigravity\lovemoneygame.cc\lovemoney-mobile\index.html"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# 1. TDK updates
orig_tdk = """  <title>Lovemoney Mobile 18+ — Play on Phone Browser (No App Download)</title>
  <meta name="description" content="Lovemoney mobile guide: No official Android/iOS app exists. Play the 18+ game on mobile browser or download Windows version. Beware fake APKs on itch.io imposters.">
  <meta name="keywords" content="lovemoney mobile, lovemoney android, lovemoney ios, lovemoney apk, lovemoney phone, mobile visual novel 18+">"""

new_tdk = """  <title>Lovemoney Mobile 18+ for Android APK & iOS — Play on Browser</title>
  <meta name="description" content="Lovemoney mobile guide: Play on Android APK & iOS devices via browser. No official app exists. Play the 18+ game on mobile safely. Beware fake APKs on itch.io imposters.">
  <meta name="keywords" content="lovemoney mobile, lovemoney Android APK & iOS, lovemoney android, lovemoney ios, lovemoney apk, lovemoney phone, mobile visual novel 18+">"""

text = text.replace(orig_tdk, new_tdk)

# 2. Add FAQ item
orig_faq_start = """        <div class="mt-8 space-y-4">
          <details class="group rounded-xl border border-black/10 dark:border-white/10 p-5 bg-slate-50/80 dark:bg-white/5">"""

new_faq_item = """        <div class="mt-8 space-y-4">
          <details class="group rounded-xl border border-black/10 dark:border-white/10 p-5 bg-slate-50/80 dark:bg-white/5">
            <summary class="cursor-pointer font-semibold focus:outline-none focus-visible:ring-2 focus-visible:ring-pink-500 rounded list-none flex items-center justify-between">
              <span>Why is my Lovemoney download failing to install?</span>
              <span class="text-pink-500 group-open:rotate-180 transition-transform" aria-hidden="true">▼</span>
            </summary>
            <div class="mt-3 text-sm text-slate-700 dark:text-white/80 leading-relaxed space-y-2">
              <p>
                If you are trying to install an <strong>Android APK & iOS</strong> version and experiencing an "App not installed" or "Download failed" error, it is because <strong>no official mobile app exists</strong>. Your device's security system is likely blocking a malicious file that was disguised as the game.
              </p>
              <p>
                We strongly advise against attempting to bypass these security warnings to force an installation. Instead of pursuing fake downloads, you can play the game safely and instantly straight through your mobile browser without downloading anything.
              </p>
            </div>
          </details>

          <details class="group rounded-xl border border-black/10 dark:border-white/10 p-5 bg-slate-50/80 dark:bg-white/5">"""

text = text.replace(orig_faq_start, new_faq_item)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
