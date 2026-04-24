import os
os.system("cls")

listlar = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

result = max(listlar, key=sum)

print(result)