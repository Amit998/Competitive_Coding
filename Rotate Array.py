class Solution:
    def rotate(self, nums, k):
        if (len(nums) > k ):
            nums[:]=nums[-k:]+nums[:-k]
        elif (len(nums) == k):
            nums[:]=nums
        else:
            k= k % len(nums) 
            self.rotate(nums,k)
        return




# nums = [1,2,3,4,5,6,7]
# k = 3
# nums = [-1,-100,3,99]
# k = 2
# nums=[1,2,3,4,5,6,7]
# k=3

# nums=[1,2]
# k=3
nums=[1,2,3]
k=5
# print(nums)
sl=Solution()
print(sl.rotate(nums,k))
print(nums)
        
        
