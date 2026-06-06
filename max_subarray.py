def maxSubArray( nums: list[int]) -> int:
    curr_sum = max_sum = nums[0]

    for i in range (1, len(nums)):
        curr_sum = max (curr_sum + nums[i], nums[i])
        max_sum = max(curr_sum, max_sum)
        
    return max_sum
print(maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))