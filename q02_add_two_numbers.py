# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1
        node2 = l2
        
        root = res = ListNode(0)
        carry = 0
        
        while node1 or node2 or carry:
            
            v1 = v2 = 0
            if node1:
                v1 = node1.val
                node1 = node1.next
            if node2:
                v2 = node2.val
                node2 = node2.next
            
            val = (v1 + v2 + carry) % 10            
            res.next = ListNode(val)
            carry = (v1 + v2 + carry) // 10
            res = res.next
        
        return root.next
            