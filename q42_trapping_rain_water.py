
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

import collections

class Solution(object):
    
    # O(kn) n: # elements, k: # unique elements
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        
        # get unique heights and count
        # O(klogk) k: unique elements
        height_count = collections.Counter(height)
        unique_height = [key for key in height_count]  #should be already sorted in ascending order
        unique_height.sort()
        
        # O(kn)
        prev_left = None
        prev_right = None
        for i in reversed(range(len(unique_height))):
            
            # find two furthest walls of given height
            left = None
            right = None
            for j in range(len(height)):
                if height[j] == unique_height[i]:
                    if left is None:
                        left = j
                    if left is not None and right < j:
                        right = j
            
            print('left = {0}, prev_left = {1}, prev_right = {2}, right = {3}'.format(left, prev_left, prev_right, right))
            extra_water = 0
            # collect all water within the two walls, and outside previous walls (if existing)
            # if there's no previous wall

            if prev_left is None and prev_right is None: 
                for k in range(left+1, right):
                    extra_water += unique_height[i] - height[k]

            # if there's previous wall:
            if prev_left is not None and prev_left > left:
                for k in range(left, prev_left):
                    extra_water += unique_height[i] - height[k]

            if prev_right is not None and prev_right < right:
                for k in range(prev_right+1, right):
                    extra_water += unique_height[i] - height[k]
            
            print('extra_water = {0}'.format(extra_water))
            water += extra_water
            prev_left = min(left, prev_left) if prev_left is not None else left
            prev_right = max(right, prev_right) if prev_right is not None else right
        
        return water
                            

                    

    # improved: O(n)
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        
        # get unique heights and positions   O(n)
        # {height: [leftmost_pos, rightmost_pos]}
        height_count = {}
        for i in range(len(height)):
            if height[i] not in height_count:
                height_count[height[i]] = [i, i]
            else:
                height_count[height[i]][1] = i
        
        unique_height = [key for key in height_count]  #should be already sorted in ascending order
        unique_height.sort()
        
        
        
        prev_left = None
        prev_right = None
        
        #O(n)
        for i in reversed(range(len(unique_height))):
                        
            left, right = height_count[unique_height[i]]
            
            #print('left = {0}, prev_left = {1}, prev_right = {2}, right = {3}'.format(left, prev_left, prev_right, right))
            extra_water = 0
            # collect all water within the two walls, and outside previous walls (if existing)
            # if there's no previous wall

            if prev_left is None and prev_right is None: 
                for k in range(left+1, right):
                    extra_water += unique_height[i] - height[k]

            # if there's previous wall:
            if prev_left is not None and prev_left > left:
                for k in range(left, prev_left):
                    extra_water += unique_height[i] - height[k]

            if prev_right is not None and prev_right < right:
                for k in range(prev_right+1, right):
                    extra_water += unique_height[i] - height[k]
            
            #print('extra_water = {0}'.format(extra_water))
            water += extra_water
            prev_left = min(left, prev_left) if prev_left is not None else left
            prev_right = max(right, prev_right) if prev_right is not None else right
        
        return water
                    
        
        