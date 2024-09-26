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
    products.append(add)
    if add == 'finish':
        products.pop()
        print(f"the item you have buy is {products} Thanks for buying this product from our shop!")
        break
checkout = input("Do you want checkout the product?".lower())
if checkout == "y":
    product = dict(products)
    print(products)
    # for key in products:
    #     print(key, products[key])








