import random
import unittest

class CombNotFoundException(Exception):
    pass

def find_two(vec: list, tot):
    vec.sort()                      # n * lg(n)
    high = len(vec) - 1
    for i in range(len(vec)):       # n * lg(n)
        low = i + 1
        if high < low:
            break
        target = tot - vec[i]
        while low <= high:
            mid = (low + high) >> 1
            if target < vec[mid]:
                high = mid - 1
            elif target > vec[mid]:
                low = mid + 1
            else:
                return (i, mid)
    raise CombNotFoundException("Cannot find.")


class MyTestCase(unittest.TestCase):
    def test_algorithm(self):
        for i in range(10000):
            vec = []
            found = False
            for _ in range(100):
                vec.append(random.randint(-200, 200))
            tot = random.randint(-400, 400)
            try:
                first, second = find_two(vec, tot)
                self.assertEqual(vec[first] + vec[second], tot)
                found = True
            except CombNotFoundException:
                for value in vec:
                    with self.assertRaises(ValueError):
                        if vec[vec.index(tot - value)] == value:
                            raise ValueError()
            print(i, "passed. found: ", found)


if __name__ == '__main__':
    unittest.main()
