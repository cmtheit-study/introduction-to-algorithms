# d 叉堆的实现

class Heap:
    def __init__(self, ary: int = 2):
        self.data = []
        self.ary = ary

    def max_heapify(self, idx: int):
        children_idx_start = idx * self.ary + 1
        children_idx_end = min(len(self.data), (idx + 1) * self.ary + 1)
        largest = idx
        for i in range(children_idx_start, children_idx_end):
            if self.data[i] > self.data[largest]:
                largest = i
        if largest != idx:
            self.data[largest], self.data[idx] = self.data[idx], self.data[largest]
            self.max_heapify(largest)

    def maximum(self):
        if self.data:
            return self.data[0]
        else:
            return None

    def extract_max(self):
        maximum = self.maximum()
        if maximum is not None:
            self.data[0], self.data[-1] = self.data[-1], self.data[0]
            self.data.pop()
            self.max_heapify(0)
        return maximum

    def insert(self, key):
        l = len(self.data)
        self.data.append(key)
        while l and self.data[(l - 1) // self.ary] < key:
            self.data[l] = self.data[(l - 1) // self.ary]
            l = (l - 1) // self.ary
        self.data[l] = key
        pass

    def check_if_heapified(self):
        for i in range(len(self.data) // self.ary + 1):
            children_idx_start = i * self.ary + 1
            children_idx_end = min(len(self.data), (i + 1) * self.ary + 1)
            for j in range(children_idx_start, children_idx_end):
                if self.data[j] > self.data[i]:
                    return False, i, j, self.data[i], self.data[j]
        return True


if __name__ == '__main__':
    h = Heap(5)
    data = [*range(1000)]
    for i in data:
        h.insert(i * i % 30)
    print(h.data)
    print(h.check_if_heapified())
    b = []
    while h.maximum() is not None:
        b.append(h.extract_max())
    print(b)
    for i in range(len(b) - 1):
        assert b[i + 1] <= b[i], i
