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

def min_heapify(arr: list[int], idx: int):
    left = idx * 2 + 1
    right = left + 1
    smallest = idx
    if left < len(arr) and arr[left] < arr[smallest]:
        smallest = left
    if right < len(arr) and arr[right] < arr[smallest]:
        smallest = right
    if smallest != idx:
        arr[idx], arr[smallest] = arr[smallest], arr[idx]
        min_heapify(arr, smallest)

if __name__ == '__main__':
    a = [3, 4, 1, 2, 3, 0, 43, 5]
    for i in range(len(a) // 2, 0, -1):
        max_heapify(a, i - 1)
    print(a)
    for i in range(len(a) // 2, 0, -1):
        min_heapify(a, i - 1)
    print(a)
