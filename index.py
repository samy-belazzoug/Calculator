def calculatrice():
    a = float(input())
    operator = input()
    
    
    if operator not in ["+","-","*","/","**","%","//"]: #User input management
        print("Wrong input, please retry : ")
        calculatrice()
    b = float(input())
    if operator == "/" and b == 0: #User input management
        print("Divion by 0 is mathematically impossible. You fool. : ")
        calculatrice()

    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return a/b
    elif operator == "**":
        return a**b
    elif operator == "%":
        return a%b
    else:
        return a//b

while 1 < 2:
    print(calculatrice())