# https://leetcode.com/problems/merge-sorted-array/
# given two int arrays sorted in non-decreasing order, lengths m and n
# sort them in place into nums1; nums1 has length m + n 
def merge(self, nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    len_combined = m + n
    i = 0
    copied_list = []
    for i in range (m):
        copied_list.append(nums1[i])
    left_ind = 0
    right_ind = 0
    i = 0
    while (left_ind < m and right_ind < n):
        if (copied_list [left_ind] < nums2 [right_ind]):
            nums1[i] = copied_list [left_ind]
            left_ind += 1
        else:
            nums1[i] = nums2 [right_ind]
            right_ind += 1
        i += 1
    while (right_ind < n):
        nums1[i] = nums2 [right_ind]
        right_ind += 1
        i += 1
    while (left_ind < m):
        nums1[i] = copied_list [left_ind]
        left_ind += 1
        i += 1
            
            

            
            
                
            
        