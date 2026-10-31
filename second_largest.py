nums= [22,44,22,55,66,77,88,99]

# nums.sort()
# print("Second largest number is:", nums[-2])

largest = second_largest = float('-inf')
for i in range (len(nums)): #O(n)
    if nums[i] > largest:
        second_largest = largest
        largest = nums[i]
    elif nums[i] > second_largest and nums[i] != largest:
        second_largest = nums[i]
result = second_largest if second_largest != float('-inf') else None
print("Second largest number is:", result)
