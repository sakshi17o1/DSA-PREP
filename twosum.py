nums = [1, 3, 4, 6, 9 ]
target= 10

def twoSum(nums, target):
    dic={}
    for i, num in enumerate(nums):
        x=target-num
        if x in dic:
            return [dic[x], i]
        dic[num]=i
    return[]
print(twoSum(nums, target))
        