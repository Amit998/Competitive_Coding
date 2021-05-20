##TC=0(N3)

class Solution:
    def longestPalindrome(self, s):
        length=len(s)
        string=""
        start = 0

        maxLength=1

        for i in range(length):
            for j in range(i,length):
                flag=1
                for k in range(0,((j-i)//2)+1):
                   
                    if (s[i+k] != s[j-k]):
                        flag=0
                if (flag != 0 and (j-i+1) > maxLength ):
                    start=i
                    maxLength=j-i+1
                    # print(start,maxLength)

        maxLength=maxLength+start-1
        # print(start,maxLength)
        string=''.join(s[start:maxLength+1])
      

                    

        return string

     





# s = "babad"
s = "cbbd"
s = "ac"
s="aaaabbaa"
s="civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"

sl=Solution()
# sl.longestPalindrome(s)
print(sl.longestPalindrome(s))
