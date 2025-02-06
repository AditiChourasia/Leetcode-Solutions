# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        # If the list has only one element, it is trivially sorted and can be rotated
        if n == 1:
            return True

        count = 1  # This keeps track of the length of the increasing sequence

        # Iterate through twice the length of the array to simulate circular rotation
        for i in range(1, 2 * n):
            # Compare the current element with the previous one in a circular manner
            if nums[(i - 1) % n] <= nums[i % n]:
                count += 1  # Increment count if order is maintained
            else:
                count = 1  # Reset count if order breaks

            # If we have found a full rotation where all elements are non-decreasing
            if count == n:
                return True

        # If no valid rotation is found, return False
        return False
