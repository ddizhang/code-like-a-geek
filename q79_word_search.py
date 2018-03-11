class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        
        self.board = board
        self.n_row = len(board)
        self.n_col = len(board[0])
        
        self.visited = [[0 for j in range(self.n_col)] for i in range(self.n_row)]
        
        for i in range(self.n_row):
            for j in range(self.n_col):
                if self.searchWord(i,j, word):
                    return True
        return False

        
    def searchWord(self, i, j, word):
        '''
        i,j: position on board
        word: word to search at the position
        '''
        # print('search pos: ' + str(i) + str(j))
        # print('searching word: ' + word)
        # print('searching pos visited: ' + str(self.visited[i][j]))
        # print('\n')
        
        if not word:
            return False
        
        # if already visited: return False
        if self.visited[i][j] == 1:
            return False
        
        # if there's only one character left: see if it's the desired word!
        if len(word) == 1:
            return self.board[i][j] == word
        
        # if there's more than one character, and the first character is not what we're looking for: return False
        if self.board[i][j] != word[0]:
            return False
        
        # set current cell to be visited
        self.visited[i][j] = 1
        
        # check neighbors
        if i+1 < self.n_row and self.searchWord(i+1, j, word[1:]):
            exist = True
        elif i-1 >= 0 and self.searchWord(i-1, j, word[1:]):
            exist = True
        elif j+1 < self.n_col and self.searchWord(i, j+1, word[1:]):
            exist = True
        elif j-1 >= 0 and self.searchWord(i, j-1, word[1:]):
            exist = True
        else:
            exist = False
            
        self.visited[i][j] = 0
        return exist
            
                    
        