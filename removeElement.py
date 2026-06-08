def removeElement(nums: list[int], val: int) -> int:
    i=0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

# example input
nums = [3,2,2,3]
val = 3
result = removeElement(nums, val)
print(result)  # Output: 2
print(nums[:result])  # Output: [2, 2]  