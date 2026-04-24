import os
os.system("cls")

list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

result = []

for t in list1:
    yangi_tuple = t[:-1] + (100,)
    result.append(yangi_tuple)

print(result)