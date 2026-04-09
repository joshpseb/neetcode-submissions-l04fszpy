class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking small boxes:
        for r in range(0, 9, 3): # 0, 3 ,6
            for c in range(0, 9, 3): # 0, 3 ,6
                count = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        num = board[i][j]
                        if num != ".":
                            if num in count:
                                return False
                            count.add(num)
        # checking rows and cols
        for row in range(9):
            row_count = set()
            col_count = set()
            for col in range(9):
                num1 = board[row][col]
                num2 = board[col][row]
                if num1 != ".":
                    if num1 in row_count:
                        return False
                    row_count.add(num1)
                if num2 != ".":
                    if num2 in col_count:
                        return False
                    col_count.add(num2)
        return True
        
        '''
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
        '''
        
