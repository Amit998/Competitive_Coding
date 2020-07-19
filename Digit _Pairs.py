import math
num=["8" ,"234", "567", "321","345", "123" ,"110", "767", "111"]
lst=[]
for i in range(len(num)):
    new=list(num[i])
    if(len(new) == 3):
        maxVal=max(new)
        minVal=min(new)
        formula=(int(maxVal)*11)+(int(minVal)*7)
        lst.append(str(formula))
    else:
        continue
bitScore=[]
val=""
flag=0
even=[]
odd=[]
for j in range(len(lst)):
    
    newList=list(lst[j])
    if( len(newList) == 2 ):
        for k in range(2):
            val=val+str(newList[k])
    else:
        newList.remove(newList[0])
        for k in range(2):
            val=val+str(newList[k])
        bitScore.append(val)
    if(flag == 0):
        even.append(val)
        flag=flag+1
        val=""
    elif(flag == 1):
        odd.append(val)
        flag=flag-1
        val=""
def counter(even,odd):
    count=0
    tempList=[]
    evenCounterList=[]
    oddCounterList=[]
    newNoDuplicate=[]
    for i in range(len(even)):
        tempList=list(even[i])
        significant=tempList[0]
        evenCounterList.append(significant)
    tempList=[]
    for j in range(len(even)):
        tempList=list(odd[j])
        significant=tempList[0]
        oddCounterList.append(significant)
    for k in range(len(evenCounterList)):
        counterEven=evenCounterList.count(evenCounterList[k])
        newNoDuplicate.append(counterEven)
    mylist = list(dict.fromkeys(newNoDuplicate))
    for i in range(len(mylist)):
        if( mylist[i] % 2 == 0  ):
            count=count+1
        elif( mylist[i] > 0 and mylist[i] % 2 !=0 ):

            count=int(math.ceil(mylist[i]/2))
        
    newNoDuplicate=[]
    
    
    for l in range(len(oddCounterList)):
        counterOdd=oddCounterList.count(oddCounterList[l])
        newNoDuplicate.append(counterOdd)

    mylist = list(dict.fromkeys(newNoDuplicate))
  
    if( mylist[i] % 2 == 0  ):
            count=count+1
    elif( mylist[i] > 0 and mylist[i] % 2 !=0 ):
        count=int(math.ceil(mylist[i]/2))+count
        
    return count
   
    
print(counter(even,odd))