import random

v = []
for i in range(100):
    v.append(random.randint(-200, 200))

def merge(v: list, a, b):
    for i in range(a, b):
        if v[i] >= v[b]:
            v.insert(i, v.pop(b))
            break

def merge2(v: list, a, b):
    if a == b - 1:
        if v[a] > v[b]:
            v[b], v[a] = v[a], v[b]
        return
    low = a
    high = b - 1
    # 初始化：v[low..high] 之间有序，v[b] 应插入 v[low..high] 的某处，low <= high < b
    while low < high:
        mid = (low + high) >> 1
        if v[b] < v[mid]:
            high = mid - 1
        elif v[b] > v[mid]:
            low = mid + 1
        else:
            low = mid
            break
        # 保持：v[low..high] 之间有序，v[b] 应插入 v[low..high] 的某处，low <= high < b
    # 终止：low == high， v[b] 插入位置为 v[low] 位置
    v.insert(low if v[low] > v[b] else (low + 1), v.pop(b))

def sort(v, a, b):
    if a < b - 1:
        sort(v, a, b - 1)
        merge2(v, a, b - 1)

def is_ordered(v: list):
    for i in range(len(v) - 1):
        if v[i] > v[i + 1]:
            return False
    return True

sort(v, 0, len(v))
print(v)
print(is_ordered(v))