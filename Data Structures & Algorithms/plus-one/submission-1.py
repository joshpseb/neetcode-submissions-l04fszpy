class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]

        carry = 1
        i = 0
        sum = 0
        while carry and i < len(digits):
            sum += carry + digits[i]
            if sum > 9:
                carry = sum // 10
                sum -= carry * 10
            else:
                carry = 0
            digits[i] = sum
            i += 1
        if carry:
            digits.append(carry)
        return digits[::-1]