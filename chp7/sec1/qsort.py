def qsort_inner(arr: list[int], begin: int, end: int):
    if end > begin:
        pap = arr[end]
        little_bound = begin - 1
        for i in range(begin, end):
            if arr[i] <= pap:
                little_bound += 1
                arr[little_bound], arr[i] = arr[i], arr[little_bound]
        arr[little_bound + 1], arr[end] = arr[end], arr[little_bound + 1]
        qsort_inner(arr, begin, little_bound)
        qsort_inner(arr, little_bound + 2, end)

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