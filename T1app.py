import numpy as np
garx, gary, garz = map(int, input().split())
f1 = open(input(), 'r')
arr  =[]
while True:
    # считываем строку
    line = f1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    arr.append(list(map(int, line.split())))
# закрываем файл
print(arr)
f1.close()
sidesp = (garx - 320)/2
backsp = (gary-560)
rowside = (sidesp - 60)/2
sideobj = []
backobj = []
s = 0
b = 0
for i in range(0,len(arr)):
    if arr[i][0]<=sidesp:
        temp = arr[i].copy()
        temp.append(i+1)
        sideobj.append(temp)
    if arr[i][1]<=backsp:
        temp = arr[i].copy()
        temp.append(i + 1)
        backobj.append(temp)
        b+=1
print(sideobj)
print(backobj)