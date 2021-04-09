class Solution:
    def majorityElement(self, nums):
        counter=0
        value=0
        tempDict={}
        res=[]

        for i in nums:
            if i not in tempDict:
                tempDict[i]=1
            else:
                tempDict[i]+=1

        maxEl=max([i for i in tempDict.values()])

        n=len(nums)
        ap=int(n/3)
        print(ap)
        for i in tempDict.keys():
            if tempDict[i]>ap:
                res.append(i)
        

        # for i in r
        # print(res)

        return res




# nums = [3,4,56,7,1]
# nums=[1]
# nums = [3,2,3]
# nums = [1,2,1,1,1,1,1,1,2]
nums=[1,2,3]
sl=Solution()
print(sl.majorityElement(nums))
