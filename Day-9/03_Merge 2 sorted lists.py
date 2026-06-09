# Merge 2 Sorted linkedlists


# Approach:
# I simply used the merge function approach of mergeSort.
# took 2 pointers for both list, a dummy node to store the final sorted nodes of ll.
# if either is none return other
# else everytime take min val node and add in dummy node ll.
# at the end add the leftover nodes 
# return head as dummy.next

# Time Complexity : O(n+m)
# Space Complexity : O(n+m)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(-1)

        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            p1 = list1
            p2 = list2
            temp = dummy

            while p1!= None and p2 != None:
                if p1.val <= p2.val:
                    newNode = ListNode(p1.val)
                    temp.next = newNode
                    temp = newNode
                    p1 = p1.next
                else:
                    newNode = ListNode(p2.val)
                    temp.next = newNode
                    temp = newNode
                    p2 = p2.next
            
            while p1 != None:
                newNode = ListNode(p1.val)
                temp.next = newNode
                temp = newNode
                p1 = p1.next
            
            while p2 != None:
                newNode = ListNode(p2.val)
                temp.next = newNode
                temp = newNode
                p2 = p2.next
        

        return dummy.next

