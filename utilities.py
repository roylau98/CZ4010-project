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

def deleteItem(path, filename):
    try:
        os.remove(path+"/"+filename)
    except OSError as e:
        print("Note does not exists.")

def deleteFromJson(deleted, type):
    with open('items.json', 'r') as f:
        allItems = json.load(f)

    typeItems = allItems[type]
    for key, value in typeItems.items():
        if 'account' in value:
            if value['account'] == deleted['account'] and value['username'] == deleted['username'] and value['password'] == deleted['password']:
                break
        elif 'title' in value:
            if value['title'] == deleted['title'] and value['path'] == deleted['path'] and value[
                'filename'] == deleted['filename']:
                break

    del typeItems[key]
    allItems[type] = typeItems

    with open('items.json', 'w', encoding='utf-8') as f:
        json.dump(allItems, f, ensure_ascii=False, indent=4)

    return key