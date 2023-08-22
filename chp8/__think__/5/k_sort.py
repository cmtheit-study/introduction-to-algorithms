# 内部递归调用的函数
def k_sort_i_inner(arr: list[int], k: int, begin: int, end: int):
    if end > begin:
        i = begin - k
        pel = arr[end]
        for j in range(begin, end, k):
            if arr[j] <= pel:
                i += k
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + k], arr[end] = arr[end], arr[i + k]
        k_sort_i_inner(arr, k, begin, i)
        k_sort_i_inner(arr, k, i + 2 * k, end)

# 对从 i 开始，间隔为 k 的子数组排序
def k_sort_i(arr: list[int], i: int, k: int):
    k_sort_i_inner(arr, i, i + (len(arr) - i - 1) // k * k, k)

def k_sort(arr: list[int], k: int):
    if len(arr) > k:
        for i in range(k):
            k_sort_i(arr, i, k)

if __name__ == '__main__':
    import random
    a = []
    for i in range(15):
        a.append(i * i % 32)
    k_sort(a, 3)
    print(a)