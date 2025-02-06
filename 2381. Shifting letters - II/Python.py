# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict
from typing import List

class Solution:
    def shift(self, c, k):
        return chr(ord('a') + (26 + ord(c) - ord('a') + k) % 26)

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        n = len(s)
        freq = defaultdict(int)  # Dictionary to store net shifts at each position

        # Apply the shifts using a difference array approach
        for l, r, d in shifts:
            d = 2 * d - 1  # Convert d=1 (right) to +1 and d=0 (left) to -1
            freq[l] += d   # Start shift at index l
            freq[r + 1] -= d  # End shift at index r + 1

        # Convert the difference array into prefix sums to get the net shift at each index
        for i in range(1, n + 1):
            freq[i] += freq[i - 1]

        # Apply the calculated shifts to each character in the string
        return "".join([self.shift(s[i], freq[i]) for i in range(n)])
