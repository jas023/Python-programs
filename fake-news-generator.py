import random

subjects = ["SRK", "Salman Khan", "Big B", "Diljit Dosanjh"]
actions = ["shoots film in", "cancels show in", "flood hits", "big news from"]
places = ["Mumbai", "Goa", "Delhi", "Agra"]

print("📰 Welcome to Breaking News Generator 📰\n")

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"Breaking News: {subject} {action} {place}!"
    print(headline)

    userinput = input("\nDo you want a new headline? (yes/no): ").strip().lower()
    if userinput == "no":
        print("\nThanks for watching Breaking News! 📺")
        break
