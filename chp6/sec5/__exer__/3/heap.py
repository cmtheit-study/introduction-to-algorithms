class Heap:
    def __init__(self):
        self.data = []

    def min_heapify(self, idx: int):
        left = idx * 2 + 1
        right = left + 1
        largest = idx
        if left < len(self.data) and self.data[left] < self.data[largest]:
            largest = left
        if right < len(self.data) and self.data[right] < self.data[largest]:
            largest = right
        if largest != idx:
            self.data[largest], self.data[idx] = self.data[idx], self.data[largest]
            self.min_heapify(largest)

    def minimum(self):
        if self.data:
            return self.data[0]
        else:
            return None

    def extract_min(self):
        minimum = self.minimum()
        if minimum is not None:
            self.data[0], self.data[-1] = self.data[-1], self.data[0]
            self.data.pop()
            self.min_heapify(0)
        return minimum

    # for exercise 5
    def insert(self, key):
        l = len(self.data)
        self.data.append(key)
        while l and self.data[((l + 1) >> 1) - 1] > key:
            self.data[l] = self.data[((l + 1) >> 1) - 1]
            l = ((l + 1) >> 1) - 1
        self.data[l] = key

if __name__ == '__main__':
    h = Heap()
    mm = 100
    for i in range(mm):
        h.insert(i ** i % 301)
    print(h.data)
    m = []
    while h.minimum() is not None:
        m.append(h.extract_min())
    print(m)
    for i in range(mm - 1):
        assert m[i + 1] >= m[i], i