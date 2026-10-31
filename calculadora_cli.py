#%%
def calculator ():
    numbers = []
    operations = []
    result = 0

    while True:
        try:
            number = float(input("Enter a valid number: "))
            numbers.append(number)

        except ValueError:
            print("Enter a valid number: ")   

        oper = input("Selecione um operador: + - / * ")
        operations.append(oper)

        if len(numbers) < 2:
            print("Please enter a second number.")
            
        else:
            if oper == "+" or operations[-2] == "+":
                result += number
                print(f"The result is: {result}")
            elif oper == "-" or operations[-2] == "-":
                result -= number
                print(f"The result is: {result}")
            elif oper == "*" or operations[-2] == "*":
                result *= number
                print(f"The result is: {result}")
            elif oper == "/" or operations[-2] == "/":
                result /= number
                print(f"The result is: {result}")
            if oper == "=":
                break

calculator()