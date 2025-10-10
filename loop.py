#while loop
#ทำจนกว่าเงื่อนไขจะเป็นเท็จ
counter = 1
while counter <= 5:
    print(counter)
    counter += 1
    
print("จบการทำงาน")

#for loop
#ทำซ้ำตามจำนวนที่กำหนด
for counter in range(3): #0-2
    print("Hello", counter)

for counter in range(1, 4): #1-3
    print("Halo", counter)

for counter in range(1, 4, 2): #1, 3
    print("swadeekub", counter)

for counter in range(5, 0, -1): #5-1
    print("sabaidee", counter)

#break / continue
for counter in range(1, 11):
    if counter == 3:
        print("ข้าม 3")
        continue
    if counter == 5:
        print("เจอ 5 หยุด")
        break
    print(counter)