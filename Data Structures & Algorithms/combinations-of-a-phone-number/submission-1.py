class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # dfs splits on each letter associated with a number
        # ends when reaching end of digits str, append to out
        # 

        
        numToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        out = []

        if len(digits) == 0:
            return out

        def dfs(i, string):
            if i == len(digits):
                out.append(string)
                return
            
            currNum = digits[i]

            for c in numToLetters[currNum]:
                dfs(i + 1, string + c)
        
        dfs(0, "")
        return out




