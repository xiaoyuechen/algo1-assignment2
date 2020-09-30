def insertion_sort(a):
    n = len(a)
    for i in range(n):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            swap(a, j, j - 1)
            j = j - 1


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


if __name__ == "__main__":
    import algotest
    algotest.test(insertion_sort)
