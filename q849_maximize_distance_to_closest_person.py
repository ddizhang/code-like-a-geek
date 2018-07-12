class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # O(n), 2 passes
        
        # find all seats with people 
        ppl = []
        for i in range(len(seats)):
            if seats[i] == 1:
                ppl.append(i)
        
        if not ppl:
            return None
        
        max_dist = 0
        # go over the scenario to sit between each two neighboring people: 
        # sitting right between each of them will generate largest possible gap
        for j in range(len(ppl)-1):
            max_dist = max(max_dist, (ppl[j+1] - ppl[j])//2)
        # sitting in front of the first person, after last person
        max_dist = max(max_dist, ppl[0], len(seats)-1-ppl[-1])
        
        return max_dist
            