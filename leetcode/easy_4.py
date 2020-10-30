"""
53. Maximum Subarray
Easy

9459

449

Add to List

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


"""
# First Solution
nums= [-2,1,-3,4,-1,2,1,-5,4]
output_d = {}
for i in range(len(nums)):
    #print(nums[i])
    list_sums = []
    list_sums.append(nums[i])
    sums = nums[i]
    for j in range(i+1, len(nums)):
        sums += nums[j]
        list_sums.append(nums[j])
        output_d[str(list_sums)] = sums
        #print(output_d)
print(max(output_d, key=output_d.get), " : ", max(output_d.values()))

## Second Solution Using Kaag's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = max_global = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current+nums[i])
            if max_current>max_global:
                max_global = max_current
        return max_global