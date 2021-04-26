
def rotateWords(input1,input2):
    rotateString=input1.split(' ')

    count=0

    for i in range(1,input2+1):
        for j in range(len(rotateString)):
            rotateString[j]=rotateString[j][1:]+rotateString[j][0]
            print(rotateString[j])
            print(rotateString[j][1:])
            print(rotateString[j][0])
            print('\n')
    
    actualWord=input1.split(' ')

    for i in range(len(rotateString)):
        for j in range(len(actualWord)):
            if rotateString[i]==actualWord[j]:
                count+=1
    
    return count


print(rotateWords("adaada",3))
print(rotateWords("llohe ereth",2))
