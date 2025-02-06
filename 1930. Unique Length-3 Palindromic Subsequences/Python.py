# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import Counter
import math

def mos_algorithm(arr, queries):
    # Calculate the block size for Mo's algorithm
    block_size = int(math.sqrt(len(arr)))
    # Sort queries based on block and then by right endpoint
    sorted_queries = sorted(queries, key=lambda x: (x[0] // block_size, x[1]))
    
    # Initialize pointers and distinct character counter
    left, right, dctr = 0, -1, 0
    ctr = [0] * 26  # To store counts of each character (a-z)
    
    def remove(x):
        """Remove character x from the current range"""
        nonlocal dctr
        ctr[x] -= 1
        if ctr[x] == 0:
            dctr -= 1  # Decrease distinct count if the character count becomes zero
    
    def add(x):
        """Add character x to the current range"""
        nonlocal dctr
        ctr[x] += 1
        if ctr[x] == 1:
            dctr += 1  # Increase distinct count if the character is added for the first time

    res = 0  # Initialize result
    
    # Process each query using Mo's algorithm
    for query_left, query_right in sorted_queries:
        # Expand or shrink the range to match the current query
        while left > query_left:
            left -= 1
            add(arr[left])
        while right < query_right:
            right += 1
            add(arr[right])
        while left < query_left:
            remove(arr[left])
            left += 1
        while right > query_right:
            remove(arr[right])
            right -= 1
        
        # Add the count of distinct characters for this query range to the result
        res += dctr
    
    return res

class Solution:
    def countPalindromicSubsequence(self, s):
        # Convert the string into numeric indices corresponding to each character ('a' -> 0, ..., 'z' -> 25)
        s = [ord(c) - ord('a') for c in s]
        n = len(s)
        
        # Arrays to store first and last occurrence of each character
        f = [-1] * 26  # First occurrence
        l = [-1] * 26  # Last occurrence
        
        # Populate first and last occurrence arrays
        for i in range(n):
            if f[s[i]] == -1:
                f[s[i]] = i
            l[s[i]] = i
        
        # List of intervals (queries) for Mo's algorithm
        inv = []
        for x in range(26):
            if f[x] + 1 < l[x]:  # Valid interval if first occurrence is before last
                inv.append((f[x] + 1, l[x] - 1))
        
        # Apply Mo's algorithm on the intervals
        return mos_algorithm(s, inv)
