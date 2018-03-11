def quicksort(nums):
    
    if not nums:
        return []
    if len(nums) == 1:
        return nums
    
    pivot = nums[0]
    left = 1
    right = len(nums) - 1
    
    while 1:
        while nums[left] < pivot and left < len(nums):
            left += 1
        while nums[right] > pivot and right >= 0:
            right -= 1
        if left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
        else:
            temp = nums[0]
            nums[0] = nums[right]
            nums[right] = temp
            break
    
    quicksort(nums[0:left])
    quicksort(nums[left:(len(nums)-1)])
    