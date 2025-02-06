# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(s1, s2):
            """
            Helper function to check if s1 is both a prefix and a suffix of s2.

            Args:
            s1 (str): The word to check as prefix and suffix.
            s2 (str): The word to be checked against.

            Returns:
            bool: True if s1 is both a prefix and suffix of s2, False otherwise.
            """
            return s2.startswith(s1) and s2.endswith(s1)

        n = len(words)  # Number of words in the list
        cnt = 0  # Initialize the count of valid pairs

        # Iterate through each pair of words (i, j)
        for i in range(n):
            for j in range(i, n):
                # Check if words[i] is a prefix and suffix of words[j] and i != j
                if isPrefixAndSuffix(words[i], words[j]) and i != j:
                    cnt += 1  # Increment the count if the condition is met

        return cnt  # Return the total count of such pairs
