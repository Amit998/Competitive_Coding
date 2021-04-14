class Solution:

    def countBits(self, num):
        lst=[]
        for i in range(num+1):
            val=list(bin(i).replace("0b",""))
            lst.append(val.count('1'))
        
        return lst
# num = 2
num = 5
sl=Solution()
print(sl.countBits(num))

# print(bin(5).replace("0b",""))

# def decimalToBinary(num):
#     temp=""
#     if num >= 1:
#         temp=decimalToBinary(num//2)
#         temp+=str(num%2)
#         return temp

# print(decimalToBinary(2))
