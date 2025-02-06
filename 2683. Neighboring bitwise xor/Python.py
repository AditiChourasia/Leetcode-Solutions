# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor_sum = 0
        # xoring all the elements of derived array
        for num in derived:
            xor_sum ^= num

        # If the XOR sum of all elements is 0, a valid original array exists
        return xor_sum == 0