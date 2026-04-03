class MinStack:

    def __init__(self):
        self.minArray = [float('inf')]
        self.stack = []

    def push(self, val: int) -> None:
        self.minArray.append(min(val, self.minArray[-1]))
        self.stack.append(val)
        return

    def pop(self) -> None:
        self.stack.pop()
        self.minArray.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minArray[-1]
