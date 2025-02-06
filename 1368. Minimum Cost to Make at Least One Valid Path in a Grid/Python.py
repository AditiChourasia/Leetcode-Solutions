# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

import collections
from typing import List


class Solution:
    _dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minCost(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        min_cost = [[float("inf")] * num_cols for _ in range(num_rows)]
        min_cost[0][0] = 0

        deque = collections.deque([(0, 0)])

        while deque:
            row, col = deque.popleft()

            for dir_idx, (dx, dy) in enumerate(self._dirs):
                new_row, new_col = row + dx, col + dy
                cost = 0 if grid[row][col] == dir_idx + 1 else 1

                if (self._is_valid(new_row, new_col, num_rows, num_cols) and min_cost[row][col] + cost < min_cost[new_row][new_col]):

                    min_cost[new_row][new_col] = min_cost[row][col] + cost

                    if cost == 1:
                        deque.append((new_row, new_col))
                    else:
                        deque.appendleft((new_row, new_col))

        return min_cost[num_rows - 1][num_cols - 1]

    def _is_valid(self, row: int, col: int, num_rows: int, num_cols: int) -> bool:
        return 0 <= row < num_rows and 0 <= col < num_cols