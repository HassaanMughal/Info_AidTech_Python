import random

def roll_dice(num_dice):
    # Simulate rolling the dice
    dice_values = [random.randint(1, 6) for _ in range(num_dice)]
    return dice_values

def display_dice(dice_values):
    # Display the result of rolling the dice
    print("\nDice values:")
    for i, value in enumerate(dice_values, start=1):
        print(f"Dice {i}: {value}")
    print(f"Total: {sum(dice_values)}\n")

print("Welcome to the Dice Rolling App!")

while True:
    try:
        num_dice = int(input("Enter the number of dice you want to roll (or 0 to quit): "))
        if num_dice < 0:
            print("Please enter a positive number.\n")
            continue
        elif num_dice == 0:
            print("Thank you for using the Dice Rolling App. Goodbye!")
            break
        dice_values = roll_dice(num_dice)
        display_dice(dice_values)
    except ValueError:
        print("Invalid input. Please enter a valid number or 0 to quit.\n")
