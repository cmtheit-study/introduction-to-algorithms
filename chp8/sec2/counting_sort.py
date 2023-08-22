def counting_sort(arr: list[int], k: int):
    c = [0 for i in range(k)]
    for i in arr:
        c[i] += 1
    for i in range(len(c) - 1):
        c[i + 1] += c[i]
    out = [0 for i in arr]
    for i in range(len(arr)):
        c[arr[i]] -= 1
        out[c[arr[i]]] = arr[i]
    return out

if __name__ == '__main__':
    import random
    a = []
    max_num = 100
    for i in range(10000):
        a.append(random.randint(0, max_num - 1))
    b = counting_sort(a, max_num)
    print(b)
    for i in range(len(b) - 1):
        assert b[i] <= b[i + 1]