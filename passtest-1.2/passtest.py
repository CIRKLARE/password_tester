#!/bin/python3
import hashlib
import getpass

print("welcome to passtest")
print(" v1.2 ")
usr = getpass.getpass('Type your password : ')
wor = input("use wordlist or not if NO (type NO) if yes type directory to the wordlist : ")
if wor == "NO":
    wor = "wordlist.txt"

#print("md5 hash :",hashlib.md5(text.encode()).hexdigest())

pass1 = hashlib.md5(usr.encode()).hexdigest()


for password in open(wor, 'r').readlines():
    hashed = hashlib.md5(password.strip().encode()).hexdigest()
    if hashed == pass1:
        print("your password is weak")
        exit()
else:
    print("your password is strong")