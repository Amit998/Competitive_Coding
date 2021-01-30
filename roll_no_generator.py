val="43251 3"
val=val.split(' ')
val1=list(val[0])
shift=val[1]
print(val1)



new_list=[]
for i in range(len(val1)):
    temp=i+int(shift)
    if (temp > len(val1)):
        new_shift=temp % len(val)
        # print(new_shift)
        new_list.append(val1[new_shift])
    else:
    
        new_list.append(val1[temp-1])

print("".join(new_list))
