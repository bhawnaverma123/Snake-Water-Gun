# Game-Python

Simple console implementation of the classic Snake–Water–Gun game (a variation of Rock–Paper–Scissors).

## Description

This small project contains a Python script that lets a user play a single round of Snake vs Water vs Gun against the computer. The computer chooses randomly and the program prints the result.

## Files

- [main.py](main.py) — Primary game script. Prompts for input (`s`, `w`, or `g`), maps them to Snake/Water/Gun, then compares with a random computer choice and prints the outcome.
- `main-shortcut-of-game.py` — (alternate/shortcut launcher; contents not provided here).

## Requirements

- Python 3.6 or newer

## How to run

Open a terminal in the project folder and run:

```bash
python main.py
```

When prompted, enter one of the following single-letter choices:

- `s` — Snake
- `w` — Water
- `g` — Gun

The program will display what you chose, what the computer chose, and whether you win, lose, or draw.

## Notes & Suggestions

- `main.py` currently assumes valid input and will raise an error for unexpected keys. Consider adding input validation and a replay loop for a better user experience.
- You can extend the game with score tracking, command-line options, or a GUI.

## License

No license specified — free to use and modify for personal projects.
