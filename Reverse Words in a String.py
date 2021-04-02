class Solution:
    def reverseWords(self, s):
        # tempList=s.split(" ")
        temp=[n for n in s.split(" ") if n !=""]
        # print(temp)
        # tempStr
        tempStr=[]
        for i in range(len(temp)):
            tempStr.append(temp[len(temp)-i-1])
        # str=
        
        return " ".join(tempStr)



# s = "a good   example"
s = "  Bob    Loves  Alice   "
# s = "Alice does not even like bob"
sl=Solution()
print(sl.reverseWords(s))
