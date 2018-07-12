# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]

# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Sort part: O(nlogn)
        # DFS part: O(n!)
        
        #print('candidates')
        #print(candidates)
        res = []
        candidates.sort()
        
        for i in range(len(candidates)):
            
            num = candidates[i]
            #print('num=' + str(num) + 'target=' + str(target))
            
            # if current number equal to target: return it
            if num == target:
                res.append([num])
            
            # if current number smaller than target: search further
            elif num < target:
                res_next = self.combinationSum(candidates[i:], target-num)
                #print('num:{0}, target:{1}, res_next: {2}'.format(num, target, res_next))
                
                if res_next:
                    [item.append(num) for item in res_next]
                    for item in res_next:
                        res.append(item)
                    
        
            #print('num:{0}, target:{1}, res:{2}'.format(num, target, res))
        
        #print('candidates:{0}, target:{1}, return res:{2}'.format(candidates, target, res))
        return res
            