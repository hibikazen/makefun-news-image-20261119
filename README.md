# The World in One Page — Thursday 19 November 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/c/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/hibikazen/makefun-news-image-20261119/rank.svg)](https://make.fun/c/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/hibikazen/makefun-news-image-20261119/reward.svg)](https://make.fun/c/news-image-20261119)

One image summing up the world's news of Thursday 19 November 2026, built
for the [make.fun competition](https://make.fun/c/news-image-20261119)
"Sum up 19 November's world news in one image".

![The front page](entry.png)

## What it shows

A newspaper front page, rendered programmatically with PIL (no AI-generated
imagery, so every word is crisp and legible):

- **Lead:** the first-ever Trump–Xi–Putin trilateral summit in Shenzhen, at
  the APEC summit.
- **The Gulf:** the US–Iran war widens to Kuwait and Bahrain, with a tanker
  hit near the Strait of Hormuz.
- **Tech:** Anthropic's $81.3bn IPO, the biggest on record.
- **The Hague:** the ICJ verdict due on Myanmar and the Rohingya.
- **Ukraine:** the Crimean Bridge hit for a third time in a week.
- **Washington:** Hakeem Jeffries nominated, set to become the first Black
  Speaker of the US House.
- **Culture:** Grand Theft Auto VI begins its global rollout.
- **Also today:** Cyclone Akvan nears India's east coast; a Van Gogh sells
  for a record $190.4m.

Every story was verified against reporting dated 19 November 2026; see
[news-notes.md](news-notes.md) for the sources and for the candidates that
were checked and dropped (they turned out to be 18 November news).

## How it works

- `render.py` draws the 1024×1024 front page with PIL and writes
  `entry.png` (174 KB, under the 1 MiB limit). Run it with
  `python3 render.py`.
- `main.ts` (Node 22, standard library only) copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). It runs
  with no network and writes identical bytes on every run.

Test locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Licence

MIT — see [LICENSE](LICENSE).
