import random
import unittest

def bin_ins(vec: list):
    for i in range(1, len(vec)):
        low = 0
        high = i - 1
        while low < high:
            mid = (low + high) >> 1
            if vec[i] < vec[mid]:
                high = mid - 1
            elif vec[i] > vec[mid]:
                low = mid + 1
            else:
                low = mid
                break
        vec.insert(low if vec[low] > vec[i] else (low + 1), vec.pop(i))


class MyTestCase(unittest.TestCase):
    def test_algorithm(self):
        v = []
        for i in range(1000):
            v.append(random.randint(-200, 200))
        vcp = v[:]
        bin_ins(v)
        vcp.sort()
        for i in range(len(v)):
            self.assertEqual(v[i], vcp[i])


if __name__ == '__main__':
    for i in range(1000):
        unittest.main()
