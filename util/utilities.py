import secrets
import string
import os
import json
import scrypt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import keccak

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

def decryptNote(path, filename, vaultKey, iv):
    with open(path + "/" + filename, 'rb') as f:
        encrypted = f.readlines()

    decrypted = decrypt(vaultKey, b"".join(encrypted), iv)
    hashed = hash(decrypted)
    return decrypted.decode("utf-8"), hashed

def saveNote(encryption, path, filename):
    with open(path+"/"+filename, 'wb') as f:
        f.write(encryption)

def deleteItem(path):
    try:
        os.remove(path)
    except OSError as e:
        print("Note does not exists.")

def encryptFile(key, path, savelocation):
    with open(path, 'rb') as f:
        plaintext = f.readlines()

    deleteItem(path)
    encrypted, iv = encrypt(key, b"".join(plaintext))
    hashedFile = hash(b"".join(plaintext))

    with open(savelocation, 'wb') as f:
        f.write(encrypted)
    return iv, hashedFile

def decryptFile(key, path, iv, hashFile):
    with open(path, 'rb') as f:
        encrypted = f.readlines()

    decrypted = decrypt(key, b"".join(encrypted), iv)
    hashed = hash(decrypted)

    with open(path, 'wb') as f:
        f.write(decrypted)

    return hashed == hashFile

def KDF(string, salt):
    # key = scrypt.hash(string, salt, 524288, 8, 1, 32)
    key = scrypt.hash(string, salt, 128, 8, 1, 32)
    return key

def encrypt(key, message):
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    encrypted = cipher.encrypt(pad(message, cipher.block_size))
    return encrypted, iv

def decrypt(key, encrypted, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted = cipher.decrypt(encrypted)
    return unpad(decrypted, cipher.block_size)

def hash(message):
    keccakHash = keccak.new(digest_bits=256)
    keccakHash.update(message)
    return keccakHash.hexdigest()