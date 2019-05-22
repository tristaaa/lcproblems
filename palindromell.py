class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
            determine if a given Linked List is a palindrome

            :type head: ListNode
            :rtype: boolean
        """
        slow=fast=head
        rev=None # store the left half in reverse order
        while fast and fast.next:
            fast=fast.next.next # this line must be above the next line, otherwise fast.next will become None because of the assignment of rev.next
            rev,rev.next,slow=slow,rev,slow.next # reverse the fist half of the linked list
        # print(rev.val,slow.val,fast)
        # in this case, there are odd number of value in the linked list,
        # thus skip comparing the middle value
        if fast: slow=slow.next
        # compare the left half and the right half
        while rev and rev.val==slow.val:
            rev,slow=rev.next,slow.next

        # if the number represented by the linked list is a palindrome, the rev must be None,
        # otherwise, it will break before go through the whole left side
        return not rev
               

# test
sol = Solution()
p=head=ListNode(5)
head.next=ListNode(4)
head.next.next=ListNode(3)
head.next.next.next=ListNode(3)
head.next.next.next.next=ListNode(4)
head.next.next.next.next.next=ListNode(5)

inputll=''
while p:
    inputll+=str(p.val)+' -> '
    p=p.next
print("the given linked list: %s is a palindrome: %s" % (inputll[:-4], sol.isPalindrome(head)))