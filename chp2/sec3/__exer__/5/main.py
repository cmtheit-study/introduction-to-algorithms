import random

v = []
for i in range(10000):
    v.append(random.randint(-200, 200))

v.sort()


def find(vec: list, value):
    if not vec:
        raise ValueError("Input list is empty")
    low = 0
    high = len(vec) - 1
    while low <= high:
        mid = (low + high) >> 1
        if vec[mid] > value:
            high = mid - 1
        elif vec[mid] < value:
            low = mid + 1
        else:
            return mid
    raise ValueError("Cannot find")

not_passed = 0

for i in v:
    has_err = False
    value = i
    result = [0, 0]
    try:
        result[0] = find(v, value)
    except ValueError:
        has_err = True
    try:
        result[1] = v.index(value)
        if has_err:
            not_passed += 1
            print(f'{not_passed}: 测试未通过, value: {value}')
            continue
        if v[result[0]] != v[result[1]]:
            not_passed += 1
            print(f"{not_passed}: 查找结果不符合, find: {result[0]}, index: {result[1]}, value: {value}")
    except ValueError:
        if not has_err:
            not_passed += 1
            print(f'{not_passed}: 测试未通过')

if not_passed:
    print(f"测试未通过数量：{not_passed}")
else:
    print("恭喜测试全部通过")