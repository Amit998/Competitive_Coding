def g_monkey(unOrdered,length):
    sec=0
    n=0
    Ordered=sorted(unOrdered)
    check=Ordered
    position=[]
    for j in range(length):
        for i in range(length):
            if(Ordered[i] == unOrdered[j]):
                # unOrdered[]="FILLE_DONE"
                # Ordered[i]="FILLE_TWO"
                position.append(i)
                
                break
    print(position)
    print(unOrdered)
    print(Ordered)
    while( n != 1 ):
        sec=sec+1
        tempList=[]
        for i in range(length):
            tempList.append(Ordered[position[i]])

        print(tempList,check)
        if(tempList == check):
            # n=1
            # print('matched')
            return sec
        else:
            Ordered=tempList
            n=0
for i in range(int(input())):
    # unOrdered=list(map(str,input().split()))
    unOrdered=['a','b','d','a']
    # length=(int(input()))
    length=len(unOrdered)
    print(g_monkey(unOrdered,length))   

# print(tempList)
# a=2
# b=5
