class MinStack:
  _stack: [(int, int)]

  def __init__(self):
    self._stack = []

  def push(self, val: int) -> None:
    if not self._stack:
      self._stack.append((val, val))

    cur_min = self._stack[-1][1]
    self._stack.append((val, min(val, cur_min)))

  def pop(self) -> None:
    if len(self._stack) == 0:
      return
    self._stack.pop()
      
  def top(self) -> int:
    if len(self._stack) == 0:
      return None
    return self._stack[-1][0]

  def getMin(self) -> int:
    return self._stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()