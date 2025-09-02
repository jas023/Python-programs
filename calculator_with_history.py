# Calculator with history
HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
        if len(lines) == 0:
            print("No history found")
        else:
            print("\n--- Calculation History ---")
            for line in reversed(lines):   # show most recent first
                print(line.strip())
    except FileNotFoundError:
        print("No history file found yet")

def clear_history():
    with open(HISTORY_FILE, 'w') as file:
        pass
    print("History is cleared")

def save_to_history(eq, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(eq + " = " + str(result) + "\n")

def calculator(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input! Use syntax: number operator number")
        return

    try:
        n1 = float(parts[0])
        n2 = float(parts[2])
    except ValueError:
        print("Invalid numbers!")
        return

    op = parts[1]

    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        if n2 == 0:
            print("Error: Division by zero")
            return
        result = n1 / n2
    else:
        print("Invalid operator! Use + - * /")
        return

    # if result has no decimals, make it integer
    if int(result) == result:
        result = int(result)

    print("Result:", result)
    save_to_history(user_input, result)

def main():
    print("------- Welcome to Simple Calculator with History -------")
    while True:
        user_input = input("\nEnter calculation using ( +, - , *, / ) or command (history, clear, exit): ").strip().lower()
        if user_input == 'exit':
            print("Thank you for using the calculator!")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculator(user_input)

main()
