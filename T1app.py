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
y3 = y
y4 = y
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

previous1 = 0
previous2 = 0
temp = 0

def check(l1, l2, w1, w2, h1, h2):
    if l1>l2 and w1>w2 and h1+h2 <= 150:
        return True
    else:
        return False

for i in range(len(sideobj)):
    # if i == 0:
    #     list_of_coordinates.append(list(x, y - sideobj[i] + sideobj[0][0], y))
    if sideobj[i][3] in indexlist:
        if both_sides == True:
            if plus_2_minus_first == True:
                temp = y1
                y1 = y1 - sideobj[i][1]
                if y1 > 0:
                    previous1 += sideobj[i][1]
                    list_of_coordinates.append([x, y1, sideobj[i][2], x + sideobj[i][0], y1 + sideobj[i][1], sideobj[i][2], sideobj[i][3]])
                    prov = 0
                    indexlist.remove(sideobj[i][3])
                    for j in range(len(sideobj)-1):
                        if sideobj[j+1][3] in indexlist:
                            if check(sideobj[i][0], sideobj[j+1][0], sideobj[i][1], sideobj[j+1][1], sideobj[i][2]+prov, sideobj[j+1][2]) == True:
                                list_of_coordinates.append([x, y1, sideobj[j+1][2]+sideobj[i][2]+prov, x + sideobj[i][0], y1 + sideobj[i][1], sideobj[j+1][2]+sideobj[i][2]+prov, sideobj[j+1][3]])
                                prov += sideobj[j+1][2]+sideobj[i][2]
                                indexlist.remove(sideobj[j+1][3])
                    plus_2_minus_first = False
                else:
                    y1 = temp
            else:
                y2 = y1 + previous1
                previous1 += sideobj[i][1]
                if y2 + sideobj[i][1] < 500:
                    list_of_coordinates.append([x, y2, sideobj[i][2], x + sideobj[i][0], y2 + sideobj[i][1], sideobj[i][2], sideobj[i][3]])
                    prov = 0
                    indexlist.remove(sideobj[i][3])
                    for j in range(len(sideobj)-1):
                        if sideobj[j + 1][3] in indexlist:
                            if check(sideobj[i][0], sideobj[j+1][0], sideobj[i][1], sideobj[j+1][1], sideobj[i][2]+prov, sideobj[j+1][2]) == True:
                                list_of_coordinates.append([x, y2, sideobj[j+1][2]+sideobj[i][2]+prov, x + sideobj[i][0], y2 + sideobj[i][1], sideobj[j+1][2]+sideobj[i][2]+prov, sideobj[j+1][3]])
                                prov += sideobj[j + 1][2] + sideobj[i][2]
                                indexlist.remove(sideobj[j+1][3])
                    plus_2_minus_first = True
            both_sides = False
        else:
            if plus_2_minus_second == True:
                temp = y3
                y3 = y3 - sideobj[i][1]
                if y3 > 0:
                    previous2 += sideobj[i][1]
                    list_of_coordinates.append([x - 320 - sideobj[i][0], y3, sideobj[i][2], x - 320, y3 + sideobj[i][1], sideobj[i][2], sideobj[i][3]])
                    prov = 0
                    indexlist.remove(sideobj[i][3])
                    for j in range(len(sideobj)-1):
                        if sideobj[j + 1][3] in indexlist:
                            if check(sideobj[i][0], sideobj[j+1][0], sideobj[i][1], sideobj[j+1][1], sideobj[i][2]+prov, sideobj[j+1][2]) == True:
                                list_of_coordinates.append([x - 320 - sideobj[i][0], y3, sideobj[j+1][2]+sideobj[i][2]+prov, x - 320, y3 + sideobj[i][1], sideobj[j+1][2]+sideobj[i][2]+prov, sideobj[j+1][3]])
                                prov += sideobj[j + 1][2] + sideobj[i][2]
                                indexlist.remove(sideobj[j+1][3])
                    plus_2_minus_second = False
                else:
                    y3 = temp
            else:
                y4 = y3 + previous2
                previous2 += sideobj[i][1]
                if y4 + sideobj[i][1] < 500:
                    list_of_coordinates.append([x - 320 - sideobj[i][0], y4, sideobj[i][2], x - 320, y4 + sideobj[i][1], sideobj[i][2], sideobj[i][3]])
                    prov = 0
                    indexlist.remove(sideobj[i][3])
                    for j in range(len(sideobj)-1):
                        if sideobj[j + 1][3] in indexlist:
                            if check(sideobj[i][0], sideobj[j+1][0], sideobj[i][1], sideobj[j+1][1], sideobj[i][2]+prov, sideobj[j+1][2]) == True:
                                list_of_coordinates.append([x - 320 - sideobj[i][0], y4, sideobj[j+1][2]+sideobj[i][2]+prov, x - 320, y4 + sideobj[i][1], sideobj[j+1][2]+sideobj[i][2]+prov, sideobj[j+1][3]])
                                prov += sideobj[j + 1][2] + sideobj[i][2]
                                indexlist.remove(sideobj[j+1][3])
                    plus_2_minus_second = True
            both_sides = True

x_zad = sidesp + 60
y_zad = 560

if y_zad < gary - 60:
    for i in range(len(sideobj)):
        if sideobj[i][3] in indexlist:
            if x_zad + sideobj[i][0] < garx - 2*x_zad and y_zad + sideobj[i][1] <= gary:
                list_of_coordinates.append([x_zad, y_zad, sideobj[i][2], x_zad + sideobj[i][0], y_zad + sideobj[i][1], sideobj[i][2], sideobj[i][3]])
                prov = 0
                for j in range(len(sideobj) - 1):
                    if sideobj[j + 1][3] in indexlist:
                        if check(sideobj[i][0], sideobj[j + 1][0], sideobj[i][1], sideobj[j + 1][1], sideobj[i][2]+prov, sideobj[j + 1][2]) == True:
                            list_of_coordinates.append([x_zad, y_zad, sideobj[j+1][2]+sideobj[i][2], x_zad + sideobj[i][0], y_zad + sideobj[i][1], sideobj[j+1][2]+sideobj[i][2], sideobj[j+1][3]])
                            prov = sideobj[j + 1][2] + sideobj[i][2]
                            indexlist.remove(sideobj[j + 1][3])
                x_zad = x_zad + sideobj[i][0]

print(list_of_coordinates)
for i in range(len(list_of_coordinates)):
    if list_of_coordinates[i][1]>500:
        print(list_of_coordinates[i])
print(len(list_of_coordinates))

