# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)  # Total number of travel days
        dp = [float('inf')] * (n + 1)  # Initialize DP array with infinity
        dp[n] = 0  # Base case: No cost if no days left to cover

        # Initialize sliding window pointers for 1-day, 7-day, and 30-day passes
        x = y = z = n - 1

        # Iterate backward through the travel days
        for i in range(n - 1, -1, -1):
            # Adjust pointers to find the range of days each pass can cover
            while x >= i and days[x] - days[i] >= 1:
                x -= 1
            while y >= i and days[y] - days[i] >= 7:
                y -= 1
            while z >= i and days[z] - days[i] >= 30:
                z -= 1

            # Compute the minimum cost for the current day
            dp[i] = min(
                costs[0] + dp[x + 1],  # Cost of a 1-day pass
                costs[1] + dp[y + 1],  # Cost of a 7-day pass
                costs[2] + dp[z + 1]   # Cost of a 30-day pass
            )

        # Return the minimum cost to cover all days starting from day 0
        return dp[0]
