# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # If both strings are already the same, return True
        if s1 == s2:
            return True
        
        mpp = defaultdict(int)  # Dictionary to track character frequency differences
        num_diff = 0  # Counter for positions where s1 and s2 differ
        n = len(s1)

        # Traverse both strings
        for i in range(n):
            if s1[i] != s2[i]:  # Count character mismatches
                num_diff += 1

            # If more than 2 differences, swapping one pair won't fix it
            if num_diff > 2:
                return False

            # Track character frequency differences
            mpp[s1[i]] += 1
            mpp[s2[i]] -= 1

        # Check if both strings have the same characters (same frequency)
        for k in mpp.values():
            if k != 0:  # If any character has a different frequency, return False
                return False

        return True  # If there are exactly 0 or 2 differences and same characters, return True
