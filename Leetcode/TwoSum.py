# Cho 1 list số nguyên và số target
# Trả về vị trí của 2 số trong list sao cho tổng 2 số đó = target

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    return [i,j]
