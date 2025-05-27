# build a simple calculator. Write a python program that works like a basic calculator in the terminal, It should ask the user to enter the first number, the second number, the operation that is to be used then the program should calculate and print the results based on the previous inputs

# first_number = float(input("Please input the first number: "))
# second_number = float(input("Please input the second number: "))
# operator = input("Enter operator: ")
# def calculator(first_number,operator,second_number):
#     return eval(f"{first_number} {operator} {second_number}")
# print(calculator(first_number,operator, second_number))


# 2nd trial.
num1 = float(input("please input the first number: "))
num2 = float(input("please input the second number: "))
operator = input("Operator please (+,-,*,/): ")
def calculator(num1,operator,num2):
    if operator == "+":
        return(num1 + num2)
    elif operator == "-":
        return(num1 - num2)
    elif operator == "/":
        if num2 == 0:
            return "Error: division by zero is infinity so no"
        return(num1/num2)
    elif operator == "*":
        return(num1*num2)
    else:
        return("Error: invalid operator.")

def calculate():
    try:
        solving = calculator(num1,operator,num2)
        print("Solution = ", solving)
    except ValueError as error:
        print(error, "This is an error please use numbers only")
    
calculate()