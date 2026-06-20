# Find nth root of m




class Solution:
    def nthRoot(self, n, m):
        # 
        
        if m == 0:
            return 0
            
        
        low, high = 1, m

        while low <= high:
            mid = (low + high) // 2

            # Store result of mid^n
            ans = 1
            for _ in range(n):
                ans *= mid
                if ans > m:
                    break

            # If mid^n equals m
            if ans == m:
                return mid

            # If mid^n is less than m
            if ans < m:
                low = mid + 1

            # If mid^n is more than m
            else:
                high = mid - 1

        return -1

