# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    # iterative, naive
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1
        node2 = l2
        root = curr = ListNode(0)
        
        while node1 or node2:
            
            if node1 and node2:
                if node1.val < node2.val:
                    curr.next = ListNode(node1.val)
                    node1 = node1.next
                else:
                    curr.next = ListNode(node2.val)
                    node2 = node2.next
            elif node1:
                curr.next = ListNode(node1.val)
                node1 = node1.next
            else:
                curr.next = ListNode(node2.val)
                node2 = node2.next
            
            curr = curr.next
        
        return root.next
                    
    # above naive approach can be improved by reducing if cases.
    # when there's only one list left, simply paste all of it to the end of result list
    def mergeTwoLists2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1
        node2 = l2
        root = curr = ListNode(0)

        while node1 and node2:
            if node1.val < node2.val:
                curr.next = ListNode(node1.val)
                node1 = node1.next
            else:
                curr.next = ListNode(node2.val)
                node2 = node2.next
            curr = curr.next

        # take whatever is left
        curr.next = node1 or node2
        # if node1:
        #     curr.next = node1
        # else: 
        #     curr.next = node2

        return root.next
    
    # recursive
    def mergeTwoLists(self, l1, l2):
        # only one list has value
        if not l1 or not l2:
            return l1 or l2
        
        # both lists have value
        else:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l2.next, l1)
                return l2
        