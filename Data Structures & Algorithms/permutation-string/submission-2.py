class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        for i in range(len(s2) - len(s1) + 1):
            sub = s2[i : i + len(s1)]
            if s1 == sorted(sub):
                return True
        return False
        '''
        if len(s2) < len(s1):
            return False

        sort1 = {}
        for c in s1:
            sort1[c] = sort1.get(c, 0) + 1
        sort1 = sorted(sort1.items())

        for i in range(len(s2) - len(s1) + 1):
            sub = s2[i : i + len(s1)]
            sort2 = {}
            for c in sub:
                sort2[c] = sort2.get(c, 0) + 1
            sort2 = sorted(sort2.items())
            print(sort1)
            print(sort2)
            if sort1 == sort2:
                return True
        return False
        '''
