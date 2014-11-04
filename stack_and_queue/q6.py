import random
class Solution:
# sort stack s so that the top contains the biggest item
# using at most one additional stack
    def sortStack(self, s):
        buffer = []
        while s:
            t = s.pop()
            if not buffer or buffer[-1] >= t:
                buffer.append(t)
            else:
                while buffer and buffer[-1] < t:
                    s.append(buffer.pop())
                buffer.append(t)
        while buffer:
            s.append(buffer.pop())
        return s

sol = Solution()
s = range(100)
random.shuffle(s)
print sol.sortStack(s) == range(100)
