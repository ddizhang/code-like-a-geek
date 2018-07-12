class Solution(object):
    
    # use dictionary
    # Time: O(n)
    # Space: O(n)
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        length = len(nums)
        #print(length)
        num_dict = {}
        for num in nums:
            print(num)
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

            if num_dict[num] > length/2:
                return num
        return None
    
    # sorting
    # Time: O(nlogn) sorting + O(n) traversal
    def majorityElement(self, nums):
        if not nums:
            return None
        length = len(nums)
        if length == 1:
            return nums[0]
        nums.sort()
        #print('length/2:' + str(length/2))
        for i in range(length/2+1):
            #print('i+length/2:' + str(i + length/2))
            if nums[i] == nums[i + length/2]:
                return nums[i]
        
        return None
            
        
    # randomization
    # randomly draw an element and count its appearance in the array
    # in expectation, only 2 draws will give us the majority element
    # Time: O(infinity)  but expecting O(n)
    # Space: O(1)
    import random
    def majorityElement3(self, nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
    
    
    