age=int(input())
day=int(input())
if age<13:total=100
elif age>13 and age<=60:total=180
else:total=120
if day==6 or day==7:total=total+50
print(total)