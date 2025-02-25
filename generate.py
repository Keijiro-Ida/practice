class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return []

        triangle = [[1]]

        for i in range(1, numRows):
            prev_row = triangle[-1]
            now_row = [1]

            for j in range(1, len(prev_row)):
                now_row.append(prev_row[j-1] + prev_row[j])

            now_row.append(1)
            triangle.append(now_row)

        return triangle
