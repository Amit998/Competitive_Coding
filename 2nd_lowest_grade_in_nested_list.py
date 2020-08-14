# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

num=int(input())
lst=[]
for i in range(num):
    temp=[]
    name=input()
    num1=input()
    temp.append(name)
    temp.append(float(num1))
    lst.append(temp)
print(lst)
arrNew=sorted(lst,key=lambda x: x[1])
temVal=arrNew[1][1]
# print(arrNew)
# print(temVal)
counter=0
for i in range(num):
    
    counter=counter+1
    # print(counter)
    # print(num-i)
    if(temVal ==arrNew[num-counter][1] ):
        print(arrNew[num-counter][0],end='\n')
    
  


# print(newVal)

# if __name__ == "__main__":
# temVal=arrNew[1]
# count=arrNew.count(temVal)

# arrNewVal=(key=lambda x: x[1])

# print(temVal)

# mylist = [[7, 8], [1, 2, 3], [2, 5, 6]]
# mylistSort = sorted(mylist, key = lambda x: (x[1]))



# print(mylistSort)