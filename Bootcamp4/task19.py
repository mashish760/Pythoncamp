import random
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*','(', ')', '-', '_', '=', '+','[', ']', '{', '}', ';', ':', '"', ',', '.', '/', '?', '|', '<', '>', '`', '~']

password=''
nr_l=int(input("How many letters in password "))
nr_n=int(input("How many number in password "))
nr_s=int(input("How many symbols in password "))

for i in range(0,nr_l):
    password +=random.choice(alphabet)

for i in range(0,nr_n):
    password +=random.choice(numbers)

for i in range(0,nr_s):
    password +=random.choice(symbols)
print(password)
