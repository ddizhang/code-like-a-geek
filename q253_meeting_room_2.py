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
                

                    
# [0,1], [0.2, 1.5], [2,3]     
def minMeetingRooms(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    intervals.sort(key = lambda x: x[0])
    end_heap = []
    heapq.heappush(end_heap, intervals[0])
    room_num = 1


    for i in range(1, len(intervals)):

        if end_heap:
            # if next meeting begins before the soonest end-time of current meeting:
            if intervals[i][0] < end_heap[0]:
                heapq.heappush(intervals[i][1])
                room_num = max(room_num, len(end_heap))

            else:
                # pop all the meetings tha had ended before current meeting starts
                while len(end_heap) > 0 and intervals[i][0] > end_heap[0]:
                    heapq.heappop()
                heapq.heappush(intervals[i][1])







