import time


def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    if low == high:
        if arr[low] == target:
            return low
    else:
        # mid = int((high - low) / 2 + low)
        mid = low + ((high - low) // 2)
        if target > arr[mid]:
            return binary_search_recursive(arr, target, mid + 1, high)
        elif target < arr[mid]:
            return binary_search_recursive(arr, target, low, mid - 1)
        elif target == arr[mid]:
            return mid


def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    low = 0
    high = len(arr) - 1
    mid = ((high - low) // 2 + low)
    while low <= high:
        if arr[mid] < target:
            low = mid + 1
            mid = (low + high) // 2
        elif arr[mid] > target:
            high = mid - 1
            mid = (low + high) // 2
        elif arr[mid] == target:
            return mid
    return -1


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

names_1.sort()


for name in names_2:
    idx = binary_search(names_1, name)
    # idx = binary_search_recursive(names_1, name, 0, len(names_1) - 1)
    if idx > 0:
        print(idx)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
