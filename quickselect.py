class Solution:
    def partition(self, nums, left, right, pivot):
        # return partition index
        # 1. move pivot to the end
        pivot_val = nums[pivot]
        nums[pivot], nums[right] = nums[right], nums[pivot]
        store = left
        for i in range(left, right):
            if nums[i] < pivot_val:
                nums[store], nums[i] = nums[i], nums[store]
                store += 1 # move every element that is smaller to the left
                # store is like the leftmost available ind
        nums[right], nums[store] = nums[store], nums[right] # move pivot to final place
        return store
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use quickselect, O(n) time and constant space, which is better than heap solution
        # on average O(n), but worst case is O(n^2)
        # return kth largest element 
        left, right = 0, len(nums) - 1
        if left == right: # if only one element
            return nums[left]
        
        translated_ind = len(nums) - k # actual index in sorted array (ex. 1st largest --> last element in list)
        pivot_ind = len(nums)
        
        while pivot_ind != translated_ind:
            rand_ind = random.randint(left, right) # helps make it O(n) on average
            pivot_ind = self.partition(nums, left, right, rand_ind)
            if pivot_ind < translated_ind: # if pivot less than desired, move left pointer to the right
                left = pivot_ind + 1
            else:
                right = pivot_ind - 1
        return nums[translated_ind]