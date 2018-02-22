class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # maintain a recorder for the current times of duplicates
        # not debugged 
        
        i = 0
        j = 0
        dup_count = 0
        
        while i < len(nums)-1 and j < len(nums)-1:
            
            while nums[i] == nums[j] and i < len(nums)-1:
                i += 1
                if dup_count < 1:
                    j += 1
                    dup_count += 1
                print('i='+str(i)+'j='+ str(j))
            
            if j < len(nums)-1 and nums[i] != nums[j]:
                j += 1        
                nums[j] = nums[i]
                dup_count = 0
            print('oneloop'+str(i)+str(j))
            
            if j >= len(nums):
                break
        
        if nums == []:
            return 0
        print('return val'+str(j+1))
        return j+1
        
                
            