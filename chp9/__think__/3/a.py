from typing import TypeVar, Callable, Any

T = TypeVar('T')

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

# 精简优化版本
def select_i(
        A: list[T],
        ii: int,
        key: Callable[[T], Any] = lambda a: a
) -> tuple[int, T]:
    if ii < (len(A) - 1) // 2:
        big = []
        for i in range(0, len(A) - 1, 2):
            more = i if key(A[i]) > key(A[i + 1]) else (i + 1)
            big.append((more, A[more]))
        # 找到较大元素组中第 i 大的
        _, (idx, res) = select_i(big, ii, lambda p: key(p[1]))
        # 将所有 2i 小的放在左边
        A[-1], A[idx] = A[idx], A[-1]
        p = -1
        for j in range(0, len(A) - 1):
            if key(A[j]) < key(res):
                p += 1
                A[p], A[j] = A[j], A[p]
        mid = p + 1
        A[mid], A[-1] = A[-1], A[mid]
        return select_o(A, 0, mid, ii, key)
    else:
        return select_o(A, 0, len(A) - 1, ii, key)

if __name__ == '__main__':
    import random
    for i in range(1000):
        A = []
        for j in range(i + 1):
            A.append(random.randint(10, 10000))
        ii = random.randint(0, len(A) - 1)
        idx, j = select_i(A, ii)
        A.sort()
        assert A[ii] == j