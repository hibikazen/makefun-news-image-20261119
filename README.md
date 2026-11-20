# The World in One Page — Thursday 19 November 2026

[![make.fun](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/c/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/hibikazen/makefun-news-image-20261119/rank.svg)](https://make.fun/c/news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/hibikazen/makefun-news-image-20261119/reward.svg)](https://make.fun/c/news-image-20261119)

One image summing up the world's news of Thursday 19 November 2026, built
for the [make.fun competition](https://make.fun/c/news-image-20261119)
"Sum up 19 November's world news in one image" —
[bounty page](https://make.fun/bounty/news-image-20261119).

![The front page](entry.png)

## What it shows

A newspaper front page, rendered programmatically with PIL (no AI-generated
imagery, so every word is crisp and legible):

- **Lead:** the first-ever Trump–Xi–Putin trilateral summit in Shenzhen ends
  with a four-point "Declaration Towards Peace" — UN reform, oil supply,
  ICC limits, nuclear-risk talks — but no mention of Ukraine.
- **The Gulf:** attacks on ships near the Strait of Hormuz hit a record
  pace, about 14 in November so far.
- **Tech:** Anthropic's first day on Nasdaq: ANT opens at $111.50, closes
  at $97.17, up 17% on the $83 IPO price.
- **The Hague:** the ICJ finds Myanmar guilty of state-sponsored genocide
  against the Rohingya — the first state ever held responsible.
- **Ukraine:** the Crimean Bridge hit for a third time in a week.
- **Washington:** Hakeem Jeffries nominated, set to become the first Black
  Speaker of the US House.
- **Culture:** Grand Theft Auto VI begins its global rollout.
- **Also today:** Cyclone Akvan nears India's east coast (~50,000
  evacuated in Odisha, landfall expected Friday); a Van Gogh sells
  for a record $190.4m.

Every story was verified against reporting dated 19 November 2026; see
[news-notes.md](news-notes.md) for the sources and for the candidates that
were checked and dropped (they turned out to be 18 November news).

## How it works

- `render.py` draws the 1024×1024 front page with PIL and writes
  `entry.png` (176 KB, under the 1 MiB limit). Run it with
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
