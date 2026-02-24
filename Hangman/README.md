# 🎮 Hangman Game

A classic command-line Hangman game built in Python, featuring ASCII art visuals and interactive gameplay.

---

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [How to Play](#how-to-play)
- [Example Gameplay](#example-gameplay)
- [Future Improvements](#future-improvements)

---

## About

This is a terminal-based Hangman game where the player tries to guess a hidden word one letter at a time. With each wrong guess, a part of the hangman figure is drawn using ASCII art. The game ends either when the player successfully guesses the word or runs out of trials.

---

## Features

- ASCII art hangman that updates with each wrong guess
- Tracks wrong guesses to avoid penalizing repeated letters
- Feedback for correct guesses including how many positions were filled
- Simple and readable game loop

---

## Project Structure

```
hangman/
│
├── main.py              # Main game logic and entry point
├── ascii_hangman.py     # ASCII art stages for the hangman figure
└── README.md            # Project documentation
```

---

## Requirements

- Python 3.x
- No external libraries required — only Python's built-in `random` and `time` modules

---

## How to Run

1. Clone or download this repository.
2. Make sure you have Python 3 installed.
3. Run the game from your terminal:

```bash
python main.py
```

---

## How to Play

1. The game will randomly select a secret word and display it as a series of underscores (e.g., `_ _ _ _`).
2. Enter one letter at a time as your guess.
3. If the letter is in the word, it will be revealed in its correct position(s).
4. If the letter is not in the word, you lose a trial and the hangman drawing progresses.
5. You win by guessing all letters before running out of trials.
6. You lose if the hangman is fully drawn before you complete the word.

---

## Example Gameplay

```
Welcome to Hangman game
You have to guess the hidden word correctly to win
Let's Get Started!

============================================================

  -----
  |   |
      |
      |
      |
      |
=========

_ _ _ _
You have 6 trials
Enter your guess: b

Correct guess!

b _ _ _
You have 6 trials
Enter your guess: z

Wrong guess

  -----
  |   |
  O   |
      |
      |
      |
=========
```

---

## Future Improvements

- Expand the word bank by loading words from an external file
- Add input validation to handle non-letter or multi-character inputs
- Track already-guessed correct letters to avoid redundant feedback
- Display previously guessed letters on each turn
- Add a "Game Over" message revealing the secret word when trials run out
- Add difficulty levels (easy / medium / hard) with varying word lengths or trial counts