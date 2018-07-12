#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



class Solution(object):
    def numIslands0(self, grid):
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
    
    


    def numIslands(self, grid):

        if not grid or len(grid) == 0:
            return 0
        
        self.ilen = len(grid)
        self.jlen = len(grid[0])
        self.visited = [[0 for j in range(self.jlen)] for i in range(self.ilen)]
        self.grid = grid
        num_island = 0

        for i in range(self.ilen):
            for j in range(self.jlen):
                if self.visited[i][j] == 0 and grid[i][j] == "1":
                    self.visit(i, j)
                    num_island += 1

        return num_island

    def visit(self, i, j):
        
        #print('visiting '+ str(i) + str(j))
        if i < 0 or i > self.ilen-1 or j < 0 or j > self.jlen-1:
            return None

        if self.visited[i][j] == 0:
            self.visited[i][j] = 1

            if self.grid[i][j] == "1":

                self.visit(i-1, j)
                self.visit(i+1, j)
                self.visit(i, j-1)
                self.visit(i, j+1)

    
    
    
    
    
    
    
    
    
    
    
    
    
            