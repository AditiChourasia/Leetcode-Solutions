# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:

        n = len(s)
        
        # If the length of the string is odd, it cannot be valid
        if n % 2 == 1:
            return False

        # Two stacks: one for open parentheses, another for extra changeable positions
        opens = []
        extra = []

        # First pass: check if we can match all close parentheses
        for i in range(n):
            if locked[i] == '0':  # If the character is not locked
                extra.append(i)  # Save its position in extra
                continue
            
            if s[i] == '(':
                opens.append(i)  # Track open parentheses positions
            else:
                # If a matching open parenthesis is available, pop it
                if opens:
                    opens.pop()
                elif extra:
                    extra.pop()  # Use an extra if no open is available
                else:
                    return False  # Invalid if no open or extra is available
        
        # Second pass: check if remaining opens can be matched with extras
        while opens:
            x = opens.pop()
            if not extra or extra[-1] < x:
                return False  # If no extras are available or the last extra is before the open, it's invalid
            extra.pop()

        # The number of remaining extras should be even
        return len(extra) % 2 == 0
