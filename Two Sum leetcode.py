class Solution:
    def twoSum(self,nums, target):
    # Loop through each element in nums
        for i in range(len(nums)):
        # Start a second loop after the current element
            for j in range(i + 1, len(nums)):
            # Check if the two numbers add up to the target
                if nums[i] + nums[j] == target:
                    return [i, j]
