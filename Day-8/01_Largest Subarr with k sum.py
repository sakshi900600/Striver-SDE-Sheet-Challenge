# Longest Subarray with Sum K

# Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
# Output: 6


# Approach:
# First thing firsts, here we can't apply sliding window coz arr containes negative elems too.

# So I have used a dct and applied the similar approach as in two sum.

# take dct,variables.
# traverse the arr and add elem in csum
# if csum == k then the length is i+1 so store in maxlen var
# reqsum will be (csum -k) and if it is in dct then get the idx and length will be i-dct[reqsum]
# store the maxlen and if reqsum not in dct then add it in dct .
# return the maxlen.


# why reqsum = csum-k not k-csum ?????

# We want: current_sum - previous_sum = k
# Rearrange: previous_sum = current_sum - k
# So we check if we've seen (current_sum - k) before


# Example: 
# Day 0-2: Spent $10 total
# Day 0-5: Spent $25 total
# You want to know: Did I spend exactly $15 between day 3-5?
# and that will be (spending from 0-5 day - spending till 3-1)


# sum(l..r) = prefix[r] - prefix[l-1]
# sum(l..r) = k
# prefix[r] - prefix[l-1] = k
# prefix[l-1] = prefix[r] - k

# that's why req = csum - k

# Now why using dct ?
# - We can also build a list of prefix sum but that will take O(n) time for lookup and in dct its O(1).


# Time Complexity: O(n)
# Space Complexity: O(n)



class Solution:
    def longestSubarray(self, arr, k):  
        # code here

        # brute force:
        # generate all subarr and see if its sum =k store maxlen from all. 
        
        n = len(arr)
        maxlen = 0
        csum = 0
        dct ={}
        
        for i in range(n):
            csum += arr[i]
            
            if csum == k:
                maxlen = max(maxlen, i+1)
            
            reqsum = csum - k
            
            if reqsum in dct:
                length = dct[reqsum]
                maxlen = max(maxlen, i-length)
            
            if csum not in dct:
                dct[csum] = i
        
        
        return maxlen
    
