# abcdaf
# gbcdf
input1=input()
input2 = input()
input1=list(input1)
input2=list(input2)

ipLenOne=len(input1)
ipLenTwo=len(input2)
print(input1,input2)

tempList=[]
PutTempList=[]
for i in range(ipLenOne):
    for j in range(ipLenTwo):
        tempList.append(0)
        print(j)
    PutTempList.append(tempList)
    tempList=[]

print(PutTempList)



for i in range(ipLenOne):
    for j in range(ipLenTwo):
        if( input1[i] == input2[j] ):
            print(input1[i] , input2[j])
            if( i==0 and j ==0 ):
   
                PutTempList[i][j]=int(PutTempList[i][j])+1
            else:
                PutTempList[i][j]=int(PutTempList[i-1][j-1])+1
    
        
newList=[]
for i in range(len(PutTempList)):
    newList.append(max(PutTempList[i]))
print(max(newList))