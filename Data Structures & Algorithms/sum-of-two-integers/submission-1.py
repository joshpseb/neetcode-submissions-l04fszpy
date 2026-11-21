class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 010
        # 111
        # if a & b & c == 1: carry = 1, res = 1
        # if a & b or a & c or b & c== 1: carry = 1, res = 0
        # if a | b | c == 1: carry = 0, res = 1
        # else:          carry = 0, res = 0



        res = 0
        carry = 0

        for i in range(32):
            valA = (a >> i) & 1
            valB = (b >> i) & 1
            
            sum = valA ^ valB ^ carry
            carry = valA & valB | valA & carry | valB & carry

            res |= sum << i
        if (res >> 31) & 1:
            return res - 2 ** 32
        return res