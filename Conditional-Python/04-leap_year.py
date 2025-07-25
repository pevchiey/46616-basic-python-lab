year_ks=int(input())
if year_ks % 400 == 0:print("Leap Year")
elif year_ks % 4 == 0:
    if year_ks % 100 == 0:print("Not a Leap Year")
    else:print("Leap Year")
else:print("Not a Leap Year")