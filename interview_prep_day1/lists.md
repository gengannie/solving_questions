# Lists

## **note: language of choice is python**

### Things to note from https://developers.google.com/edu/python/lists

- len() gets the length of lists
- "for var in list"
- range(a,b) a inclusive to b not inclusive

#### List Methods

- list.append(element) -> modifies the original
- list.insert(index, elem) -> inserts element at given index, shifts elemen to right
- list.index(elem) -> searches for given element from start of list and returns its index, throws a ValueError if not:
- thing_index = thing_list.index(elem) if elem in thing_list else -1
- list.pop(index) -> removes and returns the element at the given index. Returns the rightmost element if index is omitted 
