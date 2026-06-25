# Balanced Paranthesis


# Approach-1:
# replace all the valid pairs of (),{},[] with ""
# at the end if string is not empty then its not balanced,
# otherwise return true

# T.C = O(n)
# S.C = O(1)


# Approach-2:
# put the opening in stack
# if closing then if opening not exists or doesn't match then return false
# otherwise pop from stack
# at the end return true if st is empty else false

# T.C = O(n)
# S.C = O(n)




class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # while '()' in s or '{}' in s or '[]' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        
        # return len(s) == 0


        st = []
        for p in s:
            if p == '(' or p == '{' or p=='[':
                st.append(p)
            else:
                if not st:
                    return False
                else:
                    if not ((st[-1] == '(' and p==')') or (st[-1] == '{' and p=='}') or (st[-1] == '[' and p==']') ):
                        return False
                    
                    st.pop()
        
        return len(st) == 0


        