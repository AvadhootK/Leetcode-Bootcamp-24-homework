# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 2 pointer
        left,right = head, head
        # we do not check if there are no nodes as constraints are given as no.of nodes are 1 to 100
        while right and right.next:
            left = left.next
            right = right.next.next
        return left        