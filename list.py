product = ["กางเกง", 99.99 , 10 , True] 
# product = list(("กางเกง", 99.99 , 10 , True)) เขียนแบบนี้ก็ได้

print(type(product)) # <class 'list'>
print(len(product)) # 4

# เข้าถึงสมาชิกใน list
print(product[0]) # กางเกง
print(product[1]) # 99.99
print(product[-4]) # กางเกง
print(product[-1]) # True
print(product[1:3]) # [99.99, 10]
print(product) # ['กางเกง', 99.99, 10, True]

product[0] = "เสื้อ"
print(product) # ['เสื้อ', 99.99, 10, True]

for element in product:
    print(element)

# ฟังก์ชันที่ใช้กับ list
product.append("ของแถม") # เพิ่มสมาชิกเข้าไปใน list
product.extend(["รองเท้า", 199.99]) # เพิ่มสมาชิกหลายตัวเข้าไปใน list
product.insert(1, "เสื้อยืด") # เพิ่มสมาชิกเข้าไปในตำแหน่งที่กำหนด
product.remove("ของแถม") # ลบสมาชิกตัวแรกที่เจอ
print(product)
product.clear() # ลบสมาชิกทั้งหมดใน list

product = ["กางเกง", "ถุงเท้า", "เสื้อยืด", "รองเท้า"]
product.sort() # เรียงลำดับสมาชิกใน list
print(product)
product.reverse() # สลับลำดับหลังมาหน้าสมาชิกใน list
print(product)
print(product.count("เสื้อยืด")) # 1
