def bucket_sort(arr: list[float]):
    buckets = [[] for _ in arr]
    for v in arr:
        idx = int(v * len(arr))
        inserted = False
        for j in range(len(buckets[idx])):
            if buckets[idx][j] >= v:
                buckets[idx].insert(j, v)
                inserted = True
                break
        if not inserted:
            buckets[idx].append(v)
    last_idx = 0
    for bucket in buckets:
        arr[last_idx:(last_idx + len(bucket))] = bucket[:]
        last_idx += len(bucket)

if __name__ == '__main__':
    import random
    a = []
    for i in range(10000):
        a.append(random.random())
    bucket_sort(a)
    for i in range(len(a) - 1):
        assert a[i] <= a[i + 1], (i, a[i], a[i + 1])
