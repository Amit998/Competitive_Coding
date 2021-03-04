nums=[-2,1,-3,4,-1,2,1,-5,4]

tsum=0
max=0
for i in range(len(nums)):
    tsum+=nums[i]
    if (max > tsum):
        max=max
    else:
        max=tsum
    if (tsum < 0):
        tsum=0

# if(sum(nums)  <0):
#     max=sum(nums)
# print(sum(nums))
    
   

print(max)
