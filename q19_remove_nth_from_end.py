# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    #Maintain two pointers and update one with a delay of n steps.
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        front = head
        back = head     
        i = 1
        
        while i <= n:
            front = front.next
            i += 1
        
        if not front:
            return back.next
        
        while front.next:
            front = front.next
            back = back.next
        
        if back.next:
            back.next = back.next.next
        
        return head
            