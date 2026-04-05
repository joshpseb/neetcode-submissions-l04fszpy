class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        maxLen = 0
        l, r = 0, 1

        while r < len(s):
            sub = s[l : r]            
            if s[r] in sub:
                # find repeat letter
                while s[l] != s[r]:
                    l += 1
                l += 1
            r += 1
            maxLen = max(maxLen, r - l)
        return maxLen