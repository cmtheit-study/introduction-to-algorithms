from typing import TypeVar, Callable, Any

T = TypeVar('T')

# 顺序统计量，可以有重复元素，返回下标和值
def select_o(
        A: list[T],
        p: int,
        r: int,
        ii: int,
        key: Callable[[T], Any] = lambda a: a
) -> tuple[int, T]:
    if p == r:
        return p, A[p]
    step = 5
    mids = []
    # 对于每 5 个元素的分组
    for i in range(p, r + 1, step):
        j = min(r, i + step - 1)
        for k in range(i + 1, j + 1):
            v = A[k]
            for m in range(k, i, -1):
                if key(A[m - 1]) <= key(v):
                    A[m] = v
                    break
                else:
                    A[m - 1], A[m] = A[m], A[m - 1]
            else:
                A[i] = v
        mids.append(((i + j) // 2, A[(i + j) // 2]))
    _, (idx, x) = select_o(mids, 0, len(mids) - 1, (len(mids) - 1) // 2, lambda a: key(a[1]))
    A[idx], A[r] = A[r], A[idx]
    low = p - 1
    for j in range(p, r):
        if key(A[j]) < key(A[r]):
            low += 1
            A[low], A[j] = A[j], A[low]
    mid = low + 1
    A[mid], A[r] = A[r], A[mid]
    k = mid - p
    if k > ii:
        return select_o(A, p, mid - 1, ii, key)
    elif k < ii:
        return select_o(A, mid + 1, r, ii - k - 1, key)
    else:
        return mid, A[mid]



if __name__ == '__main__':
    import random
    for i in range(100):
        A = []
        for j in range(1000):
            A.append(random.randint(10, 10000))
        ii = random.randint(0, len(A) - 1)
        idx, j = select_o(A, 0, len(A) - 1, ii)
        A.sort()
        assert A[ii] == j
