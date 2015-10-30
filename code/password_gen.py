__author__ = 'alexander'
import random
import string
import os.path


num1 = random.randrange(100,999)
string.letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'

letters_section = ''.join(random.choice(string.letters) for _ in range(8))  # change 8 to a variable if you want to ask the user for a length or have it passed as an argument
password = str(number_section) + letters_section

password_for = input('This password is for: ')
your_pass =  'Your password for {} is: {}'.format(password_for, password)
print(your_pass)

save_path = 'C:\Users\%Username%\Desktop'
name_of_file = input("What is the name of the file: ")
completeName = os.path.join(save_path, name_of_file+".txt")
with open(completeName, "w") as file1:
    file1.write(your_pass)