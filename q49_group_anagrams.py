class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_dict = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(str)
            else:
                anagram_dict[sorted_str] = [str]
        
        return list(anagram_dict.values())
    
    #also: can set the key to letter counts 
    #{(1,1,0,2,0, ..., 1): ['abd', 'adb']}
        
        