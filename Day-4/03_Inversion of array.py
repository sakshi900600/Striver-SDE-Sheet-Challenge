# Count number of inversion:
# arr[] = [2, 4, 1, 3, 5]
# Output: 3


# Approach:
# In merge sort, merge fun we check this condition: if arr[i] > arr[j] and this is the inversion condition.


# So we will use that same code and count no of inversion here.
# now if at any moment this condition is true - count inversions
# now coz both array are sorted so if arr[i] > arr[j], which means all elem from i till mid is also > arr[j] , that's why we will add (mid-i+1) into the count variable. 



class Solution:
    def inversionCount(self, arr):
        # Code Here
        n = len(arr)
        return self.mergeSort_inv(arr, 0, n-1)
        
    
    def mergeSort_inv(self, arr, si, ei):
        if si >= ei:
            return 0
        
        inversion = 0
        mid = (si+ei) // 2
        inversion += self.mergeSort_inv(arr, si, mid)
        inversion += self.mergeSort_inv(arr, mid+1, ei)
        inversion += self.merge(arr, si, mid, ei)
        
        return inversion
    
    
    def merge(self, arr, si, mid, ei):
        i = si
        j = mid+1
        temp = []
        inv = 0
        
        while i <= mid and j <= ei:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
                inv += (mid-i+1)
        
        
        while i <= mid:
            temp.append(arr[i])
            i += 1
        
        while j <= ei:
            temp.append(arr[j])
            j += 1
        
        arr[si:ei+1] = temp[:]
        
        
        return inv
            
            
            
            
            