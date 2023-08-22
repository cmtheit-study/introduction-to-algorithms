# 可以扩展到任意的范围

def counting_sort(arr: list[int], a: int, b: int):
    c = [0 for i in range(a, b + 1)]
    for i in arr:
        c[i - a] += 1
    for i in range(len(c) - 1):
        c[i + 1] += c[i]
    out = [0 for i in arr]
    for i in range(len(arr)):
        c[arr[i] - a] -= 1
        out[c[arr[i] - a]] = arr[i]
    return out

if __name__ == '__main__':
    import random
    a = []
    max_num = 100
    for i in range(10000):
        a.append(random.randint(3, max_num - 1))
    b = counting_sort(a, 3, max_num)
    print(b)
    for i in range(len(b) - 1):
        assert b[i] <= b[i + 1]