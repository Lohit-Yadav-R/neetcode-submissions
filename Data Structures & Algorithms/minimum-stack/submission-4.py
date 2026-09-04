class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = float('Inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.minval = val
        self.stack.append(val - self.minval)
        if val < self.minval:
            self.minval = val

    def pop(self) -> None:
        poppedVal = self.stack.pop()
        if poppedVal < 0:
            self.minval += abs(poppedVal)

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.minval
        else:
            return self.stack[-1] + self.minval

    def getMin(self) -> int:
        return self.minval