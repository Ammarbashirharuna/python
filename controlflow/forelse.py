successful = True
for number in range(3):
    if successful:
        print("Login Attemp")
        break
    else:
        print("sorry dude you cant")
Login = False
for number in range(5):
    if not  Login:
        print("it seems you have already login to the system sir")
        break
    else:
        print("okay welcome")
        break
