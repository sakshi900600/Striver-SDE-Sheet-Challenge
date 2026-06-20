# 33. Search in Rotated Sorted Array


# Approach:
# Here coz arr was sorted but rotated from some idx which mean from that idx left and right part is still sorted so we can apply binary search
# to check if left part is sorted : arr[si] <= arr[mid] else right part is sorted
# if elem exists in left part: arr[si] <= tar <= arr[mid] then search there
# else search in right part
# return -1 if not found



class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)

        si = 0
        ei = n-1

        while si <= ei:
            mid = (si+ei)//2

            if nums[mid] == target:
                return mid
            
            # left part sorted
            if nums[si] <= nums[mid]:
                if nums[si] <= target <= nums[mid]:
                    ei = mid-1
                else:
                    si = mid+1
            else:
                if nums[mid] <= target <= nums[ei]:
                    si = mid+1
                else:
                    ei = mid-1
        
        return -1

        