from ecommerce.shopping import sales
#importing the complete module as an object from package and sub package
import ecommerce.shopping.sales
"""here is the example of subpackage 
    as our program grow we should need a packages and sub packages so that is why we need to import sub packages
    from packages
"""
#calling it as an object from package and sub package
trying = ecommerce.shopping.sales.ship_calc(20,2)
print(trying)




calc =  sales.ship_calc(10,30)
print(calc)

cost = sales.cost_transfer(300,100)
print(cost)
#the dir function some times we can use it for debugging if something does'nt work as expected
print(sales.__package__)
print(sales.__name__)
print(dir(sales))

