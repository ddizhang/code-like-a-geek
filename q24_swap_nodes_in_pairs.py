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
    # I don't understand it now..
    def swapPairs1(self, head):
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
    

    # this is the correct one- not reseting value but swap nodes
    def swapPairs(self, head):
        
        new_head = ListNode(0)
        new_head.next = head
        
        aprev = new_head
        a = head
        
        while a and a.next:
            print('a.val =' + str(a.val))
            b = a.next
            bnext = b.next
            #change order
            aprev.next = b
            b.next = a
            a.next = bnext
            
            aprev = a
            if a.next:
                a = a.next
            
        return new_head.next