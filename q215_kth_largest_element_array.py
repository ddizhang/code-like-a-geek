class Solution(object):
    
    # O(nlogn)
    def findKthLargest1(self, nums, k):
        nums.sort(reverse = True)
        return nums[k-1]
    
    #maintain a heap
    # Time: O(nlogk)
    # space: O(k)
    def findKthLargest(self, nums, k):
        k_largest_heap = []
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(k_largest_heap, nums[i])
            else:
                if nums[i] > k_largest_heap[0]:
                    heapq.heappop(k_largest_heap)
                    heapq.heappush(k_largest_heap, nums[i])
        return heapq.heappop(k_largest_heap)
    
    
    
    # method 1: sort the array, find by index
    # method 2: keep a priority queue for the largest k elements
    # heap: how do heap handle duplicates??
    def findKthLargest0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = [0]
        for num in nums:
            print('num: ' + str(num))
            
            # heap is not full yet
            if len(heap) < k+1:
                self.insertHeap(heap,num)
            # heap is full
            else:
                # if new number is smaller than the smallest number in heap (kth largest as of now): do nothing
                if num <= heap[1]:
                    continue
                else:
                    self.delMinHeap(heap)
                    print('heap after delmin')
                    print(heap)
                    self.insertHeap(heap,num)

            print('heap')
            print(heap)
        return heap[1]
    
    def insertHeap(self, heap, num):
        heap.append(num)
        l = len(heap)-1
        while l//2 > 0 and heap[l] < heap[l//2]:
            swap = heap[l]
            heap[l] = heap[l//2]
            heap[l//2] = swap
            l = l//2

    def delMinHeap(self, heap):
        if len(heap) == 2:
            heap.pop()
        else:
            heap[1] = heap.pop()
            l = 1
            while l*2 < len(heap) and heap[l] > heap[l*2]:
                swap = heap[l]
                heap[l] = heap[l*2]
                heap[l*2] = swap
                l = l*2