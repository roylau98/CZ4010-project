import secrets
import string
import os
import json

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

def saveNote(encryption, path, filename):
    with open(path+"/"+filename, 'w') as f:
        f.write(encryption)

def deleteItem(path, filename):
    try:
        os.remove(path+"/"+filename)
    except OSError as e:
        print("Note does not exists.")

def deleteFromJson(key, type):
    with open('items.json', 'r') as f:
        allItems = json.load(f)

    typeItems = allItems[type]

    del typeItems[key]
    allItems[type] = typeItems

    with open('items.json', 'w', encoding='utf-8') as f:
        json.dump(allItems, f, ensure_ascii=False, indent=4)

def updateJson(key, updated, type):
    with open('items.json', 'r') as f:
        allItems = json.load(f)

    typeItems = allItems[type]
    typeItems[key] = updated
    allItems[type] = typeItems

    with open('items.json', 'w', encoding='utf-8') as f:
        json.dump(allItems, f, ensure_ascii=False, indent=4)

def encryptFile(path):
    print(path)
