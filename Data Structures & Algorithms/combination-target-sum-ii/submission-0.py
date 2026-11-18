class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # dfs searches from all vals starting at i. choose between skipping and taking i
        # vals are sorted, so when skipping need to go through a while loop to reach nonduplicate number
        
        candidates.sort()
        out = []
        def dfs(i, total, path):
            if total == target:
                out.append(path.copy())
                return
            if i == len(candidates) or total > target:
                return

            # include candidates[i]
            path.append(candidates[i])
            dfs(i + 1, total + candidates[i], path)
            path.pop()

            #skip candidates[i]
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total, path)


        dfs(0, 0, [])
        return out