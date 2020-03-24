import unittest
from typing import List
import random


def merge_sort(inp: List[int]):
    """
    split the input (n elements) into 2 sub-arrays with n/2 elements
    sort these 2 sub-arrays recursively by merge_sort
    merge 2 sorted sub-arrays to produce the result
    :param inp:
    :return:
    """
    if len(inp) <= 1:
        return inp
    # split
    mid_index = len(inp) // 2
    # sort sub-lists
    left = inp[:mid_index]
    right = inp[mid_index:]
    print(f'left: {left}, right: {right}')
    left = merge_sort(inp[:mid_index])
    right = merge_sort(inp[mid_index:])

    # merge sorted sub-lists
    left_index = 0
    right_index = 0
    i = 0
    while i < len(inp):
        if left[left_index] >= right[right_index]:
            inp[i] = right[right_index]
            right_index += 1
        else:
            inp[i] = left[left_index]
            left_index += 1
        i += 1
        if left_index == len(left):
            inp[i:] = right[right_index:]
            break
        if right_index == len(right):
            inp[i:] = left[left_index:]
            break
    return inp


class MergeSortTest(unittest.TestCase):

    def test_case1(self):
        input = [1, 2, 3, 4, 5]
        self.assertEqual(input, merge_sort(input))

    def test_case2(self):
        input = [5, 4, 3, 2, 1]
        self.assertEqual([1, 2, 3, 4, 5], merge_sort(input))

    def test_cases(self):
        random.seed(42)
        for i in range(0, 50):
            inp = random.sample(range(0, 10), 10)
            print(f'input: {inp}')
            self.assertEqual([0,1,2,3,4,5,6,7,8,9], merge_sort(inp))


if __name__ == '__main__':
    unittest.main()
