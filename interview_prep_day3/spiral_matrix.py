# https://leetcode.com/problems/spiral-matrix/
# QID: 54

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        coln = len(matrix[0])
        row = len(matrix)
        ans, past = [], []
        total = row * coln
        x, y= 0, 0
        d = 0
        for i in range (total):
            ans.append(matrix[x][y])
            past.append((x,y))
            future_x = x + dirs[d][0]
            future_y = y + dirs[d][1]
            if (future_x >= row or future_x < 0 or future_y >= coln or future_y <0 or (future_x, future_y) in past):
                d += 1
                if (d > 3):
                    d = 0
            x +=  dirs[d][0]
            y +=  dirs[d][1]
        
        return ans
                
                
                
        
                
        