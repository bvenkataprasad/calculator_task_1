def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

while True:
    print("\nChoose an operation:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Division")
    print("4: Multiplication")
    print("5: Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Exiting calculator... Goodbye!")
        break

    if choice in [1, 2, 3, 4]:
        a = float(input("Enter your first number: "))
        b = float(input("Enter your second number: "))

        if choice == 1:
            print("Result:", add(a, b))
        elif choice == 2:
            print("Result:", sub(a, b))
        elif choice == 3:
            print("Result:", div(a, b))
        elif choice == 4:
            print("Result:", mul(a, b))
    else:
        print("Invalid choice. Please choose between 1 and 5.")
