# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from collections import defaultdict
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = defaultdict(int)  # Dictionary to store product frequencies

        n = len(nums)

        # Iterate through all pairs (i, j) in nums
        for i in range(n - 1):
            for j in range(i + 1, n):
                product_map[nums[i] * nums[j]] += 1  # Count occurrences of each product

        ans = 0

        # Calculate the number of valid tuples
        for k, v in product_map.items():
            if v >= 2:  # A valid tuple exists only if there are at least two pairs with the same product
                comb = (v * (v - 1)) // 2  # Number of ways to choose two pairs from v (Combination formula)
                ans += comb * 8  # Each valid combination contributes 8 permutations

        return ans
