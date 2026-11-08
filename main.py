num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number "))
operator = input("enter an operator (-, +, *, /): ")
if operator == "+":
    print (num1 + num2)
elif operator == "-":
    print (num1 - num2)
elif operator == "*":
    print (num1 * num2)
elif operator == "/":
    if num1 / 0:
        print("cannot divide by zero")
    else:
        print (num1 / num2)

    