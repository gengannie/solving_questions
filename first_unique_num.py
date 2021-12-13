from collections import OrderedDict
class FirstUnique:

    def __init__(self, nums: List[int]):
        self._queue = OrderedDict()
        self.is_unique = {}
        for num in nums:
            self.add(num)
        

    def showFirstUnique(self) -> int:
        if self._queue:
            return next(iter(self._queue))
        return -1
        

    def add(self, value: int) -> None:
        # add number to queue, mark it as unique
        if value not in self.is_unique:
            self.is_unique[value] = True
            self._queue[value] = None
        # mark value as no longer unique, remove from queue
        elif self.is_unique[value]:
            self.is_unique[value] = False
            self._queue.pop(value)