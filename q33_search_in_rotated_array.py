class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # Step 1: find rotate point
        # Step 2: mapping rotated indices to sorted indices
        # Step 3: binary search on sorted indices
        # Step 4: retrieve rotated index
        
        if nums == []:
            return -1
        
        # Another solution:
        # not debugged
        head, tail = 0, len(nums)-1
        mid = (head + tail) // 2
        print('head:'+ str(head)+' tail:'+ str(tail))
        
        while head <= tail:
            mid = (head + tail) // 2
            print('mid:'+str(mid))
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[head]:
                if nums[mid] > target and target >= nums[head]:
                    tail = mid - 1
                else:
                    head = mid + 1
            
            else:
                if nums[mid] < target and target <= nums[tail]:
                    head = head + 1
                else:
                    tail = mid - 1
            
            print('head:'+ str(head)+' tail:'+ str(tail))
        
        return -1
        
        
        