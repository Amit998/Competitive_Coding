
# 500000
# 26
# 3
# 13 9.5
# 3 6.9
# 10 5.6
# 3
# 14 8.5
# 6 7.4
# 6 9.6



import math
Principle=int(input())
Time=int(input())
# Principle=10000
# Time=20
EMI=[]
# slab=3

sum=0
for j in range(2):
    slab=int(input())
    sum=0
    for i in range(slab):
        NumberOfYear,monthlyIRate=input().split()
        monthlyIRate=float(monthlyIRate)
        # NumberOfYear=int(input())
        # monthlyIRate=float(input())
        A1=Principle * int(monthlyIRate)
        ToThePower=int(NumberOfYear)*12
        B1=1+int(monthlyIRate) ** ToThePower
        C1=1-1/B1
        D1=A1 /C1
        sum=D1+sum
    EMI.append(sum)



if( EMI[0] > EMI[1] ):
    print('BANK B',end="")
else:
     print('BANK A',end="")

# print(sum)
# print(lstEMIA,lstEMIB)