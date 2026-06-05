# Pray — App Development Roadmap

This folder contains the future native application implementations of Pray.

The Python CLI tool (`pray.py`) is the working proof of concept. The apps
will bring the same prayers to broader audiences on all platforms.

## Platform Plan

| Platform | Folder     | Approach                        | Status  |
|----------|------------|---------------------------------|---------|
| macOS    | `macos/`   | SwiftUI + AVSpeechSynthesizer   | Planned |
| iOS      | `ios/`     | Shared SwiftUI codebase         | Planned |
| Windows  | `windows/` | Electron or Python/PyQt         | Planned |
| Linux    | `linux/`   | Electron or Python/tkinter      | Planned |

## Design Principles

- Simple — prayer selector, language selector, voice selector, one button
- Multilingual — every language the prayer has traveled
- Unhurried — rate control, meditative pacing
- Free — no cost, no ads, no account required
- Open — MIT licensed, contributions welcome

*"Ask, and it shall be given you." — Matthew 7:7*
