username = input("Username: ")
password = input("Password: ")

if username == "member" and password == "1234":
    print("เข้าสู่ระบบสำเร็จ")
    service = input("ต้องการใช้บริการอะไร (ฝาก ถอน โอน): ")
    if service == "ฝาก":
        amount = float(input("กรอกจำนวนเงินที่ต้องการฝาก: "))
        if amount <= 0:
            print("จำนวนเงินไม่ถูกต้อง")
        else:
            print("ฝากเงิน", amount, "บาท สำเร็จ")
    elif service == "ถอน":
        amount = float(input("กรอกจำนวนเงินที่ต้องการถอน: "))
        if amount <= 0:
            print("จำนวนเงินไม่ถูกต้อง")
        else:
            print("ถอนเงิน", amount, "บาท สำเร็จ")
    elif service == "โอน":
        amount = float(input("กรอกจำนวนเงินที่ต้องการโอน: "))
        if amount <= 0:
            print("จำนวนเงินไม่ถูกต้อง")
        else:
            account = input("กรอกหมายเลขบัญชีที่ต้องการโอน: ")
            print("โอนเงิน", amount, "บาท ไปยังบัญชี", account, "สำเร็จ")
else:
    print("เข้าสู่ระบบไม่สำเร็จ")