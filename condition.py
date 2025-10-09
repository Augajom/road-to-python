score = int(input("กรอกคะแนนของคุณ: "))
print("คะแนนของคุณ:", score)
if score < 0 or score > 100:
    print("คะแนนไม่ถูกต้อง")
    exit() # ออกจากโปรแกรม
elif score >= 80:
    print("เกรด A")
elif score >= 70:
    print("เกรด B")
elif score >= 60:
    print("เกรด C")
elif score >= 50:
    print("เกรด D")
else:
    print("เกรด F")

#ternary operator

number = int(input("กรอกเลข: "))
print("ตัวเลขของคุณคือ", number)

print("เลขคู่" if number % 2 == 0 else "เลขคี่")