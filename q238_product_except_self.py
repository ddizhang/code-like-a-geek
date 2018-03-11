class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # three pass:
        # first pass, get the product of nums[0:i]
        # second pass, get the product of nums[i+1, len(num)-1]
        # third pass, combine the result of first two passes
        
        # space:
        # save the results in first pass
        # second and third pass can be done together, and only need to save 1 number 
        
        output = []
        prod_ft = 1
        for i in range(len(nums)):
            output.append(prod_ft)
            prod_ft = prod_ft * nums[i]
        
        prod_bk = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * prod_bk
            prod_bk = prod_bk * nums[i]
        
        return output
            
    
    # O(n) time, O(1) space
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output