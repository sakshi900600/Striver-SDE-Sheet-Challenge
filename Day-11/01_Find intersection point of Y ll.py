# Find Intersection point of ll


# Approach:
# Take 2 pointers for both ll.
# while both are not same:
# if p1 then move it otherwise start from head2
# similarly if p2 then move it otherwise start from head1
# At the end either both will be pointing the same node or both will be none.
# return any of the pointer.



class Solution(object):
    def getIntersectionNode(self, headA, headB):

        p1 = headA
        p2 = headB

        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA

        return p1

        