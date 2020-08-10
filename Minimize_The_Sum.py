import math
# lst=[20,7,5,4]
# lst=[]
# N=int(input())
# k=int(input())
N , k =input().split()
lst=list(map(int,input().split()))
# N=4
# k=3

# for i in range(N):
#     m=int(input())
#     lst.append(m)

position=0
for l in range(int(k)):
    maxVal=max(lst)
    for j in range(int(N)):
        if( lst[j] == maxVal):
            position=j
            break
    
    maxVal=maxVal//2
    lst[position]=maxVal
    
print(sum(lst))


    
    



    