def rob(arr): # returns int as max profit
    # penalized if robbing adj house
    # dp approach
    far_away = 0
    adj = arr[-1] # assuming length is at least one
    for i in range(len(arr) - 2, -1, -1): # start from second last element
        better_choice = max(adj, arr[i] + far_away)
        far_away = adj
        adj = better_choice
    return adj