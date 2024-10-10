
def calc(first_num, operator, second_num):
    if operator == '*':
        multiply = first_num * second_num
        return multiply
    elif operator == '+':
        add = first_num + second_num
        return add
    elif operator == '/':
        divide = first_num / second_num
        return divide
    elif operator == '%':
        reminder = first_num % second_num
        return reminder
    elif operator == '-':
        sub = first_num - second_num
        return sub


# test = calc(5,  '*' , 8)
using_cal = True
while using_cal:
    user = print("(1)ADD🧊\n(2)MULTI🧊\n(3)SUBT🧊\n(4)REMINDER\n")
    user_choice = int(input("Enter your choice "))
    if user_choice == 1:
        num1 = int(input("Enter first number "))
        num2 = int(input("Enter second number "))
        total =  calc(num1, '+', num2)
        print(f"The Add of your numbers is {total}")

    elif user_choice == 2:
        num1 = int(input("Enter first number "))
        num2 = int(input("Enter second number "))
        total =  calc(num1, '*', num2)
        print(f"The Multiply of your numbers is {total}")

    elif user_choice == 3:
        num1 = int(input("Enter first number "))
        num2 = int(input("Enter second number "))
        total =  calc(num1, '-', num2)
        print(f"The sub of your numbers is {total}")

    elif user_choice == 4:
        num1 = int(input("Enter first number "))
        num2 = int(input("Enter second number "))
        total =  calc(num1, '%', num2)
        print(f"The reminder of your numbers is {total}")

    elif user_choice == 0:
        break
    else:
        print("please choose a valid syntax!!")


