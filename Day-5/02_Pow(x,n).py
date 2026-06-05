# Pow(x,n) = x^n


# Approach:
# we can just multiply x with itself n times and its tc will be O(n).


# Approach: 
# we can use the property of power that is:
# if pow (n) is even then we can write it as (x*x)^(n/2)
# if pow (n) is odd then we can write it as x*(x)^(n-1)

# example: 2^10 = (2*2)^5 , 2^9 = 2*(2^8)

# and for the negative power we can write it as 1/(x^n)

# Time Complexity: O(logn)
# Space Complexity: O(1)


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if x==1 or n==0:
            return 1
        
        if n < 0 :
            n = -n
            x = 1/x

        ans = 1
        
        while n > 0:
            if n%2 == 0:
                x = x*x
                n = n/2
            else:
                ans = ans * x
                n = n-1
        
        return ans
