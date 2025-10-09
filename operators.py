#ตัวดำเนินการทางตรรกศาสตร์
# and, or, not
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("เข้าสู่ระบบสำเร็จ")
else:
    print("เข้าสู่ระบบไม่สำเร็จ")

if username == "admin" or password == "1234":
    print("เข้าสู่ระบบสำเร็จ")
else:
    print("เข้าสู่ระบบไม่สำเร็จ")

if not username == "admin":
    print("เข้าสู่ระบบสำเร็จ")
else:
    print("เข้าสู่ระบบไม่สำเร็จ")