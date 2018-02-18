class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        j = 0
        
        while i < len(nums)-1 and j < len(nums)-1:
            
            while nums[i] == nums[j] and i < len(nums)-1:
                i += 1
                print('i='+str(i))
            
            if j < len(nums)-1 and nums[i] != nums[j]:
                j += 1        
                nums[j] = nums[i]
            print('oneloop'+str(i)+str(j))
            
            if j >= len(nums)-1:
                break
        
        if nums == []:
            return 0
        print('return val'+str(j+1))
        return j+1
        
                
            