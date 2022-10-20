import secrets
import string

def passwordGenerator(pool, length):
    password = ""

    while len(password) != length:
        password += secrets.choice(pool)

    return password