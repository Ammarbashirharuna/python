#comprehension of sets
values = {x * 2 for x in range(5)}
print(values)
#comprehension of list
values = [x for x in range(10)]
print(values)
# this algo is exactly thesame as what is in line 5 and its more beautiful and
values = []
for x in range(7):
    values.append(x)
    print(values)
#dictionary comprehension
values = {x: x * 2 for x in range(5)}
print(values)