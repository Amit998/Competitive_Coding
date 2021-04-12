class Solution:
    def calculate(self, s: str) -> int:
        s=list(s)

        if len(s)==0:
            return 0
        stack=[]
        sign="+"
        num=0

        while (len(s)>0):
            c=s.pop(0)
            if c.isdigit():
                num=num*10+int(c)
            
            if c == '(':
                num=self.calculate(s)

            if len(s)==0 or (c == '+' or c == '-' or c == '*' or c == '/' or c == ')' ):
                if sign=="+":
                    stack.append(num)
                elif sign=="-":
                    stack.append(-num)
                elif sign=="/":
                    stack[-1]=int(stack[-1]/float(num))
                elif sign=="*":
                    stack[-1]=int(stack[-1]*float(num))
                sign=c
                num=0

                if sign == ')':
                    break
        print(stack)
        return sum(stack)

# s = "1 + 1"
# s = " 2-1 + 2 "
# s="(1+(4+5+2)-3)+(6+8)"

# s="3+2*2"
# s="3/2" 
# s="3+5/22"
s="0-2147483647"


sl=Solution()
print(sl.calculate(s))
