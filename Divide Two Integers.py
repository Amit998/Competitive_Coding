class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == 0 or divisor == 0): return 0


        dividend=abs(dividend) #D
        divisor=abs(divisor) #DV

        output=0
        # print(dividend,divisor)
        while (dividend >= divisor):
            temp=divisor
            mul=1
            while dividend>=temp:

                print(dividend,temp,output,mul)

                
                dividend-=temp
                output+=mul
                mul+=mul
                temp+=temp

            # dividend-=divisor
            # output+=1
        

        if (dividend < 0 and divisor < 0):
            print("hell")
            return output
        elif dividend < 0 or divisor < 0:
            print("hell")
            return -output
        
            
        return min(2147483648,max(-2147483648,output))




# dividend = 10
# divisor = 3
dividend = -7 
divisor = 3
# dividend = -100 
# divisor = -20
# dividend = 0 
# divisor = 1
# dividend = 1 
# divisor = 1

# dividend = -2147483648
# divisor = -1

sl=Solution()
print(sl.divide(dividend,divisor))
