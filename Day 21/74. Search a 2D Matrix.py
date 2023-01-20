# Solution Link

class Solution:
    def searchMatrix(self, matrix, target: int):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if target == matrix[i][j]:
                    return True
                if target < matrix[i][j]:
                    return False
        return False
                    