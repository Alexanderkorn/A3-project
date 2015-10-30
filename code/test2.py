__author__ = 'alexander'
#import mmap
#f = open('passwords.txt')
username=input("gebruikers naam:")
password=input("Wachtwoord:")
#s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
if username and password in open('passwords.txt').read():
    print("true")
""""
while password == 'lol':
    if s.find(str(username)) != -1:
        print("True")
    if s.find(str(password)) != 1:
        print("True")


import hashlib ,os
resource_file = "passwords.txt"
def encode(username,password):
    return username,hashlib.sha1(password).hexdigest()
def add_user(username,password):
    if os.path.exists(resource_file):
        with open(resource_file) as f:
            if username in f.read():
                raise Exception("user already exists")
    with open(resource_file,"a") as f:
         print(f, encode(username,password))
    return username
def check_login(username,password):
    with open(resource_file) as f:
        if encode(username,password) in f.read():
           return username

def create_username():
     try:
         username = add_user(input("enter username:"),input("enter password:"))
         print("Added User! %s" + username)
     except Exception as e:
         print("Failed to add user "+username,"! ... user already exists??" + username)
def login():
     if check_login(input("enter username:"),input("enter password:")):
        print("Login Success!!")
     else:
        print("there was a problem logging in")

while True:
    try:
        {'c':create_username,'l':login}.get(input("(c)reate user\n(l)login\n------------\n>").lower(),login)()
    except:
        break


print("Login Script")

import getpass
import csv

userbase="Usernames.csv"
CorrectUsername = "Test"
CorrectPassword = "TestPW"

loop = 'true'
while (loop == 'true'):

    username = input("Please enter your username: ")
    credentials = {}
    # with open('Usernames.csv', 'r') as f:
    #     for line in f:
    #         user, pwd = line.strip().split(';')
    #         credentials[user] = pwd

    if (username == CorrectUsername):
        loop1 = 'true'
        while (loop1 == 'true'):
            password = getpass.getpass("Please enter your password: ")
            code = int(input("uw code alstublieft"))
            f=open(userbase,'r')
            reader=csv.reader(f, delimiter=';')
            for i in reader:
                if int(i[1]) == int(code):
                    print(i[0])
                    print("Succes")
                f.close()

            if (password == CorrectPassword):
                print("Logged in successfully as " + username)
                loop = 'false'
                loop1 = 'false'
            else:
                print("Password incorrect!")

    else:
        print("Username incorrect!")
"""""