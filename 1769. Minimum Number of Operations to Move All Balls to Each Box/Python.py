# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes) #Length of boxes
        ans = [0] * n   #Initializing answer array
        for i in range(n):
            if boxes[i] == "1": #if we get 1 in string then we check for all other boxes 
                for j in range(n):
                    ans[j] += abs(j-i) #we add the answer to answer[j] in array

        return ans