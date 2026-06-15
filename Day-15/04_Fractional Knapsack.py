# Fractional Knapsack


# Approach:
# He we want to get the maximum value and we can take items in fractions
# So first of all find out value of per unit of items.
# then sort items based on unit values in decreasing order
# take whole item if its w <= cap else take in fraction 
# return maxval

# T.C = O(nlogn)
# S.C = O(n)

class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        
            
        n = len(val)
        items = []
        
        for i in range(n):
            ratio = val[i] / wt[i]
            items.append((val[i],wt[i],ratio))
        
        items.sort(key=lambda x: x[2], reverse='True')
        
        maxval = 0
        
        for v,w,r in items:
            if w <= capacity:
                maxval += v
                capacity -= w
            else:
                maxval += capacity * r
                capacity = 0
                break
        
        
        return float(format(maxval, '.6f'))
        
    