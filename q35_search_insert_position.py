class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        
        if target > nums[len(nums)-1]:
            return(len(nums))
        
        while start < end:
            mid = (start+end)//2
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid
        
        print('end'+str(end))
        
        return end