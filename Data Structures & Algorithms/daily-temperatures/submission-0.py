class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n):
            day = i
            currTemp = temperatures[day]
   
            count = 0
            while i < n:
                if temperatures[i] > currTemp:
                    res[day] = count
                    break
                else:
                    count += 1
                i += 1
            print(day, currTemp, count)
        return res