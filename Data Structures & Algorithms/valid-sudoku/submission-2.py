class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(10)]
        col_set = [set() for _ in range(10)]
        grid_set = [set() for _ in range(10)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                if num in row_set[i] or num in col_set[j]:
                    return False
                if num in grid_set[(i//3)*3 + (j//3)]:
                    return False
                row_set[i].add(num)
                col_set[j].add(num)
                grid_set[(i//3)*3 + (j//3)].add(num)
        return True
