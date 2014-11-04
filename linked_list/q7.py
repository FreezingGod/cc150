class Solution:
    def isPalindrome(head):
        if not head: return True
        stack = []
        p1, p2 = head, head
        while p2 and p2.next:
            stack.append(p1.val)
            p1 = p1.next
            p2 = p2.next.next
        if p2:
            p1 = p1.next
        while p1:
            top = stack.pop()
            if top != p1.val:
                return False
            p1 = p1.next
        return True
