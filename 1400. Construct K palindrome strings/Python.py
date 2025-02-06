# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        n = len(s)
        
        # If k is greater than the length of the string, it's impossible to construct k palindromes
        if k > n:
            return False

        # Count the frequency of each character in the string
        count = Counter(s)
        
        # cnt will keep track of the number of characters with an odd frequency
        cnt = 0

        # Iterate through the frequency counts
        for i in count.values():
            # Add the count of characters with an odd frequency
            cnt += i % 2

        # Check if the number of odd frequency characters is less than or equal to k
        # This means we can form k palindromes with these constraints
        return cnt <= k
