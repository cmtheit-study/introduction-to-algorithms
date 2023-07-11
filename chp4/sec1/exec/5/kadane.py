import random

def kadane(vec: list):
    current_sum = 0
    max_sum = float('-inf')
    for num in vec:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum

def div(vec: list, low, high):
    if low < high:
        mid = (low + high) >> 1
        left_res = div(vec, low, mid)
        right_res = div(vec, mid + 1, high)
        mid_left_sum = 0
        mid_left_max = None
        mid_right_sum = 0
        mid_right_max = None
        mid_res = [0, 0, None]
        for l in range(mid, low - 1, -1):
            mid_left_sum += vec[l]
            if mid_left_max is None or mid_left_max < mid_left_sum:
                mid_left_max = mid_left_sum
                mid_res[0] = l
        for r in range(mid + 1, high + 1):
            mid_right_sum += vec[r]
            if mid_right_max is None or mid_right_max < mid_right_sum:
                mid_right_max = mid_right_sum
                mid_res[1] = r
        mid_res[2] = mid_right_max + mid_left_max
        if left_res is not None and left_res[2] > mid_res[2]:
            mid_res = left_res
        if right_res is not None and right_res[2] > mid_res[2]:
            mid_res = right_res
        return mid_res
    elif low == high:
        return [low, high, vec[low]]
    else:
        return None

if __name__ == '__main__':
    for i in range(1000):
        data = []
        for j in range(200):
            data.append(random.randint(-256, 256))
        assert kadane(data) == div(data, 0, len(data) - 1)[-1]