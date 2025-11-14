print("Hello!")
act = input("Select your operation (+, -, *, /)")
num1 = int(input("Write your first number:"))
num2 = int(input("Write your second number:"))
if act == '+':
    resultp = (num1 + num2)
    print("Result:", resultp)
if act == '-':
    resultm = (num1 - num2)
    print("Result:", resultm)
if act == '*':
    resultu = (num1 * num2)
    print("Result:", resultu)
if act == '/':
    resultd = (num1 / num2)
    print("Result:", resultd)
