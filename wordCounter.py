

string="aabcd"

tempDic={}
tempList=list(string)
tempListNew=[]
tempStr=''

for i in range(len(tempList)):
    
    if tempList[i] not in tempDic.keys():
        tempDic[tempList[i]]=1
        # print(tempList[i])
    else:
        count=tempDic[tempList[i]]
        count=count+1
        tempDic[tempList[i]]=count
        

for i in tempDic.keys():
    # print('lol')
    # print(i)
    # # tempStr+=tempDic[i]+i
    # print(tempList)
    tempListNew.append(str(tempDic[i]))
    tempListNew.append(str(i))


print(''.join(tempListNew))
