import random
import myhelper
num=random.random()
print(num+myhelper.my_favourite_number)

num=random.uniform(10,20)
print(num)

num=random.randint(0,1)
if num==1:
    print(True)
else:
    print(False)