import secrets
import string

def passwordGenerator(pool, length):
    password = ""

    while not check(password, pool):
        password = ""
        while len(password) != length:
            password += secrets.choice(pool)

    return password

def check(password, pool):
    check = True

    if string.ascii_lowercase in pool:
        check = check and any(x in password for x in string.ascii_lowercase)

    if string.ascii_uppercase in pool:
        check = check and any(x in password for x in string.ascii_uppercase)

    if string.digits in pool:
        check = check and any(x in password for x in string.digits)

    if string.punctuation in pool:
        check = check and any(x in password for x in string.punctuation)

    return check