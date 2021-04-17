class Solution:
    def topKFrequent(self, nums, k):
        tempDict={}
        result=[]

        for i in nums:
            if i not in tempDict.keys():
                tempDict[i]=1
            else:
                tempDict[i]+=1
            # if (tempDict[i] <= k):
            #     result.append(i)
        
        # for i in range(k):
        #     if tempDict[i]<=k:
        #         result.append(i)

        # print(  max([tempDict.values()]) )
        # result=[ i for i in tempDict.keys()]

        for i in range(k):
            maxVal=max(tempDict,key= lambda x: tempDict[x] )
            del tempDict[maxVal]
            result.append(maxVal)
 
        
        return result





# nums = [1,1,1,2,2,3]
# k = 2
# nums = [1]
# k = 1

nums=[1,2]
k=2

sl=Solution()
print(sl.topKFrequent(nums,k))
