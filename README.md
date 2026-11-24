# One Word for Your Wi-Fi

[![make.fun](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A make.fun bounty entry: one word describing your Wi-Fi, aiming to be
both the funniest and the most accurate.

## The entry

**`Hideandseek`** — 11 characters, one word.

Bounty: *One Word for Your Wi-Fi* (`u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72`),
$2, entries close 28 Nov 2026 18:35 WIB. Verified locally: two runs of
`main.py` produce byte-identical output, sha256
`4cd72a14b3372ca530e40a4032ac6a0158cbb0942f4cd5d2e79e728e55677e31`.

The network appears in the list, then vanishes the moment you try to
connect. It literally plays hide-and-seek with you: instantly
understood, no explanation needed, and fresher than the words everyone
reaches for (`Slow`, `Laggy`, `Flaky`).

## How it works

`main.py` deterministically writes the word to `/output/entry.txt` —
no network calls, no randomness, no input. It asserts the gate itself:
1–20 characters, a single word, no whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## Judging (local, before picking the word)

Eight candidates were judged pairwise against the published brief
(on-subject, funny at once, true to home Wi-Fi, surprising angle,
instantly understood) by two independent local judges:

- **Caffeine router** — winner: `Moodswings`
- **Verboo deepseek-v4.1-flash** — winner: `Commitmentissues`

The two judges disagreed at the top, but `Hideandseek` placed 3rd in
**both** rankings — the most consistent word of the eight, never ranked
low by either judge — so it was picked for its high floor: concrete,
playful, recognisable, and readable at a glance as a network name.

## Files

- `main.py` — the entrypoint; writes the word to `/output/entry.txt`
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet

---

Referral code: `0txwmf1m`
