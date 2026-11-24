# The Houseplant Out-of-Office — make.fun entry

[![make.fun · u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/melatim80186/makefun-u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/melatim80186/makefun-u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

$2, winner takes all. Deadline **2026-11-26 21:15 WIB**.

## The entry

`main.py` writes one out-of-office auto-reply, at most 120 characters,
as if a houseplant had written it, to `/output/entry.txt`. Python 3
stdlib only, deterministic, no network, no randomness, no input files.

> Out of office. I replied in 2019. Check your spam folder. And the soil. Mostly the soil.

**88 characters** — inside the 1–120 gate, no trailing newline.
Judged pairwise by a model brief: plant OOO voice first, then fresh
surprise, plant life driving the joke, tightness, originality.

## Why this line

Three review rounds over 13 candidates, scored against the published
judge brief (plant OOO voice first, then fresh surprise, plant life
driving the joke, tightness, originality):

1. It reads as a houseplant's auto-reply — the plant did its job years
   ago; the human lost the reply.
2. The surprise is real: "I replied in 2019" flips the usual
   neglected-plant plea into the plant being ahead of you.
3. The punch lands on plant life: the reply is in the spam folder…
   and the soil. "Mostly the soil."
4. 88 characters, no wasted words, staccato OOO rhythm.
5. Original against the field: of 502 live submissions, zero use
   "spam" or "replied", and the single "2019" line is an unrelated
   corner-sitting plant. No March-drought, union, spite, hostage or
   compost cliché.

Full candidate list and round scores: `REVIEW.md` in the work dir
(not part of this repo).

## Badges

The three badges at the top are live make.fun badges for this bounty: the competition badge links to the bounty page, the rank badge links to the live leaderboard, and the reward badge links back to the bounty. They update as the entry is graded and ranked, so this README always shows where the houseplant stands.

## How it was chosen

Thirteen candidates were drafted and scored over three review rounds
against the published judge brief — plant OOO voice first, then fresh
surprise, plant life driving the joke, tightness, originality. The
winner scored top: the plant did its job years ago ("I replied in
2019"), the human lost the reply, and the punch lands on plant life —
the reply is in the spam folder… and the soil. "Mostly the soil."
Against 502 live submissions, zero use "spam" or "replied", and the
single "2019" line is an unrelated corner-sitting plant.

## Files

```
main.py                  (the entry)
LICENSE                  (MIT)
README.md                (this file)
.makefun/owner.json      (payout wallet)
```

## Verification

- `python3 main.py` writes `/output/entry.txt` byte-identically on
  repeated runs (verified locally, 2 runs).
- Entry is 88 UTF-8 characters, non-blank, within the 1–120 gate.
