# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxi = 0
        # checking wheather it is increasing or not using nested loops
        for i in range(len(nums)):
            curr = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[j-1]:
                    curr += 1
                else:
                    break

            maxi = max(maxi, curr)
        
        # checking wheather it is decreasing or not using nested loops
        for i in range(len(nums)):
            curr = 1
            for j in range(i+1, len(nums)):
                if nums[j] < nums[j-1]:
                    curr += 1
                else:
                    break

            maxi = max(maxi, curr)

        return maxi #returning the final answer