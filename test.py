# D={}
# P=5 #minimum length
# Q=7 #maximum length
# R=3 #minimum width
# S=4 #maximum width


# def countNow(a,b):
#     minimum=min(a,b)
#     maximum=max(a,b)

#     i=(minimum,maximum)
#     if i in D:
#         return D[i]
#     if minimum ==0:
#         return 0
#     if minimum == 1:
#         return a * b
    
#     chocolate = maximum // minimum
#     new_side= maximum % minimum
#     # chocolate += countNow(new_side,minimum)


# answer=0
# for i in range(P,Q+1):
#     for j in range(R,S+1):
#         answer  = countNow(i,j)
#         print(answer)
        
# from itertools import combinations

  
# def rSubset(arr, r): 
#     comb=[]

#     comb=list(combinations(arr, r)) 
#     print(comb)
#     return comb

#     arr = [1, 2, 3, 4] 
#     r = 2
#     print(rSubset(arr, r) )

# import itertools

# our_list = [1, 2, 3]
# new_lst=[]
# for L in range(0, len(our_list)+1):
#     for subset in itertools.combinations(our_list, L):
#         if(len(subset) != 0):
#             new_lst.append(list(subset))
# print(new_lst)


# from word2number import w2n

# lst=[1,4,8]

# for i in range(len(lst)):
#     conv=(w2n.number_formation(str(lst[i])))
#     print(conv)

# 3
# 7 4 2
# 5
# 1 2 3 4 5

# from num2words import num2words
# import itertools

# n=int(input())
# lst=[]
# lst=list(map(int,input().split()))
# counter=0
# for i in range(n):
    
#     temp_list=[]
#     temp_val=num2words(lst[i])
#     temp_list.append(temp_val)
#     temp_val_new_list=list(temp_val)
#     for j in range(len(temp_val_new_list)):
#         if ( temp_val_new_list[j]  == 'a' or temp_val_new_list[j]  == 'e' or temp_val_new_list[j]  == 'i' or temp_val_new_list[j]  == 'o' or temp_val_new_list[j]  == 'u' ):
#             counter+=1


# new_lst=[]


# for L in range(0, len(lst)+1):
#     for subset in itertools.combinations(lst, L):
#         if(len(subset) != 0):
#             new_lst.append(list(subset))
# for i in range(len(new_lst)):
    
#     if( sum(new_lst[i]) == counter ):
#         print(new_lst[i])
#         print('lol')


# import itertools
  
# large_string=input()
# lst=[]
# size=[]
# num=int(input())
# for i in range(num):
#     temp=input()
#     lst.append(temp)
    
# new_list=list(large_string)

# print(new_list)
# for i in range(num):
#     temp_list=list(lst[i])
#     for j in range(len(temp_list)):
#         print(temp_list[j])
#         if temp_list[j] in new_list:
#             new_list.remove(temp_list[j])
#             print('found')
#         else:
#             print('not found')




    # for subset in itertools.combinations(new_list,6):

    #     temp =(convertTuple(subset))
    #     print(lst[i])
    #     print(temp)

    #     if( lst[i] == temp ):
    #         print(lst[i])
    #         print(temp)
    #         print('true')
    #         break

# for L in range(0, len(new_list)+1):
#     for subset in itertools.combinations(new_list, L):
#         if(len(subset) != 0):
#             combination_list.append(list(subset))

            
# print(combination_list)




numbers = [x for x in range(0, 10)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
numWords = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] 
translate = dict(zip(numbers, numWords)) 
digits = {1:'rupees', 2: 'and', 3: 'hundred', 4: 'thousand'} 
 
numDigits = 100 
num = int(input()) 
res ="" 
 
#to loop till we get the answer 
while numDigits >= 2: 
   #to find number of digits 
    
   numDigits = len(str(num)) 
 
   #to get the first digit 
   numString = str(num) 
   first = int(numString[0]) 
 
   #to get the first output and the thousand, hundred and 'and' 
   if numDigits == 2: 
      res += " " + digits[numDigits] + " " + translate[first] 
   else: 
      res += " " + translate[first] 
    
   #to decrease by a digit we modulus divide by 1e(numDigits-1) 
   num %= pow(10, numDigits-1) 
print(res)