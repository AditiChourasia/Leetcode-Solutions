# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maximum_sum = float("-inf")

        n = len(nums)

        if n == 1:
            return nums[0] # edge case when only one element is there in nums array

        for i in range(n):
            current = nums[i]
            for j in range(i+1, n):
                if nums[j] > nums[j-1]: #checking for the ascending order
                    current += nums[j]
                else:
                    break # if we not find any ascending order, we break and go on next element to find another subarray
            maximum_sum = max(maximum_sum, current) # every time we compute the max sum

        return maximum_sum