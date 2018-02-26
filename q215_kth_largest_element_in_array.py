class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # method 1: sort the array, find by index
        # method 2: keep a priority queue for the largest k elements