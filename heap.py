def heap_sort(a):
    n = len(a)
    build_max_heap(a, n)
    while n > 1:
        swap(a, 1, n)
        n = n - 1
        max_heapify(a, 1, n)
    a.pop(0)  # remove dummy element


def max_heapify(a, k, n):
    while k * 2 <= n:
        j = k * 2
        if j < n and a[j] < a[j + 1]:
            j = j + 1
        if a[j] < a[k]:
            break
        swap(a, k, j)
        k = j
    return


def build_max_heap(a, n):
    # add dummy element to the beginning to make array indexing easier
    a.insert(0, 0)
    # now indices of Nth node's children are 2*N and 2*N+1
    for k in range(n // 2, 0, -1):
        max_heapify(a, k, n)


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def is_sorted(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True
