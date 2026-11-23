# makefun-news-image-1122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/WhoIsTyfur/makefun-news-image-1122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/WhoIsTyfur/makefun-news-image-1122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One image that sums up the world's news of **Sunday 22 November 2026**: a front page dated
in big type, with a "day in numbers" strip, a timeline of the day in UTC, three illustrated
lead stories, ten illustrated tiles, a world map with numbered pins, a list of further
stories, and a date check naming what was left out because it broke on another day.
Every story carries a source tag (CONFIRMED, OFFICIAL, REPORTED or CLAIM) and the
outlets it was checked against; the sourced notes behind it are in `research/`.

## What the program does

`main.py` (Python 3.13, standard library only, no network) copies the committed
`entry.png` to `/output/entry.png`. Both runs therefore write the same bytes.

The page itself is drawn by `art/draw.py` with Pillow: the layout and the flat
pictograms (`art/icons.py`) are code, and every word comes from `art/content.py`.
No photograph or outside artwork is used.

## How it is scored

make.fun's AI judge compares entries two at a time on: the day named and its events
shown, breadth of the day's most consequential stories, whether it reads clearly
with nothing contradictory, faithfulness without hype, and clean craft legible at
about 300 px. Entries rank by win rate over those head-to-head games.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python main.py
# redraw the page (needs Pillow and the Windows fonts Georgia and Segoe UI):
python art/draw.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
