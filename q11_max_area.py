class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        max_vol = (r-l) * min(height[l], height[r])

        while True:
            # move the left bar if the left bar is lower
            if height[l] < height[r]:
                while True:
                    l += 1
                    if height[l] > height[l-1] or l == len(height)-1:
                        break
            
            # move the right bar if right bar is lower
            else:
                while True:
                    r -= 1
                    if height[r] > height[r+1] or r == 0:
                        break

            if l >= r:
                break
            
            new_vol = (r-l) * min(height[l], height[r])
            if new_vol > max_vol:
                max_vol = new_vol
            
        return max_vol
            
