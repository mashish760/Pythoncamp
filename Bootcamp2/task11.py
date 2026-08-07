#Welcome to tip calculator
print("Welcome to tip calculator")
total_amount=float(input("please enter your total amount:$"))
tip=int(input("please enter your tip 12, 14 or 15:"))

people=int(input("please enter your number of people:"))

tipvalue=(tip*total_amount)/100
# print(tipvalue)
print("Total Amount with tip ",(total_amount+tipvalue))
per_person=round(((total_amount+tipvalue)/people),2)
print(f"Total Amount per person will be {per_person}")
