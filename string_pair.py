
import itertools


n=int(input())
lst=[]
lst=list(map(int,input().split()))
counter=0

def num2words(number):
    if( str(number) == '1' ):
        return 'one'
    elif( str(number) == '2' ):
        return 'two'
    elif( str(number) == '3' ):
        return 'three'
    elif( str(number) == '4' ):
        return 'four'
    elif( str(number) == '5' ):
        return 'five'
    elif( str(number) == '6' ):
        return 'six'
    elif( str(number) == '7' ):
        return 'seven'
    elif( str(number) == '8' ):
        return 'eight'
    elif( str(number) == '0' ):
        return 'zero'
    elif( str(number) == '9' ):
        return 'nine'

    
for i in range(n):
    temp_list=[]
    temp_val=num2words(lst[i])
    temp_list.append(temp_val)
    temp_val_new_list=list(temp_val)
    for j in range(len(temp_val_new_list)):
        if ( temp_val_new_list[j]  == 'a' or temp_val_new_list[j]  == 'e' or temp_val_new_list[j]  == 'i' or temp_val_new_list[j]  == 'o' or temp_val_new_list[j]  == 'u' ):
            counter+=1

new_lst=[]
temp=0
for L in range(0, len(lst)+1):
    for subset in itertools.combinations(lst, L):
        if(len(subset) != 0):
            new_lst.append(list(subset))

for i in range(len(new_lst)):
    # print(new_lst[i])
    if( sum(new_lst[i]) == counter ):
        # print(new_lst[i])
        if ( len(new_lst[i]) %2== 0):
           
            temp+=int(len(new_lst[i] ) / 2)
            
print(num2words(temp),end='')