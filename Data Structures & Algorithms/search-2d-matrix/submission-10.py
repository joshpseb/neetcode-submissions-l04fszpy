class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] > target:
                #if target >= matrix[mid - 1][0]:
                #    targetRow = matrix[mid - 1]
                #    break
                r = mid - 1
            elif matrix[mid][-1] < target:
                #if mid == len(matrix) - 1 or target < matrix[mid + 1][0]:
                #    targetRow = matrix[mid]
                #    break
                l = mid + 1
            else:
                break

        targetRow = matrix[(l + r) // 2]
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