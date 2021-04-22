
def get_targetSum(array,targetSum):
    tempLst=[]
    for i in range(len(array)):
        val=array[i]
        tempVal=targetSum-val
        
        # print(tempVal)
        templistIndexCheck=array[:i]+array[i+1:]
        if ( tempVal in templistIndexCheck):
            tempLst.append(tempVal)
            
    # print(tempVal)
    return tempLst

array=[3,-4,8,11,-1,6,4,5,5]
targetSum=10

print(get_targetSum(array,targetSum))
