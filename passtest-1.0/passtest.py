#!/bin/python3
import hashlib
import getpass

print("welcome to passtest")
print(" v1.0" )
usr = getpass.getpass('Type your password : ')

#print("md5 hash :",hashlib.md5(text.encode()).hexdigest())

pass1 = hashlib.md5(usr.encode()).hexdigest()


for password in open('wordlist.txt', 'r').readlines():
    hashed = hashlib.md5(password.strip().encode()).hexdigest()
    if hashed == pass1:
        print("your password is weak")
        exit()
else:
    print("your password is strong")