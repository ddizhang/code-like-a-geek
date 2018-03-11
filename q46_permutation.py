class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        if not nums:
            res = []
        elif len(nums) == 1:
            res = [nums]
        else:
            for i in range(len(nums)):
                #res += [perm.append(nums[i]) for perm in self.permute(nums[:i] + nums[i+1:])]
                for perm in self.permute(nums[:i] + nums[i+1:]):                
                    perm.append(nums[i])
                    res.append(perm)
                
        return res