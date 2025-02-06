# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0 # to count the number of strings which have prefix as given pref
        n = len(words)

        for i in range(n):
            if words[i].startswith(pref): # function to check whether particular string in array has prefix as given in problem
                count += 1 # if yes, then increment the value of count by one

        return count