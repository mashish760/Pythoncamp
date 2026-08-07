#function
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '"',
           ',', '.', '/', '?', '|', '<', '>', '`', '~']


def passwordManager():

    password_list = []
    nr_l = int(input("How many letters in password "))
    nr_n = int(input("How many number in password "))
    nr_s = int(input("How many symbols in password "))

    for i in range(0, nr_l):
        password_list.append(random.choice(alphabet))

    for i in range(0, nr_n):
        password_list.append(random.choice(numbers))

    for i in range(0, nr_s):
        password_list.append(random.choice(symbols))

    print(password_list)
    random.shuffle(password_list)
    print(password_list)
    password = ""
    for char in password_list:
        password += char

    print(f"The password is: {password}")


passwordManager()