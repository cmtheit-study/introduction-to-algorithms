def max_heapify(arr: list[int], idx: int):
    stack = [idx]
    while stack:
        idx = stack.pop()
        left = idx * 2 + 1
        right = left + 1
        largest = idx
        if left < len(arr) and arr[left] > arr[largest]:
            largest = left
        if right < len(arr) and arr[right] > arr[largest]:
            largest = right
        if largest != idx:
            arr[idx], arr[largest] = arr[largest], arr[idx]
            stack.append(largest)   # 自己实现一个调用栈

if __name__ == '__main__':
    a = [3, 4, 1, 2, 3, 0, 43, 5]
    for i in range(len(a) // 2, 0, -1):
        max_heapify(a, i - 1)
    print(a)
