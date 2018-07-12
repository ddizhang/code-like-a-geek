# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].


# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # search left, and right border seperately
        # when searching left border, end = mid if mid = target
        # and when start = end = target, return start
        
        # when searching right border, do similar
        
        left_pos, right_pos = -1, -1
        
        # find left position
        s, e = 0, len(nums) - 1

        while s <= e:
            # if the first item is target
            if nums[0] == target:
                left_pos = 0
                break
            
            m = (s + e) // 2
            print('find left position: s: {0}, m: {1}, e: {2}'.format(s, m, e))
            if nums[m] == target and nums[m-1] < target:
                left_pos = m
                break
            elif nums[m] >= target:
                e = m - 1
            else:
                s = m + 1
        
        # find right position
        s, e = 0, len(nums) - 1
        
        while s <= e:
            # if the last item is target
            if nums[-1] == target:
                right_pos = len(nums) - 1
                break
            
            m = (s + e) // 2
            print('find right position: s: {0}, m: {1}, e: {2}'.format(s, m, e))            
            if nums[m] == target and nums[m+1] > target:
                right_pos = m
                break
            elif nums[m] > target:
                e = m - 1
            else:
                s = m + 1
        
        return [left_pos, right_pos]