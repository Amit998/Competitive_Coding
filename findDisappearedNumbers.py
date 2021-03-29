# import collections
# class Solution:
#     def findDisappearedNumbers(self, nums):

#         d=collections.Counter(nums)
#         # print(d)

#         return [x for x in range(1,len(nums)+1) if x not in d]
#         # mis=[]

#         # for i in nums:
#         #     pos=abs(i) -1

#         #     if (nums[pos] >0):
#         #         pos[nums] *= -1
#         #     print(pos)
       

# nums=[4,3,2,7,8,2,3,1]
# # nums = [1,1]
# # nums = [2,2]

# sl=Solution()

# print(sl.findDisappearedNumbers(nums))
import collections
class Solution:
    def findDisappearedNumbers(self, nums):

        d={}
        for i in range(len(nums)):
            if (nums[i] in d):
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        # print(d)

        return [x for x in range(1,len(nums)+1) if x not in d.keys()]
        # mis=[]

        # for i in nums:
        #     pos=abs(i) -1

        #     if (nums[pos] >0):
        #         pos[nums] *= -1
        #     print(pos)
       

nums=[4,3,2,7,8,2,3,1]
# nums = [1,1]
# nums = [2,2]

sl=Solution()

print(sl.findDisappearedNumbers(nums))
