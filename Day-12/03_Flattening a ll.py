# Flattening a Linked List

# Here we were supposed to keep only the bottom pointer and all nodes values should be in sorted order.


# Approach:
# take a heap
# put all nodes values into heap
# create a dummy node
# get value from heap and crate new nodes and attatch newnodes in dummy bottom
# at the end return dummy bottom i.e head node.

# T.C = O(n)
# S.C = O(n)



class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

import heapq
class Solution:
    def flatten(self, root):
        # code here
        
        pq = []
        
        temp = root
        
        while temp != None:
            nextn = temp.next
            
            while temp != None:
                heapq.heappush(pq, temp.data)
                temp = temp.bottom
            
            temp = nextn
        
        dummy = Node(-1)
        temp = dummy
        
        while pq:
            data = heapq.heappop(pq)
            newNode = Node(data)
            temp.bottom = newNode
            temp = newNode
        
        return dummy.bottom
        
        
        
        
        
        