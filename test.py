import array
import json
import os
import sys
import time  # import time to calculate running time

from bubble import bubble_sort
from heap import heap_sort
from insertion import insertion_sort
from quick import quick_sort, quick_sort_pivot_median, quick_sort_pivot_rand
from rangen import rangen


def gen_nums(arr_sizes, repeat, dir):
    files = []
    for s in arr_sizes:
        for i in range(repeat):
            name = "nums_" + str(s) + "_" + str(i) + ".txt"
            rangen(s, dir + name)
            files.append(name)
    return files


def is_sorted(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True


class TestResult:
    def __init__(self, sorted=False, time=0.0):
        self.sorted = sorted
        self.time = time


def test_sorting_function(func, a: list):
    start = time.time()
    func(a)
    end = time.time()
    return TestResult(is_sorted(a), end-start)


kArrSizes = [1000, 10000, 20000]
kRepeat = 5
kTestLogDir = "test_log/"
kTestResultFile = "test_result.json"
kSortingFunctions = [
    bubble_sort,
    insertion_sort,
    heap_sort,
    quick_sort,
    quick_sort_pivot_rand,
    quick_sort_pivot_median,
]

# This is the function to verify your implemented sorting algorithm
# You need to change it a bit to call your sorting algorithm


def test():
    files = gen_nums(kArrSizes, 5, kTestLogDir)
    test_result = {}

    for file_name in files:
        header = file_name[:len(file_name)-len(".txt")]
        test_result[header] = []
        print("=================" + header + "=================")
        # read the content of nums.txt into an array
        nums_file = kTestLogDir + file_name
        nums = open(nums_file, 'r')
        a = []
        for line in nums:
            a.append(int(str.strip(line)))
        nums.close()

        for func in kSortingFunctions:
            name = func.__name__
            result = test_sorting_function(func, a.copy())
            print(name)
            print("- Sorted: " + str(result.sorted))
            print("- Time: " + str(result.time))
            r = vars(result)
            r["function"] = name
            test_result[header].append(r)

        print()

    with open(kTestLogDir + kTestResultFile, 'w') as f:
        json.dump(test_result, f, indent=2)


if __name__ == "__main__":
    test()
