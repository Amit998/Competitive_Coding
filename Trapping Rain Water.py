class Solution:
    def trap(self, height: List[int]) -> int:   
        leftArr=[]
        rightArr=[]

        rtemp=0
        ltemp=0
        tempVal=0
        minVal=0
        total=0
        
        for i in range(len(height)):
            if(ltemp < height[i]):
                ltemp=height[i]
            leftArr.append(ltemp)
            
            newVal=(len(height)-i-1)
            # print(newVal)
            # print(len(height))
            if (rtemp < height[newVal]):
                rtemp=height[newVal]
            rightArr.insert(0,rtemp)

            # if ( i != 0 and  i != len(height)-1):
            #     minVal=min(rightArr[i],)
            #     tempVal=height[i]-minVal
            #     total+=(abs(tempVal))
            #     print(i)
        
        
        for i in range(1,len(height)):

            minVal=min(rightArr[i],leftArr[i])
            tempVal=height[i]-minVal
            total+=(abs(tempVal))
        
        return total
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,5]
# height=[1,0,2,0,1,0,3,1,0,2]

Sl=Solution()
Sl.trap(height)
