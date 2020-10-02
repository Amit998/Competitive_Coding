# 3
# 10 2 12
# 5 10 15 
# 13 5 18



# 10 2
# 5 10 
# 13 5


# 3
# 10
# 2
# 5
# 10
# 13
# 5


# num=int(input())
# arrival_Time=[]
# staying_Time=[]
# Total_Time=[]

# for i in range(num):
#     at = int(input())
#     arrival_Time.append(at)
#     stt=int(input())
#     staying_Time.append(stt)
# for i in range(num):
#     total=arrival_Time[i]+staying_Time[i]
#     Total_Time.append(total)

# counter=1
# for i in range(num):
#     for j in range(num):
#         if( arrival_Time[i] >= Total_Time[j] ):
#             counter+=1


# print(counter)





arrival_Time=[]
Total_Time=[]
num=int(input())
for i in range(num):
    at , stt =map(int,input().split())
    arrival_Time.append(at)
    Total_Time.append(at+stt)

counter=1
for i in range(num):
    for j in range(num):
        if( arrival_Time[i] >= Total_Time[j] ):
            counter+=1
            arrival_Time.remove(arrival_Time[i])
            break




print(counter)