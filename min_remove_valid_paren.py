def minRemoveToMakeValid(s):
    # O(n) time and space
    # doesn't use stack
    s = list(s)
    open_count = 0

    for ind, c in enumerate(s):
        if c == "(":
            open_count += 1
        elif c == ")":
            if not open_count: # if open_count is 0
                s[ind] = ""
            else:
                open_count -= 1
    for i in range(len(s) - 1, -1, -1):
        if not open_count:
            break
        if s[i] == "(":
            s[i] = ""
            open_count -= 1
    return "".join(s)

print(minRemoveToMakeValid("(a(b(c)d))"))