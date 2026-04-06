class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1count, s2count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[r]) - ord('a')
            s2count[idx] += 1
            if s1count[idx] == s2count[idx]:
                matches += 1
            elif s1count[idx] + 1 == s2count[idx]:
                matches -= 1
            
            idx = ord(s2[l]) - ord('a')
            s2count[idx] -= 1
            if s1count[idx] == s2count[idx]:
                matches += 1
            elif s1count[idx] - 1 == s2count[idx]:
                matches -= 1
            l += 1

        return matches == 26

        '''
        s1 = sorted(s1)
        for i in range(len(s2) - len(s1) + 1):
            sub = s2[i : i + len(s1)]
            if s1 == sorted(sub):
                return True
        return False
        '''
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
