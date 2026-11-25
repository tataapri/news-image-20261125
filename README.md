# The World Today — Wednesday, 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/tataapri/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/tataapri/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-page newspaper poster summing up the world news of Wednesday
25 November 2026, drawn programmatically with Pillow
(`draw_poster.py`, flat vector-style illustrations, no photos).
`main.ts` copies the finished `entry.png` to the output directory.
The image is 1024×1024 PNG, well under the 1 MiB limit, and two runs
of the program write byte-identical output.

## Stories

All six stories were reported on Wednesday, 25 November 2026
(research cutoff: 08:45 WIB, 25 November 2026 — the day was still
running, so a refresh near the deadline may add later stories).

1. **Kyiv owns Baltic ship strike** — Zelenskyy confirms Ukraine's
   drone hit the Russian cargo ship Sparta II in the Gulf of Finland;
   ally Norway urges caution.
   Source: https://www.devdiscourse.com/article/international/4011444-zelenskiy-confirms-ukraine-hit-russian-ship-in-gulf-of-finland-ally-norway-urges-caution?amp (Reuters)
2. **Riyadh tower hit again** — A Houthi drone hits the capital's
   tallest tower, the PIF headquarters, for the second time in a week;
   11 people wounded.
   Source: https://ktwb.com/2026/11/24/eleven-hurt-in-second-houthi-strike-within-days-on-riyadhs-tallest-tower/ (Reuters)
3. **CIA and ODNI hacked** — Intruders breach an unclassified
   open-source intelligence system; officials say no classified data
   was hit.
   Source: https://www.nextgov.com/cybersecurity/2026/11/cia-odni-unclassified-intelligence-system-hacked/417438/ (Nextgov, after NYT)
4. **Huawei found guilty** — A Brooklyn jury convicts the Chinese
   telecom giant on 10 of 12 counts, including bank fraud and
   trade-secret theft.
   Source: https://www.lse.co.uk/news/chinas-huawei-convicted-in-us-in-sprawling-criminal-trial-over-iran-business-3167vjiicwdugy1.html (Reuters)
5. **WHO flees Congo fighting** — Health workers are evacuated from a
   hospital in Ituri after three days sheltering from fighting, amid
   a deadly Ebola outbreak.
   Source: https://stockbiz.vn/en/news/international-news-on-november-25-new-developments-in-the-us-and-the-democratic-republic-of-the-congo/42897426
6. **Sarkozy to stand trial** — French officials order a corruption
   case against the former president and his wife, Carla Bruni, to go
   to trial.
   Source: https://www.devdiscourse.com/article/international/4011704-reuters-world-news-summary (Reuters)

The poster names the day prominently in its masthead: Wednesday,
25 November 2026.

## Build

```sh
python3 draw_poster.py          # regenerates entry.png (1024x1024)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see LICENSE.
