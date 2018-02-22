class Solution(object):
     
    # brutal force
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] + nums[i] == target:
                    return [i, j]


    # sort the list and do binary search
    def twoSum2(self, nums, target):
        sorted_nums = sorted(nums)  #O(nlogn)
        for i in range(len(sorted_nums)-1): 
            # binary search
            val_to_search = target - sorted_nums[i]
            #j is the index of the value to search in the list
            j0 = binary_search(sorted_nums[i+1:], val_to_search) #O(logn)
            
            if j0 is not None:   
                j = i + 1 + j0
                # find the indices of the two numbers in original list
                first_ind = nums.index(sorted_nums[i])  #O(n)
                nums[first_ind] = None
                second_ind = nums.index(sorted_nums[j])  #O(n)
                return(sorted([first_ind, second_ind]))


                
    # incorrect if there're multiple number with same values and to be selected in the list
    # e.g. nums = [3,3,5], target = 6
    def twoSum3(self, nums, target):
        
        # put everything in a dict, num:index
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = i
        
        # for every key in the dict, search for another key that will form a sum of target
        for val in nums_dict.keys():
            val_to_search = target - val
            if val_to_search in nums_dict.keys():
                return sorted([nums_dict[val], nums_dict[val_to_search]])

            

    # in the dictionary, we put in:  remaining_value_to_reach_target: num_index
    def twoSum4(self, nums, target):
        
        remains_dict = {}
        for i in range(len(nums)):
            
            if nums[i] not in remains_dict:
                remains_dict[target - nums[i]] = i
            else:
                return remains_dict[nums[i]], i
        
    # double pointer
    def twoSum(self, nums, target):
        
        sorted_nums = sorted(nums) #O(nlogn)
        l = 0
        r = len(nums)-1
        
        while l < r:  #O(n)
            current_sum = sorted_nums[l] + sorted_nums[r]
            if current_sum == target:
                break
            elif current_sum > target:
                r -= 1
            else:
                l += 1
        
        first_ind = nums.index(sorted_nums[l])  #O(n)
        nums[first_ind] = None
        second_ind = nums.index(sorted_nums[r])  #O(n)
        return(sorted([first_ind, second_ind]))
    
        
        
    
    
def binary_search(sorted_nums, val_to_search):
        
    head = 0
    tail = len(sorted_nums) - 1
    mid_point = (head + tail) // 2
    
    while (mid_point - head > 0):
        if sorted_nums[mid_point] < val_to_search:
            head = mid_point
        else:
            tail = mid_point 
        mid_point = (head + tail) // 2
    
    if sorted_nums[head] == val_to_search:
        return head
    elif sorted_nums[tail] == val_to_search:
        return tail
    
        
        
        
    
                  
            

            