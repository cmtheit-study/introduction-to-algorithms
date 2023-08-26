def select_o(A: list[int], p: int, r: int, ii: int):
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
                if A[m - 1] <= v:
                    A[m] = v
                    break
                else:
                    A[m - 1], A[m] = A[m], A[m - 1]
            else:
                A[i] = v
        mids.append(A[(i + j) // 2])
    x = select_o(mids, 0, len(mids) - 1, (len(mids) - 1) // 2)
    idx = A.index(x)
    A[idx], A[r] = A[r], A[idx]
    low = p - 1
    for j in range(p, r):
        if A[j] < A[r]:
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

def select_mid(A: list[int], p: int, r: int):
    return select_o(A, p, r, (r - p) // 2)

def select_o2(A: list[int], p: int, r: int, ii: int):
    if p == r:
        return A[p]
    mid_order = (r - p) // 2
    mid_idx = p + mid_order
    mid = select_mid(A, p, r)
    if mid_order > ii:
        return select_o2(A, p, mid_idx - 1, ii)
    elif mid_order < ii:
        return select_o2(A, mid_idx + 1, r, ii - mid_order - 1)
    else:
        return mid

if __name__ == '__main__':
    from random import randint
    for i in range(100):
        A = set()
        for j in range(randint(10, 200)):
            A.add(randint(-23, 30000))
        A = list(A)
        ii = randint(0, len(A) - 1)
        o = select_o(A, 0, len(A) - 1, ii)
        o2 = select_o2(A, 0, len(A) - 1, ii)
        assert o == o2, (o, o2)