# Coin Guessing Game

A simple command-line coin toss guessing game written in Python that allows users to predict the outcome of a virtual coin flip.

## Description

This interactive game simulates a coin toss and challenges players to guess whether the coin will land on heads or tails. The program offers two different random number generation methods for the coin toss, adding an educational element about Python's random module.

## Features

- Interactive command-line interface
- Two random number generation methods:
  - `random.randint()` - Generates 0 or 1
  - `random.random()` - Generates a float between 0 and 1
- Input validation for both method selection and user guesses
- Immediate feedback on win/loss results

## Requirements

- Python 3.x
- No external dependencies (uses only Python's built-in `random` module)

## How to Run

```bash
python heads_or_tails.py
```

## How to Play

1. Launch the game
2. Choose a random number generation method (1 or 2)
3. Enter your guess:
   - `h` for heads
   - `t` for tails
4. See if you won or lost!

## Game Logic

### Method 1: `random.randint(0, 1)`
- If random number = 0 → Tails
- If random number = 1 → Heads

### Method 2: `random.random()`
- If random number > 0.5 → Tails
- If random number < 0.5 → Heads

## Code Structure

- `judge(computer, user_choice)` - Compares the computer's result with the user's guess and returns the outcome message
- `main()` - Main game loop handling user input, random generation, and game flow

## Example Output

```
Welcome to the Coin Guessing Game
==========************=================
Choose a method to toss the coin:
1.Using random.randint()
2.Using random.random()
Enter your choice (1 or 2):
1
Enter your Guess (h) for heads or(t) fortails)
h
===congratulations! you won===
    The computer's coin toss is :h
```

## License

This project is open source and available for educational purposes.