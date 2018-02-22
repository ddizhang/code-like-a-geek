class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # two pointers
        # front one iterating through all elements
        # back one to put the non-zero elements
        
        f = 0 
        b = 0
        while f < len(nums):
            
            if nums[f] != 0:
                # swap f and b
                swap = nums[b]
                nums[b] = nums[f]
                nums[f] = swap
                b += 1
            f += 1
        