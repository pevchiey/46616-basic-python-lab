score1=int(input())
score2=int(input())
score3=int(input())
if score1 <= 30 and score2 <= 30 and score3 <= 40:
    total=score1+score2+score3
if total<49:print("F")
if total<55:print("D")
if total<60:print("D+")
if total<65:print("C")
if total<70:print("C+")
if total<75:print("B")
if total<80:print("B+")
if total<=100:print("A")