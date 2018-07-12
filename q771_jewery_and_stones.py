# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        # add all jewery type into jewery dict
        j_dict = {}
        for char in J:
            j_dict[char] = 1
        
        # check if current stone in jewery dict
        res = 0
        for char in S:
            if char in j_dict:
                res += 1
        
        return res