listB = [1 for i in range(5)]
for i in listB:
    print (i)

# count starts at 0 and increments
values = [1,2,3,4]
for count, value in enumerate(values):
    print(count, value)

# change where count starts by specifying:
for count, value in enumerate(values, start = 5):
    print(count, value)

#list slice ex:
list_a = ['a', 'b', 'c', 'd']
print (list_a[1:-1])   ## ['b', 'c']
list_a[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print (list_a)       ## ['z', 'c', 'd']

# dictionaries

dict_p = {
    1 : "hey"
}
if 1 in dict_p: print (dict_p[1])
val = dict_p[1] if 1 in dict_p else -1
print(val)

# dictionary formatting

hash = {}
hash['word'] = 'garfield'
hash['count'] = 42
s = 'I want %(count)d copies of %(word)s' % hash  # %d for int, %s for string
# 'I want 42 copies of garfield'
