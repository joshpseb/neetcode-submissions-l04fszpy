class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # top left
        count = defaultdict(int)
        for row in board[0:3]:
            for num in row[0:3]:
                if num.isdigit():
                    if count[num] > 0:
                        return False
                    count[num] += 1
        
        # top middle
        count = defaultdict(int)
        for row in board[0:3]:
            for num in row[3:6]:
                if num.isdigit():
                    if count[num] > 0:
                        return False
                    count[num] += 1
        
        # top right
        count = defaultdict(int)
        for row in board[0:3]:
            for num in row[6:9]:
                if num.isdigit():
                    if count[num] > 0:
                        return False
                    count[num] += 1

        count = defaultdict(int)
        for row in board[3:6]:
            for num in row[0:3]:
                if num.isdigit():
                    if count[num] > 0:
                        return False
                    count[num] += 1

        count = defaultdict(int)
        for row in board[3:6]:
            for num in row[3:6]:
                if num.isdigit():
                    if count[num] > 0:
                        return False
                    count[num] += 1

        count = defaultdict(int)
        for row in board[3:6]:
            for num in row[6:9]:
                if num.isdigit():
                    if count[num] > 0:
                        return False
                    count[num] += 1

        count = defaultdict(int)
        for row in board[6:9]:
            for num in row[0:3]:
                if num.isdigit():
                    if count[num] > 0:
                        return False
                    count[num] += 1

        count = defaultdict(int)
        for row in board[6:9]:
            for num in row[3:6]:
                if num.isdigit():
                    if count[num] > 0:
                        return False
                    count[num] += 1

        count = defaultdict(int)
        for row in board[6:9]:
            for num in row[6:9]:
                if num.isdigit():
                    if count[num] > 0:
                        return False
                    count[num] += 1
                    
        # checking rows
        for row in range(9):
            row_count = set()
            col_count = set()
            for col in range(9):
                num = board[row][col]
                num2 = board[col][row]
                if num != ".":
                    if num in row_count:
                        return False
                    row_count.add(num)
                if num2 != ".":
                    if num2 in col_count:
                        return False
                    col_count.add(num2)
                
        
        

        
        return True

        
