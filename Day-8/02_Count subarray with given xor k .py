# count Subarrays with given XOR

# Input: arr[] = [4, 2, 2, 6, 4], k = 6
# Output: 4
# Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6]. Hence, the answer is 4.


# Approach:

# This is same as largest subarr with k sum only change is here we have to count xor.
# we will apply similar approach. 

# The thing to notice here is :
# In previous problem we were getting reqsum = csum-k coz inverse of addition is subtraction so that worked.

# here we have to get the reqxor and coz inverse operation of xor is xor itself that's why here reqxor = xor ^ k

# If a ^ b = c, then a ^ c = b and b ^ c = a


# Time Complexity: O(n)
# Space Complexity: O(n)




class Solution:
    def subarrayXor(self, arr, k):
        # code here
        
        n = len(arr)
        cnt = 0
        xor = 0
        dct ={}
        
        for i in range(n):
            xor ^= arr[i]
            
            if xor == k:
                cnt += 1
            
            reqxor = xor ^ k
            
            if reqxor in dct:
                cnt += dct[reqxor]
            
            dct[xor] = dct.get(xor,0)+1
        
        
        return cnt
        
        