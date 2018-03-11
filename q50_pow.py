class Solution(object):
    
    # 2**9 = 2**4 * 2**4 * 2**1
    # save 2**4 in a dict to prevent multiple calculation
    # Time: O(logn), Space: O(n)
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        self.n_dict = {}
        self.n_dict[1] = x
        self.n_dict[0] = 1
        self.n_dict[-1] = 1/x
        return self.pow_helper(x, n)
    
    def pow_helper(self, x, n):
        
        if n in self.n_dict:
            return self.n_dict[n]
        
        half_n = n//2
        remainder = n % 2
        half_pow = self.pow_helper(x, half_n)
        new_pow = half_pow * half_pow * self.pow_helper(x, remainder)
        self.n_dict[n] = new_pow
        return new_pow