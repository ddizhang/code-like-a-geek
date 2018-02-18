import pdb

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    #pdb.set_trace()
    for i in range(len(nums)-2):
        if i>=1 and nums[i] == nums[i-1]:
            continue
        
        if nums[i] <= 0:

            # double pointer twoSum()
            j = i+1
            k = len(nums)-1

            while j < k:
                print(str(i)+str(j)+str(k))
                two_sum = nums[j] + nums[k]
                if two_sum == -nums[i]:
                    res.append([nums[i], nums[j], nums[k]])

                if two_sum > -nums[i]:
                    #find the next k with a different value
                    while True:
                        k -= 1
                        if (nums[k] != nums[k+1]):
                            break
                else:
                    while True:
                        j += 1
                        if (nums[j] != nums[j-1] or j == len(nums)-1):
                            break
    return res
