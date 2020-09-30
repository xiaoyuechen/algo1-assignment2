import random


def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t


def pivot_last(a: list, p, r):
    return


def pivot_rand(a: list, p, r):
    idx = random.randrange(p, r+1)
    swap(a, idx, r)


def pivot_median(a: list, p, r):
    if r - p > 1:
        m = (p+r)//2
        if a[m] <= a[p] < a[r] or a[r] < a[p] <= a[m]:
            swap(a, p, r)
        elif a[p] <= a[m] < a[r] or a[r] < a[m] <= a[p]:
            swap(a, m, r)


def partition(a: list, p, r, pivot_func):
    pivot_func(a, p, r)
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            swap(a, i, j)
    swap(a, i+1, r)
    return i+1


def quick_sort_impl(a: list, p, r, pivot_func):
    if p < r:
        q = partition(a, p, r, pivot_func)
        quick_sort_impl(a, p, q-1, pivot_func)
        quick_sort_impl(a, q+1, r, pivot_func)


def quick_sort(a: list):
    quick_sort_impl(a, 0, len(a)-1, pivot_last)


def quick_sort_pivot_rand(a: list):
    quick_sort_impl(a, 0, len(a)-1, pivot_rand)


def quick_sort_pivot_median(a: list):
    quick_sort_impl(a, 0, len(a)-1, pivot_median)


if __name__ == "__main__":
    import algotest
    algotest.test(quick_sort)
