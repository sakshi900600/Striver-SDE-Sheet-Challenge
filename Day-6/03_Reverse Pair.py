# Reverse Pairs

# In this problem we have to count no of reverse paris in the given arr.
# Input: nums = [1,3,2,3,1]
# Output: 2
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1


# Brute Force:
# First I wrote the brute force 2 loops solutions.
# here basically i run 2 loops and checked if condition satisfy then increase counter
# at the end return the count value.

# Time Complexity = O(n^2)
# Space Complexity = O(1)


# Final Solution:
# Here we are using the modified merge sort.
# We are using merge sort so that we can get 2 sorted halfs and in sorted half we can find out paris in less comparisons as compared to unsorted arr. That's the whole point of using merge sort.

# so merge sort and merge fun is same.
# here we just wrote another fun count reverse pair
# inside this fun: 
# for every ith elem we are counting valid pair in jth (2nd half)
# and updating count as j - (mid + 1)

# Reasoning for the count update:
# j = current position in right half (starts at mid + 1)
# mid + 1 = first index of right half

# So: j - (mid + 1) = how many elements we've moved from the start of right half


# Time Complexity: O(n log n)
# Space Complexity = O(n)


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return self.mergeSort(nums[:], 0, len(nums)-1)
    
    def mergeSort(self, arr, si, ei):
        if si >= ei:
            return 0
        
        mid = (si + ei) // 2
        
        # Count reverse pairs in left and right halves
        cnt = 0
        cnt += self.mergeSort(arr, si, mid)
        cnt += self.mergeSort(arr, mid+1, ei)
        
        # Count cross reverse pairs (where i in left, j in right)
        cnt += self.countReversePairs(arr, si, mid, ei)
         
        self.merge(arr, si, mid, ei)
        
        return cnt
    
    def countReversePairs(self, arr, si, mid, ei):
        cnt = 0
        j = mid + 1
        
        for i in range(si, mid + 1):
            while j <= ei and arr[i] > 2 * arr[j]:
                j += 1
            cnt += j - (mid + 1)
        
        return cnt
    

    def merge(self, arr, si, mid, ei):
        temp = []
        i = si
        j = mid + 1
        
        while i <= mid and j <= ei:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        
        while i <= mid:
            temp.append(arr[i])
            i += 1
        
        while j <= ei:
            temp.append(arr[j])
            j += 1
        

        arr[si:ei+1] = temp[:]

        