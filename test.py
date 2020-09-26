from matplotlib import pyplot as plt
import time
from rangen import rangen
import sort
from heap import heap_sort
from insertion import insertion_sort
from quicksort import quicksortuser


def run_tests():
    running_time = {'insertion': 0., 'heap': 0., 'quick': 0.}

    input_sizes = [1000, 10000, 20000]
    sorts = [insertion_sort, heap_sort, quicksortuser]
    sort_names = ['insertion', 'heap', 'quick']

    insertion_time = []
    heap_time = []
    quick_time = []

    for n in input_sizes:
        trials = 5
        for i in range(trials):
            rangen(n)
            for sort, name in zip(sorts, sort_names):
                nums = open('nums.txt', 'r')
                a = []
                for line in nums:
                    a.append(int(str.strip(line)))
                start = time.time()
                sort(a)
                end = time.time()
                nums.close()
                running_time[name] += (end - start)
                assert is_sorted(a)
        running_time['insertion'] = running_time['insertion'] / trials
        running_time['heap'] = running_time['heap'] / trials
        running_time['quick'] = running_time['quick'] / trials
        print('Insertion Sort running time for n = ' + str(n) + ': ' + str(running_time['insertion']))
        print('Heap Sort running time for n = ' + str(n) + ': ' + str(running_time['heap']))
        print('Quick Sort running time for n = ' + str(n) + ': ' + str(running_time['quick']))
        insertion_time.append(running_time['insertion'])
        heap_time.append(running_time['heap'])
        quick_time.append(running_time['quick'])
        running_time = {'insertion': 0., 'heap': 0., 'quick': 0.}

    plt.plot(input_sizes, insertion_time, label='Insertion Sort')
    plt.plot(input_sizes, heap_time, label='Heap Sort')
    plt.plot(input_sizes, quick_time, label='Quick Sort')
    plt.legend()
    plt.show()


def is_sorted(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True


if __name__ == '__main__':
    run_tests()
