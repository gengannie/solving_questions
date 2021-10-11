# Quick Sort (also called partition exchange)

- strategy: divide and conquer
- best case: time is O(n logn) : each partition logn
- not a stable algorithm
- key process: partition(), given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time. 
