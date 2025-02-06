# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict

class Solution:
    def minimumLength(self, s: str) -> int:

        # Initialize a dictionary to count the frequency of each character in the string
        mpp = defaultdict(int)
        
        # Length of the original string
        n = len(s)
        
        # Count the frequency of each character in the string
        for i in s:
            mpp[i] += 1
        
        # Initialize the total number of characters to delete
        to_delete = 0
        
        # Iterate over each character and its frequency in the map
        for k, v in mpp.items():
            # Calculate pairs of identical characters that can be removed
            dels = (v - 1) // 2
            # Multiply by 2 to account for both ends and add to total deletions
            to_delete += dels * 2

        # Return the resulting length of the string after all deletions
        return n - to_delete
