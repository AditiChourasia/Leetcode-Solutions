# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)  # Length of the array
        cnt = 0  # Counter for valid splits
        totalSum = sum(nums)  # Compute the total sum of the array
        left_sum = 0  # Tracks the sum of the left part of the split

        # Iterate through the array up to the second last element
        for i in range(n - 1):
            left_sum += nums[i]  # Add the current element to the left sum
            totalSum -= nums[i]  # Subtract the current element from the total sum
            # Check if the left sum is greater than or equal to the right sum
            if left_sum >= totalSum:
                cnt += 1  # Increment the counter for valid splits

        return cnt  # Return the total count of valid splits
