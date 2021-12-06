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
    if arr[i][0]<=sidesp and arr[i][2]<=150:
        temp = arr[i].copy()
        temp.append(i+1)
        sideobj.append(temp)
    #0,1,2
    if arr[i][0]<=sidesp and arr[i][1]<=150:
        temp = arr[i].copy()
        temp[0], temp[1], temp[2] = temp[0], temp[2], temp[1]
        temp.append(i+1)
        sideobj.append(temp)
    #0,2,1
    if arr[i][1]<=sidesp and arr[i][2]<=150:
        temp = arr[i].copy()
        temp[0], temp[1], temp[2] = temp[1], temp[0], temp[2]
        temp.append(i+1)
        sideobj.append(temp)
    #1,0,2
    if arr[i][1]<=sidesp and arr[i][0]<=150:
        temp = arr[i].copy()
        temp[0], temp[1], temp[2] = temp[1], temp[2], temp[0]
        temp.append(i+1)
        sideobj.append(temp)
    #1,2,0
    if arr[i][2]<=sidesp and arr[i][1]<=150:
        temp = arr[i].copy()
        temp[0], temp[1], temp[2] = temp[2], temp[0], temp[1]
        temp.append(i+1)
        sideobj.append(temp)
    #2,0,1
    if arr[i][2]<=sidesp and arr[i][0]<=150:
        temp = arr[i].copy()
        temp[0], temp[1], temp[2] = temp[2], temp[1], temp[0]
        temp.append(i+1)
        sideobj.append(temp)
    #2,1,0


    if arr[i][1]<=backsp and :
        temp = arr[i].copy()
        temp.append(i + 1)
        backobj.append(temp)
        b+=1
print(sideobj)
print(backobj)
def MyFn(s):
    return s[0]*s[1]

sideobj = sorted(sideobj,key =MyFn, reverse=True)
backobj = sorted(backobj,key =MyFn, reverse=True)
print(sideobj)
print(backobj)