import secrets
import string
import os

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

def decryptNote(encryption, path, filename):
    with open(path+"/"+filename, 'r') as f:
        encrypted = f.readlines()

    return encrypted[0]

def deleteItem(path, filename):
    try:
        os.remove(path+"/"+filename)
    except OSError as e:
        print("Note does not exists.")