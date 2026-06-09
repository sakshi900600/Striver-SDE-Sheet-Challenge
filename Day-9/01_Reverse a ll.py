# Reverse a linkedlist

# Approach-1:
# In first approach, I simply changed the values of the nodes.
# I took a st and put all values in it.
# again i traversed ll and put the reversed val in it

# Time Complexity : O(n)
# Space Complexity : O(n)


# Approach-2:
# In second approach, I changed the links b/n nodes.
# I took a var curr at head, prev as None
# traversed the ll and stored the next_node so that after changing the link we can traverse the remaining nodes in the ll.
# then simply pointed curr's next to prev
# updated prev to curr and curr to next_node
# at the end curr will be none and prev will be pointing to last node
# which will be our reversed head so returned prev

# Time Complexity : O(n)
# Space Complexity : O(1)



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Changing the value inside node - way1
        # st = []
        # temp = head
        # while temp != None:
        #     st.append(temp.val)
        #     temp = temp.next
        
        # temp = head
        # while temp != None:
        #     temp.val = st.pop()
        #     temp = temp.next
        
        # return head
    

        # changing the links b/n nodes - way2
        if head == None or head.next == None:
            return head

        curr = head
        prev = None

        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
    

   