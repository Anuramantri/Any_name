"""This python files defines functions for sorting using different standard techniques like heapsort and mergesort"""

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    l = mergesort(arr[:mid])
    r = mergesort(arr[mid:])
    
    merged = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            merged.append(l[i])
            i += 1
        else:
            merged.append(r[j])
            j += 1
    merged += l[i:]
    merged += r[j:]
    return merged

def heapsort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
