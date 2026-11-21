class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n + 1):
            tot = 0
            while i:
                tot += i % 2
                i //= 2
            out.append(tot)
        return out
                