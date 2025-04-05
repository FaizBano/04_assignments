def add():
    print(" This program adds two numbers.")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    total : int = num1 + num2
    print(f"The sum of {num1} + {num2} = {total}. ")


if __name__ == '__main__':
    add()