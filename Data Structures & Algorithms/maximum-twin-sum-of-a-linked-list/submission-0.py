# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 5 4 2 1
        # Max sum is 6 since 

        # 5 4 1 2

        # 3 2 5 2 1 6

        # 3 2 6 1 2 5

        # 5 1 is 6
        # 4 2 is 6 so they equa

        # Can I just solve this with two pointer and move pointesr close to each
        # other until L > R?
        #Can't cause this is a singly linked list can't traverse backward
        # What if we tried flipping the second half of the linked list?
        # This would actually work, every two values would be the twin!

        #In the scenario the list length is 2, we just return the sum of two values
        slow = head
        fast = slow.next

        if not fast.next:
            return slow.val + fast.val

        #Ok we know the list is at least min 4 by constraints.
        #We need to find the middle point to flip the second half
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 5 2 1 4

        # 5 2 4 1 3 5

        second_half_head = slow.next
        prev = None #eventualy reaches the last node which is our head of second half

        #Now we reverse the second half starting from here
        while second_half_head:
            next = second_half_head.next
            second_half_head.next = prev
            prev = second_half_head
            second_half_head = next

        slow.next = prev

        # Now we traverse as normally with slow and fast pointer!
        slow2 = head
        fast2 = prev
        maxSum = 0

        while fast2:
            currSum = slow2.val + fast2.val
            maxSum = max(maxSum, currSum)
            slow2 = slow2.next
            fast2 = fast2.next

        return maxSum



        
        
        





    

        


