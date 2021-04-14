
def main():
    V=list(input())
    N=int(input())


    for _ in range(N):
        p=''
        k=input()
        j=0
        t=0
        x=len(V)
        y=len(k)

        while (j < x and t < y):
            if V[j]== k[t]:
                p=p+V[j]
                j=j+1
                t=t+1
            else:
                j+=1
        if p==k:
            print("POSITIVE")
        else:
            print("NEGATIVE")

            
main()

# coronavirus
# 3
# abcde
# crnas
# onarous
