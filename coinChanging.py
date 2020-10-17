coins=[2,3,7,8,10]
total=11
lst=[]
temp=[]
for i in range(len(coins)):
    tempList=[]
    for j in range(total+1):
        if(j == 0):
            tempList.append('T')
        else:
            tempList.append('F')
    lst.append(tempList)
for i in range(len(coins)):
    currCoin=coins[i]
    for j in range(total+1):
        if(coins[i] > j):
            lst[i][j]=lst[i-1][j]
        elif(coins[i] ==j or lst[i-1][j] == 'T'):
            lst[i][j]='T'
        elif(lst[i][j] == 'F'):
            lst[i][j]=lst[i-1][j-(coins[i])]
        print(lst[i][j])
print(lst)

# lst=[[ 'F' for i in range(total+1)] for j in range(len(coins)) if j is not 0 else 'T' ]
# print(lst)

