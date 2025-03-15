import random

def play_game():
    print("🎮 Welcome to the Number Guessing Game! 🎮")
    print("Guess a number between 1 and 100.")
    
    # Choose difficulty
    while True:
        difficulty = input("Select difficulty: 1️⃣ Easy (10 lives) | 2️⃣ Hard (5 lives) | ❌ Exit: ")
        if difficulty == "1":
            lives = 10
            break
        elif difficulty == "2":
            lives = 5
            break
        elif difficulty.lower() in ["exit", "no"]:
            print("Goodbye! 👋")
            return
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")

    number_guess = random.randint(1, 100)
    correct = False
    attempts = 0  # Track the number of guesses

    while not correct and lives > 0:
        try:
            number_try = int(input(f"\n🎯 Guess the number (Lives: {lives}): "))

            if number_try == number_guess:
                print(f"🎉 The number {number_try} was correct! You won in {attempts+1} attempts! 🏆")
                correct = True
            else:
                lives -= 1
                attempts += 1
                
                # Hints System
                if number_try > number_guess:
                    print("📉 Too high!")
                else:
                    print("📈 Too low!")

                # Warmer/Colder Hint
                difference = abs(number_guess - number_try)
                if difference <= 5:
                    print("🔥 You're very close!")
                elif difference <= 10:
                    print("🌡️ Getting warmer!")
                else:
                    print("❄️ Still far away...")

                if lives == 0:
                    print(f"💀 You ran out of lives. The correct number was {number_guess}.")
        
        except ValueError:
            print("❌ Please enter a valid number!")

    # Play Again Option
    play_again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing! See you next time! 👋")

# Start the game
if __name__ == "__main__":
    play_game()
