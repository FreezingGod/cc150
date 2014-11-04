class Solution:
    def nthToLast(head, n):
        if not head: return None
        p2 = head
        for i in range(n):
            if not p2:
                return None
            p2 = p2.next
        p1 = head
        while p2:
            p1 = p1.next
            p2 = p2.next
        return p1
