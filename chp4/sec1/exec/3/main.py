import random
import threading
import time
import numpy as np

def test(repeat):
    data = []
    for i in range(random.randint(10, 200)):
        data.append(random.randint(-256, 256))
    res = {}
    begin = time.time()
    for i in range(repeat):
        vio(data)
    res['vio'] = time.time() - begin
    begin = time.time()
    for i in range(repeat):
        div(data, 0, len(data) - 1)
    res['div'] = time.time() - begin
    return res

def vio(vec: list):
    max_tup = [0, 0, None]
    for i in range(len(vec)):
        sum = 0
        for j in range(i, len(vec)):
            sum += vec[j]
            if max_tup[-1] is None or max_tup[-1] < sum:
                max_tup[0], max_tup[1], max_tup[2] = i, j, sum
    return max_tup

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

def one_test(dic: {'vio': list, 'div': list}, dic_lock: threading.Lock, repeat):
    res = test(repeat)
    dic_lock.acquire(True)
    dic['vio'].append(res['vio'])
    dic['div'].append(res['div'])
    dic_lock.release()

if __name__ == '__main__':
    for i in range(1000):
        res = {
            'vio': [],
            'div': []
        }
        lock = threading.Lock()
        repeat = 10
        threading.Thread(target=one_test, args=[res, lock, repeat]).start()