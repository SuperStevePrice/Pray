# Pray

> *"The wind bloweth where it listeth, and thou hearest the sound thereof,*
> *but canst not tell whence it cometh, and whither it goeth:*
> *so is every one that is born of the Spirit."*
> — John 3:8

Hear sacred prayers spoken in many voices, in many languages, on many platforms.

---

## What This Is

**Pray** is an open-source project that brings ancient prayers to modern computing
platforms — beginning with a Python command-line tool for macOS, with native apps
for macOS, iOS, Windows, and Linux planned.

The project was conceived by Rodney Stephen Price (called Steve), an Episcopal lay
preacher and retired software engineer, in a conversation about the meaning of the
word *bitte* in the German Hail Mary. It was built in collaboration with Claude,
Anthropic's AI assistant — an example of human devotional intention and artificial
capability working together toward a prayerful end.

---

## Current Release: pray.py

A Python command-line tool for macOS using the built-in `say` command.

### Requirements
- macOS (any recent version)
- Python 3.9+
- No external dependencies

### Installation
```bash
python3 installPray.py
```

### Usage
```bash
pray.py                                      # show help
pray.py --list                               # list all prayers, languages, voices
pray.py --prayer ave --language italian      # Ave Maria in Italian
pray.py --prayer lords --language german     # Lord's Prayer in German
pray.py --prayer ave --language latin        # Ave Maria in Latin (Italian voices)
pray.py --all --prayer ave                   # all Ave Maria combinations
pray.py --all --language french              # all prayers in French
pray.py --all --voice Grandma                # Grandma prays everything
pray.py --rate 80                            # meditative pace
```

### Prayers
| Key     | Prayer           | Languages |
|---------|-----------------|-----------|
| `ave`   | Ave Maria        | English, German, Italian, Latin, French, Spanish, Portuguese, Polish |
| `lords` | Lord's Prayer    | English, German, Italian, Latin, French, Spanish, Portuguese, Polish |

### Testing
```bash
python3 testPray.py              # test all prayers
python3 testPray.py --prayer ave # test Ave Maria only
python3 testPray.py --dry-run    # preview without audio
```
Logs are written to `logs/test_pray_TIMESTAMP.log`.

---

## Adding a New Prayer

1. Create `prayers/my_prayer.py` following the pattern in `prayers/ave_maria.py`
2. Import and register it in `prayers/__init__.py`
3. Run `python3 testPray.py` to verify

---

## Future Development

Native apps for macOS, iOS, Windows, and Linux are planned.
See the [`app/`](app/) folder for roadmap and architecture notes.

**Additional languages welcome.** Each language requires a text entry and the
appropriate system voice. Pull requests from any language community are welcome.

---

## License

MIT — free to use, modify, and extend for any purpose.

---

*Ave Maria, gratia plena. Pater noster, qui es in caelis.*
