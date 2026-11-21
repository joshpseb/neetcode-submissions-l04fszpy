class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        while n:
            out += n % 2
            n = n >> 1
        return out