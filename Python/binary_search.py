arr = [4,56,78,23,98,34,24,42,65,78,90]
arr.sort()

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start<=end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
         start = mid + 1
        else: 
            end = mid - 1
            
    return -1

print(arr)
print(binary_search(arr,34))