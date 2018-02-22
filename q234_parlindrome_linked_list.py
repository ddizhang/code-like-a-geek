# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    # put into list:
    # O(n) time, O(n) space
    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        
        # put all node values into a list
        curr = head
        val_list = [curr.val]
        while curr.next:
            curr = curr.next
            val_list.append(curr.val)
        
        # double pointer to find palindrome
        front, back = 0, len(val_list)-1
        
        while front < back:
            if val_list[front] != val_list[back]:
                return False
            front += 1
            back -= 1
        return True

    
    def isPalindrome(self, head):
        
        if head is None or head.next is None:
            return True

        # find mid point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # now slow pointing at the head of second half

        # reverse the second half
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        test = head
        while test:
            print('head')
            print(test.val)
            test = test.next
            
        test = prev
        while test:
            print('tail')
            print(test.val)
            test = test.next
        
        # compare the two halves
        # first one starts at head, second one starts at prev
        node1 = head
        node2 = prev
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        return True
        
        
        
            
            