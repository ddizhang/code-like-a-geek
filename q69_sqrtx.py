class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # find the closest integer that is smaller than the square root
        
        left = 0
        right = x
        mid = (left+right)//2

        
        while left <= right:
            
            mid = (left + right) // 2
            if mid**2 <= x < (mid+1)**2:
                return mid
            
            elif mid**2 > x:
                right = mid - 1
            else:
                left = mid + 1
   