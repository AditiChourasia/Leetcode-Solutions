# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)  # Number of rows in the matrix
        n = len(mat[0])  # Number of columns in the matrix

        # Dictionary to map each number in the matrix to its position (row, column)
        pos_map = {}
        for i in range(m):
            for j in range(n):
                pos_map[mat[i][j]] = (i, j)

        # Arrays to count how many numbers have been marked in each row and column
        rowCount = [0] * m
        colCount = [0] * n

        # Total number of cells in the matrix
        total_cells = n * m

        # Iterate over each number in the sequence `arr`
        for i in range(total_cells):
            cell = pos_map[arr[i]]  # Get the position (row, column) of the current number from `pos_map`

            # Increment the count for the corresponding row and column
            rowCount[cell[0]] += 1
            colCount[cell[1]] += 1

            # Check if the current row or column is completely filled
            if rowCount[cell[0]] == n or colCount[cell[1]] == m:
                return i  # Return the current index as the first complete index

        return -1  # If no row or column is completely filled, return -1
