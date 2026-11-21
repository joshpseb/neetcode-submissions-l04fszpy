class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        place = 1
        sum = 0
        for i in range(len(digits) - 1, -1, -1):
            sum += digits[i] * place
            place *= 10
        sum += 1
        sum = str(sum)
        
        out = []
        for d in sum:
            out.append(int(d))
        return out