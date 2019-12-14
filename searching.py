from timeit import default_timer as timer
import random


def linearSearch(arr, searchItem):
    for index, element in enumerate(arr):
        if element == searchItem:
            return index
    return None


def binarySearch(arr, searchItem):
    """ binary search using array"""
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == searchItem:
            return mid
        elif arr[mid] > searchItem:
            end = mid - 1
        else:
            start = mid + 1
    return None


# Driver code
if __name__ == '__main__':
    # array = []
    array = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    # # adding random values to the array
    # for i in range(50):
    #     array.append(random.randint(1, 200))

    # array.sort()
    print(array)

    # searchItem = random.choice(array)
    searchItem = 60
    print('Looking for', searchItem)

    # start = timer()

    # print('Found at index', linearSearch(array, searchItem))
    print('Found at index', binarySearch(array, searchItem))

    # stop = timer()
    # print('Execution Time in seconds:', stop - start)
