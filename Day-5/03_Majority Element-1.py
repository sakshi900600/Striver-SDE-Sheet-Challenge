# Majority Element

# Approach:
# First I used freq counting using dct and based on that returning the majority elem.

# I then tried to do it without any extra space. so the logic is:
# if an elem is majority then its freq will be largest. So i just took 2 variables: count and elem 
# if count is 0 --> set count=1, elem=curr
# otherwise if curr==elem --> count+1 else count-1

# through this we will get the highest freq elem. 
# now count toatal freq of this elem and if > n//2 then majority otherwise doesn't exists.

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # dct = {}
        # for elem in nums:
        #     dct[elem] = dct.get(elem,0)+1
        
        # for k,v in dct.items():
        #     if v > n//2:
        #         return k
        
        # return -1


        cnt = 0
        elem = -1

        for i in range(n):
            if cnt == 0:
                cnt = 1
                elem = nums[i]
            else:
                if nums[i] == elem:
                    cnt += 1
                else:
                    cnt -= 1
        
        cnt = 0
        for i in nums:
            if i == elem:
                cnt += 1
        
        if cnt > n//2:
            return elem
        
        return -1


