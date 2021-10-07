# hint: Matrix = [[0 for x in range(w)] for y in range(h)] 
def spiral (n):
    ans = [[0]*n for i in range(n)]
    right, horizontal = True, True
    vertical, down = False, False
    curr_hori_ind, curr_verti_ind = 0, 0
    for i in range (1,n*n+1):
        if (curr_hori_ind >= n or curr_hori_ind < 0 or curr_verti_ind >= n or curr_verti_ind < 0):
            down = not down
            right = (not right)
            horizontal = (not horizontal)
            vertical = not vertical
            if (curr_hori_ind >= n):
                curr_hori_ind -= 1
            elif (curr_hori_ind < 0):
                curr_hori_ind = 0
            elif (curr_verti_ind >= n):
                curr_verti_ind -= 1
            elif (curr_verti_ind < 0):
                curr_verti_ind = 0
        if (horizontal):
            ans [curr_hori_ind] [curr_verti_ind] = i
            if (right):
                curr_hori_ind += 1
            else:
                curr_hori_ind += -1
        elif (vertical):
            ans [curr_hori_ind] [curr_verti_ind] = i
            if (down):
                curr_verti_ind += 1
            else:
                curr_verti_ind -= 1
    return ans

n = 4
print_ans = spiral (n)
for i in range (n):
    for j in range (n):
        print(print_ans[i][j])