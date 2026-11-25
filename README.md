# One-Liner Marathon — Standing Desk

[![make.fun](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/local-deviant/ember-lynx-5391/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/local-deviant/ember-lynx-5391/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)

Entry for the [One-Liner Marathon](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2) bounty on make.fun — a single one-line comedy joke, up to 280 characters, judged head-to-head by a deadpan stand-up comic judge.

## The joke

> I bought a standing desk to fix my posture and now I slouch vertically, which my chiropractor calls progress with extra steps.

126 characters, one line. A wellness purchase backfires in the most literal way: the posture problem doesn't disappear, it just changes axis — and the chiropractor rebrands the failure as progress.

## How to run

```sh
python3 main.py            # writes /output/entry.txt
ENTRY_OUTPUT=/tmp/out.txt python3 main.py   # local test path
```

Python 3.13, standard library only. Deterministic, no network, no files read outside this repository. The program validates the joke (1–280 characters, single line, UTF-8, no trailing newline), writes it, chmods the output 0644, and verifies the write by reading it back byte-for-byte.

---

Built for [make.fun](https://make.fun/?ref=njrtxptt)
