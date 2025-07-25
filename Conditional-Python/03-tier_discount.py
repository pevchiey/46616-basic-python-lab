cost=float(input())
if cost >= 2000:
    total=cost-(0.15*cost)
elif cost >= 1000:
    total=cost-(0.1*cost)
elif cost >= 500:
    total=cost-(0.15*cost)
else:
    total=cost
print (float(total))