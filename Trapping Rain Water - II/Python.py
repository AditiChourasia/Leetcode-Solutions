# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        m = len(heightMap)  # Number of rows
        n = len(heightMap[0])  # Number of columns

        # Priority queue (min-heap) to process the boundary cells based on their height
        heap = []

        # 2D visited array to keep track of the cells that have been processed
        v = [[False] * n for _ in range(m)]

        # Initialize the heap with all the boundary cells
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    v[i][j] = True  # Mark boundary cells as visited

        res = 0  # This will store the total water trapped

        # Directions for moving to adjacent cells (up, left, down, right)
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        # Process the cells in the priority queue
        while heap:
            h, i, j = heapq.heappop(heap)  # Pop the cell with the minimum height

            # Check all four adjacent cells
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and not v[x][y]:
                    v[x][y] = True  # Mark the cell as visited
                    if heightMap[x][y] < h:
                        # If the adjacent cell is lower, water can be trapped
                        res += h - heightMap[x][y]
                    # Update the height of the adjacent cell to the maximum of its current height or h
                    heightMap[x][y] = max(heightMap[x][y], h)
                    # Push the updated height cell into the heap
                    heapq.heappush(heap, (heightMap[x][y], x, y))

        return res
