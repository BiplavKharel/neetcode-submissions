class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top = 0
        bottom = len(matrix) - 1
        row = 0
        while top <= bottom:
            mid_row = (bottom + top) // 2
            row = mid_row
            if matrix[mid_row][0] == target:
                return True
            if matrix[mid_row][0] > target:
                bottom = mid_row - 1
            else:
                if matrix[mid_row][0] < target and matrix[mid_row][-1] >= target:
                    if matrix[mid_row] == target:
                        return True
                        row = mid_row
                    break;
                else:
                    top = mid_row + 1

        
        l = 0
        r = len(matrix[row]) - 1
        print(row)
        while l <= r:
            mid = (l + r) //2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
            

        