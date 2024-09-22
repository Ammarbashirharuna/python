products = []
available_product = {"Milk":50,
"Egg":20,
"Rice":30,
"Bugger":45,
"Shawma":50,
"Fish":10,
"Apple":15,
"pawpaw":13,
"cocumber":60,
"guava":100
}

maximum_product = len(available_product)

print(available_product)
while True:
    add = input("Add product to Cart ")
    print(f"you have added {add} to your shopping item")
    products.append(products)
    if add == 'finish':
        products.pop()
        print(f"the item you have buy is {products} thanks for buying from our store")
        break
pay = input("Do you want to cashout your product?  Y/N")
if pay := "Y":
    total = 0
    for value in available_product:
        total += value
        print(f"the total item you have buy is {total}")
        print("Cash please")







