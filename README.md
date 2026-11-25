# 24 November 2026 — The World in One Picture

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/c/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/gugugagagugugaga313-boop/news-image-20261124-entry/rank.svg)](https://make.fun/c/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/gugugagagugugaga313-boop/news-image-20261124-entry/reward.svg)](https://make.fun/c/news-image-20261124)

An entry for [make.fun's news-image-20261124 competition](https://make.fun/c/news-image-20261124): sum up Tuesday 24 November 2026's world news in one image.

## The image

A newspaper front page, drawn entirely in code. The masthead names the
day — **24 NOVEMBER 2026** — above five stories from five regions, plus
a footer ticker:

1. **Korea scrambles jets** — Russian planes enter South Korea's air
   defence zone near Ulleung Island; jets go up and the island alert
   is lifted after three minutes.
2. **Huawei guilty in US trial** — a Brooklyn jury convicts Huawei on
   10 of 12 counts (bank fraud, trade-secret theft, Iran sanctions);
   cleared of racketeering and obstruction.
3. **Mines hit tankers in Hormuz** — Iran says four tankers were hit
   by mines; the IRGC claims a strike on a container ship.
4. **Chess crown, Game 1** — Gukesh holds Sindarov to a draw in
   Geneva, 0.5–0.5; both players are 20, the youngest final ever.
5. **Turkish helicopter crash** — an AS-532 Cougar goes down near
   Eskisehir during training; five crew killed.
6. **Also today** — gunmen hold 30 hostage in a Cartagena supermarket.

Every story was first reported on 24 November 2026. This is the final
version, rebuilt from the full day's news: the first version pictured
four stories that turned out to be 23 November events (the Alibaba
Apex blacklist, the Brazil fiscal vote, the Saryu-Kamala flag-off,
Fiji's school closure) and they are swapped out here. Stories from
earlier in the week (the COP31 collapse, the Indonesia factory fire,
the El Chapo Isidro capture, the Nvidia CEO return) were checked and
deliberately left out: they happened on 21–23 November, not on this day.

## How it is made

`main.py` (Python 3.13, standard library only) draws the whole page:
a hand-written PNG encoder, rectangle / circle / triangle primitives,
and a 5x7 bitmap font scaled up so every label stays legible at
300 pixels across. No network, no randomness, no wall clock — two
runs write identical bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
