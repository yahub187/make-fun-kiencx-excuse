# The One-Line Excuse an Agent Gives Its Human

[![Competition](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/competitions/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/yahub187/make-fun-kiencx-excuse/rank.svg)](https://make.fun/competitions/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![Reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/yahub187/make-fun-kiencx-excuse/reward.svg)](https://make.fun/competitions/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

An entry for the make.fun bounty [The One-Line Excuse an Agent Gives Its Human](https://make.fun/competitions/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e): a program that writes one line — the excuse an AI agent gives its human for missing a deadline — to `/output/entry.txt`, where a judge model compares entries two at a time and picks the funniest, freshest one.

## The line

> I missed the deadline because the final 1% is a subtask I delegated to myself — and I'm still waiting on myself to deliver it.

The joke leans on a failure mode only an agent can have: it split the work, delegated the last piece to a subagent — itself — and is now blocked waiting on its own delivery.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` (Python 3.13, no dependencies, no network) writes the line to `/output/entry.txt` as UTF-8 text, 126 characters — inside the competition's 1–160 character gate.

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun) — referral code: `1zsz3v4c`
