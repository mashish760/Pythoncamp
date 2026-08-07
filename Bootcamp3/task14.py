# code

height = input("Enter Height : ")
if int(height) < 120:
    print(f"Height {height} is less than 120, You can't ride")
else:
    print(f"Height {height} is greater than 120, You can ride")
    age = input("Enter Age : ")
    ticketValue = 0
    if int(age) < 12:
        ticketValue=5
        print(f"Age {age} is less than 12, You can ride")
    elif int(age) > 12 and int(age) < 18:
        ticketValue = 12
        print(f"Age {age} is greater than 18 and less than 12, You can ride")
    else:
        ticketValue = 18
        print(f"Age {age} is greater than 18, You can ride")
    pho=input("Are you want to take photo ? yes or no ")
    if(pho=='yes'):
        print("Want Photo add 3 more")
        photoAmt=int(ticketValue)+3
        print(f"Total bill {photoAmt}")
    else:
        print(f"Total bill {ticketValue}")
