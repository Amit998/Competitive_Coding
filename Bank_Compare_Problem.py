# 5
# 9.5
# 10
# 9.6
# 5
# 8.5
# 10
# 6.9
# 5
# 8.5
# 5
# 7.9

import math
# Principle=int(input())
# Time=int(input())
Principle=10000
Time=20
EMI=[]
slab=3
sum=0
for j in range(2):
    sum=0
    for i in range(slab): 
        NumberOfYear=int(input())
        monthlyIRate=float(input())
        A1=Principle * monthlyIRate
        ToThePower=NumberOfYear*12
        B1=1+monthlyIRate ** ToThePower
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