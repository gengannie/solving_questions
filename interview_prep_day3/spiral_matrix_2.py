# https://leetcode.com/problems/spiral-matrix-ii/
# QID: 59

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans_matrix =  [[0 for i in range (n)] for j in range (n)]
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        past = []
        max_i = n*n
        x, y = 0,0
        d = 0
        for i in range (0, max_i):
            ans_matrix[x][y] = i + 1
            past.append((x,y))
            future_x = x + dirs[d][0]
            future_y = y + dirs[d][1]
            if (future_x >= n or future_x < 0 or future_y >= n or future_y < 0 or (future_x, future_y) in past):
                d += 1
                if (d > 3):
                    d = 0
            x += dirs[d][0]
            y += dirs[d][1]
        return ans_matrix
                