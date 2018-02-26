class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        # keep a queue / stack for BFS/DFS
        # set visited cell value to zero
        
        if not grid:
            return 0
        
        self.grid = grid
        self.row_num = len(grid)
        self.col_num = len(grid[0])
        
        island_num = 0
        
        for i in range(self.row_num):
            for j in range(self.col_num):
                island_num += self.sink(i,j)
        
        return island_num
    
    def sink(self, i,j):
        
        # print('examine:' + str(i) + str(j))
        # print('row_num' + str(self.row_num))
        # print('col_num' + str(self.col_num))
        # print('grid value' + self.grid[i][j])
        if (0 <= i < self.row_num) and (0 <= j < self.col_num) and self.grid[i][j] == '1':
            #print('sinking:' + str(i) + str(j))
            self.grid[i][j] = 0
            self.sink(i, j+1)
            self.sink(i, j-1)
            self.sink(i+1, j)
            self.sink(i-1, j)
            # map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
            return 1
        return 0
            