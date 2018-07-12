
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.elements = []
        self.min_element = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.elements.append(x)
        if self.min_element is None or self.min_element > x:
            self.min_element = x
        

    def pop(self):
        """
        :rtype: void
        """
        res = self.elements.pop()
        if self.min_element == res:
            if len(self.elements) > 0:
                self.min_element = min(self.elements)
            else:
                self.min_element = None
        return res
        

    def top(self):
        """
        :rtype: int
        """
        return self.elements[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_element


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()