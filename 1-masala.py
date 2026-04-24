import os
os.system("cls")

a = int(input("A son kiriting: "))
b = int(input("B son kiriting: "))

list1 = []

for i in range(a, b):
    if i % 2 == 0:
        list1.append(i)

print(list1)
    
