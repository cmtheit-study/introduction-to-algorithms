from viodelta import ticket_delta

def div(vec, low, high):
    if low < high:
        mid = (low + high) >> 1
        left_max = div(vec, low, mid)
        right_max = div(vec, mid + 1, high)
        mid_left_max = None
        mid_left_sum = 0
        mid_right_max = None
        mid_right_sum = 0
        mid_tup = [0, 0, None]
        for l in range(mid, low - 1, -1):
            mid_left_sum += vec[l]
            if mid_left_max is None or mid_left_sum > mid_left_max:
                mid_left_max = mid_left_sum
                mid_tup[0] = l
        for r in range(mid + 1, high + 1):
            mid_right_sum += vec[r]
            if mid_right_max is None or mid_right_sum > mid_right_max:
                mid_right_max = mid_right_sum
                mid_tup[1] = r
        mid_sum = mid_right_max + mid_left_max
        mid_tup[2] = mid_sum
        if left_max[2] is not None and left_max[2] > mid_tup[2]:
            mid_tup = left_max
        if right_max[2] is not None and right_max[2] > mid_tup[2]:
            mid_tup = right_max
        return tuple(mid_tup)
    elif low == high:
        return (low, high, vec[low])
    else:
        return (low, high, None)

if __name__ == '__main__':
    delta = ticket_delta.deltas
    res = div(delta, 0, len(delta) - 1)
    ticket_delta.set_in_out_delta(res[0], res[1])
    ticket_delta.report()