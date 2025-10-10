product = ("apple watch", 150.0, 5)
# product = tuple(("apple watch", 150.0, 5)) # สร้าง tuple แบบนี้ก็ได้
# product[0] = "iphone" # ไม่สามารถเปลี่ยนค่าได้เพราะเป็น tuple

print(type(product)) # <class 'tuple'>
print(len(product)) # 3
print(product)
print(product[0]) # apple watch
print(product[1]) # 150.0
print(product[2]) # 5
print(product[-1]) # 5
print(product[-2]) # 150.0

for item in product:
    print(item)

name, price, quantity = product # แยกมาเก็บใส่ตัวแปร
print(name) # apple watch
print(price) # 150.0
print(quantity) # 5