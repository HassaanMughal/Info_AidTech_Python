import random

def play_game():
    number = random.randint(1, 100)
    attempts = 10

    print("\nLet's Begin the Guessing Game...")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have only {attempts} attempts to guess the correct number.")

    while attempts > 0:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess == number:
                print("\nYou guessed the correct number.")
                return True

            if guess < number:
                print("\nToo low!")
            else:
                print("\nToo high!")

            attempts -= 1
            print(f"Attempts left: {attempts}")

        except ValueError:
            print("\nInvalid input. Please enter a number.")

    print("\nGame over! You ran out of attempts.")
    print(f"The number I was thinking of was: {number}")
    return False

def play_again():
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            return True
        elif play_again.lower() == "no":
            return False
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")

# Start of the game
print("\nWelcome to the Number Guessing Game!")
print("Following are the rules of this Number Guessing Game: ")
print("1. This is a Number Guessing Game. Please only enter numbers as your guesses.")
print("2. You have only 10 attempts to guess the number correctly, or else you will fail.")
print("3. You can choose to play the game again or quit.")

name = input("\nEnter your name to start the game: ")

while True:
    if play_game():
        print("Congratulations, You won!")
    else:
        print("Better luck next time!")

    if not play_again():
        print("\nThank you for playing!")
        break
