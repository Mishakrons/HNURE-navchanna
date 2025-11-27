def res_nump(num1, num2):
    print("Result:", num1 + num2)


def res_numm(num1, num2):
    print("Result:", num1 - num2)


def res_numu(num1, num2):
    print("Result:", num1 * num2)


def res_numd(num1, num2):
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero!")


def result():
    act = input("Select your operation (+, -, *, /): ")
    num1 = int(input("Write your first number: "))
    num2 = int(input("Write your second number: "))

    if act == "+":
        res_nump(num1, num2)
    elif act == "-":
        res_numm(num1, num2)
    elif act == "*":
        res_numu(num1, num2)
    elif act == "/":
        res_numd(num1, num2)
    else:
        print("Unknown operation!")

    answ = input("Do you want to continue? (yes/no): ")
    if answ == "yes":
        result()
    if answ == "no":
        print("Good bye!")
    else:
        return


result()
