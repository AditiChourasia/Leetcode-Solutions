# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Create a dictionary to store the maximum frequency of each letter across all words in words2
        mpp = defaultdict(int)

        # Build the maximum frequency dictionary for words2
        for word in words2:
            for letter in set(word):
                mpp[letter] = max(mpp[letter], word.count(letter))

        def helper(s1: str) -> bool:

            # Create a temporary frequency dictionary for the current word s1
            temp = defaultdict(int)
            for ele in s1:
                temp[ele] += 1
            
            # Check if s1 satisfies the universal condition defined by mpp
            for key, val in mpp.items():
                if temp[key] < val:
                    return False
            return True

        res = []  # List to store the result of universal words from words1

        # Check each word in words1 using the helper function
        for word in words1:
            if helper(word):
                res.append(word)

        return res  # Return the list of universal words
