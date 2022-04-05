# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        prev = None
        curr = head
        while(curr):

            if curr.val not in lst:

                lst.append(curr.val)
                prev = curr 
                curr = curr.next

            else:
                curr = curr.next
                prev.next = curr

        return head
                
 
