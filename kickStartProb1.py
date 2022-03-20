s1="KickstartIsFun"
s2="kkickstartiisfun"


num=int(input())
for k in range(num):
    str1=input()
    str1List=list(str1)
    str2=input()
    str2List=list(str2)

    m=len(str1)
    n=len(str2)

    i=0
    j=0
    ans=0

    while (j < n and i < m):
        if(str1List[i] == str1List[j]):
            i+=1
        else:
            ans+=1
        j+=1 
    if(i == m):
        print("Case #",k+1,": ",ans+n-j)
    else:
        print("Case #",k+1,": IMPOSSIBLE")
