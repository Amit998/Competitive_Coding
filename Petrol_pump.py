# import math

# # lst=[25,30,35,20,90,110,45,70,80,12,30,35,85]




# def calc_dif(a,n):
#     s=(sum(a))
#     matrix=[[0 for i in range (s+1)] for j in range(n+1) ]
#     print(matrix)

#     for i in range(n+1):
#         matrix[i][0]=1
#     for i in range(1,n+1):
#         for j in range(1,s+1):
#             matrix[i][j]=matrix[i-1][j]
#             if(a[i-1]<=j):
#                 matrix[i][j] |= matrix[i-1][j-a[i-1]]
   
#     for j in range(s//2,-1,-1):
#         if(matrix[n][j] ==1):
#             diff=s-(2*j)
#             break
    
#     return diff

# ip_arr=[1,2,3,4,5,10,11,3,6,16] 

# diff=calc_dif(ip_arr,len(ip_arr))

# min=(sum(ip_arr) - diff)/2
# print(sum(ip_arr),'sum',diff)
# max=int(min) + diff
# print(max)


# lst.sort()
# flag=0

# lst1=[1,16,3,10]
# lst2=[2,11,4,5,6]
# lst1=[]
# lst2=[]

# print(int(len(lst)))

# for i in range(int(len(lst)/2)):
#     print(lst[i])
 
#     if(flag == 0):
        
#         lst1.append(i)
#         flag=1
#     else:
#         lst2.append(i)
#         flag=0
# length=(len(lst))
# counter=1
# for i in range(len(lst)):
#     if( sum(lst1) == sum(lst2) ):
#         lst2.append(lst[length-counter])
#         counter+=1
#     elif ( sum(lst1) > sum(lst2) ):
#         lst2.append(lst[length-counter])
#         counter+=1
#     elif( sum(lst1) < sum(lst2) ):
#         lst1.append(lst[length-counter])
#         counter+=1


# print(lst1)
# print(lst2)

# print(sum(lst1))
# print(sum(lst2))

def calcDiff(input,sum):
    size=len(input)-1
   
    dp=[[0 for i in range(sum+1)] for j in range(size+1) ]
    for i in range(size+1):
        dp[i][0]=True
    for j in range(1,sum+1):
        dp[0][j]=False
        
    for i in range(1,size+1):
        for j in range(1,sum+1):
            dp[i][j]=dp[i-1][j]
            if(input[i-1] <= j):
                dp[i][j] |= dp[i-1][j-input[i-1]]
    print(dp[len(dp)-1])
    for j in range(sum//2,-1,-1):
        if (dp[size][j] == True):
            diff=sum-(2*j)
            break
    
    return diff
            


input=[25,30,35,20,90,110,45,70,80,12,30,35,85]
# input=[1,2,3,4,5,10,11,3,6,16]
sum=sum(input)
diff=(calcDiff(input,sum))
min_p=(sum-diff)/2
max_p=min_p+diff
print(min_p)
print(max_p)