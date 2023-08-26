from typing import TypeVar

T = TypeVar('T')

def select_o(A: list[T], p: int, r: int, ii: int, key=lambda a: a):
    if p == r:
        return A[p]
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
        mids.append(A[(i + j) // 2])
    x = select_o(mids, 0, len(mids) - 1, (len(mids) - 1) // 2, key)
    idx = A.index(x)
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
        return select_o(A, p, mid - 1, ii)
    elif k < ii:
        return select_o(A, mid + 1, r, ii - k - 1)
    else:
        return A[mid]

def mid_k(A: list[T], k: int, key=lambda a: a):
    if k > len(A):
        return A
    mid = select_o(A, 0, len(A) - 1, (len(A) - 1) // 2, key)
    diffs: dict[int, list[T]] = {}
    for i in range(len(A)):
        if diffs.get(abs(A[i] - mid)):
            diffs[abs(A[i] - mid)].append(A[i])
        else:
            diffs[abs(A[i] - mid)] = [A[i]]
    found = []
    i = 0
    ds = list(diffs.keys())
    while len(found) < k:
        found.extend(diffs[select_o(ds, 0, len(ds) - 1, i)])
        i += 1
    return found

A = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(A) + 1):
    print(i, mid_k(A, i))