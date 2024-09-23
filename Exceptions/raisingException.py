def calculate(age):
    if age <= 0:
        raise ValueError("the number can not be zero")
    return 10 / age


try:
    calculate(-1)
except ValueError as error:
    print(error)