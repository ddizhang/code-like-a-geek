# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# keep the first k obs
# for new obs i: for k/i probability to keep the ith obs, remove one of k from current list randomly

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        selected = self.head.val
        i = 1.0
        curr = self.head
        while curr.next:
            i += 1
            curr = curr.next
            rand = random.random()
            # print('curr.val:' + str(curr.val))
            # print('i=' + str(i))
            # print('1/i=' + str(1/i))
            # print('rand=' + str(rand))
            if rand < 1/i:
                selected = curr.val
            # print('selected = '+str(selected))
            # print('\n')
        
        return selected
            
#     def getRandom(self):
#         result, node, index = self.head, self.head.next, 1
#         while node:
#             if random.randint(0, index) is 0:
#                 result = node
#             node = node.next
#             index += 1
#         return result.val    


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()