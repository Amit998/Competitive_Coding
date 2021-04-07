class Solution:
    def singleNumber(self, nums):
        tempDict={}
        tempList=[]
      
        for i in nums:
            if i not in tempDict.keys():
               
                tempDict[i]=1
               
            # elif i in tempDict.keys() and tempDict[i] <2:
            else:
               
                tempDict[i]+=1
       
        for i in tempDict.keys():
            if tempDict[i] == 1:
                tempList.append(i)
        print(tempDict)
           
        return tempList


# nums = [2,2,1]
nums = [4,4,4,10,1,10,44,1,2,1,2]
# nums=[1]
sl=Solution()
print(sl.singleNumber(nums))
