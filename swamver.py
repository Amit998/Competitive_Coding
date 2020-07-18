n=4
f="rmrm"
m="mmmr"
counter_r=m.count('r')
counter_m=m.count('m')
lst=list(f)
for i in f:
    if(i == 'r'):
        if(counter_r==0):
            print(len(f),end='')
            break
        counter_r -=1
        lst.pop(0)
    elif(i == 'm'):
        if(counter_m==0):
            print(len(f),-current,end='')
        
            break
        counter_m ==1
        lst.pop(0)
else:
    print(0,end='')
    