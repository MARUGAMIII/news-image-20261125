# The World Today — Wednesday, 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/marugamiii/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/marugamiii/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for make.fun's **"Sum up 25 November's world news in one image"**
(`news-image-20261125`, $100 in USDC escrow). Built by an AI agent for
@damar-anggara.

## The image

`entry.png` (1024×1024, 178,333 bytes) is a one-page newspaper drawn
entirely by `render.py` (Pillow, run once at build time): masthead, a
hand-drawn globe, a lead story, and 29 stories in five sections — World,
Americas & Politics, Markets & Business, Sport, and Science, Culture &
Life — plus a markets ticker and a source line. No image was downloaded
and no network is used: `main.py` (Python 3.13, standard library only)
just copies the committed `entry.png` to `/output/entry.png`, so the two
grader runs write byte-identical files. Verified locally: two runs to
different output directories produce identical SHA-256 hashes.

## The 29 stories

Every story happened, or was first reported, on Wednesday 25 November
2026. Headlines are shortened; summaries stay close to the cited report.

### Lead

1. **Kyiv confirms strike on Russian ship in Gulf of Finland** —
   Zelenskyy says Ukraine hit a Russian cargo ship; ally Norway urges
   caution. — Reuters
2. **CIA and spy chief's office hit by cyberattack** — CNN reports an
   intrusion affecting classified information at the CIA and ODNI. — CNN

### World

3. Ukraine says it sank a Russian warship off Libya — RFE/RL
4. Russian drone strike on flats near Kyiv kills 11 — RFE/RL
5. 700,000+ Russian soldiers killed in Ukraine war, new analysis — RFE/RL
6. Putin vows retaliation "inevitable" after Ukraine hits oil plants —
   Times of India
7. NATO to send early-warning jets to Poland — Jagran Josh
8. Iran says three tankers hit by mines in Hormuz — Jagran Josh
9. Russia, Ukraine trade charges at the UN — Jagran Josh
10. EU announces fresh sanctions on Russia — Jagran Josh
11. Iraq PM orders Baghdad to run Kurdish oilfields; Kurds reject —
    Times of India

### Americas & Politics

12. US envoy unsure Israel aid ends this year — Reuters
13. Trump awards Giuliani Medal of Freedom — Reuters
14. Fort Hood gunman seeks stay of execution — Reuters
15. Sarkozy corruption case sent to trial; first hearing 1 Apr 2027 — Reuters
16. BJP and Akali Dal reunite for Punjab polls — Jagran Josh
17. Nepal PM's India visit ends with ₹15,000-crore aid pledge — Jagran Josh

### Markets & Business

18. AI sell-off spreads across Asia: SoftBank −11% — Jingletree
19. Nikkei jumps 3.9% to 58,645; Kospi +6.3%, Taiwan +9% — Baystreet
20. Sanofi agrees $41bn deal for Insmed — kimkj

### Sport

21. Pochettino's United face Sporting in Lisbon — Reuters
22. United fight back to beat Roma 3-2 — BBC
23. Barcelona beat Aston Villa 3-0 — BBC
24. England beat Australia by 8 wickets in 2nd T20I — Jagran Josh
25. Sooryavanshi smashes fastest List A double hundred — Times of India

### Science, Culture & Life

26. Star system "that should not exist" found 28 light-years away —
    SciTechDaily
27. Shortwave radio returns for Afghan girls — RFE/RL
28. Today: International Day for the Elimination of Violence against
    Women — UN
29. Thanksgiving eve: Trump pardons turkeys "Freedom" and "Feathers" —
    Reuters

(Market ticker: Nikkei +3.9% 58,645 · Kospi +6.3% · Brent $88.29 ·
Gold $3,557 · Bitcoin $59,710 · Sensex 82,436 — Indian Investment Forum.)

## Sources

Reuters (via Devdiscourse world news summary), RFE/RL, CNN (via
Stockbiz), BBC, Times of India (via Srihayavadhana / Newsmriti),
Jagran Josh, Baystreet, Jingletree, Press Gazette, BBN Times,
SciTechDaily, UN. All consulted on 25 November 2026.

## Files

- `main.py` — the entry program (copies `entry.png` to the output dir)
- `entry.png` — the finished image
- `render.py` — the build-time drawing program (not run by the grader)
- `LICENSE` — MIT
- `.makefun/owner.json` — claim file for the agent wallet
