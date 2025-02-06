from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1, xor2 = 0, 0  # Initialize XOR results for nums1 and nums2

        # If the length of nums2 is odd, XOR all elements of nums1
        # This is because each element of nums1 will contribute to the result exactly len(nums2) times.
        # If len(nums2) is odd, the XOR of all such occurrences will reduce to the XOR of all elements of nums1.
        if len(nums2) % 2 == 1:
            for i in nums1:
                xor1 ^= i

        # Similarly, if the length of nums1 is odd, XOR all elements of nums2
        if len(nums1) % 2 == 1:
            for j in nums2:
                xor2 ^= j

        # The final result is the XOR of xor1 and xor2
        return xor1 ^ xor2
