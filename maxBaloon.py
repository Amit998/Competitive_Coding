



# word="balloon"
# word=list(word)


# test="nlaebolko"
# test="leetcode"

# tempStr=list(test)
# print(tempStr)

# tempDict={}


# def minVal(a,b):
#     # print(a,b)
#     # return 1
#     if( a < b):
#         # print(b)
#         return a
#     else:
#         # print(a)
#         return b

# for i in range(len(tempStr)):
#     if tempStr[i] not in tempDict.keys() and tempStr[i] in word:
#         tempDict[tempStr[i]]=1
#         pass
#     elif(tempStr[i] in word):
#         tempDict[tempStr[i]]+=1

# print(tempDict)

# wordCount=[]
# tempStr

# if(tempDict.values() in word):
#     print('true')
# else:
#     print('false')
# if (len(tempDict.values()) < len(word)-2 ):
#     print(0)


# print(tempDict)
# print(len(tempDict.values()) , len(word)-2)

# # minVal=0
# min=min(tempDict,key=lambda x:tempDict[x])

# print(tempDict[min])
# for j in tempDict.keys():
    # print(j)
    # print(tempDict[j])
    # minVal(tempDict[j],min)
    # min=minVal(int(tempDict[j]),min)

    # print(min)

# print(min)

def balloon_counter(text):
    word="balloon"
    word=list(word)

    tempStr=list(text)
    tempDict={}

    if(len(tempStr) < len(text) ): return 0

    for i in range(len(tempStr)):
        if tempStr[i] not in tempDict.keys() and tempStr[i] in word:
            tempDict[tempStr[i]]=1
            pass
        elif(tempStr[i] in word):
            tempDict[tempStr[i]]+=1
    
    # print(tempDict)
    
    if (len(tempDict.values()) < len(word)-2):  return 0

    if (tempDict['l'] < 2 or  tempDict['o'] < 2 ):
        print('this')
        return 0

    tempDict['l']=int( tempDict['l']/ 2)
    tempDict['o']= int(tempDict['o']/ 2)

    print(tempDict)

    minVal=min(tempDict,key=lambda x:tempDict[x])

    return tempDict[minVal]
    


# test="nlaebolko"
# test="leetcode"
# test="leetcode"
# test="balon"
# test="krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"
print(balloon_counter(test))
