import os
import array
import sys

import time #import time to calculate running time
import insertion
import heap
import quicksort
import rangen

# Bubble Sort
# This is the system's sorting algorithm that you use to compare with your result

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t


def bubblesort(a):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                swap(a, i, i+1)
                sorted = False

def gen_nums(arr_sizes, repeat):
    files = [] 
    for s in arr_sizes:
        for i in range(repeat):
            name = "nums_" + str(s) + "_" + str(i) + ".txt"
            rangen.rangen(s, name)
            files.append(name)
    return files

kArrSizes = [50, 100, 1000, 10000, 20000]
kRepeat = 5

# This is the function to verify your implemented sorting algorithm
# You need to change it a bit to call your sorting algorithm
def test():
    files = gen_nums(kArrSizes, 5)
    
    for file_name in files:
        print("=================" + file_name + "=================")
        # read the content of nums.txt into an array
        nums = open(file_name, 'r')
        a = []
        for line in nums:
            a.append(int(str.strip(line)))
        nums.close()
        
        ref_name = "nums_ref_" + file_name[len("nums_"):]
        os.system("sort -n " + file_name + "> " + ref_name)

        sorting_functions = [
            ("bubble_sort", bubblesort), 
            ("insertion_sort", insertion.insertion_sort), 
            ("heap_sort", heap.heap_sort), 
            ("quick_sort", quicksort.quicksortuser),
            ]

        for func in sorting_functions: 
            a_copy = a.copy()
            # sort the array using bubblesort and calculate running time
            start=time.time()
            func[1](a_copy)# You need to change here to call your sorting algorithm
            end=time.time()
            print(func[0] + " running time:   ",end-start)
            
            output_file_name = "nums_" + func[0] + ".txt"
            # output nums_sorted.txt
            nums_sorted = open(output_file_name, 'w')
            for element in a_copy:
                nums_sorted.write(str(element) + "\n")
            nums_sorted.close()
            
            temp_file_name = "tmp_" + func[0] + ".txt"
            ret = os.system("diff " + output_file_name + " " + ref_name + " > " + temp_file_name)

            # output result
            if int(ret) == 0:
                print("Sorted!")

            if int(ret) != 0:
                print("Not sorted!")


# python sort.py runs test
if __name__ == "__main__":
    test()
