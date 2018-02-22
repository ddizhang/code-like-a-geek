class Solution(object):
    
    # sorting 
    def hIndex1(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations == []:
            return 0
        
        citations.sort(reverse = True)
        i = 0
        while i < len(citations) and citations[i] > i:
            print('i:'+ str(i)+ 'citations:'+str(citations[i]))
            i += 1
        return i
            
    # count and cumsum
    # count the number of papers having same number of citation (if citation count > paper count, set it to paper count)
    # cumulate sum: # of paper with citation count >= paper count
    # bug with input [0]
    # time O(n), space O(n)
    def hIndex(self, citations):
        if citations == []:
            return 0
        
        count = [0 for i in range(len(citations)+1)]
        for i in range(len(citations)):
            idx = min(citations[i], len(citations))
            count[idx] += 1
            
        i = len(count)-2
        while i >= 0:
            count[i] = count[i] + count[i+1]
            if count[i] >= i:
                return i
            i -= 1
        
            
        