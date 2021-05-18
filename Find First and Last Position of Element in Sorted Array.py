class Solution:
    def searchRange(self, nums, target):
        left=self.binSearch(nums,target,True)
        right=self.binSearch(nums,target,False)

        return [left,right]



    def binSearch(self,nums,target,leftBias):

        l,r=0,len(nums)-1
        i=-1
        while (l<=r):   
            m=(l+r)//2
            if target > nums[m]:
                l=m+1
            elif target < nums[m]:
                r=m-1
            else:
                i=m
                if leftBias:
                    r=m-1
                else:
                    l=m+1
        return i

        
        
        



nums = [5,7,7,8,8,10]
target = 8
# nums = [5,7,7,8,8,10]
# target = 6
# nums = []
# target = 0
sl=Solution()
print(sl.searchRange(nums,target))
