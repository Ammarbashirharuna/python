print("welcome to password checker".title())
password = input("input your password for checking.....")
check = "123" in  password or "3456" in password or "09808" in password 
find = "abc" in password or "cfg" in password or "jgkh" in password or "mnc" in password or "kbdge" in password or "abc" in password
sign =  "@#$" in password or "&%$!" in password 
choice =  True or False
#checking the existing of numbers characters and signs
if check == True and find == True and sign == True:
    print("Nice password is very strong ...")
elif check == True and  find == True:
    print("yor passeord is medium you have to combine with some keywords...")
    print(password)
elif check == True and find == False:
    print("this password is very week to use as security")
#chainig operators
age = 90
if age <= age < 65:
    print("eligible")
else:
    print("not eligible")

