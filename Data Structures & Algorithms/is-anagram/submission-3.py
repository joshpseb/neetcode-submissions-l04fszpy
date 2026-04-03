class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for c in t:
            if c in count:
                count[c] -= 1
                if count[c] < 0:
                    return False
            else:
                return False
        for num in count.values():
            if num != 0:
                return False 
        return True