def radix_sort(arr: list[int], dig: int = 32):
    for i in range(dig):
        res = [0 for _ in arr]
        c = [0, 0]
        for v in arr:
            if v & (1 << i):
                c[1] += 1
            else:
                c[0] += 1
        c[1] += c[0]
        for j in range(len(arr) - 1, -1, -1):
            if arr[j] & (1 << i):
                c[1] -= 1
                res[c[1]] = arr[j]
            else:
                c[0] -= 1
                res[c[0]] = arr[j]
        arr[:] = res[:]

if __name__ == '__main__':
    import random
    a = []
    for i in range(1000):
        a.append(random.randint(0, 100000))
    radix_sort(a)
    for i in range(len(a) - 1):
        assert a[i] <= a[i + 1]