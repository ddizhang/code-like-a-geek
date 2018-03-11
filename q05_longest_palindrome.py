class Solution(object):
    
    # solution 1: dynamic programming
    # time: O(n2)
    # space: O(n2)
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        
        # special cases
        if not s:
            return ''    
        if len(s) == 1:
            return s 
        
        # initiate a dp matrix
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        
        # initiate single char palindrome
        for i in range(len(s)):
            dp[i][i] = True
            if len(result) < 1:
                result = s[i:i+1]
        
        # initiate double char palindrome
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                if len(result) < 2:
                    result = s[i:i+2]

        # calculate palindrome status for other start/end position combination
        # calculate along the diagonal
        for j in range(2, len(s)):
            for i in range(len(s)-j):
                if s[i] == s[i+j] and dp[i+1][i+j-1]:
                    dp[i][i+j] = True
                    if j+1 > len(result):
                        result = s[i:i+j+1]
        
        return result
    
    
    # below is not tested
    # basic idea: go through all possible centers of palindrome, which is, every character in the string
    # and between every two neighbor characters.
    # And try to expand the palindrome as far as possible
    # Time complexity: O(n2)
    # Space complexity: O(1)
    def longestPalindrome1(self, s):
        
        result = ''
        
        for i in range(len(s)):
            new_pal = self.palindromeAroundCenter(i, i, s)
            if len(new_pal) > len(result):
                result = new_pal
        
        for i in range(len(s)-1):
            new_pal = self.palindromeAroundCenter(i, i+1, s)
            if len(new_pal) > len(result):
                result = new_pal
        
        return result

    
    def palindromeAroundCenter(l, r, s):
        '''
        l: left index
        r: right index
        s: string
        '''
        if s[l] != s[r]:
            return s[l]
        
        while l-1 > 0 and r+1 < len(s) and s[l-1] == s[r+1]:
            l = l-1 
            r = r+1
        
        return s[l:r+1]
        
            
        
        
            
            