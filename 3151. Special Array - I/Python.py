# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(1, n):
            if (nums[i] % 2) == (nums[i-1] % 2): # Checking wheather both integers have same parity, if yesnthen return false
                return False

        return True # return true is all adjacent elements in array have different parity