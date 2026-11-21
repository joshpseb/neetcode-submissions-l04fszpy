class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        while n:
            n &= n - 1
            out += 1
        return out