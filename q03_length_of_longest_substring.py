class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """        
        start = 0
        char_dict = {}
        max_length = 0
        
        for i,c in enumerate(s):
            
            # if c is already in the current accumulating substring: start from the char after c appeared last time
            # if last time c appeared is before the start point of current substring: it's fine. substring is still cumulating
            if c in char_dict and start <= char_dict[c]:
                start = char_dict[c] + 1
            # this is to cumulate the substring length
            else:
                max_length = max(max_length, i-start+1)
            char_dict[c] = i
            
        return max_length