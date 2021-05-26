class Solution:
    def reverse(self, x: int) -> int:
        tempStr=list(str(x))
        
        newStr=[]
        flag=-1
        tempChar=""
        counter=0
        for i in range(len(tempStr)):
            if(tempStr[len(tempStr)-i-1] == "-"):
                flag=1
                continue
           
            elif(tempStr[len(tempStr)-i-1] == "0"):
                newStr.append(tempStr[len(tempStr)-i-1])
                counter+=1
                continue 
                
                
            else:
                newStr.append(tempStr[len(tempStr)-i-1])
        if(counter == len(tempStr)):
            return 0
        tempLen=len(newStr)
        i=0
        while (newStr[i] =="0"):
            i+=1
            # print(i)
        newStr[:]=newStr[i:]    
        # print(newStr)

        if ( int(''.join(newStr)) > (2**31)-1 ):
            return 0

        
        if(flag==1):
            new="-"+''.join(newStr)
            # print(new)
        else:
            new=''.join(newStr)
            # print(new)
        
        
        # print(new)
        return new
x = 123
x = -123
# x = 120
# x = 0
# x=90100000000000000000
# x=1534236469

sl=Solution()
print(sl.reverse(x))
