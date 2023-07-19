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

def heap_make(arr):
    for i in range(len(arr) >> 1, 0, -1):
        max_heapify(arr, i - 1)

def merge_list(l: list[list[int]], a: int, b: int):
    if b - a > 1:
        mid = (a + b) >> 1
        l0 = merge_list(l, a, mid)
        l0.extend(merge_list(l, mid + 1, b))
        heap_make(l0)
        return l0
    elif b - a == 1:
        l0 = l[a][:]
        l0.extend(l[b])
        heap_make(l0)
        return l0
    else:
        return l[a][:]

if __name__ == '__main__':
    vec = [[10, 9, 3, 1], [100, 10, 3], [3, 2, 1], [33, 32, 2], [1], [], [100, 99, 88, 77]]
    print(merge_list(vec, 0, len(vec) - 1))
    # 没有卵用
