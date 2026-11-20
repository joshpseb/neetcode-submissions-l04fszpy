class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # dfs that breaks when theres an invalid string
        # keep a count of open and closed paren
        # if close > open, break
        # dfs splits on open and close paren

        res = []
        def dfs(open, closed, string):
            if closed > open:
                return
            if open > n:
                return
            if closed == open == n:
                res.append(string)
                return
            dfs(open + 1, closed, string + '(')
            dfs(open, closed + 1, string + ')')
        
        dfs(0, 0, "")
        return res