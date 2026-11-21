class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1  # check bit at i from right
            #shift bit val by 31 - i
            bit <<= 31 - i
            res |= bit
        return res
