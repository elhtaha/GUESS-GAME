import random

def get_difficulty():
    print("\n🎮 Welcome to Guess the Number!")
    print("=" * 35)
    print("Choose a difficulty:")
    print("  1. Easy   — 1 to 50   (10 attempts)")
    print("  2. Medium — 1 to 100  (7 attempts)")
    print("  3. Hard   — 1 to 200  (5 attempts)")
    print("=" * 35)

    levels = {
        "1": ("Easy",   50,  10),
        "2": ("Medium", 100,  7),
        "3": ("Hard",   200,  5),
    }

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice in levels:
            return levels[choice]
        print("❌ Invalid choice. Please enter 1, 2, or 3.")


def play_game():
    level_name, max_number, max_attempts = get_difficulty()
    secret = random.randint(1, max_number)
    attempts = 0

    print(f"\n🔢 I'm thinking of a number between 1 and {max_number}.")
    print(f"   You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"  Attempts remaining: {remaining}")

        try:
            guess = int(input("  Your guess: "))
        except ValueError:
            print("  ⚠️  Please enter a valid number.\n")
            continue

        if guess < 1 or guess > max_number:
            print(f"  ⚠️  Please guess between 1 and {max_number}.\n")
            continue

        attempts += 1

        if guess == secret:
            print(f"\n🎉 Correct! You guessed it in {attempts} attempt(s)!")
            score = round((max_attempts - attempts + 1) / max_attempts * 100)
            print(f"⭐ Score: {score}/100")
            return
        elif guess < secret:
            hint = "📈 Too low!"
        else:
            hint = "📉 Too high!"

        # Give a hot/cold hint when close
        diff = abs(guess - secret)
        if diff <= max_number * 0.05:
            hint += " 🔥 Very close!"
        elif diff <= max_number * 0.15:
            hint += " 🌡️  Getting warmer..."

        print(f"  {hint}\n")

    print(f"\n💀 Out of attempts! The number was {secret}.")


def main():
    while True:
        play_game()
        while True:
            again = input("\n▶️  Play again? (1 = Yes / 2 = No): ").strip()
            if again == "1":
                break
            elif again == "2":
                print("\n👋 Thanks for playing! See you next time.\n")
                return
            else:
                print("  ⚠️  Please enter 1 or 2.")
 


if __name__ == "__main__":
    main()