
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue

class Solution(object):
    
    # time O(N*n), N: ttl # nodes, n:ttl # lists
    # time limit exceeded
    # space: O(1) constant space, all changes happen in-place
    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res_head = ListNode(0)
        res_cur = res_head
        
        while len(lists) > 0:
            #print('len(lists) = {0}'.format(len(lists)))    
            
            # find smallest node
            min_pos = -1
            remove_pos = []
            for i in range(len(lists)):
                # if it's a valid listNode (not null)
                #print('lists[i] = {0}'.format(lists[i].val if lists[i] else 'None'))
                
                if lists[i]:
                    if min_pos < 0 or lists[min_pos].val > lists[i].val:
                        min_pos = i
                else:
                    remove_pos.append(i)
            #print('min_pos = {0}'.format(min_pos))
            
            # append smallest node to result list
            res_cur.next = lists[min_pos]
            res_cur = res_cur.next
            
            # smallest node in [lists]: move to the next node
            if min_pos >= 0:
                lists[min_pos] = lists[min_pos].next
            
            # remove all None elements
            lists = [b for i,b in enumerate(lists) if not i in remove_pos]
        
        return res_head.next
                        
    
    # Use Priority Queue!
    # time: O(Nlogn)
    # space: O(n) for the priority queue
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res_head = ListNode(0)
        res_cur = res_head
        
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        
        while not q.empty():
            val, node = q.get()
            res_cur.next = node
            res_cur = res_cur.next
            node = node.next
            if node:
                q.put((node.val, node))
        
        return res_head.next
            
    # hmmm.. isn't it the same as using a heap?
    
    
    
    
    