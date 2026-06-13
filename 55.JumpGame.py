def canJump (nums: list[int]) -> bool:
    max_index = 0
    for i in range (0, len(nums)):
        if i > max_index :
            return False
        max_index= max(max_index, i + nums[i])
    return True

print(canJump(nums = [2,3,1,1,4]))
print(canJump(nums = [3,2,1,0,4]))
