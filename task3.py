#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]


x = input("enter username: ")
if x in users:
    y = input("enterpasswords: ")
    if y in passwords:
        print("access granted")
    else:
        print("access denied")
else:
    print("access denied")