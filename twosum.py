nums = [2, 7, 11, 15 ]
target= 9

def twoSum(nums, target):
   dic={}
   for i, num in enumerate(nums):
    x=target-num
    if x in dic:
        return [dic[x], i]
    dic[num]=i
   return[]
print(twoSum(nums, target))
        