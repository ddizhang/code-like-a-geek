import pdb

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    lenAll = len(nums1) + len(nums2)
    medLen = lenAll%2
    pdb.set_trace() 
    i = 1
    while i <= lenAll//2:
        if len(nums1) == 0:
            num = nums2.pop(0)
        elif len(nums2) == 0:
            num = nums1.pop(0)
        elif nums1[0] < nums2[0]:
            num = nums1.pop(0)
        else:
            num = nums2.pop(0)
        i = i + 1
    #after the while loop, we'll have the (len//2)th smallest number
    
    #get the (len//2 + 1)th smallest number
    if lenAll == 1:
        num2 = num
    elif len(nums1) == 0:
        num2 = nums2.pop(0)
    elif len(nums2) == 0:
        num2 = nums1.pop(0)
    elif nums1[0] < nums2[0]:
        num2 = nums1.pop(0)
    else:
        num2 = nums2.pop(0)
    
    if medLen == 1:
        med = num2
    else:
        med = (num + num2)/2
    
    return med



findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4])
