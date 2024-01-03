# main function
def main():
    expression = input("Expression: ")
    splited_expression = expression.split()
    x = splited_expression[0]
    y = splited_expression[1]
    z = splited_expression[2]

    if y == "+":
        print(f"{float(x) + float(z)}")
    elif y == "-":
        print(f"{float(x) - float(z)}")
    elif y == "*":
        print(f"{float(x) * float(z)}")
    elif y == "/" and z != 0 :
        print(f"{float(x) / float(z)}")


main()
