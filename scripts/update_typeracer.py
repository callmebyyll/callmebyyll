import urllib.request
import json
import re

TR_USERNAME = "0xpng"  # Ganti ke "byyll" jika username TypeRacer-mu byyll
API_URL = f"https://typeracer.com:{TR_USERNAME}"

req = urllib.request.Request(API_URL, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode())

stats = data.get("tstats", {})
avg_wpm = round(stats.get("wpm", 0), 1)
best_wpm = round(stats.get("bestGameWpm", 0), 1)
recent_wpm = round(stats.get("recentAvgWpm", 0), 1)
total_races = stats.get("cg", 0)

section = f"""<!-- TYPERACER:START -->
### ⌨️ TypeRacer Stats ([`@{TR_USERNAME}`](https://typeracer.com{TR_USERNAME}))

| Metric | Score |
| :--- | :--- |
| **Average Speed** | `{avg_wpm} WPM` |
| **Best Speed** | `{best_wpm} WPM` |
| **Recent Average (Last 10)** | `{recent_wpm} WPM` |
| **Total Races** | `{total_races}` |
<!-- TYPERACER:END -->"""

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

updated = re.sub(
    r"<!-- TYPERACER:START -->.*?<!-- TYPERACER:END -->",
    section,
    readme,
    flags=re.DOTALL,
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)
