# Merge two sorted arrays without extra space
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]


# Approach:
# take 3 pointer, 2 at end of both array and 3rd at the last elem of 1st arr.
# Until all elem is not placed from arr2 into arr1 run loop
# everytime place the larger elem from both arr at the end
# this way both will be merged in a sorted fashion.


# Time Complexity: O(n+m)
# Space Complexity: O(1)


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        i = m-1
        j = n-1
        k = n+m-1

        while j >= 0:
            if i >=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            
            k -= 1
        

                



        