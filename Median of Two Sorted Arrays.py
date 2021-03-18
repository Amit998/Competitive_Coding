

# def get_median(lst):
#     lst.sort()
#     if (len(lst) == 1):
#         return lst[0]
#     if (len(lst)%2 == 0):
#         num1=lst[int(len(lst)/2)]
#         num2=lst[int(len(lst)/2) -1]
#         return float(int(num1 + num2) /2)
#     else:
#         return float(lst[int(len(lst)/2)])




# # lst=[1,2,3,4]
# # lst=[1,2,3,4]
# # print(get_median(lst))

# def findMedianSortedArrays(nums1, nums2):

#     if (len(nums1) == 0 and len(nums2) != 0):
#         return get_median(nums2)
#         # print(nums2)
    
#     if (len(nums2) == 0 and len(nums1) != 0):
#         # print(nums1)
#         return get_median(nums1)
    
#     if (len(nums2) == 0 and len(nums1) == 0):
#         return 0.00
    
#     nums1.extend(nums2)


#     val=get_median(nums1)

#     return val

# # nums1=[1,3]
# # nums2=[2]

# nums1=[2]
# nums2=[]
# print(findMedianSortedArrays(nums1,nums2))

# print(len(nums1))
# lst=[1,2,3,40,2]

# lst.sort()

# print(lst)

# def myFunc(e):
#   return len(e)

# # cars = ['1','5','2']
# cars=[1,23,4,22,3]

# cars.sort()

# print(cars)

class Solution:

    def __init__(self):
        pass
    
    def get_median(self,lst):
        # print(lst)
        if(len(lst) == 0):
            print(lst,' hello')
            return 0.00
        if ( len(lst) == 1): return float(lst[0])
        lst.sort()
        # print(lst)
        # if ( len(lst) == 1):
        #     return float(lst[0])
        print(lst)
        if (len(lst)%2 == 0):
            # print(lst)
            
            num1=lst[int(len(lst)/2)]
            num2=lst[int(len(lst)/2) -1]
            return float(int(num1 + num2) /2)
        else:
            return float(lst[int(len(lst)/2)])

    def findMedianSortedArrays(self, nums1, nums2):
        if (len(nums2) == 0 and len(nums1) == 0):
            # print('hello')
            return 0.00000
        if (len(nums1) == 0 and len(nums2) != 0):

            # print('hello')
            return self.get_median(nums2)
        if (len(nums2) == 0 and len(nums1) != 0):
            print(nums1)
            return self.get_median(nums1)

        

        nums1.extend(nums2)

        val=self.get_median(nums1)
        
        
        return val

nums1=[2]
nums2=[]
sl=Solution()
print(sl.findMedianSortedArrays(nums1,nums2))

# nums2
