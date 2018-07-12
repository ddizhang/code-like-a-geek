# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".


class Solution(object):
    def reverseString0(self, s):
        """
        :type s: str
        :rtype: str
        """
        # O(n)
        # time limit exceeded..
        res = ''
        for i in range(len(s)):
            res = res + s[len(s)-1-i]
        return res
    
    
    # okay.. Join is faster than appending chars one by one
    def reverseString(self, s):
    
        rev_str_list = reversed([i for i in s])
        res = ''.join(rev_str_list)
        
        return(res)