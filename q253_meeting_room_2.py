# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e



class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # maintain a heap of current ongoing meeting
        # pop if new meeting starts after current ends
        # count length of heap
        # Time: O(nlogn) has to sort first
        # Space: O(n) heap for all meetings
        intervals.sort(key = lambda x: x.start)
        curr_mtg_end = []  # a heap
        mtg_rooms = 0
        
        for new in intervals:
            # if there're meetings going on:
            if curr_mtg_end:
                # if new meeting starts after one of current meeting ends:
                if new.start >= curr_mtg_end[0]:
                    #pop the meeting that ends soonest
                    heapq.heappop(curr_mtg_end)
            # push new meeting to meeting schedule
            heapq.heappush(curr_mtg_end, new.end)
            # if current meeting length is larger than mtg_room: add one room
            mtg_rooms = max(mtg_rooms, len(curr_mtg_end))
        
        return mtg_rooms
                
                    
                    
                