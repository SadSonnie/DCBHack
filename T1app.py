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
# print(arr)
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


    if arr[i][1]<=backsp and arr[i][2]<=150:
        temp = arr[i].copy()
        temp.append(i + 1)
        backobj.append(temp)
        b+=1
    # 0,1,2
    if arr[i][2]<=backsp and arr[i][1]<=150:
        temp = arr[i].copy()
        temp[0], temp[1], temp[2] = temp[0], temp[2], temp[1]
        temp.append(i + 1)
        backobj.append(temp)
        b+=1
    # 0,2,1
    if arr[i][0]<=backsp and arr[i][2]<=150:
        temp = arr[i].copy()
        temp[0], temp[1], temp[2] = temp[1], temp[0], temp[2]
        temp.append(i + 1)
        backobj.append(temp)
        b+=1
    # 1,0,2
    if arr[i][2]<=backsp and arr[i][0]<=150:
        temp = arr[i].copy()
        temp[0], temp[1], temp[2] = temp[1], temp[2], temp[0]
        temp.append(i + 1)
        backobj.append(temp)
        b+=1
    # 1,2,0
    if arr[i][0]<=backsp and arr[i][1]<=150:
        temp = arr[i].copy()
        temp[0], temp[1], temp[2] = temp[2], temp[0], temp[1]
        temp.append(i + 1)
        backobj.append(temp)
        b+=1
    # 2,0,1
    if arr[i][1]<=backsp and arr[i][0]<=150:
        temp = arr[i].copy()
        temp[0], temp[1], temp[2] = temp[2], temp[1], temp[0]
        temp.append(i + 1)
        backobj.append(temp)
        b+=1
    # 2,1,0
# print(sideobj)
# print(backobj)
def MyFn(s):
    return s[0]*s[1]

sideobj = sorted(sideobj,key =MyFn, reverse=True)
backobj = sorted(backobj,key =MyFn, reverse=True)
# print(sideobj)
# print(backobj)

y = 250
y1 = y
y2 = y
x = garx - sidesp
sideminus = 0
indexlist = []
control = 0
both_sides = True
plus_2_minus_first = True
plus_2_minus_second = True
for i in range(len(sideobj)):
    indexlist.append(i+1)

list_of_coordinates = []

for i in range(len(sideobj)):
    # if i == 0:
    #     list_of_coordinates.append(list(x, y - sideobj[i] + sideobj[0][0], y))
    previous = sideobj[i][1]/2
    if sideobj[i][3] in indexlist:
        if both_sides == True:
            if plus_2_minus_first == True:
                list_of_coordinates.append([x, y1 - previous, sideobj[i][2], x + sideobj[i][0], y1 + previous, sideobj[i][2], sideobj[i][3]])
                previous = sideobj[i][1]/2
                y1 = y - previous
                plus_2_minus_first = False
                indexlist.remove(sideobj[i][3])
            else:
                list_of_coordinates.append([x, y2 - previous, sideobj[i][2], x + sideobj[i][0], y2 + previous, sideobj[i][2], sideobj[i][3]])
                previous = sideobj[i][1] / 2
                y2 = y1 + 2*previous
                plus_2_minus_first = True
                indexlist.remove(sideobj[i][3])
            both_sides = False
        else:
            if plus_2_minus_second == True:
                list_of_coordinates.append([x - 320, y1 - previous, sideobj[i][2], x - sideobj[i][0], y1 + previous, sideobj[i][2], sideobj[i][3]])
                previous = sideobj[i][1] / 2
                y1 = y - previous
                plus_2_minus_second = False
                indexlist.remove(sideobj[i][3])
            else:
                list_of_coordinates.append([x - 320, y2 - previous, sideobj[i][2], x - sideobj[i][0], y2 + previous, sideobj[i][2], sideobj[i][3]])
                previous = sideobj[i][1] / 2
                y2 = y1 + 2 * previous
                plus_2_minus_second = True
                indexlist.remove(sideobj[i][3])
            both_sides = True

print(list_of_coordinates)

