# unstable, divide and conquer, in-place
# time: avg: O(nlogn) space: O(log n)
# worst case: O(n^2), space: O(n)

# divide collection into two -> random pivot
# elements smaller than pivot gets moved to the left
# elements greater to the right
# repeated until whole array is sorted
import random
import unittest
def quick_sort(arr, left, right):
    if left >= right:
        return
    partition_ind = partition(arr, left, right)
    quick_sort(arr, left, partition_ind - 1)
    quick_sort(arr, partition_ind + 1, right)
    return arr

def partition_2(arr, left, right):
    ind = random.randrange(left, right)
    # pass 
    return ind
def partition(arr, left, right):
    random_pivot = random.randrange(left, right)
    pivot_ele = arr[random_pivot]
    # let pivot element be the last
    arr[random_pivot], arr[right] = arr[right], arr[random_pivot]

    ind = left
    for i in range(left, right):
        if arr[i] < pivot_ele:
            arr[ind], arr[i] = arr[i], arr[ind]
            ind += 1
    arr[right], arr[ind] = arr[ind], arr[right]
    return ind

class MyTest(unittest.TestCase):
    dataT = [[2,5,7,1,3,8,4,6], [], [3,2,1], [4,4,7,4,3,2,5]]
    dataF = [[1,2,3,4,5,6,7,8], [], [1,2,3], [2,3,4,4,4,5,7]]

    def test_unique(self):
        # true check
        for ind, data in enumerate(self.dataT):
            actual = quick_sort(data, 0, len(data) - 1)
            if not actual:
                continue
            self.assertTrue(self.dataF[ind]== actual)
        
if __name__ == "__main__":
    unittest.main()
#input = [2,5,7,1,3,8,4,6]
#print(quick_sort(input, 0, len(input) - 1))
    