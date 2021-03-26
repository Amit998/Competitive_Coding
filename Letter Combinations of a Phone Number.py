class Solution:

    
    
    def letterCombinations(self, digits):
        digitToChar={
            "0":" ",
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res=[]
        def backtrack(i,curStr):
            print(curStr,len(digits))
            print(i,'i')
            if (len(curStr) == len(digits)):
                res.append(curStr)
                return
            
            for c in digitToChar[digits[i]]:
                print(c,'c')
                backtrack(i+1,curStr+c)

        if digits:
            backtrack(0,"")
        return res


digits = "23"
# digits = ""
# digits = "2"

sl=Solution()

print(sl.letterCombinations(digits))
