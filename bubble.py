# Bubble Sort
# This is the system's sorting algorithm that you use to compare with your result

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t


def bubble_sort(a):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                swap(a, i, i+1)
                sorted = False