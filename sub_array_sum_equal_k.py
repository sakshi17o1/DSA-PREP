def subarray_sum(nums, k):
    count = 0
    for start in range(len(nums)):
        total = 0
        for end in range(start, len(nums)):
            total += nums[end]
            if total == k:
                count += 1
    return count

print(subarray_sum([1, 1, 1], 2))   # 2