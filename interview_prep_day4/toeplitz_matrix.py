# https://leetcode.com/problems/toeplitz-matrix/

# More elegant solution from leetcode
# Time Complexity: O(M∗N)
# Space Complexity: O(M+N


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True
# My solution
# time complexity: O (m*n)
# space complexity: constant?? not really allocating memory for anything new???
def main(matrix):
    row = len(matrix)
    col = len(matrix[0])
    # can start from top left and explore the 1st row and 1st col
    #search_th = m + n - 1
    dirs_s = [(0, 1), (1, 0)]
    x, y = 0, 0
    top_x, top_y = 0, 0
    curr_ind = 0
    checking_sim = matrix [x] [y]
    count = 0
    while(True):
        count += 1
        future_xx = top_x + dirs_s [curr_ind] [0]
        future_yy = top_y + dirs_s [curr_ind] [1]
        if (x + 1 >= row or y + 1  >= col): # checking if diagonal is out of bounds
            top_x += dirs_s [curr_ind] [0]
            top_y += dirs_s [curr_ind] [1]
            if (future_xx >= row or future_yy >= col): # check if dirs_s is out of bounds
                curr_ind += 1
                if (curr_ind >= 2):
                    return True
                top_x = dirs_s [curr_ind] [0]
                top_y = dirs_s [curr_ind] [1]
                x = top_x
                y = top_y
                checking_sim = matrix [x][y]
                continue
            x = top_x
            y = top_y
            checking_sim = matrix [x][y]
        else: 
            x += 1
            y += 1
            if (not matrix[x][y] == checking_sim):
                print(x,y,matrix[x][y], checking_sim)
                return False
    return True
if __name__ == "__main__":
    print(main([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))