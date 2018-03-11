# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        #print
#         print('sort list:')
#         p = head
#         while p:
#             print(str(p.val))
#             p = p.next
                
        if not head:
            return None
        
        if not head.next:
            return head
        
        # devide the list into two halves
        slow = fast = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        
        
        # merge sort the two halves
        # sortList() returns the head of sorted list
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        # merge the two halves
        new_head = ListNode(0)
        curr_node = new_head
        
        while l1 and l2:
            if l1.val < l2.val:
                curr_node.next = l1
                l1 = l1.next
            else:
                curr_node.next = l2
                l2 = l2.next
            curr_node = curr_node.next
        
        if l1:
            curr_node.next = l1
        else:
            curr_node.next = l2
        
        return new_head.next
            
                
        