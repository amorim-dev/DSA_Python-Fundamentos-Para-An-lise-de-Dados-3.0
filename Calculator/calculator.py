print("***************Python calculator***************\n")
print("\n***Operations***\n""1 - Sum\n" "2 - Subtraction\n" "3 - Multiplication\n" "4 - Division\n")


def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

operation = float(input("Choose the number of the operation you want to calculate (1,2,3,4): "))
valid_operations = [1,2,3,4]

if operation in valid_operations:
    num1 = float(input("\nType the first number: "))
    num2 = float(input("Type the second number: "))

    if (operation == 1):
        print("\n")
        print(num1, "+", num2, "=", add(num1, num2))
        print("\n")
    elif (operation == 2):
        print("\n")
        print(num1, "-", num2, "=", subtract(num1, num2))
        print("\n")
    elif (operation == 3):
        print("\n")
        print(num1, "x", num2, "=", multiply(num1, num2))
        print("\n")
    elif (operation == 4):
        if num2 == 0:
            print("\nYou can not divide by zero!\n")
        else:
            print("\n")
            print(num1, "/", num2, "=", round(divide(num1, num2),2))
            print("\n")
else:
    print("The option that you select is incorrect, please try again selecting one of the valid options: 1,2,3,4. \n")
