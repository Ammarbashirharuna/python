Login_attempt = 0
try_login = 3
while Login_attempt < try_login:
    login = input("enter your password")
    if login == "123":
        print("welcome sir")
        break
    else:
        login