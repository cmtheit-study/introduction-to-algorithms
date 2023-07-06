a = [1, 3, 8, 0, 32, 123]

def search(vec, key):
    # 初始化：搜索过的子数组为空，不包含 key
    for i in range(len(vec)):
        if vec[i] == key:
            return True
        # 保持：搜索过的子数组仍然不包含 key
    # 终止：整个数组不包含 key
    return False

print(search(a, 10), search(a, 8))