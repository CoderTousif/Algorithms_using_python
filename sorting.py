import random
cal = 0


def bubbleSort(arr):
    length = len(arr) - 1
    for j in range(length, 0, -1):
        for i in range(j):
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
                global cal
                cal += 1

    return arr, cal


def selectionSort(arr):
    arrLength = len(arr)
    for i in range(arrLength):
        minIdx = i
        for j in range(i+1, arrLength):
            if arr[j] < arr[minIdx]:
                minIdx = j
                global cal
                cal += 1

        arr[i], arr[minIdx] = arr[minIdx], arr[i]

    return arr, cal


def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            global cal
            cal += 1
        arr[j + 1] = key

    return arr


def mergeSort(arr):
    global cal
    cal += 1
    length = len(arr)
    if length == 1:
        return arr
    mid = length // 2
    left = arr[:mid]  # left array
    right = arr[mid:]  # right array
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    # global cal
    # cal += 1
    result = []
    i = j = 0
    leftLength = len(left)
    rightLength = len(right)
    # Copy data to result arrays left[] and right[]
    while i < leftLength and j < rightLength:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # If anything left in the array then copy rest of them
    if i < leftLength:
        result.extend(left[i:])
    if j < rightLength:
        result.extend(right[j:])

    return result


# Quick sort
def quickSort(arr, start, end):
    global cal
    cal += 1
    if start < end:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, start, end)
        # Separately sort elements before partition and after partition
        quickSort(arr, start, pi - 1)
        quickSort(arr, pi + 1, end)

    return arr


def partition(arr, start, end):
    # i = (start - 1)  # index of smaller element
    i = start  # index of smaller element
    pivot = arr[end]  # pivot
    # loop from arr[start] to arr[end-1]
    for j in range(start, end):
        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            # swapping i and j
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    # placing pivot at correct position by swapping
    # arr[i + 1], arr[end] = arr[end], arr[i + 1]
    arr[i], arr[end] = arr[end], arr[i]
    # returns index of pivot
    return i


# driver code to test the above code
if __name__ == '__main__':

    randomArray = [32, 37, 40, 83, 1, 8, 50, 7, 26, 34, 44, 13, 8, 15, 24, 44,
                   39, 48, 41, 10, 69, 3, 98, 12, 26, 60, 17, 88, 52, 56]
    sortedArray = [1, 3, 7, 8, 8, 10, 12, 13, 15, 17, 24, 26, 26, 32, 34,
                   37, 39, 40, 41, 44, 44, 48, 50, 52, 56, 60, 69, 83, 88, 98]
    reversedArray = [98, 88, 83, 69, 60, 56, 52, 50, 48, 44, 44, 41, 40, 39, 37,
                     34, 32, 26, 26, 24, 17, 15, 13, 12, 10, 8, 8, 7, 3, 1]
    partiallySortedArray = [1, 3, 7, 8, 8, 10, 12, 13, 15, 17, 24, 26, 26, 32, 34,
                            39, 48, 41, 10, 69, 3, 98, 12, 26, 60, 17, 88, 52, 56]
    # array = []
    # for i in range(1000):
    #     # adding random values to the array
    #     array.append(random.randint(1, 20000))

    array = sortedArray
    print("Given array is")
    print(array)

    print("Sorted array is: ")
    # print(mergeSort(array))
    # print(quickSort(array, 0, len(array)-1))
    # print(bubbleSort(array))
    # print(selectionSort(array))
    print(insertionSort(array))

    print("Number of calculations:", cal)
