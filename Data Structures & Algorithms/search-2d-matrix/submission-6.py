class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        larr = 0
        rarr = len(matrix) - 1
        while larr <= rarr:
            mid = larr + ((rarr - larr) // 2)
            if matrix[mid][-1] < target:
                larr = mid + 1
            elif target < matrix[mid][0]:
                rarr = mid - 1
            else:
                break
        if not larr <= rarr:
            return False
        l = 0
        m = larr + ((rarr - larr) // 2)
        r = len(matrix[m]) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            num = matrix[m][mid]
            if num == target:
                return True
            if num < target:
                l += 1
            else:
                r -= 1
        return False
            








