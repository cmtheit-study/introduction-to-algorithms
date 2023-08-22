def bucket_sort(arr: list[(float, float)]):
    buckets = [[] for _ in arr]
    for x, y in arr:
        v = x ** 2 + y ** 2
        idx = int(v * len(arr))
        inserted = False
        for j in range(len(buckets[idx])):
            if buckets[idx][j][0] ** 2 + buckets[idx][j][1] ** 2 >= v:
                buckets[idx].insert(j, (x, y))
                inserted = True
                break
        if not inserted:
            buckets[idx].append((x, y))
    last_idx = 0
    for bucket in buckets:
        arr[last_idx:(last_idx + len(bucket))] = bucket[:]
        last_idx += len(bucket)

if __name__ == '__main__':
    import random
    a = []
    for i in range(10000):
        x = random.random()
        y = ((random.random() * (1 - x) + x) ** 2 - x ** 2) ** 0.5
        a.append((x, y))
    bucket_sort(a)
    for i in range(len(a) - 1):
        assert a[i][0] ** 2 + a[i][1] ** 2 <= a[i + 1][0] ** 2 + a[i + 1][1] ** 2, (i, a[i], a[i + 1])
