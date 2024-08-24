from itertools import count


def TAKE_OFF(a):
    aInAir = a in airPlane
    if not aInAir:
        print("YOU ARE NOT HERE")
    elif aInAir and a in landingList:
        print("YOU ARE LANDING NOW")
    elif aInAir and a in takeOffList:
        print("YOU ARE TAKING OFF")
    elif aInAir and freeBond.count(0) == 0:
        print("NO FREE BOUND")
    else:
        takeOffList.append(a)
        freeBond[freeBond.index(0)] = a


def LANDING(a):
    aInAir = a in airPlane
    aInLand = a in landingList
    aInTake = a in takeOffList
    if aInAir and not aInLand and not aInTake:
        print("YOU ARE HERE")
    elif aInAir and aInTake:
        print("YOU ARE TAKING OFF")
    elif aInAir and aInLand:
        print("YOU ARE LANDING NOW")
    elif not aInAir and freeBond.count(0) == 0:
        print("NO FREE BOUND")
    else:
        landingList.append(a)
        airPlane.append(a)
        freeBond[len(freeBond) - freeBond[::-1].index(0) - 1] = a


def PLANE_STATUS(a):
    aInAir = a in airPlane
    aInLand = a in landingList
    aInTake = a in takeOffList
    if aInAir and not aInLand and not aInTake:
        print("1")
    elif aInAir and aInTake:
        print("2")
    elif aInAir and aInLand:
        print("3")
    else:
        print("4")


def BAND_STATUS(a):
    a -= 1
    if freeBond[a] == 0:
        print("FREE")
    else:
        print(freeBond[a])


n, k = input().split()
n = int(n)
k = int(k)
airPlane = []
takeOffList = []
landingList = []
freeBond = [0]*k
for i in range(n):
    airPlane.append(input())
dastor = []
q = int(input())
for i in range(q):
    dastor.append(input().split(" "))


for i in range(q):
    if dastor[i][0] == "TAKE-OFF":
        TAKE_OFF(dastor[i][1])
    elif dastor[i][0] == "LANDING":
        LANDING(dastor[i][1])
    elif dastor[i][0] == "PLANE-STATUS":
        PLANE_STATUS(dastor[i][1])
    else:
        BAND_STATUS(int(dastor[i][1]))
