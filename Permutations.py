class Solution:
    def permute(self, nums):
        result=[]

        if( len(nums) == 1):
            return [nums[:]]

        for i in range(len(nums)):
            n=nums.pop(0)
            perms=self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        # print(result)
        
        return result
        
        





nums = [1,2,3]
# nums = [0,1]
# nums = [1]

sl=Solution()
print(sl.permute(nums))
