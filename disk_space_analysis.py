n=5
space=[1,2,3,1,2]
x=1


globalMinima=[]
for i in range(len(space)-1):
    tempList=space[i:i+x]

    if (len(tempList) != x):
        continue
    
    print(tempList)
    minVal=min(tempList)
    globalMinima.append(minVal)

print(max(globalMinima))
