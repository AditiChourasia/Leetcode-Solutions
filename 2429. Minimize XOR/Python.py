# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set_bits_count = num2.bit_count()
        res = 0
        
        # First, try to match the set bits of num1 to the result as much as possible
        for i in range(31, -1, -1):
            if num1 & (1 << i):
                if set_bits_count > 0:
                    res |= (1 << i)
                    set_bits_count -= 1
        
        # Then, fill the remaining set bits in the lowest available positions
        for i in range(32):
            if set_bits_count == 0:
                break
            if not (res & (1 << i)):
                res |= (1 << i)
                set_bits_count -= 1
        
        return res
