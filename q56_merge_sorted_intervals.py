# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        #intervals_list.sort(key = lambda x: x[1])
        intervals.sort(key=lambda x: x.start)
        
        if intervals == []:
            return []
        
        output = [intervals[0]]
        j = 0
        
        for i in range(len(intervals)):
            
            # right bound of consolidated is greater than left bound of new:
            # the two intervals can be merged
            if output[j].end >= intervals[i].start:
                output[j].end = max(output[j].end, intervals[i].end)

            else:
                output.append(intervals[i])
                j += 1
        
        return output
                
            