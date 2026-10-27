#%%

number1 = float(input("Write the first number:"))
op = str(input("Enter the desired operation: \
    + : Addition \
    - : Subtraction \
    * : Multiplication \
    / : Division"))
number2 = float(input("Write the second number:"))    
    
def calculator(number1,  number2, op):

    if op == "+":
        result = (number1 + number2)
        print(f"The result is {result}")
    elif op == "-":
        result = (number1 - number2)
        print(f"The result is {result}")
    elif op == "*":
        result = number1 * number2
        print(f"The result is {result}")
    elif op == "/":
        result = (number1 / number2)
        print(f"The result is {result}")
    else:
        print("Oops, please reset your account!")


calculator (number1, number2, op)
