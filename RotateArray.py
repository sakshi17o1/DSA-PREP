def rotate(nums: list[int], k: int) -> None:    
    """
        Do not return anything, modify nums in-place instead.
        """
    n = len(nums)
    r = k % n
    for _ in range (0, r):
        e = nums.pop()
        nums.insert(0,e)
    return r

# example input
nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
