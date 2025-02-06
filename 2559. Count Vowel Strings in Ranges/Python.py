# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Define a set of vowels for quick lookup
        vowels = {"a", "e", "i", "o", "u"}
        
        n = len(words)  # Total number of words
        # Prefix sum array to store cumulative counts of vowel strings
        prefix = [0] * (n + 1)
        
        # Build the prefix sum array
        for i in range(n):
            # Check if the current word is a vowel string
            if words[i][0] in vowels and words[i][-1] in vowels:
                # Increment the prefix sum by 1 if it's a vowel string
                prefix[i + 1] = prefix[i] + 1
            else:
                # Otherwise, carry forward the previous prefix sum
                prefix[i + 1] = prefix[i]
        
        # Answer each query using the prefix sum array
        ans = []
        for li, ri in queries:
            # Subtract the prefix sums to get the count in the range [li, ri]
            ans.append(prefix[ri + 1] - prefix[li])
        
        return ans
