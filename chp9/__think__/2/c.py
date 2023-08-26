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


# 选出中位数
def select_mid(
        A: list[T],
        p: int,
        r: int,
        key: Callable[[T], Any] = lambda a: a
):
    return select_o(A, p, r, (r - p) // 2, key)


# 求带权中位数
def weighted_mid(
        A: list[T],
        weight: Callable[[T], float] = lambda a: a
):
    low = 0
    high = len(A) - 1
    tot = 0.0
    while high > low:
        mid, mid_val = select_mid(A, low, high, weight)
        t_tot = tot
        for i in range(low, mid):
            t_tot += weight(A[i])
            if t_tot >= 0.5:
                high = mid - 1
                break
        else:
            if weight(mid_val) + t_tot >= 0.5:
                return A[mid]
            tot = t_tot
            low = mid if low != mid else (mid + 1)
    else:
        return A[low]


if __name__ == '__main__':
    A = [0.1, 0.35, 0.05, 0.1, 0.15, 0.05, 0.2]
    print(weighted_mid(A), A)
    A = [1]
    print(weighted_mid(A), A)
    A = [0.2, 0.2, 0.2, 0.4]
    print(weighted_mid(A), A)
    A = [0.1, 0.3, 0.01, 0.09, 0.0, 0.0, 0.03, 0.07, 0.13, 0.02, 0.05, 0.2]
    print(weighted_mid(A), A)

__all__ = ('weighted_mid',)
