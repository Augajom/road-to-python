# การเชืื่อมสตริง
fname = "suphamethee"
lname = "intharalib"

fullname = fname + " " + lname + " Au"
print(fullname)

# ใช้เมื่อมีหลายบรรทัด
address = """
123/45
หมู่ 1
ตำบล อิอิ
อำเภอ อิอิ
จังหวัด อิอิ
12345
"""
print(address)

# string + integer
# ใช้ f นำหน้า
age = 20
salary = 15000

message = f"อายุ {age} ปี"
data = f"เงินเดือน {salary:.2f} บาท"

print(message)
print(data)

# string count
text = "Hello world"
print("Hello world มี string ทั้งหมด ", len(text), " ตัวอักษร")

# string index
# H     e     l     l     o       w     o     r     l     d
# 0     1     2     3     4   5   6     7     8     9     10
# -11 -10    -9    -8    -7  -6  -5    -4    -3    -2    -1
print(text[0]) # H
print(text[1]) # e
print(text[2]) # l
print(text[3]) # l
print(text[4]) # o
print(text[6:]) # world
print(text[6:11]) # world
print(text[6:10]) # worl
print(text[-5:]) # world

# ใช้ for loop เข้ามาดึงตัวอักษรใน string
for c in text:
    print(c)

# ฟังก์ชันจัดการ string
text2 = "LocAtIon"
print(text2.upper()) # แปลงเป็นตัวพิมพ์ใหญ่
print(text2.lower()) # แปลงเป็นตัวพิมพ์เล็ก

text3 = "นายอู๋"
print(text3.startswith("นาย")) # ตรวจสอบขึ้นต้นด้วยคำว่า "นาย" TRUE
print(text3.endswith("อู๋"))   # ตรวจสอบลงท้ายด้วยคำว่า "TRUE
print(text3.startswith("นาง")) # ตรวจสอบขึ้นต้นด้วยคำว่า "นาง" FALSE
print(text3.endswith("โบ")) # ตรวจสอบขึ้นต้นด้วยคำว่า "โบ" FALSE

if text3.startswith("นาย"):
    print("เพศชาย")
else:
    print("เพศหญิง")

text4 = "กันยายน"

if text4.endswith("ยน"):
    print("เดือนนี้มี 30 วัน")
else:
    print("เดือนนี้มี 31 วัน")

# ฟังก์ชัน find
text5 = "Hello Python"
print(text5.find("Python")) # 6
print(text5.find("Hello")) # 0
print(text5.find("Java")) # -1

# ฟังก์ชัน count
text6 = "Hello Hello Hello World"
print(text6.count("Hello")) # 3
print(text6.count("World")) # 1

# ฟังก์ชัน replace
text7 = "Hello World"
print(text7.replace("World", "Python")) # Hello Python

# ฟังก์ชัน strip
text8 = "   Hello World   ".strip() # ลบช่องว่างด้านหน้าและด้านหลังออก
print(len(text8)) # 11

# ฟังก์ชัน format
text9 = "ฉันชื่อ {0} นามสกุล {1} อายุ {2} ปี".format("ศุภเมธี", "อินทรลิบ", 21)
print(text9) # ฉันชื่อ ศุภเมธี นามสกุล อินทรลิบ อายุ 21 ปี

# ฟังก์ชัน split
text10 = "นายอู๋,นางสาวโบ,นางสาวบิว"
names = text10.split(",") # แยกสตริงโดยใช้ , เป็นตัวแบ่ง
for name in names:
    print(name)