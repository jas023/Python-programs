#word_guessing_game
import random
print("-----------Welcome to guessing the word game-------------")
print("You have to guess the word, lets see if you can!")
print("Choose difficulty level!")
print("1. Easy level ")
print("2. Medium level")
print("3. Hard level")
level = input("Level: ").lower()

easy_words = ["cat", "dog", "sun", "ball", "tree"]
medium_words = ["garden", "purple", "school", "monkey", "planet"]
hard_words = ["astronaut", "crocodile", "mountain", "bicycle", "knowledge"]

if level == "easy":
    word = random.choice(easy_words)
elif level == "medium":
    word = random.choice(medium_words)
elif level == "hard":
    word = random.choice(hard_words)
else:
    print("Invalid Input! So, defaulting to easy level!")
    word = random.choice(easy_words)

attempts = 0
print("Guess the word.")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == word:
        print(f"Congratulations you gussed the word in {attempts} attempts!")
        break

    hint = ""

    for i in range(len(word)):
        if i < len(guess) and guess[i] == word[i]:
            hint += guess[i]
        else:
            hint += "_"
            
    print("Hint: " + hint)
    print("Game Over!")
        





