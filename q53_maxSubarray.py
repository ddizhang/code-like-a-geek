class Solution(object):
    
    # can be written iteratively instead of recursively
    def maxSubArray1(self, nums):
        
        cur_sum = 0
        msa = nums[0]
        for i in range(len(nums)):
            cur_sum = max(cur_sum + nums[i], nums[i])
            msa = max(cur_sum, msa)
        
        return msa
    
    
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dynamic programming.
        # msa_helper(nums, i) returns the largest subarray ending in position i
        # next position's msa value msa_helpr(nums, i+1) is a function of msa_helper(nums, i)
        # update a global variable recording the max subarray value
        
        self.nums = nums
        self.pos_msa = [None for _ in range(len(nums))]
        self.pos_msa[0] = nums[0]
        self.msa = nums[0]
        self.msa_helper(len(nums)-1)
        return self.msa
        
    # maximum recursion depth reached...
    def msa_helper(self, i):
        
        #print('i=' + str(i))
        #print('pos_msa')
        #print(self.pos_msa)
        if self.pos_msa[i] is not None:
            return self.pos_msa[i]
        
        else:
            msa_prev = self.msa_helper(i-1)
            new_pos_msa = msa_prev + self.nums[i] if msa_prev > 0 else self.nums[i]
            self.pos_msa[i] = new_pos_msa
            # update the global max subarray value
            if new_pos_msa > self.msa:
                self.msa = new_pos_msa

        return self.pos_msa[i]
        