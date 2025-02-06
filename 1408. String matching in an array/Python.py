# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()  # Set to store unique words that are substrings

        n = len(words)  # Total number of words in the list

        # Compare each word with every other word
        for i in range(n):
            for j in range(n):
                # Check if words[j] is a substring of words[i] and they are not the same word
                if words[j] in words[i] and i != j:
                    ans.add(words[j])  # Add words[j] to the set

        # Convert the set to a list to return the result
        ans = list(ans)
        return ans
