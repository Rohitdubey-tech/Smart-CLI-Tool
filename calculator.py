def calculator():
    print("Welcome to the calculator!")
    print("You can perform basic arithmetic operations: +, -, *, /")
    
    try:
        a = flaot(input("Enter the first number: "))
        op = input("Enter the operator (+, -, *, /): ")
        b = float(input("Enter the second number: "))

        if op == "+":
            print("Rsult: ", a+b)
        elif op == "-":
            print("Result: ", a-b)
        elif op == "*":
            print("Result: ", a*b)
        elif op == "/":
            if b != 0:
                print("Result: ", a/b)
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Error: Invalid operator.")
        
    except Exception as e:
        print("Error: ", e)