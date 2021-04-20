


def primeCheck(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            return number

def main():
    n=int(input())
    for i in range(n):
        tempList=[]
        
        val=list(map(int,input().split()))
        lowerbound,upperbound=val[0],val[1]

        for i in range(lowerbound,upperbound+1):
            minval=primeCheck(i)
            if minval != None:
                break
        
        for i in range(lowerbound,upperbound+1):
            maxVal=primeCheck(lowerbound+upperbound-i)
            if maxVal != None:
                break
        
        # print(minval,maxVal)
        if (maxVal == None and minval == None):
            print(-1)
        elif maxVal == minval:
            print(0)

        else:
         print(maxVal-minval)
        
      
    
                    
main()

# 5
# 5 5
# 2 7
# 8 10
# 10 20
# 4 5
# 5
# 5 5
# [5]
# 2 7
# [2, 3, 5, 7]
# 8 10
# []
# 10 20
# [11, 13, 17, 19]
# 4 5
# [5]

# 1
# 8 10
