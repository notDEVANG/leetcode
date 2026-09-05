class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2
            value = matrix[mid // n][mid % n]
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False