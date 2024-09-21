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
#using  * to repeat item of a list
letters = ["mango", "banana", "apple"]
print(letters[0 ] * 3)
#concatinating a list
nums = [1,4,5,6,78,]
item = ["guava", "apple", "goruba"]
concatinate = nums + item
print(concatinate)
#using list function 
numbers = list(range(20))
print(numbers)
print(len(numbers))
#reversing of an item in a list
print(numbers[::-1])
#unpacking list
product = ["kwakwa", "milk","banana", "rice", "beans"]
kwakwa , milk , banana , rice, beans = product
print(kwakwa, milk)
#unpacking specific item from the list
kwakwa , milk, *others = product
print(kwakwa)
print(milk)
print(others)
#uncpacking first and last item from the list
milk, *others, beans = product
print(beans)
print(others)
# looping over the list
for item in product:
    print(item)
#adding item to  a list
product.append("gurasa")
print(product)
#removing item from the end of the list
product.pop()
print(product)
#removing item from the specific index
product.pop(3)
print(product)
#replacing item from the list using its name
product.remove("milk")
print(product)
#finding the item in a list
item = ["oil","fish","egg","meat","apple"]
print(item.index("oil"))
print(item)
#sorting list
nums = [1,4,7,3,9,6]
nums.sort()
print(nums)
#sorting an item from a  tuple
products = [
    ("waina1", 10),
    ("waina2", 8),
    ("waina3", 15)
]
def sort_item(products):
    return products[1]
products.sort(key=sort_item)
print(products)
#using lambda function instead of defining another function we can use lambda anonymous function
products.sort(key=lambda products:product[1])
print(products)
items = [
    ("kwakwa", 50),
    ("kwakwa", 80),
    ("kwakwa", 30),
    ("mik",70),
    ("rice",40),
    ("egg",60)
]
price = map(lambda items: items[1], items)
#looping over the price
for item in price:
    print(item)
#printing them as a list
prises = list(map(lambda items: items[1], items))
print(prises)
#using list comprehension
prices = [item[1] for item in items]
print(f"this is better {prices}")
#filter an item from the list
filtered = list(filter(lambda items: items[1] > 30, items))
print(filtered)
#using list comprehension
filtered = [item for item in items if item[1] > 30]
print(filtered)
#Zip function to combine the two list together
first_list = [1,4,6,7,8]
second_list = ["mango", "banana","apple","date","guava","pawpaw"]
zipping = zip(first_list,second_list)
print(list(zipping))