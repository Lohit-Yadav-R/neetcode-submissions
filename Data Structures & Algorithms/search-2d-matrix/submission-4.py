class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1
        while top <= bot:
            row = top + ((bot - top) //2)
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        if not top <= bot:
            return False
        row = top + ((bot - top) // 2)
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False








