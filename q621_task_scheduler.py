class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        n += 1
        ans = 0
        # tasks are prioritized by their repitition
        tb = collections.Counter(tasks)
        
        # using a heap to keep the tasks
        task_tb_heap = [-c for c in tb.values()]
        heapq.heapify(task_tb_heap)
        
        #while there're task left in the heap
        while task_tb_heap:
            # to keep the tasks that current round 
            #(in a iteration of cooling cycle where most prioritized task is executed first)
            curr_round_stack = []
            cnt = 0
            
            for _ in range(n):
                if task_tb_heap:
                    #execute a task
                    c = heapq.heappop(task_tb_heap)
                    # cnt is used to count tasks if a cycle is not used fully.
                    cnt += 1
                    #if this task has to be repeated later: add back into the heap
                    #not add back now, because it can't be executed anyways (it's cooling down)
                    if c < -1:
                        curr_round_stack.append(c+1)
            # put the executed and to-be-repeated tasks back to the heap
            for item in curr_round_stack:
                heapq.heappush(task_tb_heap, item)
            # count number of tasks executed
            ans += n if task_tb_heap else cnt
        return ans
        