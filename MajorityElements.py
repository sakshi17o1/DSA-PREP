def majorityElement(nums: list[int]) -> int:
    result = -1 
    count = 0
    for num in nums :
        if count == 0:
            result = num
        if result == num:
            count += 1
        else:
            count -=1
    return result

# example input
nums = [2,2,1,1,1,2,2]
result = majorityElement(nums)
print(result)  # Output: 2
