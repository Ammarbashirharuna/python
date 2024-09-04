customer = {
    "name": "ammar bashir",
    "age": "30",
    "is_married": False
}
customer["birth"] = "1990"
print(customer.get("name"))
print(customer.get("birth"))
#try
print("welcome " + customer.get("name") +  " it seems your are  " + customer.get("age"))