numbers = [2,4,56,7,89,78,34,]
largest =  numbers[0]
for number in numbers:
    if number > largest:
        largest = number
        print(f"the largest number is {largest}")
#finding the smallest number
numbers = [2,4,6,89,56,9,1]
smallest = numbers[0]
for small in numbers:
    if small < smallest:
        print(smallest)
product = [1,30,40,5,6,8,9,3]
for item in product:
    print(item)
#2D list
matrix =[
    [3,5,7,89,5,6],
    [4,55,77,88,90,],
    [2,3,68,77,65,23]
]
print(matrix[0][0:4])
for row in matrix:
    for item in row:
        print(item)
#sorting a list
numbers1 = [2,4,5,67,8,9,0]
numbers1.sort()
print(numbers1)
#adding item to a  list
numbers1.append(3)
print(numbers1)
#removing item from a list
numbers1.pop()
#reversing of a list
numbers1.reverse()
print(numbers1)