string = "Hello, World!"
number = 10
float_num = 3.14
boolean = True
a, b, c = 1, 2, 3

print(a, b, c)

name = input("กรอกชื่อของคุณ: ")
year = int(input("กรอกปีเกิดของคุณ: "))

print("สวัสดี", name)
print("เกิดในปี", year)

# input เก็บเป็น string เสมอ
# ต้องแปลงก่อนถ้าจะเอาไปใช้คำนวณ
#print("ปีนี้คุณอายุ", 2568 - int(year), "ปี") # แปลงแค่ส่วนนี้ ถ้าอยากให้เป็น int ตั้งแต่ต้นให้เพิ่ม int() ที่ตัวแปลเลย
print("ปีนี้คุณอายุ", 2568 - year, "ปี")

print(type(name))
print(type(year))

# ตัวแปลงทั้งหมด
# int() float() str() bool()