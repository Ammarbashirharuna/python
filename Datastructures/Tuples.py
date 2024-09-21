numbers = (1,2,5,6,78,7,)
print(numbers[0])
print(numbers)
#unpacking
numbers = (3,5,7)
x,y,z = numbers
print(x)
print(y)
print(z)
#tuples of product
item = ("beans","bread","milk","flour","egg","rice","spagetti")
ugent_item = item[4], item[2],item[-1]
print(ugent_item)
product = (2,3,5,67,7,8,)
print(product[3])
#practice
point = (1,2,3,4,6,4,7,3,4)
print(point)
if 3 in point:
    print("exists")
#swapping variable
x = 10
y = 30
x , y = y, X
print("X", x)
print("y", y)


