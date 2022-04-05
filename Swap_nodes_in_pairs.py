# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        p1=head
        # p2=p1.next
        if head==None or head.next==None:
            return head
        
        elif head.next:
            p2=head.next
            
        dummy=ListNode(0)
        dummy.next= head.next
        
        while p1!=None and p2!=None:    
        #swap 
            if prev==None:
                prev = p1
                
            elif prev!= None:
                prev.next=p2
                # print(prev.next.val)
                prev=p1
                
            p1.next = p2.next
            p2.next = p1
            # print(prev.next.val)
        
            p1=p1.next
            if p1==None:
                p2=p1
            else:
                p2=p1.next
        return dummy.next
        
