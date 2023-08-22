def variable_digits_sort(arr: list[(int, int)]):
    dmin = min(arr, key=lambda v: v[1])[1]
    dmax = max(arr, key=lambda v: v[1])[1]
    ds   = [0 for i in range(dmin, dmax + 1)]
    out = [() for _ in arr]
    for i in arr:
        ds[i[1] - dmin] += 1
    for i in range(len(ds) - 1):
        ds[i + 1] += ds[i]
    ds_bp = ds[:]
    for i in range(len(arr) - 1, -1, -1):
        value, dig = arr[i]
        ds[dig - dmin] -= 1
        out[ds[dig - dmin]] = arr[i]
    # 计数排序完成

    ds = ds_bp
    for d in range(len(ds)):
        dig = d + dmin
        start = 0 if not d else ds[d - 1]
        stop  = ds[d]
        for m in range(dig):
            ms = [0, 0]
            buf = [() for i in range(start, stop)]
            for num in range(start, stop):
                value, _ = out[num]
                if value & (1 << m):
                    ms[1] += 1
                else:
                    ms[0] += 1
            ms[1] += ms[0]
            for num in range(stop - 1, start - 1, -1):
                value, _ = out[num]
                if value & (1 << m):
                    ms[1] -= 1
                    buf[ms[1]] = out[num]
                else:
                    ms[0] -= 1
                    buf[ms[0]] = out[num]
            out[start:stop] = buf[:]
    arr[:] = out[:]

if __name__ == '__main__':
    import random, math
    a = []
    for i in range(10000):
        value = random.randint(10, 1314000)
        a.append((value, int(math.log2(value)) + 1))
    variable_digits_sort(a)
    for i in range(len(a) - 1):
        assert a[i + 1][0] >= a[i][0]