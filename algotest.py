import os
import sys

import time  # import time to calculate running time


def test(func):
    # check if nums.txt exists
    if not os.path.exists('nums.txt'):
        print("First create nums.txt")
        sys.exit(0)

    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # sort the array using bubblesort and calculate running time
    start=time.time()
    func(a)# You need to change here to call your sorting algorithm
    end=time.time()
    print(func.__name__, " running time:   ", end-start)
    nums.close()
    
    # output nums_sorted.txt
    nums_sorted = open('nums_sorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()

    # compare your result (nums_sorted.txt) against the result of bubblesorting algorithm (nums_ref.txt)
    os.system('sort -n nums.txt > nums_ref.txt')
    ret = os.system('diff nums_sorted.txt nums_ref.txt > tmp.txt')

    # output result
    if int(ret) == 0:
        print("Sorted!")

    if int(ret) != 0:
        print("Not sorted!")
