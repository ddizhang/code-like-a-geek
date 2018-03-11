# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # use a stack to store the path to next object
        # we want to change the index later so use a list not tuple
        self.next_loc_stack = [[nestedList, 0]]  # nestedList ind 0

    def next(self):
        """
        :rtype: int
        """
        # after hasNext(), stack should has the proper next element location
        self.hasNext()
        s = self.next_loc_stack
        nestedList, i = s[-1]
        # naively set the new next location
        s[-1][1] += 1
        return nestedList[i].getInteger()

    # have the last item in stack pointing correctly to next item
    def hasNext(self):
        """
        :rtype: bool
        """
        s = self.next_loc_stack
        while s:
            nestedList, i = s[-1]
            # if current setted location is not a proper search location: (this is set naively by hasNext())
            # pop it, search the parent level (next one in stack)
            if i == len(nestedList):
                s.pop()
            else:
                # if next location is a integer: return True
                if nestedList[i].isInteger():
                    return True
                else:
                    # if next location is a nestedList: properly set the next search location
                    s[-1][1] += 1
                    s.append([nestedList[i].getList(), 0])
                    
        # if nothing's found after whole search process: return False
        return False
        
        
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())