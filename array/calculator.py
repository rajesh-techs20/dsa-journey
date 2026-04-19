import math

def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    elif op == "^":
        return a ** b
    elif op == "%":
        if b != 0:
            return a % b
        else:
            return "Cannot mod by zero "
    else:
        return "Invalid operation "


while True:
    print("\n Calculator Menu")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. ^ (power)")
    print("6. % (modulus)")
    print("7. √ (square root)")
    print("8. Exit")

    choice = input("Enter choice:")

    if choice == "8":
        print("Exiting")
        break

    if choice == "7":
        a = float(input("Enter number: "))
        print("Result:", math.sqrt(a))
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    op_map = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
        "5": "^",
        "6": "%"
    }

    if choice in op_map:
        op = op_map[choice]
        print("Result:", calculator(a, b, op))
    else:
        print("Invalid choice")