# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict
from typing import List

class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:

        n = len(a)  # Length of the input arrays
        c = [0] * n  # Initialize the prefix common array with zeros

        # Sets to keep track of elements seen in `a` and `b` up to the current index
        seen_a = set()
        seen_b = set()

        # Variable to keep count of common elements found so far
        common_count = 0

        # Iterate over each index `i` from 0 to n-1
        for i in range(n):
            # Add the current elements of `a` and `b` to their respective sets
            seen_a.add(a[i])
            seen_b.add(b[i])

            # If the current element of `a` is also in `b`'s seen set, increment the common count
            if a[i] in seen_b:
                common_count += 1

            # If the current element of `b` is also in `a`'s seen set, increment the common count
            if b[i] in seen_a:
                common_count += 1

            # If `a[i]` and `b[i]` are the same, we counted it twice; decrement once
            if a[i] == b[i]:
                common_count -= 1

            # Set the current index in the prefix common array to the current common count
            c[i] = common_count

        return c
