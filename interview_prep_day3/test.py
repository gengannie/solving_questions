from collections import deque
open_paren = deque()
s = "()[]{}"
matching_closed = {")" : "(", "}" : "{", "]" : "["}
for c in s:
    if (not c in matching_closed):
        open_paren.append(c)
    elif (open_paren and open_paren [-1] == matching_closed[c]):
        open_paren.pop()
    else:
        print("false")
    print(c, open_paren)
print("true")
elem = [1,2,3,4]
print(elem [:-1])
    