class Solution:
    def maxCoins(self, nums):
        print(nums)
        points=sorted(nums,key= lambda x: x[1])
        # points=sorted([ sorted(i) for i in nums ])
        print(points)
        count=0
        ending=float('-inf')
        # print(ending)

        for baloon in points:
            if baloon[0] > ending:
                
                count+=1
                ending=baloon[1]
        return count





# nums= [[10,16],[2,8],[1,6],[7,12]]
# nums = [[1,2],[3,4],[5,6],[7,8]]
# nums = [[1,2],[2,3],[3,4],[4,5]]
nums=[[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]

sl=Solution()
print(sl.maxCoins(nums))
