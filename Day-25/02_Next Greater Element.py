# Next greater element;


# Approach:
# for nge: start from last and store elem in st
# while st top is less than curr elem pop
# store nge as the st top elem if stack has elem
# find out indx of elem in nums1 in nums2 and get nge of that elem and store in ans
# finally return ans

# T.C = O(n)
# S.C = O(n)


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        nge_n2 = [-1]*len(nums2)

        st = []
        st.append(nums2[-1])

        for i in range(len(nums2)-2,-1,-1):
            curr = nums2[i]
            while st and st[-1] < curr:
                st.pop()
            
            if st:
                nge_n2[i] = st[-1]
            
            st.append(curr)
        

        # print(nge_n2)

        ans = [-1]*len(nums1)

        for i in range(len(nums1)):
            elem = nums1[i]
            ein2 = nums2.index(elem)
            ans[i] = nge_n2[ein2]
        
        return ans



        