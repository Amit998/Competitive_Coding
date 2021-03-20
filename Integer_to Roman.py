class Solution:
    num = 1994

    op="MCMXCIV"

    def get_romanian_symbol(self,val):



        switcher={
            1:"I",
            4:"IV",
            5:"V",
            9:"IX",
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"
        }
        return switcher.get(val)


    def intToRoman(self, num):

        # tempList2=[]

        tempStr=""

        tempList=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
        tempList.reverse()

        tempStr=""

        while (num != 0):
            for i in range(len(tempList)):
                if(num >= tempList[i]):


                    # print(tempList[i])
                    tempVal=num / tempList[i]
                    num=num % tempList[i]
                    # print(num)

                    tempStr+=self.get_romanian_symbol(tempList[i])*int(tempVal)
                    # print(tempList[i],int(tempVal))
                    # print(tempStr)

        return tempStr


            # if (num / tempList[i] != 0):
                # print(tempList[i])
            # if (num > tempList[i] and num < tempList[i+1] ):
            #     print(num)




        # print(self.get_romanian_symbol(num))
        # pass


# num=1249
# num=2944
# num = 3
# num = 4
# num = 58
num = 1994

op="MCMXCIV"

sol=Solution()
print(sol.intToRoman(num))
