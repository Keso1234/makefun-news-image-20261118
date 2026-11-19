# The World in One Day — 18 November 2026

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Keso1234/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Keso1234/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

An entry for the [make.fun](https://make.fun) bounty
[news-image-20261118](https://make.fun/bounty/news-image-20261118):
sum up 18 November 2026's world news in one image.

## What it is

A front-page-style image of Wednesday 18 November 2026, drawn entirely
by code (PIL, no photographs):

- **Lead story — Gulf war escalates:** U.S. strikes an Iranian missile
  site on Qeshm Island; Iran hits U.S. bases in Kuwait and Bahrain.
- **Xi & Putin meet in Shenzhen** ahead of Thursday's trilateral summit
  with Trump.
- **Kerch Bridge hit** — a Ukrainian strike drops an arch into the strait.
- **Peltola flips Alaska** — Democrats take a 56–44 Senate majority.
- **Measles-free status lost** — 5,412 U.S. cases in 2026, after 26 years.
- **Voyager 1 goes further than ever** — one light-day from Earth,
  16 billion miles out.
- Ticker: Ebola in DR Congo passes 11,000 cases; Nvidia posts a record
  $115.8B quarter; Israel elects Matan Kahana speaker.

Sources: Reuters, Associated Press, AFP, NASA, WHO.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. `generate.py` is the program that drew the image;
re-running it reproduces the exact same bytes (fixed seed, no clock,
no network).

```sh
python3 generate.py entry.png   # rebuild the image
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
