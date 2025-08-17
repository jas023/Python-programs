import random

number = random.randint(1, 50)   # computer picks a number
chances = 5                      # total chances for user

print("🎮 Welcome to Guess the Number!")
print("Guess the number from between 1 to 50.")
print(f"You have {chances} chances to guess it.\n")

for i in range(chances):
    guess = int(input(f"Chance {i+1}: Enter your guess: "))
    
    if guess == number:
        print("🎉 Correct! You guessed it!")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print(f"\n😢 Game Over! The number was {number}")
