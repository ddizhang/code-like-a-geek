# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs0(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        i = 1
        
        if not curr:
            return head
        
        while curr.next:
            #odd position
            if i%2:
                swap = curr.val
                curr.val = curr.next.val
                curr.next.val = swap
            curr = curr.next
            i += 1
                
        return head
    
    
    # simpler solution: only passing odd positions
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        i = 1
        
        if not curr:
            return head
        
        while curr and curr.next:
            #odd position
            swap = curr.val
            curr.val = curr.next.val
            curr.next.val = swap
            curr = curr.next.next
            i += 2
                
        return head
    
