import itertools

def countOneZero(num):
    lst=list(str(num))
    
    one=lst.count('1')
    zero=lst.count('0')
    # print(one,'one',zero,'zero',num)
    return one,zero


temp_list=[]
def eq(val,counter):
    
    Temp_one=0
    Temp_zero=0
    
    for j in range(len(val)):
        binary=(format(int(val[j]),'04b'))
        one,zero=countOneZero(binary)
        Temp_one+=one
        Temp_zero+=zero
    if ( Temp_one == Temp_zero ):
        temp_list.append(1)



n=int(input())

lst=list(map(int,input().split()))

new_lst=[]
for L in range(0, len(lst)+1):
    for subset in itertools.combinations(lst, L):
        if(len(subset) != 0):
            new_lst.append(list(subset))

counter=0
for i in range(len(new_lst)):
    eq(new_lst[i],counter)

binaryVal=(format(len(temp_list),'04b'))
bin=list(binaryVal)

print(binaryVal)




# 3
# 2 7 10