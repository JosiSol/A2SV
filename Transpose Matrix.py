class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows,columns = len(matrix), len(matrix[0])
        res = [[0] * rows for _ in range(columns)]

        for i in range(rows):
            for j in range(columns):
                res[j][i] = matrix[i][j]
        return res
