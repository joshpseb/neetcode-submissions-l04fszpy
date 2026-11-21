class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while True:
            digits = str(n)
            sum = 0
            for d in digits:
                sum += int(d) ** 2
            
            if sum == 1:
                return True
            if sum in s:
                return False
            else:
                s.add(sum)
                n = sum
