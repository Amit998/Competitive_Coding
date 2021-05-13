class Solution:
    def calculate(self,s):
        happy_num=0
        for i in s:
            happy_num+=int(i)*int(i)
        return happy_num
    
    def isHappy(self, n: int) -> bool:
        tempDict={}

        tempList=list(str(n))

        while True:
            val=self.calculate(tempList)
            # print(val)
            if val in tempDict.keys():
                
                return False
            elif (val == 1):
                return True
            else:
                tempDict[val]=1
                tempList=list(str(val))
