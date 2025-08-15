def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "Error! Division by zero ia not possible."
    return x/y

print("Select operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice of operation (1,2,3,4): ")
    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
        except ValueError:
            print("Invalid input, Please enter a number. ")
            continue
        
        if choice == '1':
            print(f"Result: {add(num1,num2)}")
            
        elif choice == '2':
            print(f"Result: {sub(num1,num2)}")
            
        elif choice == '3':
            print(f"Result: {mul(num1,num2)}")
            
        elif choice == '4':
            print(f"Result: {divide(num1,num2)}")
            
        else:
            print("Invalid choice.")        
            
    next_calc = input("Do you want another calculation? (yes/no): ")
    if next_calc.lower() != 'yes':
           break