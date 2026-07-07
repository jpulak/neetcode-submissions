class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, ele in enumerate(nums):
            diff = target - ele

            if diff in hashmap:
                return [hashmap[diff], index]
            hashmap[ele] =index

'''
can use two pointer for more efficient time complexity
first pointer at the left front, second to the right end
if sum is SMALLER, move the left since it can get bigger numbers
if sum is LARGER, move the right since it can get smaller nums
if sum is equal, return the index of each

DOESNT WORK CUZ ITS NOT SORTEDDD
cant sort cuz it iwll loose place of the index

create a hashmap
ad 
'''