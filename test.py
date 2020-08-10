D={}
P=5 #minimum length
Q=7 #maximum length
R=3 #minimum width
S=4 #maximum width


def countNow(a,b):
    minimum=min(a,b)
    maximum=max(a,b)

    i=(minimum,maximum)
    if i in D:
        return D[i]
    if minimum ==0:
        return 0
    if minimum == 1:
        return a * b
    
    chocolate = maximum // minimum
    new_side= maximum % minimum
    # chocolate += countNow(new_side,minimum)


answer=0
for i in range(P,Q+1):
    for j in range(R,S+1):
        answer  = countNow(i,j)
        print(answer)
        