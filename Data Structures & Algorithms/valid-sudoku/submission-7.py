class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c]) - 1
                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & boxes[(r // 3) * 3 + (c // 3)]:
                    return False
                
                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                boxes[(r // 3) * 3 + (c // 3)] |= (1 << val)
        return True

        
        '''
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                box_index = (r // 3) * 3 + (c // 3)

                if (val == '.'):
                    continue
                
                if (val in rows[r] or
                    val in cols[c] or
                    val in boxes[box_index]):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
        return True
        '''
        '''
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                val = int(board[r][c]) - 1
                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
                    return False

                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[(r // 3) * 3 + (c // 3)] |= (1 << val)

        return True
        '''
        '''
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    if (val in rows[r] or val in cols[c] 
                        or val in squares[(r // 3, c // 3)]):
                        return False
                    rows[r].add(val)
                    cols[c].add(val)
                    squares[(r // 3, c // 3)].add(val)
        return True
        '''
        '''
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
        
