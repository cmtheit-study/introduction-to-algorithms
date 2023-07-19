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

def heap_sort(arr: list[int]):
    res = []

    for i in range(len(arr) // 2, 0, -1):
        max_heapify(arr, i - 1)

    for i in range(len(arr)):
        arr[0], arr[-1] = arr[-1], arr[0]
        res.insert(0, arr.pop())
        max_heapify(arr, 0)

    arr[:] = res[:]

if __name__ == '__main__':
    a = [3, 4, 1, 2, 3, 0, 43, 5]
    heap_sort(a)
    print(a)
