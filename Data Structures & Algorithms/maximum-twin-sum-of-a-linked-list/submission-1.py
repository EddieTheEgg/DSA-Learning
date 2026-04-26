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
        #Step 1. We need to find the middle point to flip the second half
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next


        #Step 2. Reverse the linked list at this second half head
        second_half_curr = slow.next
        prev = None

        while second_half_curr:
            next = second_half_curr.next
            second_half_curr.next = prev # 5 -> 4 becomes None <- 5 / 4
            prev = second_half_curr # None <- 5 / 4 becomes 5 <- 5 / 4
            second_half_curr = next # curr pointer is now at 4, and repeat this until we reach null

        #Connect the head before the middle point to the reversed head
        #prev becomes the head of the reversed linked list portion
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



        
        
        





    

        


