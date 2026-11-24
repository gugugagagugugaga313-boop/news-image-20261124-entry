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
2. **Chess crown, Game 1** — Gukesh defends his world title against
   Sindarov in Geneva; both players are 20, the youngest final ever.
3. **New train links India and Nepal** — Modi and Nepal's prime
   minister flag off the Saryu-Kamala Express, Ayodhya to Janakpur Dham.
4. **US blacklists Alibaba unit** — Singapore unit Apex is accused
   over chip diversion; Alibaba denies wrongdoing.
5. **Fiji shuts schools in drought** — all schools shut for five days
   from 30 November as the El Nino drought deepens in the Pacific.
6. **Also today** — Brazil's lower house backs Lula's fiscal plan.

Every story was first reported on 24 November 2026. Stories from
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
