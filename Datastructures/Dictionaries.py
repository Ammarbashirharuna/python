
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
#some program about Dictionary
employer = {
    "name": "john",
    "age": "50",
    "work":"engineer"

}
employer_age = employer["age"]
print(employer_age)
employer_name = employer["name"]
employer_work = employer["work"]
print(f"Hello {employer_name} welcome to our company it seems you are {employer_age} and you are {employer_work} in this company hope to do the work with carefulll!" )
point = dict(x=20,y=30,)
print(point)
point["x"] = 10
print(point)
#printing the value associated with x
print(point["x"])
#adding value to the dictionary
point["z"] = 80
print(point)
#deleting value from the dictionary
del point["z"]
print(point)
for key in point:
    print(key, point[key])