class Solution:
    # time complexity: O(n^2) as we iterate through all the sudoku
    # space complexity: O(n^2) as we store all the numbers if solved sudoku
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue

                box_index = (i // 3) * 3 + (j // 3)

                if (
                    num in rows[i]
                    or num in cols[j]
                    or num in boxes[box_index]
                ):
                    return False

                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        return True
