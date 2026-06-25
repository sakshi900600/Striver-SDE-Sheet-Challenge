# Sort a stack:


# Done with the help of a temp stack.


class Solution:
    def sortStack(self, st):
        # code here 
        temp_st = []
        
        while st:
            if len(temp_st) == 0:
                temp_st.append(st.pop())
            
            else:
                if temp_st and st[-1] >= temp_st[-1]:
                    temp_st.append(st.pop())
                else:
                    elem = st.pop()
                    while temp_st and temp_st[-1] > elem:
                        st.append(temp_st.pop())
                    temp_st.append(elem)
        
        
        st[:] = temp_st
        
                    
