N=int(input())
K=int(input())
lst=[]

for i in range(N):
    val=int(input())
    lst.append(val)
newLst=[]
for j in range(K):
    newLst.append(lst[j])
unique=[]
for k in newLst:
    if k not in unique:
        unique.append(k)
print(len(unique))