

def prime_check(number):
    if number == 1:
        return None
    if number>1:
        for i in range(2,number):
            if ( number % i == 0):
                # print("Not P")
                break
            else:
                return number

# n=int(input())
n=10
val=prime_check(n)
if val==None:
    print(f"{n} is not a Prime Number")
else:
    print(f"{val} is Prime Number")