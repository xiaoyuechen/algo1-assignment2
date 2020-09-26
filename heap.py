def heap_sort(a):
    n = len(a)
    build_max_heap(a, n)
    while n > 1:
        swap(a, 1, n)
        n = n - 1
        max_heapify(a, 1, n)


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
    a.insert(0, 0)
    for k in range(n // 2, 0, -1):
        max_heapify(a, k, n)


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]
