class Solution(object):
    
    # dynamic programming
    # Time: O(m*n)
    # Space: O(m*n)
    # not tested
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[1])
        
        # initialize a min_sum grid 
        dp = [[-1 for i in range(n)] for j in range(m)]
        
        # calculate the left and top edge
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1,n):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        
        # calculate one column right and one column down
        # for each cell, sum is the grid value plus the minimum of the cell above it and left to it
        for k in range(min(m,n)):
            for i in range(1,m):
                dp[i][1] = grid[i][1] + min(dp[i-1][1], dp[i][0])
            for j in range(2,n):
                dp[1][j] = grid[1][j] + min(dp[1][j-1], dp[0][j])
        
        return dp[m-1][n-1]
        
        