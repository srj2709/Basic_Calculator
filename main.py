try:
    a = int(input("Enter the first number: "))

    b = int(input("Enter the second number: "))

    print("Choose an operation:\n1. Press + for Addition\n2. Press - for Subtraction\n3. Press * for Multiplication\n4. Press / for Division")
    
    o = input("Enter the operation: ")
    match o:
        case "+":
            print(f"The result of {a} + {b} is: {a + b}")
        case "-":
            print(f"The result of {a} - {b} is: {a - b}")
        case "*":
            print(f"The result of {a} * {b} is: {a * b}")
        case "/":
            if b!=0:
                print(f"The result of {a} / {b} is : {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        case default:
            print("Invalid operation selected. Please choose +, -, *, or /.")
    


except Exception as e:
    print(f"An error occurred: {e}")

