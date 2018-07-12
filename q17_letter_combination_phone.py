class Solution(object):
    
    # not debugged
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        digit_dict = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        comb = ['']
        
        for digit in digits:
            comb = [cur_str + new_char for cur_str in comb for new_char in digit_dict[int(digit)]]
        
        return comb