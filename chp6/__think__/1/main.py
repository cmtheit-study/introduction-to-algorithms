class Heap:
    def __init__(self):
        self.data = []

    def max_heapify(self, idx: int):
        left = idx * 2 + 1
        right = left + 1
        largest = idx
        if left < len(self.data) and self.data[left] > self.data[largest]:
            largest = left
        if right < len(self.data) and self.data[right] > self.data[largest]:
            largest = right
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
        while l and self.data[l >> 1] < self.data[l]:
            self.data[l], self.data[l >> 1] = self.data[l >> 1], self.data[l]
            l >>= 1

def max_heapify(arr: list[int], idx: int):
    left = idx * 2 + 1
    right = left + 1
    largest = idx
    if left < len(arr) and arr[left] > arr[largest]:
        largest = left
    if right < len(arr) and arr[right] > arr[largest]:
        largest = right
    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        max_heapify(arr, largest)

def heap_make(arr: list[int]):
    for i in range(len(arr) >> 1, 0, -1):
        max_heapify(arr, i - 1)

if __name__ == '__main__':
    h = Heap()
    data = [*range(10)]
    for i in data:
        h.insert(i)
    print(h.data)
    mhd = data[:]
    heap_make(mhd)
    print(mhd)