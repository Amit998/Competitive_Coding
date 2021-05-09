import random

class Solution:
   
    def __init__(self, nums):
        self.original=nums[:]
        # self.tempList=[null]
        

    def reset(self):
  
        return self.original
       
        

    def shuffle(self):
        results=self.original[:]
        random.shuffle(results)
        return results
        


# Your Solution object will be instantiated and called as such:
nums=[1, 2, 3]
obj = Solution(nums)

param_1 = obj.reset()

param_2 = obj.shuffle()
