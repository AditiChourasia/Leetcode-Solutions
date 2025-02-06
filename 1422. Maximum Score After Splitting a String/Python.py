# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = 0
        maxi = float("-inf")  # Start with the smallest possible score to update later
        n = len(s)

        # Iterate through the string to find all valid split points
        for i in range(1, n):  # Split the string at index `i` (cannot split at 0 or n)
            cnt = 0
            # Split the string into left and right parts
            left = s[:i]       # Left part includes indices 0 to i-1
            right = s[i:]      # Right part includes indices i to n-1

            # Count the number of '0's in the left part and '1's in the right part
            cnt += left.count("0")
            cnt += right.count("1")

            # Update the maximum score if the current split score is higher
            maxi = max(maxi, cnt)

        # Return the maximum score found
        return maxi
