import random
import string

def generate_password(length):
    choice = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(choice) for i in range(length))
    return password
print(generate_password(10))