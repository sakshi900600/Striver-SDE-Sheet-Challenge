# 138. Copy List with Random Pointer


# Approach:
# First I created the duplicate node of all original nodes and stored both in dct.
# Then again i traversed the given ll
# get the duplicate node of temp node from dct
# pointed the next and random of duplicate to the next and random or org nodes in the dct(#duplicate)
# return the dct[head]

# T.C = O(n)
# S.C = O(n)



# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        dct = {}
        temp = head

        while temp != None:
            if temp not in dct:
                dct[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp != None:
            dupln = dct.get(temp)
            dupln.random = dct.get(temp.random)
            dupln.next = dct.get(temp.next)
            temp = temp.next
        
        return dct.get(head)

        
