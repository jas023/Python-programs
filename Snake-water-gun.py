import random

def game():
    print("Welcome to the game Snake Water Gun")
    user_choice = input("Enter your choice (Snake, Water or Gun): ").capitalize()
    computer_choice = random.choice(["Snake", "Water", "Gun"])
    print(f"You chose {user_choice} & computer chose {computer_choice}")

    # Win conditions for user
    if (user_choice == "Snake" and computer_choice == "Water") \
        or (user_choice == "Water" and computer_choice == "Gun") \
        or (user_choice == "Gun" and computer_choice == "Snake"):
        print("You win!")

    # Win conditions for computer
    elif (computer_choice == "Snake" and user_choice == "Water") \
        or (computer_choice == "Water" and user_choice == "Gun") \
        or (computer_choice == "Gun" and user_choice == "Snake"):
        print("Computer wins!")

    # Draw condition
    elif user_choice == computer_choice:
        print("It's a draw!")

    else:
        print("Invalid input. Please enter Snake, Water or Gun.")

# Call the function to play
game()
