# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    # iteratively
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return []
        
        curr = head
        prev = None
    
        # three pointers: prev, curr, next
        # set curr.next = prev
        # move all pointers forward
    
        while curr is not None:
            
            next_node = curr.next #moving next_node forward, putting it here because we need to verify curr is not None
            curr.next = prev
            prev = curr
            curr = next_node  
        
        return prev
    
    
    # recursivelly
    # time limit exceeded
    # O(n^2)
    def reverseList2(self, head):
        
        # no node: return None
        if head is None:
            return None
        
        # one node: return self
        elif head.next is None:
            return head
        
        # else: exchange first node and the reversed second-to-last nodes
        else:
            new_head = self.reverseList(head.next)
            head.next = None
            curr = new_head
            while curr.next is not None:
                curr = curr.next
            curr.next = head
            return new_head
    

    # recursivelly
    # O(n)
    def reverseList(self, head):
        
        # no node: return None
        if head is None or head.next is None:
            return head

        else:
            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return new_head
    