bill=float(input("The total bill for today is "))
tips=int(input("the persent tips for this bill will be "))
person=int(input("today we have people of "))
print("------------------------------")
total=(bill*(tips/100)+bill)/4
print("The total for today will be",total,"baht. Thank you for visiting us!")