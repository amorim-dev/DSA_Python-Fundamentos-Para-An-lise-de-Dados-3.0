print("***************Python calculator***************\n")
print("\n***Operations***\n""1 - sum\n" "2 - Subtraction\n" "3 - Multiplication\n" "4 - Division\n")


def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

operation = int(input("Choose the number of the operation you want to calculate (1,2,3,4): "))

num1 = int(input("\nType the first number: "))
num2 = int(input("Type the second number: "))

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
    print("\n")
    print(num1, "/", num2, "=", divide(num1, num2))
    print("\n")
else:
    print("The option that you select is incorrect, please try again")