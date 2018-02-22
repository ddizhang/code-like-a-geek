class Solution(object):
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # two pass.
        # first pass: count 0's and 1's and 2's
        # second pass: overwrite nums with number of 0's and 1's and 2's
        count = [0, 0, 0]
        
        for i in range(len(nums)):
            count[nums[i]] += 1
        
        for j in range(count[0]):
            nums[j] = 0
        
        for j in range(count[0], count[0]+count[1]):
            nums[j] = 1
        
        for j in range(count[0]+count[1], count[0]+count[1]+count[2]):
            nums[j] = 2
        
        
    # one pass, constant space
    # three pointers
    # first one for 0's, second one for 1's, third one for 2's
    # swap 1st and 2nd to get 0's in place
    # swap 2nd and last element to get 2's in place 
    # can't pass [1,2,0].. so close!
    def sortColors2(self, nums):
        
        if len(nums) == 2:
            if nums[0] > nums[1]:
                temp = nums[0]
                nums[0] = nums[1]
                nums[1] = temp
        
        if len(nums) > 2:
            red_ptr = 0
            white_ptr = 1
            unclassified_ptr = len(nums)-1
            
            # last non-blue item
            while nums[unclassified_ptr] == 2:
                unclassified_ptr -= 1
            
            while white_ptr <= unclassified_ptr:
                
                print('red_ptr:'+ str(red_ptr) + ' white_ptr:' + str(white_ptr) + ' unclassified_ptr:' + str(unclassified_ptr))
                # if white pointing to a blue item:
                # [0,2,x], [1,2,x], [2,2,x]
                if nums[white_ptr] == 2:
                    # swap with the last unclassified item
                    nums[white_ptr] = nums[unclassified_ptr]
                    nums[unclassified_ptr] = 2
                    #move unclassified_ptr forward to the next non-blue item
                    unclassified_ptr -= 1
                    while nums[unclassified_ptr] == 2:
                        unclassified_ptr -= 1
                
                # red_ptr greater than white_ptr: [2,1], [2,0], [1,0]
                elif nums[red_ptr] > nums[white_ptr]:
                    # swap them
                    temp = nums[red_ptr]
                    nums[red_ptr] = nums[white_ptr]
                    nums[white_ptr] = temp
                
                # [0,1], [0,0]
                elif nums[red_ptr] == 0:
                    red_ptr += 1
                    white_ptr += 1
                    
                    while nums[red_ptr] == 0 and red_ptr < unclassified_ptr:
                        red_ptr += 1
                        white_ptr += 1
                
                # [1,1]
                else:
                    while nums[white_ptr] == 1 and white_ptr < unclassified_ptr:
                        white_ptr += 1
                
                print('down red_ptr:'+ str(red_ptr) + ' white_ptr:' + str(white_ptr) + ' unclassified_ptr:' + str(unclassified_ptr))
                print(nums)
                while white_ptr <= unclassified_ptr and nums[white_ptr] == nums[unclassified_ptr]:
                    white_ptr += 1
                
    #If the white pointer is red (nums[white] == 0), 
    #we swap with the red pointer and move both white and red pointer forward. 
    #If the pointer is white (nums[white] == 1), the element is already in correct place, 
    #so we don’t have to swap, just move the white pointer forward. 
    #If the white pointer is blue, we swap with the latest unclassified element.    
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
                    
    
                
                
                    
                
                    
                    

                    
            
        
        
        
        
        
        
        
        