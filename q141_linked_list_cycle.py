# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    # Method 1:
    # put every visited node into a dictionary
    # at every step: check if node is already in the dict
    # O(n) time, O(n) space

    # Method 2:
    # two pointers. for every step fast pointer moving forward,
    # slow pointer check previous steps
    # two pass O(n2)    
    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = head
        step = 0
        
        while fast and fast.next:
            fast = fast.next
            step += 1
            slow = head
            check_step = 0
            while check_step < step:
                if slow and slow == fast:
                    return True 
                slow = slow.next
                check_step += 1
        
        return False
        
    
    # Method 3:
    # two pointers. fast moves 2 steps ahead each time, slow moves 1 step ahead.
    # if there's a loop, fast will eventually meet slow..
    def hasCycle(self, head):
        fast = slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
            