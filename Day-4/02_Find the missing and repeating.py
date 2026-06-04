# Find missing and repeating number

# Approach -1:
# Counting freq of elem and based on that returning missing and repeating. 


# Approach -2 (Maths based):

# Using sum and square sum of n natural no and given arr to find missing and repeating.



class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        
        n = len(grid)

        dct = {}

        for i in range(n):
            for j in range(n):
                num = grid[i][j]
                dct[num] = dct.get(num,0)+1
        

        for i in range(1, (n*n)+1):
            if dct.get(i) > 1 :
                rep = i
            
            if dct.get(i) == None:
                mis = i
            
        return [rep, mis]
    

    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        
        n = len(grid)
        li = [] 

        for i in range(n):
            for j in range(n):
                li.append(grid[i][j])

        length = len(li)
        # sum and square sum of n natural no
        sn = length*(length+1)//2
        s2n = length*(length+1)*(2*length+1)//6

        # sum and square sum of elem of given arr.
        s = 0
        s2 = 0

        for elem in li:
            s += elem
            s2 += elem*elem
        
        val1 = s-sn
        val2 = s2-s2n

        val2 = val2 // val1

        rep = (val1 + val2)//2
        mis = rep - val1

        return [rep, mis]

