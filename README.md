# Guess The Number Game

A simple Python terminal game where the player tries to guess a randomly generated number within a limited number of attempts.  
The game includes multiple difficulty levels, score calculation, input validation, and hint messages to make the experience more interactive.

## Features

- 3 difficulty levels:
  - Easy: numbers from 1 to 50 with 10 attempts
  - Medium: numbers from 1 to 100 with 7 attempts
  - Hard: numbers from 1 to 200 with 5 attempts
- Random number generation
- Input validation
- Higher / lower hints
- Extra hot/cold style hints when the guess is close
- Score calculation
- Replay option

## Technologies Used

- Python
- `random` module

## How It Works

1. The player chooses a difficulty level.
2. The program generates a random secret number.
3. The player enters guesses until:
   - the correct number is found, or
   - the attempts run out.
4. After each wrong guess, the game provides hints:
   - Too low
   - Too high
   - Very close
   - Getting warmer
5. At the end, the player can choose to play again.

## How to Run

1. Make sure Python is installed on your computer.
2. Save the code in a file, for example:

```bash
guess_game.py
