class Solution:
    def swap(self,a,b):
        return b,a
    def sortColors(self, nums):
        leng=len(nums)
        high=0
        low=0
        mid=0
        i=0

        zero=[]
        one=[]
        two=[]

        
        while ( i< leng):
            if (nums[i]==0):
                mid+=1
                low+=1
                zero.append(0)
                # print(low)
            elif (nums[i]==1):
                mid+=1
                one.append(1)
                # print(mid)
            elif (nums[i] == 2):
                high+=1
                two.append(2)
                
            i=i+1
        # print(one,two,zero)
        one.extend(two)
        zero.extend(one)
        nums[:]=zero
        # print(nums)
        # print(low,mid,high)
        


nums=[1,0,1,2,1,1,2,0,1]
# nums = [2,0,2,1,1,0]
# nums = [2,0,1]
# nums = [0]
# nums = [1]

sl=Solution()

sl.sortColors(nums)

print(nums)
