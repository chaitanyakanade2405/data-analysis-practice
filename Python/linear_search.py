arr = [4,56,78,23,98,34,24,42,65,78,90]
target = 24
def linear_search(arr, target):
    for i in range (len(arr)):
        if arr[i]==target:
            return i
        
print(linear_search(arr,target))