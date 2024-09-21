#xars we use when we want call morethan two argument in a parameter
def numbers(*numbers):
    return numbers


print(numbers(1,4,7,8,90,))
#xxargs can use it to pass
def save_user(**user):
    print(user)


user = save_user(id=1,name="ammar",age=40)
print(user)