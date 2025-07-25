score=int(input()) #นำเข้าข้อมูลเลข
if score <=100 and score >=0: #คัดกรองตัวเลขให่มีเพียงแค่ 0-100
    if score >= 50:
        print("Pass") #50ขึ้นไป ผ่าน
    elif score > 50:
        print("Fail") #น้อยกว่า 50 ตก