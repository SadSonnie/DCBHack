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
print(sidesp, backsp)
rowside = (sidesp - 60)/2
sideobj = []
backobj = []
curwa = []
s = 0
b = 0
for i in range(len(arr)):
    if arr[i][0]<=sidesp:
        curwa = arr[i]
        sideobj.append(curwa)
        sideobj[s].extend(str(i+1))
        s+=1
    if arr[i][1]<=backsp:
        backobj.append(arr[i])
        backobj[b].append(i+1)
        b+=1
print(sideobj)
print(backobj)
print(arr)