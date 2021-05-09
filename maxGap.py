class Solution:
    def maximumGap(self, nums):
        nums=sorted(nums)
        gap=0
        # print(nums)
        for i in range(len(nums)-1):
            diff=nums[i+1]-nums[i]
            if (gap < diff):
                gap=diff
        
        # print(gap)/

        return gap
        

nums = [3,6,9,1]
nums = [10]
sl=Solution()
print(sl.maximumGap(nums))
