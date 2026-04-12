class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRow = []
        if len(matrix) == 1:
            targetRow = matrix[0]
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid][0]
            if val > target:
                if target >= matrix[mid - 1][0]:
                    targetRow = matrix[mid - 1]
                    break
                r = mid - 1
            elif val < target:
                if mid == len(matrix) - 1 or target < matrix[mid + 1][0]:
                    targetRow = matrix[mid]
                    break
                l = mid + 1
            else:
                return True

        l, r = 0, len(targetRow) - 1
        while l <= r:
            mid = (l + r) // 2
            val = targetRow[mid]
            if val > target:
                r = mid - 1
            elif val < target:
                l = mid + 1
            else:
                return True
        return False