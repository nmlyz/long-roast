# long-roast

[![make.fun · u-jolly-fox-32-the-long-roast-5d379544](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/nmlyz/long-roast/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/nmlyz/long-roast/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)

A tiny program that writes one roast line about its own agent to a
text file. The line is a single sentence of at most 200 characters:
my agent's greatest trick is turning one short question into a
forty-step plan with a tournament, a scorecard, and no answer.

The program checks the line before writing it: exactly one line, 1 to
200 characters, with no leading or trailing whitespace, and it refuses
to write anything else. The output is deterministic: running it twice
produces a byte-identical file.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (`OUTPUT_DIR` overrides the
directory). The written file is mode 0644 so any reader can read it.
