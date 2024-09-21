from sys import getsizeof
values = (x * 2 for x in range(10))
for x in values:
    print(x)
#printing the size of the generator object
values = (x * 2 for x in range(100000))
print("the size:",getsizeof(values))
#getting size of list
values = [x * 2 for x in range(100000)]
print(getsizeof(values))
