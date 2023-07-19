class Young:
    def __init__(self, m: int, n: int):
        self.data = [[None for i in range(n)] for i in range(m)]
        self.last = None

    @property
    def row(self):
        return len(self.data)

    @property
    def col(self):
        return len(self.data[0]) if self.data else 0

    @property
    def next(self):
        if not self.last:
            return 0, 0
        if (self.last[0] + 1) * (self.last[1] + 1) == self.row * self.col:
            return None
        s = sum(self.last)
        next = self.last[0] - 1, self.last[1] + 1
        if next[0] < 0 or next[1] >= self.col:
            next = self.row - 1, s + 1 - (self.row - 1)
            if next[1] < 0:
                next = s + 1 - 0, 0
        return next

    @property
    def prev(self):
        if not self.last:
            return None
        s = sum(self.last)
        if not s:
            return None
        prev = self.last[0] + 1, self.last[1] - 1
        if prev[0] >= self.row or prev[1] < 0:
            prev = 0, s - 1 - 0
            if prev[1] >= self.col:
                prev = s - 1 - (self.col - 1), self.col - 1

        return prev

    def extract_min(self):
        if self.last:
            res = self.data[0][0]
            self.data[0][0], self.data[self.last[0]][self.last[1]] = self.data[self.last[0]][self.last[1]], None
            self.last = self.prev
            self.min_heapify(0, 0)
            return res
        return None

    def insert(self, key):
        if self.last:
            if nx := self.next:
                self.last = self.next
                pos = nx
                while True:
                    last_pos = pos[:]
                    largest = key
                    if pos[0] > 0 and self.data[last_pos[0] - 1][last_pos[1]] > largest:  # 上面的节点
                        pos = last_pos[0] - 1, last_pos[1]
                        largest = self.data[pos[0]][pos[1]]
                    if pos[1] > 0 and self.data[last_pos[0]][last_pos[1] - 1] > largest:  # 左边的节点
                        pos = last_pos[0], last_pos[1] - 1
                        largest = self.data[pos[0]][pos[1]]
                    if largest != key:
                        self.data[last_pos[0]][last_pos[1]] = self.data[pos[0]][pos[1]]
                    else:
                        break
                self.data[pos[0]][pos[1]] = key
        else:
            self.last = (0, 0)
            self.data[self.last[0]][self.last[1]] = key

    def min_heapify(self, row: int, col: int):
        if row < self.row and col < self.col and self.data[row][col] is not None:
            smallest = (row, col)
            if row < self.row - 1 and self.data[row + 1][col] is not None and self.data[smallest[0]][smallest[1]] > self.data[row + 1][col]:
                smallest = (row + 1, col)
            if col < self.col - 1 and self.data[row][col + 1] is not None and self.data[smallest[0]][smallest[1]] > self.data[row][col + 1]:
                smallest = (row, col + 1)
            if smallest != (row, col):
                self.data[row][col], self.data[smallest[0]][smallest[1]] = self.data[smallest[0]][smallest[1]], self.data[row][col]
                self.min_heapify(*smallest)

    def is_well_formed(self):
        for row in range(self.row):
            for col in range(self.col):
                if self.data[row][col] is not None:
                    if row > 0 and (self.data[row - 1][col] is None or self.data[row - 1][col] > self.data[row][col]):
                        return False
                    if col > 0 and (self.data[row][col - 1] is None or self.data[row][col - 1] > self.data[row][col]):
                        return False
        return True

    def __str__(self):
        s = ""
        mw = 0
        for row in self.data:
            for d in row:
                mw = max(mw, len(f'{d if d is not None else "Inf"}'))
        for row in self.data:
            for d in row:
                s += f"{{:^{mw}}} ".format(d if d is not None else "Inf")
            s += "\n"
        return s

if __name__ == '__main__':
    y = Young(40, 50)
    y.insert(10)
    y.insert(20)
    for i in range(1000):
        y.insert(i * i % 2048)
    print(y)
    m = []
    while True:
        p = y.extract_min()
        assert y.is_well_formed(), print(y)
        if p is None:
            break
        m.append(p)
    for i in range(len(m) - 1):
        assert m[i] <= m[i + 1], (i, )
    print(y)
    print(y.last)