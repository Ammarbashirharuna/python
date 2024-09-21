values = [1,2,3,45,]
#unpacking
print(*values)
#unpacking itterable
print(*range(10))
values = [*range(10)]
print(values)
#unpacking strings
item = [*"hello worlsd hope we are all doing well"]
print(item)
#unpacking two variables
first = [1,45,6,78,89]
second = [3,46,67,8,89,]
unpacking = tuple([*first, *second])
print(unpacking)
#unpacking dictionaries
first = {"x": 20, "y": 30,}
second = {"m": 40, "y":80}
combined = {**first, **second}
print(combined)
