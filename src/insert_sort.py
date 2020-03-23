import unittest
from typing import List
import random

def insert_sort(inp: List[int]):
    """
    pick the first element
    with remain elements, do:
    - pick next element as current element
    - compare it with sorted elements, from biggest to smallest.
    - if current element is greater than a sorted element, we shift the sorted element to the right.
      to reserve a space for new element
    - if current element is smaller than a sorted element, then we insert current element right before the sorted element
    :param inp:
    :return:
    """
    # pick the first element
    # with remain elements, do
    for k in range(1, len(inp)):
        " Pick next element"
        key = inp[k]
        " compare with sorted elements, from biggest to smallest"
        ck = k - 1
        " if current element is smaller than a sorted element"
        while ck >= 0 and inp[ck] > key:
            " shift the sorted element to the right. To reserve a space"
            inp[ck+1] = inp[ck]
            ck = ck - 1
        " if current element is greater than a sorted element, or compared to all sorted element"
        " insert the current element to the space"
        inp[ck + 1] = key
    return inp


class InsertSortTest(unittest.TestCase):

    def test_case1(self):
        input = [1, 2, 3, 4, 5]
        self.assertEqual(input, insert_sort(input))

    def test_case2(self):
        input = [5, 4, 3, 2, 1]
        self.assertEqual([1, 2, 3, 4, 5], insert_sort(input))

    def test_cases(self):
        random.seed(42)
        for i in range(0, 50):
            inp = random.sample(range(0, 10), 10)
            print(f'input: {inp}')
            self.assertEqual([0,1,2,3,4,5,6,7,8,9], insert_sort(inp))

if __name__ == '__main__':
    unittest.main()
