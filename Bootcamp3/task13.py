#if else statement

print("Welcome to conditional operators")
num=int(input("enter your number even or odd "))

if num%2==0:
    print("number is even")
    if num<10:
        print("number is less than 10")
    elif num==10:
        print("number is equal to 10 than 10")
        if num:
            print("number is equal to 10",num**2)
    else:
        print("number is greater than 10")
else:
    print("number is odd")
    if num ==10:
        print("number is equal to 10")
    else:
        print("number is not equal 10")