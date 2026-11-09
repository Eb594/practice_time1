while True:
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    operator = input("enter an operator(+, -, *, /): ")
    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        if num1 == 0:
            print("cannot divide by zero")
        else:
            print("Result:", num1 * num2)
    elif operator == "/":
        if num1 == 0:
            print("cannot divide by zero")
        else:
            print("Result:", num1 / num2)
    else:
        print("invalid operator!")
    print("\nDo another calculation or Press ctrl + c to exit.\n")
    