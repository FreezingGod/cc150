class Solution:
# return the kth number whose sole prime factors are 3, 5 and 7
    def findKth(self, k):
        result = []
        result.append(1)
        q3, q5, q7 = [], [], []
        while len(result) < k:
            q3.append(3*result[-1])
            q5.append(5*result[-1])
            q7.append(7*result[-1])
            result.append(min(q3[0], q5[0], q7[0]))
            if result[-1] == q3[0]:
                q3.pop(0)
            if result[-1] == q5[0]:
                q5.pop(0)
            if result[-1] == q7[0]:
                q7.pop(0)
        return result
    def findKthv2(self, k):
        result = [1]
        q3, q5, q7 = [3], [5], [7]
        while len(result) < k:
            result.append(min(q3[0], q5[0], q7[0]))
            if result[-1] == q3[0]:
                q3.pop(0)
                q3.append(3*result[-1])
                q5.append(5*result[-1])
                q7.append(7*result[-1])
            elif result[-1] == q5[0]:
                q5.pop(0)
                q5.append(5*result[-1])
                q7.append(7*result[-1])
            else:
                q7.pop(0)
                q7.append(7*result[-1])
        return result


sol = Solution()
r = []
#print sol.findKth(100)
#print sol.findKthv2(100)
if sol.findKth(1000) == sol.findKthv2(1000):
    print True
else:
    print False
