import random
import unittest
import list_common_elements as common
from time import time


class CommonElementsCase(unittest.TestCase):
    def test_common(self):
        random.seed(30)
        l1 = [random.randrange(0, 100000) for _ in range(5000)]
        l2 = [random.randrange(0, 200000) for _ in range(10000)]
        t0 = time()
        common_l1_l2 = set()
        for x in l1:
            if x in l2:
                common_l1_l2.add(x)
        common_l1_l2 = list(common_l1_l2)
        print(sorted(common_l1_l2))
        t1 = time()
        print(sorted(common.common(l1, l2)))
        t2 = time()
        print("bf time", t1-t0)
        print("merge  time", t2-t1)
        self.assertEqual(sorted(common_l1_l2), sorted(common.common(l1, l2)))


if __name__ == '__main__':
    unittest.main()
