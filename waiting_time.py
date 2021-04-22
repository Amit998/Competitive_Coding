

array=[3,2,1,2,6]


def waiting_time(array):
    sumVal=0
    array.sort()
    print(array)
    for i in range(len(array)):
        tempList=array[:i]
        sumVal+=sum(tempList)
        print(tempList)
    
    print(sumVal)



waiting_time(array)
