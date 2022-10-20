import secrets
import string

def passwordGenerator():
    temp = string.ascii_letters + string.punctuation + string.digits
    length = 24
    password = ""

    while len(password) != length:
        password += secrets.choice(temp)

    print(password)
    return password