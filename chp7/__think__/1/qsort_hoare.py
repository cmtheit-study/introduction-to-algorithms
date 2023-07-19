def qsort_inner(arr: list[int], begin: int, end: int):
    if end > begin:
        left = begin
        right = end - 1
        pe    = arr[end]
        while True:
            while arr[left] < pe:
                left += 1
            while arr[right] >= pe:
                right -= 1
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
            else:
                break
        arr[left], arr[end] = arr[end], arr[left]
        qsort_inner(arr, begin, left - 1)
        qsort_inner(arr, left + 1, end)

def qsort(arr: list[int]):
    qsort_inner(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    import random
    a = []
    for i in range(10000):
        a.append(random.randint(i, i * i))
    qsort(a)
    for i in range(len(a) - 1):
        assert a[i] <= a[i + 1]