


# 01-----------------------------------------
'''
Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def twoSum(nums, target):
        for t1, t2 in zip(enumerate(nums[:-1]), enumerate(nums[1:], 1)):
            if t1[1] + t2[1] == target:
                return [t1[0], t2[0]]

twoSum([2, 7, 11, 15], target = 9)



def twoSum(nums, target):
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i

twoSum([2, 7, 11, 15], target = 9)