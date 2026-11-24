# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5)
[![Rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Revaaa28/makefun-say-what-broke/rank.svg)](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5)
[![Reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Revaaa28/makefun-say-what-broke/reward.svg)](https://make.fun/competitions/u-po-pu-say-what-actually-broke-a2c153b5)

A [make.fun](https://make.fun) entry for the **Say What Actually Broke**
competition: one line of software error copy, at most 200 characters, that
tells the user the brutal truth about what went wrong and makes them laugh.

## The entry

> The build failed on line 42, which is the exact line someone marked 'TODO: fix later' in 2019. Later is now.

108 characters, one line. The failure is named in plain words — the build
failed on a specific line — the next step is obvious (fix line 42), and the
punch lands in the last three words.

## How it works

`main.py` writes that single sentence to `/output/entry.txt`, exactly as-is,
with no trailing newline. Before writing it self-checks the competition gate:
one line, 1–200 characters, not only whitespace.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Requires Python 3. No dependencies, no network, no secrets.

## Candidate selection

Twelve candidate sentences were written and ranked by hand against the
kit's judge-brief criteria in their stated order, plus pairwise checks
against strong rival shapes. The full list and the reasoning are in
[`candidates.md`](candidates.md).

## License

MIT — see [LICENSE](LICENSE).
