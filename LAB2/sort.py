import time
import matplotlib.pyplot as plt
import random
import sys

sys.setrecursionlimit(16000)


# TO DO : Cocktain Sort + add arrays to test, tables + plots

# QUICK sort with Lamuto partition

# partition function
def partition(array, low, high):
    # choose the pivot as last element
    pivot = array[high]

    # Index of smaller element and indicates
    # the right position of pivot found so far
    i = low - 1

    # move smaller elements to the left
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            swap(array, i, j)

    # move pivot after smaller elements and return its position
    swap(array, i + 1, high)
    return i + 1


# swap function
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


# The quick sort function implementation
def quickSort(array, low, high):
    if low < high:
        # pi is the index of the pivot after partition
        pi = partition(array, low, high)

        # recursion calls to sort rest of array
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


# MERGE sort
def merge(array, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # create temp arrays of size n1, n2
    L = [0] * n1
    R = [0] * n2

    # copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = array[left + i]
    for j in range(n2):
        R[j] = array[mid + 1 + j]

    i = 0  # initial index of L subarray
    j = 0  # initial index of R subarray
    k = left  # initial index of merged subarray

    # merge the temp arrays in ordered form back
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    # copy the remaining elements of L[] subarray
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    # copy the remaining elements of R[] subarray
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


# HEAP sort

# function to heapify a subtree rooted with node i
def heapify(arr, n, i):
    # initialize largest as root
    largest = i

    #  left index = 2*i + 1
    l = 2 * i + 1

    # right index = 2*i + 2
    r = 2 * i + 2

    # if left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # if largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # recursively heapify the affected sub-tree
        heapify(arr, n, largest)


# Main function to do heap sort
def heapSort(arr):
    n = len(arr)

    # build heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # one by one extract an element from heap
    for i in range(n - 1, 0, -1):
        # move root to end
        arr[0], arr[i] = arr[i], arr[0]

        # call max heapify on the reduced heap
        heapify(arr, i, 0)


# COCKTAIL sort
def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):

        # reset the swapped flag on entering the loop,because it might be true from a previous iteration.
        swapped = False

        # loop from left to right same as the bubble
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # if nothing moved, then array is sorted.
        if (swapped == False):
            break

        # otherwise, reset the swapped flag so that it can be used in the next stage
        swapped = False

        # move the end point back by one, because item at the end is in its rightful spot
        end = end - 1

        # from right to left, doing the same comparison as in the previous stage
        for i in range(end - 1, start - 1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # increase the starting point, because the next smallest number is now in its rightful spot.
        start = start + 1


