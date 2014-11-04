class Solution:
    def addList(l1, l2):
        if not l1: return l2
        if not l2: return l1
        carry = 0
        head = None
        p = None
        while l1 or l2 or carry:
            cur = carry
            if l1:
                cur += l1.val
                l1 = l1.next
            if l2:
                cur += l2.val
                l2 = l2.next
            if cur >= 10:
                carry = cur / 10
                cur = cur % 10
            else:
                carry = 0
            n = ListNode(cur)
            if not head:
                head = n
                p = head
            else:
                p.next = n
                p = p.next
        return head
    def addList2(l1, l2):
        if not l1: return l2
        if not l2: return l1
        v1, v2 = 0, 0
        while l1:
            v1 = v1 * 10 + l1.val
            l1 = l1.next
        while l2:
            v2 = v2 * 10 + l2.val
            l2 = l2.next
        s = v1 + v2
        head, p = None, None
        k = 1
        while k < s:
            k *= 10
        k /= 10
        while s:
            cur = s / k
            s = s % k
            k /= 10
            n = ListNode(cur)
            if not head:
                head = n
                p = n
            else:
                p.next = n
                p = p.next
        return head
